import requests
import bs4
from selenium import webdriver

url = input(" ")

response = requests.get(url)
filename = "r_s.html"
bs = bs4.BeautifulSoup(response.text, "html.parser")
format_save = bs.prettify()



with open(filename, "w") as f:
    f.write(format_save)

list_as_img=bs.find_all('img')
i=len(list_as_img)
print("images in home page",i)
list_as_a=bs.find_all('a')
ac=len(list_as_a)
print("anchors in home page",ac)
links=bs.find_all('href')
l=len(links)
print("links",l)