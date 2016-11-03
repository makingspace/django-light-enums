from django.db.models import IntegerField
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class EnumField(IntegerField):
    """
    Implements storage of an enum value in a db field
    """

    def __init__(self, enum=None, enum_values=None, choices=None, default=None, *args, **kwargs):
        choices = choices or enum.choices
        default = default or min(enum.enum_values)
        self.enum_values = enum_values or enum.enum_values
        return super(EnumField, self).__init__(choices=choices, default=default, *args, **kwargs)

    def pre_save(self, model_instance, add):
        # Do some validation on the value of the field being stored.
        value = getattr(model_instance, self.attname)
        if value is None:
            if not self.null:
                raise ValidationError(_('None is not a valid value in this non-null enum.'))
        elif value not in self.enum_values:
            raise ValidationError(
                _('(%(value)s) is not a valid value in this enum. '
                  'Possible values are: %(values)s.'),
                params={
                    'value': value,
                    'values': ', '.join(
                        '{} ({})'.format(name, value)
                        for value, name in self.choices
                    ),
                },
            )
        return value

    def deconstruct(self):
        name, path, args, kwargs = super(EnumField, self).deconstruct()
        kwargs['enum_values'] = self.enum_values
        return name, path, args, kwargs
