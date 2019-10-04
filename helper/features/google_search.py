from selenium import webdriver

from helper.features.tts import say

CHROME_DRIVER_PATH = 'C:/chromedriver_win32/chromedriver.exe'
SEARCH_TAB_URL = "https://www.google.com/search?btnI=Im+Feeling+Lucky&q="

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=selenium")
chrome_options.add_argument("start-maximized")
browser = webdriver.Chrome(CHROME_DRIVER_PATH, options=chrome_options)


def google_search(search_text):
    search_text = search_text.replace('search ', '')
    search_url = f'{SEARCH_TAB_URL} {search_text}'
    browser.get(search_url)
    browser.switch_to.window(browser.window_handles[0])
    say(f'[SEARCHED] {search_text}')
