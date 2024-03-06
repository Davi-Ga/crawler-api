from pydantic import BaseModel,HttpUrl

class NameSearch(BaseModel):
    name: str
    
class Crawler(BaseModel):
    title: str
    body: str
    url: HttpUrl
    
class CrawlerResponse(BaseModel):
    jurisprudences: list[Crawler]
    