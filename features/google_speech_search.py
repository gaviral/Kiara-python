import sys

from pyautogui import press, hotkey
from selenium import webdriver

from custom_utilities.os.os_util import focus_my_browser
from features.text_to_speech import say

CHROME_DRIVER_PATH = 'C:/chromedriver_win32/chromedriver.exe'
SEARCH_TAB_URL = "https://www.google.com/search?btnI=Im+Feeling+Lucky&q="
GOOGLE_URL = "https://www.google.com/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=selenium")
chrome_options.add_argument("start-maximized")

try:
    my_browser = webdriver.Chrome(CHROME_DRIVER_PATH, options=chrome_options)
except:
    e = sys.exc_info()[0]
    say(e)


def wait_for_url_change():
    _url = my_browser.current_url
    while my_browser.current_url == _url:
        continue


def i_am_feeling_lucky(_feeling_lucky=True):
    if _feeling_lucky:
        press('tab')
        press('enter')
        press('enter')


def google_speech_search(feeling_lucky=True):
    # Redirect first tab to Google
    my_browser.get(GOOGLE_URL)

    focus_my_browser()

    # Escape out of error: "Chrome didn't shut down correctly"
    press('tab')
    press('tab')
    press('esc')

    # Focus inside web-page
    press('tab')
    press('tab')

    # Start google's speech search
    hotkey('ctrl', 'shift', '.')

    # Wait for search results
    wait_for_url_change()

    # Open the first google search results (aka: `I'm Feeling lucky` Name of Google's search feature)
    i_am_feeling_lucky(feeling_lucky)
