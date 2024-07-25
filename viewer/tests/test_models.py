from datetime import datetime, timedelta, timezone

from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from viewer.forms import EventForm
from viewer.models import Event


class EventModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("user1", "user1@example.com", "password")

    def test_create_event(self):
        start_date = datetime.now(tz=timezone.utc) + timedelta(days=3)
        end_date = datetime.now(tz=timezone.utc) + timedelta(days=5)
        event = Event(
            title="Foo",
            start_date=start_date,
            end_date=end_date,
            description="My Description",
            created_by=self.user,
            type="food",
            price=290.45,
            location="Fórum Karlín",
            region="JM",
        )
        event.save()

        event_from_db = Event.objects.get(id=event.id)
        self.assertEqual(event_from_db, event)
