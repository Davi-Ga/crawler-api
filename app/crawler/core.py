import bs4 as bs
from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config import config_api

def generate_url(name:str)->str:
    processed_name=name.replace(" ","+")
    return f"https://www.jusbrasil.com.br/jurisprudencia/busca?q={processed_name}"

def get_page(url:str)->bs.BeautifulSoup:
    webdriver_options = webdriver.ChromeOptions()
    
    webdriver_options.add_argument('--headless=new')
    webdriver_options.add_argument("--no-sandbox")
    webdriver_options.add_argument('--disable-dev-shm-usage')
    webdriver_options.binary_location = '/usr/bin/chromium-browser'
    dr = webdriver.Chrome(options=webdriver_options)
    
    try: 
        login(driver=dr)
        dr.get(url)
        soup = bs.BeautifulSoup(dr.page_source, 'html.parser')
    
        return soup
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Erro: {e}")
    
    finally:
        dr.quit()
    
def login(driver:webdriver.Chrome) -> None:
    driver.get('https://www.jusbrasil.com.br/login')
    driver.find_element(By.ID,'FormFieldset-email').send_keys(config_api.EMAIL)
    driver.find_element(By.ID,'FormFieldset-password').send_keys(config_api.PASSWORD)
    driver.find_element(By.CLASS_NAME,'SubmitButton').submit()

async def get_jurisprudences(name:str)->List[str]:
    url=generate_url(name)
    page=get_page(url)
    raw=page.find_all(class_='search-snippet-base_SearchSnippetBase__sMKry')
    jurisprudences=[]
    for j in raw:
        item={
            "title":j.find(class_='search-snippet-base_SearchSnippetBase-titleLink__ms7sZ').text,
            "body":j.find(class_='search-snippet-base_SearchSnippetBase-body__OY5oa').text,
        }
        jurisprudences.append(item)
        
    return jurisprudences

