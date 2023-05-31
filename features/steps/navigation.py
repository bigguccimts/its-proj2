from behave import given, when, then
from selenium.webdriver.common.by import By


@given(u'the user is on a page where the Categories navigation bar is displayed')
def step_impl(context):
    context.driver.get("http://opencart:8080/")


@when(u'the user hovers mouse on desired category')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Desktops").click()


@when(u'the user clicks on an item from the displayed dropdown menu displayed')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Mac (1)").click()


@then(u'the user will be redirected to a page containing all products from that category')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h2").text == "Mac"
