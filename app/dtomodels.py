from pydantic import BaseModel


class DtoPlayer(BaseModel):
    name: str
    price: int
    desc: str
