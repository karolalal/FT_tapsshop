from tests.helpers.support_functions import *

taps_logo = '//*[@id="masthead"]/div[1]/div[1]/a/img'

my_account_page_header_link = 'menu-item-100'
cart_page_header_link = 'menu-item-99'
add_hoodie_to_card = '//*[@id="post-83"]/div/div[3]/ul/li[3]/div[2]/a'
go_to_cart_under_item = '//*[@id="post-83"]/div/div[3]/ul/li[3]/div[2]/a[2]'
cart_button_header = 'site-header-cart'


def taps_logo_visible(driver_instance):
    elem = wait_for_visibility_of_element_xpatch(driver_instance, taps_logo)
    return elem.is_displayed()


def go_to_login_page(driver_instance):
    wait_for_visibility_of_element(driver_instance, my_account_page_header_link)
    driver_instance.find_element(By.ID, my_account_page_header_link).click()


def add_item_to_cart(driver_instance):
    driver_instance.find_element(By.XPATH, add_hoodie_to_card).click()


def go_to_cart_page(driver_instance):
    wait_for_visibility_of_element_xpatch(driver_instance, go_to_cart_under_item)
    driver_instance.find_element(By.XPATH, go_to_cart_under_item).click()
