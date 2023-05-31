from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@given(u'the user has created an account before with "<email>" and "<password>"')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=account/register")
    context.driver.find_element(By.ID, "input-firstname").click()
    context.driver.find_element(By.ID, "input-firstname").send_keys("test")
    context.driver.find_element(By.ID, "input-lastname").click()
    context.driver.find_element(By.ID, "input-lastname").send_keys("test")
    context.driver.find_element(By.ID, "input-email").click()
    context.driver.find_element(
        By.ID, "input-email").send_keys("test@test.com")
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys("test")
    context.driver.find_element(By.NAME, "agree").click()
    context.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    context.driver.find_element(By.LINK_TEXT, "Continue").click()


@given(u'the user is currently not logged in')
def step_impl(context):
    context.driver.get(
        "http://opencart:8080/en-gb?route=account/account&customer_token=20b1afa84baea5fab733f6a2f9")
    context.driver.find_element(By.LINK_TEXT, "Logout").click()
    context.driver.find_element(By.LINK_TEXT, "Continue").click()


@given(u'the user clicked on My Account button')
def step_impl(context):
    context.driver.get(
        "http://opencart:8080/")
    context.driver.find_element(
        By.XPATH, "//nav[@id='top']/div/div[2]/ul/li[2]/div/a/span").click()
    time.sleep(1)


@given(u'the user selected Login from the dropdown menu')
def step_impl(context):
    # context.driver.get("http://opencart:8080/en-gb?route=account/login")
    context.driver.find_element(By.LINK_TEXT, "Login").click()


@given(u'the user filled in the email and password fields')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=account/login")
    context.driver.find_element(By.ID, "input-email").click()
    context.driver.find_element(
        By.ID, "input-email").send_keys("asdf@asdf.com")
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys("asdf")


@when(u'the user clicks on the Continue button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@type=\'submit\']").click()


@then(u'a warning will be displayed')
def step_impl(context):
    alert = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert"))).text
    assert alert != ''


@then(u'the user will not be logged in')
def step_impl(context):
    assert context.driver.find_element(
        By.CSS_SELECTOR, "#form-login > h2").text == "Returning Customer"


@given(u'the user filled in the email and password fields with "test@test.com" and "test"')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=account/login")
    context.driver.find_element(By.ID, "input-email").click()
    context.driver.find_element(
        By.ID, "input-email").send_keys("test@test.com")
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys("test")


@then(u'the user will be logged in')
def step_impl(context):
    assert context.driver.find_element(
        By.XPATH, "//div[@id='content']/h2").text == "My Account"
