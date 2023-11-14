import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def test_search_pouch():
    driver = Chrome()
    driver.maximize_window()
    driver.get("https://militarist.ua/ua/")
    slider_carousel_locator = "//*[@class='main-slider-container']"
    assert slider_carousel_locator == "//*[@class='main-slider-container']"
    search_field_locator = "//*[@id='title-search-input']"
    element = driver.find_element("xpath", search_field_locator)
    element.send_keys("підсумок медичний горизонтальний")
    element.send_keys(Keys.ENTER)
    search_result = "//span[contains(text(), 'підсумок медичний горизонтальний')]"
    assert search_result == "//span[contains(text(), 'підсумок медичний горизонтальний')]"
    time.sleep(2)


def test_open_shoes_category():
    driver = Chrome()
    driver.maximize_window()
    driver.get("https://militarist.ua/ua/")
    slider_carousel_locator = "//*[@class='main-slider-container']"
    assert slider_carousel_locator == "//*[@class='main-slider-container']"
    shoes_category_locator = "//a[text()='Взуття']"
    element = driver.find_element("xpath", shoes_category_locator)
    element.click()
    shoes_category = "//h1[text()='Взуття']"
    assert shoes_category == "//h1[text()='Взуття']"
    time.sleep(2)


def test_open_sneakers_category():
    driver = Chrome()
    driver.maximize_window()
    driver.get("https://militarist.ua/ua/")
    slider_carousel_locator = "//*[@class='main-slider-container']"
    assert slider_carousel_locator == "//*[@class='main-slider-container']"
    shoes_category_locator = "//a[text()='Взуття']"
    element = driver.find_element("xpath", shoes_category_locator)
    action = ActionChains(driver)
    action.move_to_element(to_element=element)
    action.perform()
    sneakers_locator = "//a[text()='Кросівки']"
    sneakers = driver.find_element("xpath", sneakers_locator)
    sneakers.click()
    sneakers_category = "//h1[text()='Кросівки']"
    assert sneakers_category == "//h1[text()='Кросівки']"
    time.sleep(2)


def test_open_item():
    driver = Chrome()
    driver.maximize_window()
    driver.get("https://militarist.ua/ua/")
    slider_carousel_locator = "//*[@class='main-slider-container']"
    assert slider_carousel_locator == "//*[@class='main-slider-container']"
    equip_category_locator = "//a[text()='Спорядження та екіпіровка']"
    element = driver.find_element("xpath", equip_category_locator)
    action = ActionChains(driver)
    action.move_to_element(to_element=element)
    action.perform()
    medic_dropdown_menu = "//a[text()='Гемостатичні засоби']"
    hemostatics = driver.find_element("xpath", medic_dropdown_menu)
    hemostatics.click()
    hemostatics_category = "//h1[text()='Гемостатичні засоби']"
    assert hemostatics_category == "//h1[text()='Гемостатичні засоби']"
    hemostatic_item_locator = "//span[text()='SAM Chito 100 кровоспинна губка 10х10 см']"
    hemostatic_item = driver.find_element("xpath", hemostatic_item_locator)
    hemostatic_item.click()
    item_card = "//h1[text()='SAM Chito 100 кровоспинна губка 10х10 см']"
    assert item_card == "//h1[text()='SAM Chito 100 кровоспинна губка 10х10 см']"
    time.sleep(2)


def test_registration_form():
    driver = Chrome()
    driver.maximize_window()
    driver.get("https://militarist.ua/ua/")
    slider_carousel_locator = "//*[@class='main-slider-container']"
    assert slider_carousel_locator == "//*[@class='main-slider-container']"
    registration_form_locator = "//div[@class='user-login']//a[text()='Реєстрація']"
    element = driver.find_element("xpath", registration_form_locator)
    element.click()
    registration_form = "//h5[text()='Реєстрація']"
    assert registration_form == "//h5[text()='Реєстрація']"
    name_locator = "//input[@name='REGISTER[NAME]']"
    name = driver.find_element('xpath', name_locator)
    name.send_keys("test name")
    last_name_locator = "//input[@name='REGISTER[LAST_NAME]']"
    last_name = driver.find_element('xpath', last_name_locator)
    last_name.send_keys("test last name")
    email_locator = "//input[@name='REGISTER[EMAIL]']"
    email = driver.find_element('xpath', email_locator)
    email.send_keys("test@e-mail")
    password_locator = "//input[@name='REGISTER[PASSWORD]']"
    password = driver.find_element('xpath', password_locator)
    password.send_keys("test password")
    confirm_password_locator = "//input[@name='REGISTER[CONFIRM_PASSWORD]']"
    confirm_password = driver.find_element('xpath', confirm_password_locator)
    confirm_password.send_keys("test password")
    phone_number_locator = "//input[@name='REGISTER[PHONE_NUMBER]']"
    phone_number = driver.find_element('xpath', phone_number_locator)
    phone_number.send_keys("123")
    registrate_button = driver.find_element('xpath', "//input[@value='Реєстрація']")
    registrate_button.click()
    time.sleep(2)
    register_error = "//*[@class='errortext']"
    assert register_error == "//*[@class='errortext']"
    time.sleep(2)
