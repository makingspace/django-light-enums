from six import with_metaclass

from .db import EnumField


class EnumType(type):

    def __new__(mcl, name, bases, nmspc):
        cls = super(EnumType, mcl).__new__(mcl, name, bases, nmspc)
        cls._enum_values = {
            value: field for field, value in cls.__dict__.items()
            if not callable(value) and not field.startswith('__')
        }
        cls._choices = [(value, field) for field, value in cls._enum_values.items()]
        return cls

    def get_name(cls, value):
        return cls._enum_values[value]

    def get_value(cls, name):
        return getattr(cls, name)

    def is_valid_value(cls, value):
        return value in cls._enum_values.keys()

    @property
    def enum_values(cls):
        return cls._enum_values.keys()

    @property
    def enum_names(cls):
        return cls._enum_values.values()


class Enum(with_metaclass(EnumType)):
    pass
