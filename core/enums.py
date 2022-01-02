from enum import Enum


class EnumChoices(Enum):
    @classmethod
    @property
    def choices(cls):
        return tuple(instance.value for instance in cls.__members__.values())
