from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("C:\Development\chromedriver2.exe")
browser = webdriver.Chrome(service=serv)
url = "https://inlnk.ru/jElywR"
browser.get(url)

NAMES_LIST = []


def parsing():
    names_list_page = browser.find_elements(By.CSS_SELECTOR, ".mw-category-columns li")
    for name in names_list_page:
        NAMES_LIST.append(name.text)
    next_page = browser.find_element(By.XPATH, '//*[@id="mw-pages"]/a[2]')
    next_page.click()

# #Нахождение кол-ва страниц(если нужны и английские названия)
# pages = browser.find_element(By.CSS_SELECTOR, "#mw-pages p")
# text_pages = pages.text.split(" ")
# str_of_page = text_pages[4] + text_pages[5]
# sum_of_page = int(str_of_page.replace(",", ""))

# while sum_of_page > len(NAMES_LIST):
#     parsing()

while 19300 > len(NAMES_LIST):
    parsing()

# Удаляет названия из нескольких слов
list_for_remove = []
for name in NAMES_LIST:
    if " " in name:
        list_for_remove.append(name)
    else:
        pass

NAMES_LIST = [name for name in NAMES_LIST if name not in list_for_remove]

letter = "А"
count = 0
result = ""
for name in NAMES_LIST:
    # Пропуск английских названий
    if name[0] == "A" or name[0] == "Ё":
        pass
    elif name[0] == letter:
        count += 1
        result = f"{letter}: {count}"
    else:
        print(result)
        count = 0
        letter = name[0]
        count += 1
        result = f"{letter}: {count}"
print(result)
