import fastapi
import pydantic

import crud
import models
import schema

from typing import Annotated

from dependencies import SessionDependency
from database import connect_db

STATUS_SUCCESS_RESPONSE = {"status": "success"}

app = fastapi.FastAPI(
    title='Advertisement',
    version='0.0.1',
    lifespan=connect_db
)


class AdvertisementRequest(pydantic.BaseModel):
    pass


class AdvertisementResponse(pydantic.BaseModel):
    description: str


@app.get("/advertisement/{advertisement_id}", response_model=schema.GetAdvertisementResponse)
async def get_advtg(advertisement_id: int, session: SessionDependency):
    advtg = await crud.get_item(session, models.Advertisement, advertisement_id)

    return advtg.dict


@app.get("/advertisement", response_model=schema.GetAdvertisementResponse)
async def search_advtg(session: SessionDependency, q: Annotated[str, fastapi.Query(max_length=50)]):
    advtg = await crud.search_item(session, q)

    return advtg


@app.post("/advertisement", response_model=schema.CreateAdvertisementResponse)
async def create_advtg(json_data: schema.CreateAdvertisementRequest, session: SessionDependency):
    advtg = models.Advertisement(**json_data.dict())
    advtg = await crud.add_item(session, advtg)

    return advtg.dict


@app.patch("/advertisement/{advertisement_id}", response_model=schema.UpdateAdvertisementResponse)
async def update_advtg(advertisement_id: int, json_data: schema.UpdateAdvertisementRequest, session: SessionDependency):
    advtg = await crud.get_item(session, models.Advertisement, advertisement_id)
    advtg_patch = json_data.dict(exclude_unset=True)
    for field, value in advtg_patch.items():
        setattr(advtg, field, value)
    await crud.add_item(session, advtg)

    return advtg.id_dict


@app.delete("/advertisement/{advertisement_id}", response_model=schema.DeleteTodoResponse)
async def delete_advtg(advertisement_id: int, session: SessionDependency):
    await crud.delete_item(session, models.Advertisement, advertisement_id)

    return STATUS_SUCCESS_RESPONSE
