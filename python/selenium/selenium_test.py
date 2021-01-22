from selenium import webdriver

path = "C:\\Users\\i\\Work\\webdriver\\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://www.google.com")
print(driver.title)

search_box = driver.find_element_by_name("q")
search_box.send_keys("아마존 웹 서비스")
search_box.submit()
