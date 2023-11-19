from homework_21.core.base_locators import BaseLocator


class CategoryLocator(BaseLocator):
    def __int__(self):
        self.sort_by_popular = "//a[contains(text(), 'популярності')]"
        self.sort_by_price = "//a[contains(text(), 'ціні')]"
        self.sort_by_promotion = "//a[contains(text(), 'акціям')]"
        self.sort_by_new = "//a[contains(text(), 'новинкам')]"
        self.sort_by_sales = "//a[contains(text(), 'розпродажі')]"
        self.display_15 = "//div[@class='count-filter']/a[contains(text(), '15')]"
        self.display_30 = "//div[@class='count-filter']/a[contains(text(), '30')]"
        self.display_45 = "//div[@class='count-filter']/a[contains(text(), '45')]"
