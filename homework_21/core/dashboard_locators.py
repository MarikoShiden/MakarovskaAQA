from homework_21.core.base_locators import BaseLocator


class DashBoardLocator(BaseLocator):
    def __init__(self):
        super().__init__()
        self.shoes_category = "//a[text()='Взуття']"
        self.search_field = "//*[@id='title-search-input']"
        self.registration_form = "//div[@class='user-login']//a[text()='Реєстрація']"

