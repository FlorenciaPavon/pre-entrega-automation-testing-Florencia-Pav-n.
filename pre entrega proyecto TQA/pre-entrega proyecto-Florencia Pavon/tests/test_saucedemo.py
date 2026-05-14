import pytest
from utils.helpers import login

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login(driver):
    login(driver, "standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url

    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title=="Products"

def test_inventario_nombre(driver):
    login(driver, "standard_user", "secret_sauce")

    title = driver.find_element(By.CLASS_NAME, "app_logo").text
    assert title == "Swag Labs"

@pytest.mark.productos
def test_catalogo_productos(driver):
    login(driver, "standard_user", "secret_sauce")

    title = driver.find_element(By.CSS_SELECTOR,'div.header_secondary_container .title').text
    assert title=="Products"

    productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(productos) > 0
    assert productos[0].is_displayed()

    print(f'Se encontraron {len(productos)} productos.')


def test_interfaz (driver):
    login(driver, "standard_user", "secret_sauce")

    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu.is_displayed()

    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filtro.is_displayed()

    carrito_icono = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    assert carrito_icono.is_displayed()

    print("Interfaz validada correctamente")
    


def test_agregar_carrito(driver):
    login(driver, "standard_user", "secret_sauce")

    wait= WebDriverWait(driver, 10)    
    
    btn_add = wait.until (
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )    
    btn_add.click()

    #validar contador
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert badge == "1"

    #encontrar el producto
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    producto_agregado = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    producto_agregado_nombre = producto_agregado.text
    assert producto_agregado.is_displayed()
    assert producto_agregado_nombre != ""
    assert producto_agregado_nombre == "Sauce Labs Backpack"

    