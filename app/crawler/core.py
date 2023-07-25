import requests as rq
import bs4 as bs
from typing import List
from aiohttp import ClientSession
import asyncio
from fastapi import HTTPException,status
from selenium import webdriver




def generate_url(name:str)->str:
    processed_name=name.replace(" ","+")
    return f"https://www.jusbrasil.com.br/jurisprudencia/busca?q={processed_name}"

def get_page(url:str)->bs.BeautifulSoup:
    dr=webdriver.Chrome()
    dr.get(url)
    soup = bs.BeautifulSoup(dr.page_source, 'html.parser')
    return soup

def get_jurisprudences(name:str)->List[str]:
    url=generate_url(name)
    page=get_page(url)
    raw=page.find_all(class_='SearchResults-documents')
    return raw

if __name__ == "__main__":
    print(get_jurisprudences("Roberto Naves"))