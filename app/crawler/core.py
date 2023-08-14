import bs4 as bs
from typing import List
from selenium import webdriver


def generate_url(name:str)->str:
    processed_name=name.replace(" ","+")
    return f"https://www.jusbrasil.com.br/jurisprudencia/busca?q={processed_name}"

def get_page(url:str)->bs.BeautifulSoup:
    options=webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless=new')
    dr=webdriver.Chrome(options=options)
    
    dr.get(url)
    soup = bs.BeautifulSoup(dr.page_source, 'html.parser')
    dr.quit()
    return soup

async def get_jurisprudences(name:str)->List[str]:
    url=generate_url(name)
    page=get_page(url)
    raw=page.find_all(class_='DocumentSnippet')
    jurisprudences=[]
    for j in raw:
        item={
            "title":j.find(class_='BaseSnippetWrapper-title').text,
            "body":j.find(class_='BaseSnippetWrapper-body').text,
        }
        jurisprudences.append(item)
        
    return jurisprudences