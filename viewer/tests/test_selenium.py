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
        cls.selenium.implicitly_wait(10)

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
        self.selenium.get(f"{self.live_server_url}/create/")

        title_field = self.selenium.find_element(By.ID, "id_title")
        title_field.send_keys("Foo")

        start_date_field = self.selenium.find_element(By.ID, "id_start_date")
        start_date_field.send_keys("12/12/2026 11:00")

        end_date_field = self.selenium.find_element(By.ID, "id_end_date")
        end_date_field.send_keys("12/12/2027 15:00")

        description_field = self.selenium.find_element(By.ID, "id_description")
        description_field.send_keys("My Description")

        create_by_field = Select(self.selenium.find_element(By.ID, "id_created_by"))
        create_by_field.select_by_visible_text(self.user.username)

        type_field = self.selenium.find_element(By.ID, "id_type")
        type_field.send_keys("Cinema")

        price_field = self.selenium.find_element(By.ID, "id_price")
        price_field.send_keys("290.45")

        location_field = self.selenium.find_element(By.ID, "id_location")
        location_field.send_keys("Praha 1")

        region_field = Select(self.selenium.find_element(By.ID, "id_region"))
        region_field.select_by_visible_text("Praha")

        submit_button = self.selenium.find_element(By.XPATH, "/html/body/div/form/button")
        submit_button.click()

        self.selenium.get(self.live_server_url)

        event_name_element = self.selenium.find_element(By.XPATH, "/html/body/div/div/div/h5")
        self.assertEqual(event_name_element.text, "Foo")

        event_description_element = self.selenium.find_element(By.XPATH, "/html/body/div/div/div/p")
        self.assertEqual(event_description_element.text, "My Description")
