from pages.dashboard_page import DashboardPage
from playwright.sync_api import Page, expect
import re


def test_logout(admin_page):
    dashboard = DashboardPage(admin_page)
    dashboard.logout()
    expect(admin_page).to_have_url(re.compile(r"/bank"))