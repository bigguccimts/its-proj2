from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@given(u'the admin has clicked on the Catalog item in the navigation menu')
def step_impl(context):
    context.driver.find_element(
        By.LINK_TEXT, "Catalog").click()


@when(u'the admin clicks on the Products item in the dropdown menu')
def step_impl(context):
    context.driver.find_element(
        By.LINK_TEXT, "Products").click()


@then(u'list of all products will be displayed')
def step_impl(context):
    assert context.driver.find_element(
        By.CSS_SELECTOR, ".col .card-header").text == "Product List"


@given(u'the list of all products is displayed')
def step_impl(context):
    context.driver.find_element(
        By.LINK_TEXT, "Catalog").click()

    context.driver.find_element(
        By.LINK_TEXT, "Products").click()

    assert context.driver.find_element(
        By.CSS_SELECTOR, ".col .card-header").text == "Product List"


@given(u'the list is not empty')
def step_impl(context):
    assert context.driver.find_element(
        By.CSS_SELECTOR, ".col-sm-6:nth-child(2)").text == "Showing 1 to 10 of 19 (2 Pages)"


@when(u'the admin clicks on the blue edit button with the pencil')
def step_impl(context):
    context.driver.find_element(
        By.CSS_SELECTOR, "tr:nth-child(1) .fa-pencil").click()


@then(u'the admin will be able to edit the product')
def step_impl(context):
    assert context.driver.find_element(
        By.CSS_SELECTOR, ".card-header").text == "Edit Product"


@given(u'the product edit page is displayed')
def step_impl(context):
    context.driver.find_element(
        By.LINK_TEXT, "Catalog").click()
    context.driver.find_element(
        By.LINK_TEXT, "Products").click()
    context.driver.find_element(
        By.CSS_SELECTOR, "tr:nth-child(1) .fa-pencil").click()
    assert context.driver.find_element(
        By.CSS_SELECTOR, ".card-header").text == "Edit Product"


@when(u'the user clicks on Data')
def step_impl(context):
    context.driver.find_element(
        By.LINK_TEXT, "Data").click()


@when(u'changes the quantity of the product')
def step_impl(context):
    context.driver.find_element(
        By.ID, "input-quantity").send_keys(Keys.BACK_SPACE)
    context.driver.find_element(
        By.ID, "input-quantity").send_keys(Keys.BACK_SPACE)
    context.driver.find_element(
        By.ID, "input-quantity").send_keys(Keys.BACK_SPACE)
    context.driver.find_element(
        By.ID, "input-quantity").send_keys(Keys.BACK_SPACE)
    context.driver.find_element(By.ID, "input-quantity").send_keys("1")


@when(u'saves the changes')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//body').send_keys(Keys.HOME)
    context.driver.find_element(
        By.CSS_SELECTOR, ".fa-floppy-disk").click()
    alert = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert"))).text
    assert alert == 'Success: You have modified products!'
    time.sleep(5)


@when(u'returns to the product list page')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//body').send_keys(Keys.HOME)
    time.sleep(2)
    context.driver.find_element(
        By.CSS_SELECTOR, ".breadcrumb-item:nth-child(2) > a").click()


@then(u'the updated quantity will be displayed')
def step_impl(context):
    time.sleep(5)
    assert context.driver.find_element(
        By.XPATH, "//form[@id='form-product']/div/table/tbody/tr/td[6]/span").text == '1'
