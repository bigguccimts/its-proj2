from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from behave import fixture, use_fixture
from selenium.webdriver.support import expected_conditions as EC
import time


@fixture
def del_orders(context):
    context.driver.implicitly_wait(5)
    context.driver.get(
        "http://opencart:8080/administration/index.php?route=common/login")
    context.driver.find_element(By.ID, "input-username").click()
    context.driver.find_element(By.ID, "input-username").send_keys("user")
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys("bitnami")
    context.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    context.driver.find_element(
        By.CSS_SELECTOR, ".col-lg-3:nth-child(1) a").click()
    context.driver.find_element(By.CSS_SELECTOR, ".form-check-input").click()
    context.driver.find_element(By.CSS_SELECTOR, ".fa-trash-can").click()
    assert context.driver.switch_to.alert.text == "Are you sure?"
    context.driver.switch_to.alert.accept()
    try:
        WebDriverWait(context.driver, 2).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".btn-close"))).click()
    except:
        context.driver.find_element(
            By.CSS_SELECTOR, "#nav-logout .d-none").click()


@given(u'the admin is logged in the administration page')
def step_impl(context):
    use_fixture(del_orders, context)
    time.sleep(1)
    context.driver.get(
        "http://opencart:8080/administration/")
    context.driver.find_element(By.ID, "input-username").click()
    context.driver.find_element(By.ID, "input-username").send_keys("user")
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys("bitnami")
    context.driver.find_element(By.CSS_SELECTOR, ".btn").click()


@given(u'the admin is at the dashboard page')
def step_impl(context):
    pass


@when(u'the admin clicks the View more button on the total customers image')
def step_impl(context):
    context.driver.find_element(
        By.CSS_SELECTOR, ".col-lg-3:nth-child(3) a").click()


@then(u'the list of all customers will be displayed')
def step_impl(context):
    assert context.driver.find_element(
        By.CSS_SELECTOR, "tbody .text-center").text == "No results!"


@given(u'the list of all customers is displayed')
def step_impl(context):
    time.sleep(1)
    context.driver.get("http://opencart:8080/en-gb?route=account/register")
    time.sleep(1)
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

    context.driver.get(
        "http://opencart:8080/administration/index.php?route=common/login")
    context.driver.find_element(By.ID, "input-username").click()
    context.driver.find_element(By.ID, "input-username").send_keys("user")
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys("bitnami")
    time.sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, ".btn").click()

    context.driver.find_element(
        By.CSS_SELECTOR, ".col-lg-3:nth-child(3) a").click()


@when(u'the admin clicks on the Edit button')
def step_impl(context):
    context.driver.find_element(
        By.CSS_SELECTOR, ".fa-pencil").click()


@then(u'the admin will be able to edit the customer data')
def step_impl(context):
    assert context.driver.find_element(
        By.CSS_SELECTOR, ".card-header").text == "Edit Customer"
