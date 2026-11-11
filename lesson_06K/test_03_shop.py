from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop(driver):
    wait = WebDriverWait(driver, 10)

# Откройте сайт магазина: https://www.saucedemo.com/ в FireFox.
    driver.get("https://www.saucedemo.com/")

# Авторизуйтесь как пользователь standard_user
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

# Добавьте в корзину товары: Sauce Labs Backpack,
# Sauce Labs Bolt T-Shirt,
# Sauce Labs Onesie.
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

# Перейдите в корзину.
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

# Нажмите Checkout.
    wait.until(EC.element_to_be_clickable(
        (By.ID, "checkout"))
    ).click()

# Заполните форму своими данными: # имя, фамилия, почтовый индекс.
    driver.find_element(By.ID, "first-name").send_keys("Irina")
    driver.find_element(By.ID, "last-name").send_keys("Milakovich")
    driver.find_element(By.ID, "postal-code").send_keys("629500")

# Нажмите кнопку Continue.
    driver.find_element(By.ID, "continue").click()

# Прочитайте со страницы итоговую стоимость (Total).
    total_element = wait.until(EC.presence_of_element_located((
        By.CLASS_NAME, "summary_total_label"))
    )

# Проверьте, что итоговая сумма равна $58.29
    total_text = total_element.text
    assert "$58.29" in total_text
