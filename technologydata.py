from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
URL = 'https://www.itpassportsiken.com/word/'

technology_words = []
technology_texts = []
technology_urls = []
driver = webdriver.Chrome()

def selenium():
    driver.get(URL)
    driver.find_elements(By.LINK_TEXT, '基礎理論(14)')[0].click()
    sleep(1)
    list_elements = driver.find_elements(By.CLASS_NAME, 'wordLink.cf')
    for list_element in list_elements:
        li_elements = list_element.find_elements(By.TAG_NAME, 'li')
        for li_element in li_elements:
            word = li_element.text
            technology_words.append(word)
            url = URL + word + '.html'
            technology_urls.append(url)
    driver.quit()
    print('ok')
    return technology_words, technology_urls

def maketext():
    for technology_url in technology_urls:
        driver.get(technology_url)
        sleep(1)
        text = driver.find_element(By.XPATH, '//*[@id="quizQWrap"]/div').text
        technology_texts.append(text)
        driver.quit()
    print('okok')
    return technology_texts