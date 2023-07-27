from fastapi import APIRouter

from crawler.core import get_jurisprudences

router=APIRouter()

@router.get('/search/{name}')
async def jurisprudences(name:str):
    data = await get_jurisprudences(name)
    return data