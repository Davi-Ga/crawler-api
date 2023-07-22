import requests as rq
import bs4 as bs
from typing import List

def generate_url(month:str, day:int)->str:
    return f"https://www.onthisday.com/day/{month}/{day}"

def get_page(url:str)->bs.BeautifulSoup:
    page = rq.get(url)
    soup = bs.BeautifulSoup(page.content, 'html.parser')
    return soup

def events_of_the_day(mounth:str,day:int)->List[str]:
    url=generate_url(mounth,day)
    page=get_page(url)
    raw_events=page.find_all(class_="event")
    print(raw_events)

events_of_the_day("july",5)    

    