from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
import pytest 
import os
import json

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, base_url):
    return {
        **browser_context_args,
        "base_url": base_url                              
    }
    
@pytest.fixture(scope="session")
def credentials():
    config_path = os.path.join(os.path.dirname(__file__), "test_data.json")
    with open(config_path,"r", encoding="utf-8") as f:
        return json.load(f)

@pytest.fixture()
def admin_page(page,credentials):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(
        username = credentials["users"]["admin"]["username"],
        password = credentials["users"]["admin"]["password"])
    return page
    