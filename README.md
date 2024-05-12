# web-scraping-with-selenium
# Requirement
* pandas (1.4.2)
* selenium (4.20.0)
* beautifulsoup4 (4.11.1) 
* requests (2.28.1)
# Usage
Substitute this URL with the URL of the site you want to scrape.
```python
URL = 'YOUR_WEB_SITE_URL'
```
Please enter a file name for saving.
```python
makecsv(main_words, main_texts, main_urls, 'CSV_NAME')
```
# memo
For selenium 4.3.0 and earlier versions
```python 
driver.find_element_by_xpath("xpath")
```
For selenium 4.3.0 and later versions
```python
driver.find_element(by=By.XPATH, value="xpath")
```