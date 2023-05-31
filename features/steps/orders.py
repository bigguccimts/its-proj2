from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import fixture, use_fixture
import time


@fixture
def create_order(context):
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
    time.sleep(1)
    context.driver.get("http://opencart:8080/")
    context.driver.find_element(
        By.CSS_SELECTOR, ".col:nth-child(2) .img-fluid").click()
    context.driver.find_element(By.ID, "button-cart").click()
    context.driver.get("http://opencart:8080//en-gb?route=checkout/checkout")
    context.driver.find_element(By.ID, "input-shipping-firstname").click()
    context.driver.find_element(
        By.ID, "input-shipping-firstname").send_keys("test")
    context.driver.find_element(By.ID, "input-shipping-lastname").click()
    context.driver.find_element(
        By.ID, "input-shipping-lastname").send_keys("test")
    context.driver.find_element(By.ID, "input-shipping-address-1").click()
    context.driver.find_element(
        By.ID, "input-shipping-address-1").send_keys("test 33")
    context.driver.find_element(By.ID, "input-shipping-city").click()
    context.driver.find_element(
        By.ID, "input-shipping-city").send_keys("Bratislava")
    context.driver.find_element(By.ID, "input-shipping-postcode").click()
    context.driver.find_element(
        By.ID, "input-shipping-postcode").send_keys("12345")
    context.driver.find_element(By.ID, "input-shipping-country").click()
    dropdown = context.driver.find_element(By.ID, "input-shipping-country")
    dropdown.find_element(By.XPATH, "//option[. = 'Slovak Republic']").click()
    context.driver.find_element(By.ID, "input-shipping-zone").click()
    dropdown = context.driver.find_element(By.ID, "input-shipping-zone")
    dropdown.find_element(By.XPATH, "//option[. = 'Bratislavský']").click()
    context.driver.find_element(By.ID, "button-shipping-address").click()
    context.driver.find_element(By.ID, "button-shipping-methods").click()
    context.driver.find_element(
        By.XPATH, "//form[@id='form-shipping-method']/div/input").click()
    context.driver.find_element(By.ID, "button-shipping-method").click()
    context.driver.find_element(By.ID, "button-payment-methods").click()
    context.driver.find_element(
        By.XPATH, "//form[@id='form-payment-method']/div/input").click()
    context.driver.find_element(By.ID, "button-payment-method").click()
    context.driver.find_element(By.XPATH, '//body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    context.driver.find_element(By.ID, "button-confirm").click()
    context.driver.find_element(By.LINK_TEXT, "Continue").click()


@given(u'the main dashboard page is displayed')
def step_impl(context):
    pass


@when(u'the admin clicks on the view more button on the total orders image')
def step_impl(context):
    context.driver.find_element(
        By.CSS_SELECTOR, ".col-lg-3:nth-child(1) a").click()


@then(u'list of all orders will be displayed')
def step_impl(context):
    assert context.driver.find_element(
        By.CSS_SELECTOR, ".col-lg-9 .card-header").text == "Order List"


@given(u'the list of orders is displayed')
def step_impl(context):
    use_fixture(create_order, context)


@when(u'the admin clicks on the blue button with eye')
def step_impl(context):
    context.driver.get(
        "http://opencart:8080/administration/")
    context.driver.find_element(By.ID, "input-username").click()
    context.driver.find_element(By.ID, "input-username").send_keys("user")
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys("bitnami")
    context.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    context.driver.find_element(
        By.CSS_SELECTOR, ".col-lg-3:nth-child(1) a").click()
    assert context.driver.find_element(
        By.CSS_SELECTOR, ".col-lg-9 .card-header").text == "Order List"
    context.driver.find_element(
        By.CSS_SELECTOR, "tr:nth-child(1) .fa-solid").click()


@then(u'the order details will be displayed')
def step_impl(context):
    assert context.driver.find_element(
        By.CSS_SELECTOR, ".card:nth-child(1) > .card-header")


@given(u'the order details page is displayed')
def step_impl(context):
    use_fixture(create_order, context)
    context.driver.get(
        "http://opencart:8080/administration/")
    context.driver.find_element(By.ID, "input-username").click()
    context.driver.find_element(By.ID, "input-username").send_keys("user")
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys("bitnami")
    context.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    context.driver.find_element(
        By.CSS_SELECTOR, ".col-lg-3:nth-child(1) a").click()
    assert context.driver.find_element(
        By.CSS_SELECTOR, ".col-lg-9 .card-header").text == "Order List"
    context.driver.find_element(
        By.CSS_SELECTOR, "tr:nth-child(1) .fa-solid").click()
    assert context.driver.find_element(
        By.CSS_SELECTOR, ".card:nth-child(1) > .card-header")


@given(u'the admin changes details of the order')
def step_impl(context):
    context.driver.find_element(
        By.CSS_SELECTOR, ".col:nth-child(1) .float-end > .fa-solid").click()
    context.driver.find_element(
        By.ID, "input-comment").click()
    context.driver.find_element(By.ID, "input-comment").send_keys("asdf")
    context.driver.find_element(
        By.ID, "input-comment").click()
    context.driver.find_element(
        By.CSS_SELECTOR, "#modal-comment .btn-close").click()


@when(u'the admin clicks on the "Confirm" button')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    context.driver.find_element(
        By.ID, "button-confirm").click()


@then(u'the order details will be updated')
def step_impl(context):
    alert = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert"))).text
    assert alert == "Success: You have modified orders!"
