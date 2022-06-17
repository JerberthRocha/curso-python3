from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

chrome = webdriver.Chrome(ChromeDriverManager().install())

chrome.get('https://github.com/')


try:
    btn_sign_up = chrome.find_element(By.LINK_TEXT, 'Sign up')
    btn_sign_up.click()
    sleep(2)
    input_email = chrome.find_element(By.ID, 'email') 
    input_email.send_keys('email@email.com.br')
    sleep(2)
    btn_continue = chrome.find_element(By.CSS_SELECTOR, 'button')
    btn_continue.click()
    sleep(2)
    # input_senha = chrome.find_element_by_id('password') # SINTAXE ANTIGA
    input_senha = chrome.find_element(By.ID, 'password') # SINTAXE NOVA
    input_senha.send_keys('@Corenam23')
except Exception as e:
    print('Não foi possivel clicar em Sign up. Erro:', e)

sleep(2)
chrome.quit()
