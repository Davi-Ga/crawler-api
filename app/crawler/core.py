import bs4 as bs
from typing import List
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import undetected_chromedriver as uc
from time import sleep
from config import config_api



def generate_url(name:str)->str:
    processed_name=name.replace(" ","+")
    return f"https://www.jusbrasil.com.br/jurisprudencia/busca?q={processed_name}"


def get_page(url:str,driver:uc.Chrome)->bs.BeautifulSoup:
    
    try: 
        
        driver.get(url)
        soup = bs.BeautifulSoup(driver.page_source, 'html.parser')
    
        return soup
    
    except (TimeoutException, NoSuchElementException) as e:
        raise(f"Erro: {e}")
    
 
    
def login(driver:uc.Chrome) -> None:
    driver.get('https://www.jusbrasil.com.br/login')
    driver.find_element(By.ID,'FormFieldset-email').send_keys(config_api.EMAIL)
    driver.find_element(By.ID,'FormFieldset-password').send_keys(config_api.PASSWORD)
    driver.find_element(By.CLASS_NAME,'SubmitButton').click()
    sleep(30)
    
    

async def get_jurisprudences(name:str)->List[str]:
    webdriver_options = uc.ChromeOptions()
    # webdriver_options.add_argument('--headless=new')
    dr = uc.Chrome(options=webdriver_options)
    login(driver=dr)
    url=generate_url(name)
    initial_page=get_page(url,dr)
    raw=initial_page.find_all(class_='search-snippet-base_SearchSnippetBase__sMKry')
    jurisprudences=[]
    
    for j in raw:
        
        jurisprudence_page=get_page(j.find(class_='search-snippet-base_SearchSnippetBase-titleLink__ms7sZ')['href'],dr)
        
        if jurisprudence_page.find(class_='tabs-link') is not None:
            tab_page=get_page(str(jurisprudence_page.find_all(class_='tabs-link').pop(1)).split('href="').pop(1).split('"').pop(0),dr)
            item={
                "title":tab_page.find(class_='JurisprudencePage-title').text,
                "body":tab_page.find(class_='JurisprudencePage-content').text,
            }
        else:
            item={
                "title":jurisprudence_page.find(class_='JurisprudencePage-title').text,
                "body":jurisprudence_page.find(class_='JurisprudencePage-content').text,
            }
            
        jurisprudences.append(item)
    
    dr.quit()
        
    return jurisprudences
