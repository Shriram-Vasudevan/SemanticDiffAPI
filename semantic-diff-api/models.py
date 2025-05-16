from pydantic import BaseModel

class DiffRequest(BaseModel):
    before: str
    after: str
