from fastapi import FastAPI, HTTPException
from pydantic import ValidationError
from tortoise.contrib.fastapi import register_tortoise
from tortoise.functions import Max

from currency import config, consts, models, schemas

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
    if not models.BankCurrency.filter(**pyd_obj_dict).exists():
        raise HTTPException(status_code=404, detail="Item not found")
    obj = await models.BankCurrency.get(**pyd_obj_dict)
    return await schemas.pyd_bank_currency.from_tortoise_orm(obj)


@app.get("/currency/get-best-usd-sell/{city_name}")
async def get_best_usd_by_city(city_name: str):
    if city_name not in consts.Cities.choices:
        raise HTTPException(status_code=404, detail=f"City not found. Choices are '{' ,'.join(consts.Cities.choices)}'")
    max_value_dict = (
        await models.BankCurrency.filter(city_name=city_name)
        .annotate(max_value=Max("usd_sell"))
        .first()
        .values("max_value")
    )
    object_list = models.BankCurrency.filter(city_name=city_name, usd_sell=max_value_dict.get("max_value"))
    return await schemas.pyd_bank_currency.from_queryset(object_list)
