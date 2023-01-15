from tests.helpers.support_functions import *

my_account_details_tab = '//*[@id="post-9"]/div/div/nav/ul/li[5]/a'


def my_account_header_visible(driver_instance):
    elem = wait_for_visibility_of_element_xpatch(driver_instance, my_account_details_tab)
    return elem.is_displayed()



