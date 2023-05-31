#!/usr/bin/env python3
from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time


@fixture
def del_users(context):
    context.driver.implicitly_wait(1)
    context.driver.get(
        "http://opencart:8080/administration/index.php?route=common/login")
    context.driver.find_element(By.ID, "input-username").click()
    context.driver.find_element(By.ID, "input-username").send_keys("user")
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys("bitnami")
    context.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    context.driver.find_element(
        By.CSS_SELECTOR, ".col-lg-3:nth-child(3) a").click()
    context.driver.find_element(By.CSS_SELECTOR, ".form-check-input").click()
    context.driver.find_element(By.CSS_SELECTOR, ".btn-danger").click()
    assert context.driver.switch_to.alert.text == "Are you sure?"
    context.driver.switch_to.alert.accept()
    try:
        WebDriverWait(context.driver, 2).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".btn-close"))).click()
    except:
        context.driver.find_element(
            By.CSS_SELECTOR, "#nav-logout .d-none").click()


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


def get_driver():
    '''Get Chrome/Firefox driver from Selenium Hub'''
    try:
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
    except WebDriverException:
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX)
    driver.implicitly_wait(5)

    # Web stranku ziskate nasledujicim:
    # (jedno nebo druhe, zalezi na nastaveni prostedi)
    # driver.get("http://opencart:8080/")
    # driver.get("http://localhost:8080/")

    return driver

    # Nezapomente vzdy po ukonceni testovani zavrit driver:
    # driver.close() nebo .quit()


def before_all(context):
    # waiting until docker is loaded up
    time.sleep(60)
    context.driver = get_driver()


def before_scenario(context, scenario):
    context.driver.implicitly_wait(2)
    # deleting created users after every scenario
    use_fixture(del_users, context)


def after_feature(context, feature):
    # deleting created orders after every feature
    use_fixture(del_orders, context)


def after_all(context):
    context.driver.quit()
