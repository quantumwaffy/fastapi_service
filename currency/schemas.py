from tortoise.contrib.pydantic import pydantic_model_creator

from currency import models

pyd_bank_currency = pydantic_model_creator(models.BankCurrency, name="BankCurrency", exclude_readonly=True)
pyd_bank_by_city = pydantic_model_creator(
    models.BankCurrency,
    name="BankByCity",
    include=(
        "bank_name",
        "city_name",
    ),
    exclude_readonly=True,
)
