from behave import given, when, then
from selenium.webdriver.common.by import By


@given(u'application is at a page where search bar is displayed')
def step_impl(context):
    context.driver.get("http://opencart:8080/")


@when(u'the user enters {query} into the search bar')
def step_impl(context, query):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys(query)
    context.driver.find_element(By.CSS_SELECTOR, ".btn-light").click()


@then(u'products that match the searched {query} are displayed')
def step_impl(context, query):
    assert context.driver.find_element(
        By.CSS_SELECTOR, "h1").text == ('Search - '+query)


@then(u'no products matching the criteria will be shown')
def step_impl(context):
    assert context.driver.find_element(
        By.CSS_SELECTOR, "p:nth-child(7)").text == "There is no product that matches the search criteria."
