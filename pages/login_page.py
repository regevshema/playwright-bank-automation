from playwright.sync_api import Page

class LoginPage:
    
    def __init__(self, page: Page):
        self.page = page
        self.url_path = ""
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_test_id("password-input")
        self.login_button = page.get_by_test_id("login-button")
        self.username_display = self.page.locator("#username-display")
        
    
        
    
    def navigate(self):
        self.page.goto(self.url_path)
        
    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        
    def get_displayed_username(self) -> str:
        return self.username_display.inner_text()