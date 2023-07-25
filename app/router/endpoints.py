from fastapi import APIRouter


api_router=APIRouter(prefix='/api',tags=['add'])

@api_router.get('/test')
def add():
    return {'message':'add'}