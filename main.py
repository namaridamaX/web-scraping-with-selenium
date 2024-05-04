import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
URL = 'https://www.itpassportsiken.com/word/'



driver = webdriver.Chrome() # Chromeを指定

def main():
    print('start')
    main_words, main_urls = selenium() # 単語とURL取得
    main_texts = maketext(main_urls) # テキスト取得
    makecsv(main_words, main_texts, main_urls, 'management') # csv作成

def makecsv(words, texts, urls, csv_name):
    data = {
        '語句' : words,
        '語句の意味' : texts,
        'URL' : urls
    }
    df_data = pd.DataFrame(data)
    file_path = 'csv/' + csv_name + '.csv'
    df_data.to_csv(file_path, index=False, mode='x', encoding="utf-8")

def selenium():
    words = []
    urls = []
    driver.get(URL)
    driver.find_elements(By.LINK_TEXT, 'システム開発技術(21)')[0].click()
    sleep(1)
    list_elements = driver.find_elements(By.CLASS_NAME, 'wordLink.cf')
    for list_element in list_elements:
        li_elements = list_element.find_elements(By.TAG_NAME, 'li')
        for li_element in li_elements:
            word = li_element.text
            words.append(word)
            url = URL + word + '.html'
            urls.append(url)
            sleep(1)
    driver.quit()
    print('単語とURL取得完了')        
    return words, urls

def maketext(urls):
    texts = []
    for url in urls:
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.find('div', id='quizQWrap').text
        texts.append(text)
        driver.quit()
        print('text取得完了')
        sleep(1)
    return texts

if __name__ == '__main__':
    main()