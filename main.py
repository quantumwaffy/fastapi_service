from fastapi import FastAPI, HTTPException
from pydantic import ValidationError
from tortoise.contrib.fastapi import register_tortoise

import currency.models
from currency import config, schemas

app = FastAPI()


@app.on_event("startup")
async def startup():
    register_tortoise(app, config=config.DB_CONFIG, generate_schemas=False, add_exception_handlers=True)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/currency/get-bank-in-city/{bank_name}/{city_name}")
async def get_bank_by_city(bank_name: str, city_name: str):
    try:
        pyd_obj_dict = schemas.pyd_bank_by_city(bank_name=bank_name, city_name=city_name).dict()
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    if not currency.models.BankCurrency.filter(**pyd_obj_dict).exists():
        raise HTTPException(status_code=404, detail="Item not found")
    obj = await currency.models.BankCurrency.get(**pyd_obj_dict)
    return await schemas.pyd_bank_currency.from_tortoise_orm(obj)
