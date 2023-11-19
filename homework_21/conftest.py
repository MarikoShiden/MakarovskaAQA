import pytest
from selenium.webdriver import Chrome

from pages.dashboard import MainPage
from pages.category import Category
from pages.sub_category import SubCategory
from pages.item_page import ItemPage
from pages.registration import Registration


@pytest.fixture()
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def main_page(driver):
    driver.get('https://militarist.ua/ua/')
    yield MainPage()


@pytest.fixture()
def category(driver):
    driver.get('https://militarist.ua/ua/catalog/shoes/')
    yield Category()


@pytest.fixture()
def sub_category(driver):
    driver.get('https://militarist.ua/ua/catalog/shoes/shoess/krossovki/')
    yield SubCategory()


@pytest.fixture()
def item_page(driver):
    driver.get('https://militarist.ua/ua/catalog/armeyskoe-snaryazhenie/meditsina/gemostaticheskie-sredstva/sam-chito-100-krovospinna-gubka-10kh10-sm/')
    yield ItemPage


@pytest.fixture()
def registration(driver):
    pass
