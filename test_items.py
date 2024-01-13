from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestProduct:
    def test_add_to_basket_form(self, browser):
        browser.get(link)
        trash = browser.find_element(By.ID, "add_to_basket_form")
        assert trash.is_enabled(), "Кнопка добавить в корзину отсутствует"
