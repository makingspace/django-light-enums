import logging

from django.test import TestCase
from django.core.exceptions import ValidationError

from .models import Status, DbModel


class EnumTests(TestCase):

    def test_enum_get_value(self):
        self.assertEqual(Status.STATUS_ONE, Status.get_value('STATUS_ONE'))
        self.assertEqual(Status.STATUS_TWO, Status.get_value('STATUS_TWO'))
        self.assertEqual(Status.STATUS_THREE, Status.get_value('STATUS_THREE'))

    def test_enum_get_name(self):
        self.assertEqual('STATUS_ONE', Status.get_name(Status.STATUS_ONE))
        self.assertEqual('STATUS_TWO', Status.get_name(Status.STATUS_TWO))
        self.assertEqual('STATUS_THREE', Status.get_name(Status.STATUS_THREE))

    def test_enum_choices(self):
        self.assertEqual(
            [
                ('STATUS_ONE', Status.STATUS_ONE),
                ('STATUS_TWO', Status.STATUS_TWO),
                ('STATUS_THREE', Status.STATUS_THREE)
            ],
            Status._choices
        )


class EnumFieldTests(TestCase):

    def setUp(self):
        logging.disable(logging.WARNING)

    def test_storage_and_retrieval(self):
        INVALID_VALUE = 999999
        with self.settings():

            obj = DbModel.objects.create()
            # default value is the first
            self.assertEqual(obj.status, Status.STATUS_ONE)

            # status change
            obj.status = Status.STATUS_TWO
            obj.save()
            obj.refresh_from_db()

            self.assertEqual(obj.status, Status.STATUS_TWO)

            # status change
            obj.status = Status.STATUS_THREE
            obj.save()
            obj.refresh_from_db()

            self.assertEqual(obj.status, Status.STATUS_THREE)

            with self.assertRaises(ValidationError):
                obj.status = INVALID_VALUE
                obj.save()
