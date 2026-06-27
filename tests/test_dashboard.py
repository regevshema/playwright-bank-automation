from pages.dashboard_page import DashboardPage
from playwright.sync_api import Page, expect
import re

def test_dashboard_sanity(admin_page):
    dashboard = DashboardPage(admin_page)
    expect(admin_page).to_have_url(re.compile(dashboard.url_path))
    

def test_dashboard_initial_balance(admin_page):
    dashboard = DashboardPage(admin_page)
    current_balance = dashboard.get_total_balance()
    assert current_balance > 0

def test_withdraw_money_success(admin_page, credentials):
    dashboard = DashboardPage(admin_page)
    
    admin_page.wait_for_timeout(3000)
    initial_balance = dashboard.get_total_balance()
    withdraw_amount = float(credentials["users"]["admin"]["withdraw_amount"])
    
    dashboard.withdraw_money(withdraw_amount)
    dashboard.navigate_to_dashboard()
    
    expected_balance = initial_balance - withdraw_amount
    formatted_expected_balance = f"{expected_balance:,.2f}"
    
    expect(dashboard.total_balance).to_contain_text(formatted_expected_balance)
    
def test_withdraw_money_insufficient_funds(admin_page, credentials):
    dashboard = DashboardPage(admin_page)
    
    admin_page.wait_for_timeout(1500)
    invalid_amount = float(credentials["users"]["admin"]["insufficient_withdraw_amount"])
    
    dashboard.withdraw_fail(invalid_amount)
    
    expect(dashboard.transaction_alert).to_be_visible()
    expect(dashboard.transaction_alert).to_contain_text("Insufficient balance for this transaction")
    
def test_deposit_money(admin_page, credentials):
    dashboard = DashboardPage(admin_page)
    
    admin_page.wait_for_timeout(3000)
    initial_balance = dashboard.get_total_balance()
    deposit_amount = float(credentials["users"]["admin"]["deposit_amount"])
    
    dashboard.deposit_money(deposit_amount)
    
    expected_balance = initial_balance + deposit_amount
    formatted_expected_balance = f"{expected_balance:,.2f}"
    
    expect(dashboard.total_balance).to_contain_text(formatted_expected_balance)
    
def test_successful_transfer_primary_to_secondary(admin_page, credentials):
    dashboard = DashboardPage(admin_page)
    
    admin_page.wait_for_timeout(3000)
    initial_balance = dashboard.get_primary_balance()
    transfer_amount = float(credentials["users"]["admin"]["transfer_amount"])
    
    dashboard.transfer_money_primary_to_secondary(transfer_amount)
    
    expected_balance = initial_balance - transfer_amount
    formatted_expected_balance = f"{expected_balance:,.2f}"
    
    expect(dashboard.primary_balance).to_contain_text(formatted_expected_balance)
    
def test_successful_transfer_secondary_to_primary(admin_page, credentials):
    dashboard = DashboardPage(admin_page)
    
    admin_page.wait_for_timeout(3000)
    initial_balance = dashboard.get_secondary_balance()
    transfer_amount = float(credentials["users"]["admin"]["transfer_amount"])
    
    dashboard.transfer_money_secondary_to_primary(transfer_amount)
    
    expected_balance = initial_balance - transfer_amount
    formatted_expected_balance = f"{expected_balance:,.2f}"
    
    expect(dashboard.secondary_balance).to_contain_text(formatted_expected_balance)
    

    

    
   