from selenium.webdriver.common.by import By

username = 'username'
password = 'password'
login_button = '//*[@id="customer_login"]/div[1]/form/p[3]/button'

proper_email1 = 'cotaga1249@maillei.net'
proper_password1 = 'VRrMhK8MqFyd'

proper_email2 = 'wowen49501@maillei.net'
proper_password2 = 'lxsg#GAqH$Ke'

proper_email3 = 'bomineg967@onmail3.com'
proper_password3 = 'zedvu@##)CZy'

proper_email4 = 'wacog70401@tinkmail.net'
proper_password4 = 'Lk*3Q9&am3zL'

proper_email5 = 'calose2528@maillei.net'
proper_password5 = 'lkSb&SAJwLWo'


def correct_login(driver_instance):
    elem = driver_instance.find_element(By.ID, username)
    elem.send_keys(proper_email1)
    elem1 = driver_instance.find_element(By.ID, password)
    elem1.send_keys(proper_password1)
    elem2 = driver_instance.find_element(By.XPATH, login_button)
    elem2.click()

