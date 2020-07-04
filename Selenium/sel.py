from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = input()
browser = webdriver.Chrome(
    "C:/Users/Dell/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0/LocalCache/local-packages/Python38/Scripts/chromedriver_win32/chromedriver.exe"
)
browser.get(url)
html = browser.page_source
bs = BeautifulSoup(html, "html.parser")
time.sleep(10)
format = bs.prettify()
filename = "links"

with open(filename, "w") as f:
    for link in bs.find_all("a", href=True):
        print(link["href"])
        f.write(link["href"])

