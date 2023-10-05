import bs4 as bs
from typing import List, Union
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import undetected_chromedriver as uc
from time import sleep
from utils import json_saver,generate_url,get_names


def get_page(url:str,driver:uc.Chrome)->bs.BeautifulSoup:
    
    try: 
        driver.get(url)
        soup = bs.BeautifulSoup(driver.page_source, 'html.parser')
    
        return soup
    
    except (TimeoutException, NoSuchElementException) as e:
        raise(f"Erro: {e}")
    
 
    
def login(driver:uc.Chrome) -> None:
    driver.get('https://www.jusbrasil.com.br/login')
    driver.find_element(By.ID,'FormFieldset-email').send_keys("davigaldinoky@gmail.com")
    driver.find_element(By.ID,'FormFieldset-password').send_keys("Pibic2023@@20")
    driver.find_element(By.CLASS_NAME,'SubmitButton').click()
    sleep(30)


def access_page(name:str,driver:uc.Chrome,jurisprudences:List[str]) -> List[str]:
    url=generate_url(name)
    initial_page=get_page(url,driver)
    raw=initial_page.find_all(class_='search-snippet-base_SearchSnippetBase__sMKry')

    for j in raw:
        jurisprudence_title=j.find(class_='search-snippet-base_SearchSnippetBase-titleLink__ms7sZ')['href']
        jurisprudence_page=get_page(jurisprudence_title,driver)
       
        if jurisprudence_page.find(class_='error-page_main__kx7NZ') is None:
            
            if jurisprudence_page.find(class_='tabs-link') is not None:
                tab_page=get_page(str(jurisprudence_page.find_all(class_='tabs-link').pop(1)).split('href="').pop(1).split('"').pop(0),driver)
                item={
                    "title":tab_page.find(class_='JurisprudencePage-title').text,
                    "body":tab_page.find(class_='JurisprudencePage-content').text,
                }
                print(f'Adicionado com sucesso {item["title"]}')
                
            else:
                if jurisprudence_page.find(class_='JurisprudencePage-title') is not None:
                    
                    item={
                        "title":jurisprudence_page.find(class_='JurisprudencePage-title').text,
                        "body":jurisprudence_page.find(class_='JurisprudencePage-content').text,
                    }
                    print(f'Adicionado com sucesso {item["title"]}')
                else:
                    item={
                        "body":jurisprudence_page.find(class_='DocumentPage-content').text,
                    }
                    print(f'Adicionado com sucesso item que não possui titulo')
        else:
            print(f'Página não encontrada {jurisprudence_title}, pulando para a próxima jurisprudência')
            continue
        
        jurisprudences.append(item)
    
    print (f'Busca finalizada no nome de {name}')
    
    return jurisprudences


def get_jurisprudences(name_or_names: Union[str, List[str]])->List[str]:
    webdriver_options = uc.ChromeOptions()
    # webdriver_options.add_argument('--headless=new')
    dr = uc.Chrome(options=webdriver_options)
    content=[]
    
    if isinstance(name_or_names, list):
        login(driver=dr)
   
        for name in name_or_names:
            jurisprudences=[]
            print(f'Iniciando busca no nome de {name} na lista de nomes')
            content=access_page(name,dr,jurisprudences)
            print(f'Adicionando ao arquivo {name}')
            json_saver(content,name)
            
    if isinstance(name_or_names, str):
        login(driver=dr)
        print(f'Iniciando busca no nome de {name}')
        jurisprudences=[]
        content=access_page(name,dr,jurisprudences)
        print(f'Adicionando ao arquivo {name}')
        json_saver(content,name)
            
    
    dr.quit()    

get_jurisprudences(get_names())