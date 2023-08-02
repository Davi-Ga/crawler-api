from fastapi import HTTPException

class JurisprudenceNotFoundException(HTTPException):
    def __init__(self,name: str):
        super().__init__(status_code=404, detail=f"Jurisprudences with name {name} was not found")
        
class InternalServerException(HTTPException):
    def __init__(self):
        super().__init__(status_code=500, detail=f"Internal server error")