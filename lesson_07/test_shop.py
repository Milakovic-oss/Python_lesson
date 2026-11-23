from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_buy_items(driver):
    # авторизуемся
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # добавляем товары и идем в корзину
    main_page = MainPage(driver)
    main_page.add_backpack_to_cart()
    main_page.add_t_shirt_to_cart()
    main_page.add_onesie_to_cart()
    main_page.get_to_cart()

    # проверяем количество товаров корзины
    # (должно быть 3) и нажимаем checkout
    cart_page = CartPage(driver)
    items = cart_page.get_cart_item()
    assert len(items) == 3
    cart_page.click_checkout()

    # заполняем форму и нажимаем continue
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Ирина", "Милакович", "123456")
    checkout_page.click_continue()

    # получаем итоговую стоимость и проверяем
    total = checkout_page.get_total_amount()
    print(f"Итоговая сумма: {total}")

    # проверяем, что в тексте нужная сумма
    assert "58.29" in total
