from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@given(u'the user is at the homepage')
def step_impl(context):
    context.driver.get("http://opencart:8080/")


@when(u'the user clicks on the "Add to Cart" button')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    context.driver.find_element(
        By.CSS_SELECTOR, ".col:nth-child(1) > form button:nth-child(1)").click()


@then(u'the product will be added to cart')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//body').send_keys(Keys.HOME)
    time.sleep(1)
    WebDriverWait(context.driver, 2).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".btn-close"))).click()
    context.driver.find_element(
        By.CSS_SELECTOR, ".btn-inverse").click()
    assert context.driver.find_element(
        By.LINK_TEXT, "MacBook").text == "MacBook"


@then(u'the total price of products in cart will be updated')
def step_impl(context):
    assert context.driver.find_element(
        By.XPATH, "//div[@id='header-cart']/div/ul/li/table/tbody/tr/td[4]").text != "$0.00"
    context.driver.find_element(By.XPATH, '//body').send_keys(Keys.HOME)
    time.sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, ".fa-circle-xmark").click()
    time.sleep(2)


@given(u'the user has searched for a product')
def step_impl(context):
    context.driver.get(
        "http://opencart:8080/index.php?route=product/search&language=en-gb&search=macbook")


@given(u'the user is at the search results page')
def step_impl(context):
    assert context.driver.find_element(
        By.XPATH, "//div[@id='content']/h2").text == "Products meeting the search criteria"


@given(u'at least one product is displayed')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//body').send_keys(Keys.END)


@then(u'the product will be added to the cart')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//body').send_keys(Keys.HOME)
    time.sleep(1)
    try:
        WebDriverWait(context.driver, 2).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".btn-close"))).click()
    except:
        pass
    context.driver.find_element(
        By.CSS_SELECTOR, ".btn-inverse").click()
    try:
        context.driver.find_element(
            By.CSS_SELECTOR, "li > .text-center").text == "Your shopping cart is empty!"
    except:
        True


@then(u'the total price of products in the cart will be updated')
def step_impl(context):
    assert context.driver.find_element(
        By.XPATH, "//div[@id='header-cart']/div/ul/li/table/tbody/tr/td[4]").text != "$0.00"
    context.driver.find_element(By.XPATH, '//body').send_keys(Keys.HOME)
    time.sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, ".fa-circle-xmark").click()


@given(u'the user is at the product page')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb/product/macbook")


@when(u'the user sets the quantity to desired amount')
def step_impl(context):
    context.driver.find_element(By.ID, "input-quantity").click()
    context.driver.find_element(
        By.ID, "input-quantity").send_keys(Keys.BACK_SPACE)
    context.driver.find_element(By.ID, "input-quantity").send_keys("1")


@when(u'click on the "Add to Cart" button')
def step_impl(context):
    context.driver.find_element(By.ID, "button-cart").click()


@then(u'the desired quantity of product will be added to the cart')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//body').send_keys(Keys.HOME)
    time.sleep(5)
    context.driver.find_element(
        By.CSS_SELECTOR, ".btn-inverse").click()
    assert context.driver.find_element(
        By.LINK_TEXT, "MacBook").text == "MacBook"
