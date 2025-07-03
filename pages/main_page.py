import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    @allure.step('Ожидание прогрузки кнопки "Заказать" в хэдере')
    def wait_for_visibility_order_button_in_header(self):
        self.wait_visibility_of_element(MainPageLocators.order_button_in_header)

    @allure.step('Кликнуть по кнопке заказать')
    def click_on_order_button_in_header(self):
        self.click_element(MainPageLocators.order_button_in_header)

    @allure.step('Ожидание прогрузки части лого с надписью "Самокат" в хэдере.')
    def wait_visibility_of_header_logo_scooter(self):
        self.wait_visibility_of_element(MainPageLocators.header_logo_scooter)

    @allure.step('Ожидание прогрузки части лого с надписью "Яндекс" в хэдере.')
    def wait_visibility_of_header_logo_yandex(self):
        self.wait_visibility_of_element(MainPageLocators.header_logo_yandex)

    @allure.step('Кликнуть по части лого с надписью "Самокат" в хэдере.')
    def click_on_header_logo_scooter(self):
        self.click_element(MainPageLocators.header_logo_scooter)

    @allure.step('Кликнуть по части лого с надписью "Яндекс" в хэдере.')
    def click_on_header_logo_yandex(self):
        self.click_element(MainPageLocators.header_logo_yandex)

    @allure.step('Ожидание прогрузки отображения заголовка главной страницы.')
    def wait_visibility_of_main_header(self):
        self.wait_visibility_of_element(MainPageLocators.main_header)

    @allure.step('Проверить отображение заголовка главной страницы')
    def check_displaying_of_main_header(self):
        return self.check_displaying_of_element(MainPageLocators.main_header)

    @allure.step('Проскролить до секции "Вопросы о важном".')
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocators.faq_section)

    @allure.step('Подождать прогрузку нужного номера вопроса в аккордеоне "Вопросы о важном".')
    def wait_visibility_of_faq_items(self, data):
        self.wait_visibility_of_element(MainPageLocators.faq_questions_items[data])

    @allure.step('Кликнуть на нужный номер вопроса в аккордеоне "Вопросы о важном".')
    def click_on_faq_items(self, data):
        self.click_element(MainPageLocators.faq_questions_items[data])

    @allure.step('Подождать прогрузку нужного номера ответа в аккордеоне "Вопросы о важном".')
    def wait_visibility_of_faq_answer(self, data):
        self.wait_visibility_of_element(MainPageLocators.faq_answers_items[data])

    @allure.step('Получить текст нужного ответа в аккордеоне "Вопросы о важном".')
    def get_displayed_text_from_faq_answer(self, data):
        return self.get_text_on_element(MainPageLocators.faq_answers_items[data])






