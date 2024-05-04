from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
URL = 'https://www.itpassportsiken.com/word/'

management_words = []
management_texts = []
management_urls = []
driver = webdriver.Chrome()

def selenium():
    driver.get(URL)
    driver.find_elements(By.LINK_TEXT, 'システム開発技術(21)')[0].click()
    sleep(1)
    list_elements = driver.find_elements(By.CLASS_NAME, 'wordLink.cf')
    for list_element in list_elements:
        li_elements = list_element.find_elements(By.TAG_NAME, 'li')
        for li_element in li_elements:
            word = li_element.text
            management_words.append(word)
            url = URL + word + '.html'
            management_urls.append(url)
    driver.quit()
    print('okokokokok')        
    return management_words, management_urls

def maketext():
    for management_url in management_urls:
        driver.get(management_url)
        sleep(1)
        text = driver.find_element(By.XPATH, '//*[@id="quizQWrap"]/div').text
        management_texts.append(text)
        driver.quit()
        sleep(1)
    print('okokokokokok')
    return management_texts