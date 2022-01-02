from tortoise import fields

from core import models as core_models


class BankCurrency(core_models.TimestampMixin, core_models.AbstractBaseModel):
    bank_name = fields.CharField(max_length=255, null=True, source_field="bank")
    city_name = fields.CharField(max_length=7, null=True, source_field="city")
    usd_buy = fields.DecimalField(max_digits=4, decimal_places=3, null=True)
    usd_sell = fields.DecimalField(max_digits=4, decimal_places=3, null=True)
    euro_buy = fields.DecimalField(max_digits=4, decimal_places=3, null=True)
    euro_sell = fields.DecimalField(max_digits=4, decimal_places=3, null=True)
    rub_buy = fields.DecimalField(max_digits=4, decimal_places=3, null=True)
    rub_sell = fields.DecimalField(max_digits=4, decimal_places=3, null=True)
    usd_buy_from_euro = fields.DecimalField(max_digits=4, decimal_places=3, null=True)
    usd_sell_from_euro = fields.DecimalField(max_digits=4, decimal_places=3, null=True)

    class Meta:
        table_description = "Bank actual currency info"
        table = "telegram_bot_actualcurrencyinfo"

    def __str__(self):
        return f"{self.city}_{self.bank}"
