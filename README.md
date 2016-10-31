# django-light-enums

django-light-enums is a [Django][django] application for easy-to-use light-weight enums.

The general approach borrows heavily from [django-enumfield][django-enumfield],
which doesn't work with Django 1.9+ and has some confusing interfaces.

[django]: https://www.djangoproject.com/
[django-enumfield]: https://github.com/5monkeys/django-enumfield

# How to install

```shell
pip install django-light-enums
```

And add to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'django_light_enums',
    ...
]
```

# An Example

## Create your EnumField on your Model

```python
from django.db import models

from django_light_enums import enum


class Dog(models.Model):

    class Size(enum.Enum):
        BIG = 10
        MEDIUM = 20
        SMALL = 30

    size = enum.EnumField(Size, default=Size.BIG)
```

## Use it

```python
EXTERNAL_INPUT = 50

small_dog = Dog.objects.create(size=Dog.Size.SMALL)

assert small_dog.size == Dog.Size.SMALL

assert Dog.Size.is_valid_value(EXTERNAL_INPUT) is False

assert Dog.Size.get_name(Dog.Size.SMALL) == 'SMALL'

assert Dog.Size.get_value('MEDIUM') == Dog.Size.MEDIUM
```
