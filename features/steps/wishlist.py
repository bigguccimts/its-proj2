from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@given(u'the application is at the homepage')
def step_impl(context):
    context.driver.get("http://opencart:8080/")


@given(u'the user is not logged in')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, "//nav[@id='top']/div/div[2]/ul/li[2]/div/a/span").click()
    time.sleep(1)
    context.driver.find_element(By.LINK_TEXT, "Login").click()
    assert context.driver.find_element(
        By.CSS_SELECTOR, "#form-login > h2").text == "Returning Customer"


@when(u'the user clicks on Add to Wish List button')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb/product/iphone")
    context.driver.find_element(By.CSS_SELECTOR, ".btn > .fa-heart").click()


@then(u'he will be prompted to create an account or log in')
def step_impl(context):
    alert = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert"))).text
    assert alert == 'You must login or create an account to save iPhone to your wish list!'


@given(u'the user is logged in')
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


@then(u'the item will be added to his Wish List')
def step_impl(context):
    alert = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert"))).text
    assert alert == 'Success: You have added iPhone to your wish list!'


@given(u'the user is in their Wishlist page')
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

    context.driver.get("http://opencart:8080/en-gb/product/iphone")
    context.driver.find_element(By.CSS_SELECTOR, ".btn > .fa-heart").click()

    alert = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert"))).text
    assert alert == 'Success: You have added iPhone to your wish list!'

    context.driver.get("http://opencart:8080")
    context.driver.find_element(
        By.XPATH, "//a[@id='wishlist-total']/span").click()


@given(u'the user has items in their Wishlist')
def step_impl(context):
    pass


@when(u'the user clicks on the Add to cart button')
def step_impl(context):
    context.driver.find_element(
        By.CSS_SELECTOR, ".btn-primary > .fa-solid").click()
    context.driver.find_element(
        By.LINK_TEXT, "Continue").click()


@when(u'the user clicks on the Remove button')
def step_impl(context):
    context.driver.find_element(
        By.CSS_SELECTOR, ".btn-danger").click()


@then(u'the products will be removed from the Wishlist')
def step_impl(context):
    alert = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert"))).text
    assert alert == 'Success: You have removed an item from your wishlist'
    assert context.driver.find_element(
        By.XPATH, "//div[@id='wishlist']/p").text == "Your wish list is empty."
