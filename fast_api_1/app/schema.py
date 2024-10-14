from pydantic import BaseModel
from typing import Literal


class IdReturnBase(BaseModel):
    id: int


class StatusSuccessBase(BaseModel):
    status: Literal["success"]


class GetAdvertisementResponse(BaseModel):
    id: int
    header: str
    description: str
    owner: str


class CreateAdvertisementRequest(BaseModel):
    header: str
    description: str
    owner: str


class CreateAdvertisementResponse(IdReturnBase):
    pass


class UpdateAdvertisementRequest(BaseModel):
    header: str
    description: str
    owner: str


class UpdateAdvertisementResponse(IdReturnBase):
    pass


class DeleteTodoResponse(StatusSuccessBase):
    pass
