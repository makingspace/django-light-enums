from six import with_metaclass

from .db import EnumField

EnumField = EnumField


class EnumType(type):

    def __new__(mcl, name, bases, nmspc):
        cls = super(EnumType, mcl).__new__(mcl, name, bases, nmspc)
        cls._enum_values = {
            value: field for field, value in cls.__dict__.items()
            if not callable(value) and not field.startswith('_')
        }
        return cls

    def get_name(cls, value):
        return cls._enum_values.get(value)

    def get_value(cls, name):
        if not name:
            return None
        return getattr(cls, name, None)

    def is_valid_value(cls, value):
        return value in cls._enum_values.keys()

    @property
    def enum_values(cls):
        return cls._enum_values.keys()

    @property
    def enum_names(cls):
        return cls._enum_values.values()

    @property
    def choices(cls):
        return list(cls._enum_values.items())

    @property
    def choices_inverse(cls):
        return [(name, value) for value, name in cls._enum_values.items()]


class Enum(with_metaclass(EnumType)):
    pass
