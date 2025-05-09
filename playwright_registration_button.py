from playwright.sync_api import sync_playwright, expect
import time

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_button_disabled = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button_disabled).to_be_disabled()

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    unique_email = f"user{int(time.time())}@gmail.com"
    email_input.fill(unique_email)

    user_name_input = page.get_by_test_id('registration-form-username-input').locator('input')
    user_name_input.fill("username")

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("password")

    registration_button_enabled = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button_enabled).not_to_be_disabled()

