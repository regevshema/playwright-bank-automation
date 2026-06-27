from playwright.sync_api import Page
from pages.login_page import LoginPage
from playwright.sync_api import expect
import re

def test_valid_login(page:Page, credentials):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(
        username = credentials["users"]["admin"]["username"],
        password = credentials["users"]["admin"]["password"]
    )
    expect(page).to_have_url(re.compile("/dashboard"))
    
def test_admin_user_login(page:Page, credentials):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(
        username = credentials["users"]["admin"]["username"],
        password = credentials["users"]["admin"]["password"]
    )
    expect(login_page.username_display).to_have_text(credentials["users"]["admin"]["username"])
    
