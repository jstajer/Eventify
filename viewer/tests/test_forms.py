from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.test import TestCase

from viewer.forms import EventForm


class EventFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("user1", "user1@example.com", "password")

    def test_create_event(self):
        form = EventForm(data={
            "title": "Foo",
            "start_date": datetime.now() + timedelta(days=3),
            "end_date": datetime.now() + timedelta(days=5),
            "description": "My Description",
            "created_by": self.user,
            "type": "Food",
            "price": 290.45,
            "location": "Fórum Karlín",
            "region": "JM"
        })

        self.assertTrue(form.is_valid())

    def test_create_event_missing_location(self):
        form = EventForm(data={
            "title": "Foo",
            "start_date": datetime.now() + timedelta(days=3),
            "end_date": datetime.now() + timedelta(days=5),
            "description": "My Description",
            "created_by": self.user,
            "type": "Food",
            "price": 290.45,
            "region": "JM"
        })

        self.assertTrue(form.is_valid())