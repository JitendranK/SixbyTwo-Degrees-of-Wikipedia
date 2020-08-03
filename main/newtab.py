from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from collections import deque
import time
import extractlinks as el

# Opens each article in a separate tab in the Google Chrome browser.
def open_in_new_tab(article_stack):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    tab = 1
    while article_stack:
        name = article_stack.pop()
        print(name)
        name_url = el.get_url(name)
        driver.get(name_url)
        time.sleep(1)
        if article_stack:
            driver.execute_script("window.open('');") # Opens a new tab.
            driver.switch_to.window(driver.window_handles[tab]) # Switches to the previously opened tab.
            tab = tab + 1
    time.sleep(15) # Pauses the chrome window for 15 seconds before closing it.