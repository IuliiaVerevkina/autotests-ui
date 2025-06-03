import time
import pytest
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage

@pytest.mark.regression
@pytest.mark.registration
class TestRegistration:
    def test_fill_successful_registration_form(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        unique_email = f"user{int(time.time())}@gmail.com"
        username = "testuser"
        password = "TestPassword123!"
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.fill(email=unique_email, username=username, password=password)
        registration_page.registration_form.check_visible(email=unique_email, username=username, password=password)
        registration_page.click_registration_button()

        dashboard_page.dashboard_component.check_visible()