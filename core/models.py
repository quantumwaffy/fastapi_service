from tortoise import Model, fields


class AbstractBaseModel(Model):
    id = fields.IntField(pk=True)

    class Meta:
        abstract = True


class TimestampMixin:
    created_at = fields.DatetimeField(auto_now_add=True, null=True)
    modified_at = fields.DatetimeField(auto_now=True, null=True, source_field="updated_at")
