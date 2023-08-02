from fastapi import Request
from fastapi.responses import JSONResponse
from .exceptions import InternalServerException,JurisprudenceNotFoundException

async def internal_server_error_handler(request: Request, exception: InternalServerException):
    # Manipulador de exceção personalizado para tratar a exceção InternalServerError
    return JSONResponse(status_code=exception.status_code, 
                        content={
                            "message": str(exception.detail),
                            "request": request.url.path
                        })
    
async def jurisprudence_not_found_handler(request: Request, exception: JurisprudenceNotFoundException):
    # Manipulador de exceção personalizado para tratar a exceção JurisprudenceNotFoundException
    return JSONResponse(status_code=exception.status_code, 
                        content={
                            "message": str(exception.detail),
                            "request": request.url.path
                        })