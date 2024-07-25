import time

from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.select import Select


class EventTestSelenium(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(5)

    def setUp(self):
        user_password = "password"
        self.user = User.objects.create_superuser("user1", "user1@example.com", user_password)

        self.selenium.get(f"{self.live_server_url}/accounts/login/")
        username_field = self.selenium.find_element(By.ID, "id_username")
        username_field.send_keys(self.user.username)

        password_field = self.selenium.find_element(By.ID, "id_password")
        password_field.send_keys(user_password)

        login_button = self.selenium.find_element(By.XPATH, "/html/body/div/div/form/button")
        login_button.click()

    def test_create_event(self):
        presentation = True  # Nastavte na False, pokud nechcete spustit time.sleep
        self.selenium.get(f"{self.live_server_url}/create/")

        title_field = self.selenium.find_element(By.ID, "id_title")
        title_field.send_keys("Foo")
        if presentation: time.sleep(1)

        start_date_field = self.selenium.find_element(By.ID, "id_start_date")
        start_date_field.send_keys("12/12/2026 11:00")
        if presentation: time.sleep(1)

        end_date_field = self.selenium.find_element(By.ID, "id_end_date")
        end_date_field.send_keys("12/12/2027 15:00")
        if presentation: time.sleep(1)

        description_field = self.selenium.find_element(By.ID, "id_description")
        description_field.send_keys("My Description")
        if presentation: time.sleep(1)

        create_by_field = Select(self.selenium.find_element(By.ID, "id_created_by"))
        create_by_field.select_by_visible_text(self.user.username)
        if presentation: time.sleep(1)

        type_field = Select(self.selenium.find_element(By.ID, "id_type"))
        type_field.select_by_visible_text("Food")
        if presentation: time.sleep(1)

        price_field = self.selenium.find_element(By.ID, "id_price")
        price_field.send_keys("290.45")
        if presentation: time.sleep(1)

        location_field = self.selenium.find_element(By.ID, "id_location")
        location_field.send_keys("Praha 1")
        if presentation: time.sleep(1)

        region_field = Select(self.selenium.find_element(By.ID, "id_region"))
        region_field.select_by_visible_text("Praha")
        if presentation: time.sleep(1)

        submit_button = self.selenium.find_element(By.XPATH, "/html/body/div/div/form/button")
        submit_button.click()

        self.selenium.get(self.live_server_url)

        event_name_element = self.selenium.find_element(By.XPATH, "/html/body/div/div/div/div/div/h5")
        self.assertEqual(event_name_element.text, "Foo")

        event_description_element = self.selenium.find_element(By.XPATH, "/html/body/div/div/div/div/div/p")
        self.assertEqual(event_description_element.text, "My Description")


class SignUpTestSelenium(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(5)

    def test_signup(self):
        self.selenium.get(f"{self.live_server_url}/signup/")
        email = "petr@seznam.cz"

        username_field = self.selenium.find_element(By.ID, "id_username")
        username_field.send_keys("Petr")

        email_field = self.selenium.find_element(By.ID, "id_email")
        email_field.send_keys(email)

        password1_field = self.selenium.find_element(By.ID, "id_password1")
        password1_field.send_keys("heslo1234+")

        password2_field = self.selenium.find_element(By.ID, "id_password2")
        password2_field.send_keys("heslo1234+")

        submit_button = self.selenium.find_element(By.XPATH, "/html/body/div/div/form/button")
        submit_button.click()

        self.selenium.get(self.live_server_url)

        email_field_readonly = self.selenium.find_element(By.XPATH, "/html/body/nav/div/ul[2]/li[2]/span")
        logout_button = self.selenium.find_element(By.XPATH, "/html/body/nav/div/ul[2]/li[3]/a")

        self.assertEqual(email_field_readonly.text, email)
        self.assertEqual(logout_button.text, "Logout")

    def test_signup_weak_password(self):
        self.selenium.get(f"{self.live_server_url}/signup/")

        username_field = self.selenium.find_element(By.ID, "id_username")
        username_field.send_keys("Petr")

        email_field = self.selenium.find_element(By.ID, "id_email")
        email_field.send_keys("petr@seznam.cz")

        password1_field = self.selenium.find_element(By.ID, "id_password1")
        password1_field.send_keys("123")

        password2_field = self.selenium.find_element(By.ID, "id_password2")
        password2_field.send_keys("123")

        submit_button = self.selenium.find_element(By.XPATH, "/html/body/div/div/form/button")
        submit_button.click()

        too_short_password_li = self.selenium.find_element(By.XPATH, "/html/body/div/div/form/ul[2]/li[1]")
        too_common_password_li = self.selenium.find_element(By.XPATH, "/html/body/div/div/form/ul[2]/li[2]")
        only_numbers_password_li = self.selenium.find_element(By.XPATH, "/html/body/div/div/form/ul[2]/li[3]")

        self.assertEqual(
            too_short_password_li.text,
            "This password is too short. It must contain at least 8 characters."
        )
        self.assertEqual(too_common_password_li.text, "This password is too common.")
        self.assertEqual(only_numbers_password_li.text, "This password is entirely numeric.")
