from playwright.sync_api import Page

class DashboardPage:
    
    def __init__(self, page: Page):
        self.page = page
        self.url_path = "bank/dashboard"
        self.total_balance = self.page.get_by_test_id("total-balance")
        self.new_transaction_btn = self.page.get_by_test_id("quick-new-transaction")
        self.transaction_type_select = self.page.get_by_test_id("transaction-type-select")
        self.deposit_option = self.page.get_by_label("Deposit").get_by_text("Deposit")
        self.from_account_select = self.page.get_by_test_id("from-account-select")
        self.savings_option = self.page.get_by_role("option", name="Primary Savings")
        self.withdrawal_option = self.page.get_by_role("option", name="Withdrawal")
        self.amount_input = self.page.get_by_test_id("transaction-amount-input")
        self.submit_button = self.page.get_by_test_id("submit-transaction-button")
        self.nav_dashboard = self.page.get_by_test_id("nav-dashboard")
        self.transaction_alert = self.page.get_by_test_id("transaction-alert")
        self.close_transaction_button = self.page.get_by_role("button", name="Close")
        self.logout_button = self.page.get_by_test_id("logout-button")
        
        # --- Transfer Flow Locators ---
        self.transfer_option = self.page.get_by_label("Transfer").get_by_text("Transfer")
        self.to_account_select = self.page.get_by_test_id("to-account-select")
        self.checking_option = self.page.get_by_role("option", name="Checking Account")
        self.transfer_history_cell = self.page.get_by_role("cell", name="Transfer to Checking Account")
        
        # --- Dynamic Balance Locators (Fixed) ---
        self.primary_balance = self.page.locator('[id^="account-balance-id_"]').first
        self.secondary_balance = self.page.locator('[id^="account-balance-id_"]').nth(1)

            
    def get_total_balance(self) -> float:
        raw_text = self.total_balance.inner_text()  
        clean_text = self.get_clean_balance(raw_text)
        return float(clean_text)
    
    def navigate_to_dashboard(self):
        self.nav_dashboard.click()
    
    def get_clean_balance(self, raw_text: str) -> float:
        clean_text = raw_text.replace('$', '').replace(',', '').strip()
        return clean_text
    
    def deposit_money(self, amount: float):
        self.new_transaction_btn.click()
        self.transaction_type_select.click()
        self.deposit_option.click()
        self.from_account_select.click()
        self.savings_option.click()
        self.amount_input.fill(str(amount))
        self.submit_button.click()
        self.navigate_to_dashboard()  
        
    def withdraw_money(self, amount: float):
        self.new_transaction_btn.click()
        self.transaction_type_select.click()
        self.withdrawal_option.click()
        self.from_account_select.click()
        self.savings_option.click()
        self.amount_input.fill(str(amount))
        self.submit_button.click()
        
    def withdraw_fail(self, amount: float):
        self.new_transaction_btn.click()
        self.transaction_type_select.click()
        self.withdrawal_option.click()
        self.from_account_select.click()
        self.savings_option.click()
        self.amount_input.fill(str(amount))
        self.submit_button.click()
        
    def close_transaction_window(self):
        self.close_transaction_button.click()
        
    def logout(self):
        self.logout_button.click()

    def transfer_money_primary_to_secondary(self, amount: float):
        self.new_transaction_btn.click()
        self.transaction_type_select.click()
        self.transfer_option.click()
        self.from_account_select.click()
        self.savings_option.click()
        self.to_account_select.click()
        self.checking_option.click()
        self.amount_input.click()
        self.amount_input.fill(str(amount))
        self.submit_button.click()
        self.navigate_to_dashboard()  
        
    def transfer_money_secondary_to_primary(self, amount: float):
        self.new_transaction_btn.click()
        self.transaction_type_select.click()
        self.transfer_option.click()
        self.from_account_select.click()
        self.checking_option.click()
        self.to_account_select.click()
        self.savings_option.click()
        self.amount_input.click()
        self.amount_input.fill(str(amount))
        self.submit_button.click()
        self.navigate_to_dashboard()
        
    def get_primary_balance(self) -> float:
        raw_text = self.primary_balance.inner_text()
        clean_text = self.get_clean_balance(raw_text)
        return float(clean_text)
    
    def get_secondary_balance(self) -> float:
        raw_text = self.secondary_balance.inner_text()
        clean_text = self.get_clean_balance(raw_text)
        return float(clean_text)