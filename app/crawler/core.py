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
    driver.find_element(By.ID,'FormFieldset-password').send_keys("Pibic2023@@12")
    driver.find_element(By.CLASS_NAME,'SubmitButton').click()
    sleep(30)


def access_page_jurisprudences(name:str,driver:uc.Chrome,jurisprudences:List[str]) -> List[str]:
    pagination_items=get_page(generate_url(name),driver).find_all(class_='pagination_pagination-pages-item__RTw7L')
    if pagination_items is not None:
        number_pagination_items=len(pagination_items)
        print(f'Número de páginas {number_pagination_items}')
        pages=1
        while pages <= number_pagination_items:
            print(f'Iniciando busca na página {pages}')
            url=generate_url(name,2,page=pages)
            initial_page=get_page(url,driver)
            raw=initial_page.find_all(class_='search-snippet-base_SearchSnippetBase__sMKry')

            for j in raw:
                jurisprudence_title=j.find(class_='search-snippet-base_SearchSnippetBase-titleLink__ms7sZ')['href']
                jurisprudence_page=get_page(jurisprudence_title,driver)
                print(jurisprudence_title)
            
                if jurisprudence_page.find(class_='error-page_main__kx7NZ') is None:
                    
                    if jurisprudence_page.find(class_='tabs-link') is not None:
                        tab_page=get_page(str(jurisprudence_page.find_all(class_='tabs-link').pop(1)).split('href="').pop(1).split('"').pop(0),driver)
                        if tab_page.find(class_='JurisprudencePage-title') is not None:
                            item={
                                "title":tab_page.find(class_='JurisprudencePage-title').text,
                                "body":tab_page.find(class_='JurisprudencePage-content').text,
                            }
                            print(f'Adicionado com sucesso {item["title"]}')
                        elif tab_page.find(class_='DocumentPage-title') is not None:
                            item={
                                "body":tab_page.find(class_='DocumentPage-content').text,
                            }
                            print(f'Adicionado com sucesso item que não possui titulo')
                        
                        else:
                            print(f'Provavelmente atingimos o limite de busca')
                            break
                        
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
                
                sleep(3)
                jurisprudences.append(item)
            pages+=1
        print (f'Busca finalizada no nome de {name}')
    else:
        pass

    return jurisprudences

def access_page_procedural_parts(name:str,driver:uc.Chrome,parts:List[str]) -> List[str]:
    pagination_items=get_page(generate_url(name,1),driver).find_all(class_='pagination-item-link')
    if pagination_items is not None:
        number_pagination_items=len(pagination_items)
        print(f'Número de páginas {number_pagination_items}')
        pages=1
        while pages <= number_pagination_items:
            print(f'Iniciando busca na página {pages}')
            url=generate_url(name,1,page=pages)
            initial_page=get_page(url,driver)
            raw=initial_page.find_all(class_='DocumentSnippet')
            sleep(3)

            for j in raw:
                part_title=j.find(class_='BaseSnippetWrapper-title-anchor')['href']
                sleep(3)
                part_page=get_page(part_title,driver)
                if part_page.find(class_='error-page_main__kx7NZ') is None:
                   
                    related_documents_element = part_page.find(class_='RelatedDocuments-list')
                    if related_documents_element is not None:
                        related_documents = related_documents_element.find_all(class_='RelatedDocuments-link')
                    else:
                        related_documents = []
                        
                    if related_documents:
                        petition={
                            "title_petition":part_page.find(class_='document-title').text,
                            "body_petition":part_page.find(class_='MotionPage-content').text or part_page.find(class_='document-content').text,
                        }
                        
                        for related_document in related_documents:
                            decision=related_document.find(class_='RelatedDocuments-group-type')
                            print(decision.text)
                            if decision.text == 'Decisão' or decision.text == 'Sentença' or decision.text == 'Acórdão':
                                decision_page=get_page(related_document['href'],driver)
                                sleep(3)
                                if decision_page.find(class_='tabs-link') is not None:
                                    tab_page=get_page(str(decision_page.find_all(class_='tabs-link').pop(1)).split('href="').pop(1).split('"').pop(0),driver)
                                       
                                    if tab_page.find(class_='JurisprudencePage-title') is not None:
                                        item={
                                            "title":tab_page.find(class_='JurisprudencePage-title').text,
                                            "body":tab_page.find(class_='JurisprudencePage-content').text,
                                        }
                                        print(f'Adicionado com sucesso {item["title"]}')
                                        break
                                    elif tab_page.find(class_='DocumentPage-title') is not None:
                                        item={
                                            "body":tab_page.find(class_='DocumentPage-content').text,
                                        }
                                        print(f'Adicionado com sucesso item que não possui titulo')
                                        break
                        
                                    else:
                                        print(f'Provavelmente atingimos o limite de busca')
                                        break
                        
                                elif decision_page.find(class_='JurisprudencePage-title') is not None:
                                    item={
                                        "title":decision_page.find(class_='document-title').text,
                                        "body":decision_page.find(class_='JurisprudencePage-content').text,
                                    }
                                    print(f'Adicionado com sucesso {item["title"]}')
                                    break
                                else:
                                    item={
                                        "body":decision_page.find(class_='DocumentPage-content').text,
                                    }
                                    print(f'Adicionado com sucesso item que não possui titulo')
                                    break
                            else:
                                item={
                                    'title': 'Petição Inicial não possui decisão',
                                }
                                break  
                    else:
                        item={
                            'title': 'Petição Inicial não possui decisão',
                        }       
                        petition={
                            "title_petition":part_page.find(class_='document-title').text,
                            "body_petition":part_page.find(class_='MotionPage-content').text or part_page.find(class_='document-content').text,
                        }
                else:
                    print(f'Página não encontrada {part_title}, pulando para a próxima parte processual')
                    continue
                
                sleep(2)
                parts.extend([item, petition])
            pages+=1
        print (f'Busca finalizada no nome de {name}')
    else:
        pass

    return parts


def get_jurisprudences(name_or_names: Union[str, List[str]])->List[str]:
    webdriver_options = uc.ChromeOptions()
    # webdriver_options.add_argument('--headless=new')
    dr = uc.Chrome(options=webdriver_options)
    content=[]
    
    if isinstance(name_or_names, list):
        login(driver=dr)
   
        for name in name_or_names:
            parts=[]
            print(f'Iniciando busca no nome de {name} na lista de nomes')
            content=access_page_procedural_parts(name,dr,parts)
            print(f'Adicionando ao arquivo {name}')
            json_saver(content,name)
            
    if isinstance(name_or_names, str):
        login(driver=dr)
        name=name_or_names
        print(f'Iniciando busca no nome de {name}')
        parts=[]
        content=access_page_procedural_parts(name,dr,parts)
        print(f'Adicionando ao arquivo {name}')
        json_saver(content,name)
            
    
    dr.quit()    
    print('Busca finalizada')

get_jurisprudences(get_names(person_color='Negra',analised_row='COR',wanted_row='NOME',delimiter='|'))


