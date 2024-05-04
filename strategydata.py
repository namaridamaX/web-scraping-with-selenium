from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
URL = 'https://www.itpassportsiken.com/word/'

strategy_words = []
strategy_texts = []
strategy_urls = []
driver = webdriver.Chrome()

def selenium():
    driver.get(URL)
    driver.find_elements(By.LINK_TEXT, '企業活動(113)')[0].click()
    sleep(1)
    list_elements = driver.find_elements(By.CLASS_NAME, 'wordLink.cf')
    for list_element in list_elements:
        li_elements = list_element.find_elements(By.TAG_NAME, 'li')
        for li_element in li_elements:
            word = li_element.text
            strategy_words.append(word)
            url = URL + word + '.html'
            strategy_urls.append(url)
    driver.quit()
    print('okokok')
    return strategy_words, strategy_urls

def maketext():
    for strategy_url in strategy_urls:
        driver.get(strategy_url)
        sleep(1)
        text = driver.find_element(By.XPATH, '//*[@id="quizQWrap"]/div').text
        strategy_texts.append(text)
        driver.quit()
    print('okokokok')
    return strategy_texts