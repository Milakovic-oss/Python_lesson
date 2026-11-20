from pages.calculator_page import CalculatorPage


def test_calculator(driver):
    # создаем объект страницыб передавая драйвер из conftest.py
    calc_page = CalculatorPage(driver)
    calc_page.open()

    # вводим задержку 45
    calc_page.set_delay(45)

    # нажимаем кнопки по очереди
    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    # ждем появления 45
    # проверяем, что результат действительно 15
    actual_result = calc_page.wait_for_result("15")
    assert actual_result == "15", f"Ожидали 15, получили {actual_result}"
