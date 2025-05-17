import pytest
from playwright.sync_api import expect, Page
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_empty_view()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.click_create_course_button()
