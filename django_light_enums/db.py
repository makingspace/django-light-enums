from django.db.models import IntegerField
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class EnumField(IntegerField):
    """
    Implements storage of an enum value in a db field
    """

    def __init__(self, enum, *args, **kwargs):
        kwargs['choices'] = enum.choices
        kwargs.setdefault('default', min(enum.enum_values))
        self.enum = enum
        return super(EnumField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname)
        if value is None:
            if not self.null:
                raise ValidationError(_('None is not a valid value in this non-null enum.'))
        elif not self.enum.is_valid_value(value):
            raise ValidationError(
                _('(%(value)s) is not a valid value in this enum. '
                  'Possible values are: %(values)s.'),
                params={
                    'value': value,
                    'values': ', '.join(
                        '{} ({})'.format(name, value)
                        for value, name in self.enum.choices
                    ),
                },
            )
        return value

    def deconstruct(self):
        name, path, args, kwargs = super(EnumField, self).deconstruct()
        args.append(self.enum)
        kwargs.pop('choices', None)
        return name, path, args, kwargs
