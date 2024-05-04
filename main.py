from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
from time import sleep

junle_list = ['企業活動(113)', 'システム開発技術(21)', '基礎理論(14)']
a_texts = [] 
words = []
driver = webdriver.Chrome()
sleep(2)
driver.get('https://www.itpassportsiken.com/word/')
sleep(2)
# a_list_elements = driver.find_elements(By.CLASS_NAME, 'index')
# for a_list_element in a_list_elements:
#     li_elements = a_list_element.find_elements(By.TAG_NAME, 'li')
#     sleep(1)
#     for li_element in li_elements:
#         a_texts.append(li_element.text)
for junle in junle_list:
    driver.find_elements(By.LINK_TEXT, junle)[0].click()
    sleep(2)
    b_list_elements = driver.find_elements(By.CLASS_NAME, 'wordLink.cf')
    for b_list_element in b_list_elements:
        li_elements = b_list_element.find_elements(By.TAG_NAME, 'li')
        for li_element in li_elements:
            # if(li_element.text == 'Created TensorFlow Lite XNNPACK delegate for CPU.'): break
            # words.append(li_element.text)
            word = li_element.text
            print(word)
            driver.find_elements(By.LINK_TEXT, word)[0].click()
            # text = driver.find_element(By.XPATH, '//*[@id="quizQWrap"]/div').text
            # URL = driver.current_url
            # print(word, text, URL)
            # b_texts.append(li_element.text)
            sleep(2)
            driver.back()
            # sleep(2)
            # driver.find_elements(By.XPATH, '//*[@id="mainCol"]/div[1]/a[3]')[0].click()
print(words)
# header = ['語句', '語句の意味', 'URL']
# with open('sample.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#     writer.writerow(b_texts)
# f.close()
# driver.find_elements(By.LINK_TEXT, a_texts[0])[0].click()
# b_list_elements = driver.find_elements(By.CLASS_NAME, 'wordLink.cf')
# sleep(1)
# for b_list_element in b_list_elements:
#     li_elements = b_list_element.find_elements(By.TAG_NAME, 'li')
#     for li_element in li_elements:
#         b_texts.append(li_element.text)
#         sleep(2)
# print(a_texts)
# print(texts)
# sleep(2)
# a_list = driver.find_elements(By.LINK_TEXT, '企業活動(113)')
# //*[@id="mainCol"]/div[2]/ol[1]/li[2]/a
# a_list = driver.find_elements(By.XPATH, '//*[@id="mainCol"]/div[2]/ol[1]/li[1]/a')
# a_list[0].click()
# sleep(2)
# a_list_elements = driver.find_elements(By.CLASS_NAME, 'wordLink.cf')
# for a_list_element in a_list_elements:
#     li_elements = a_list_element.find_elements(By.TAG_NAME, 'li')
#     for li_element in li_elements:
#         texts.append(li_element.text)
# print(texts)
# sleep(2)
# b_list = driver.find_elements(By.XPATH, '//*[@id="mainCol"]/div[2]/ul[1]/li[1]/a')
# word = b_list[0].text
# b_list[0].click()
# sleep(2)
# text = driver.find_element(By.XPATH, '//*[@id="quizQWrap"]/div').text
# URL = driver.current_url
# print(word, text, URL)

driver.quit()