from behave import given, then
from selenium.webdriver.common.by import By


@given(u'the user selected Register from the dropdown menu')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Register").click()


@given(u'account with credentials already exists')
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

    context.driver.find_element(By.LINK_TEXT, "Logout").click()
    context.driver.find_element(By.LINK_TEXT, "Continue").click()


@given(u'the user filled in all blank fields')
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


@given(u'the user has not checked the agreement to the Privacy Policy')
def step_impl(context):
    pass


@then(u'the user can not continue with the account creation')
def step_impl(context):
    assert context.driver.find_element(
        By.CSS_SELECTOR, "h1"). text == "Register Account"


@given(u'the user has checked the agreement to the Privacy Policy')
def step_impl(context):
    context.driver.find_element(By.NAME, "agree").click()


@then(u'new account will be created')
def step_impl(context):
    assert context.driver.find_element(
        By.XPATH, "//h1[contains(.,'Your Account Has Been Created!')]").text == "Your Account Has Been Created!"
