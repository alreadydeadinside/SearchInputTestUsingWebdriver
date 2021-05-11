from selenium import webdriver
from selenium.webdriver.common.keys import Keys


PATH = 'chromedriver.exe'
URL = "https://hotline.ua/"
SEARCH_TEMPLATE = "Игрушка"

browser = webdriver.Chrome(executable_path=PATH)
searchTerm = "Гід покупця. Як вибрати..."
browser.get(URL)
browser.implicitly_wait(30)
browser.find_element_by_css_selector('[id="searchbox"]').send_keys(SEARCH_TEMPLATE)
browser.find_element_by_css_selector('[id="searchbox"]').send_keys(Keys.ENTER)
actualText = browser.find_element_by_css_selector('[class = "h2"]').text
expectedText = searchTerm
print(actualText)
assert actualText == expectedText
browser.close()
