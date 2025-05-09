from playwright.sync_api import sync_playwright, expect
import time

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    unique_email = f"user{int(time.time())}@gmail.com"
    email_input.fill(unique_email)

    userName_input = page.get_by_test_id('registration-form-username-input').locator('input')
    userName_input.fill("username")

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("password")

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    title_visible_text = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(title_visible_text).to_be_visible()
    expect(title_visible_text).to_have_text("Dashboard")
    page.wait_for_timeout(3000)
