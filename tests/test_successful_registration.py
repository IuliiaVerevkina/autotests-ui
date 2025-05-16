import time
import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

@pytest.mark.regression
def test_fill_successful_registration_form(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    unique_email = f"user{int(time.time())}@gmail.com"
    username = "testuser"
    password = "TestPassword123!"
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form(email=unique_email, username=username, password=password)
    registration_page.click_registration_button()

    dashboard_page.check_visible_dashboard_title()