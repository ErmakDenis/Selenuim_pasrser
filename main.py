from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent

# URL для парсинга
url = 'https://www.nseindia.com/'

# Настройки для Chrome
options = webdriver.ChromeOptions()

# Создание фейкового User-Agent
useragent = UserAgent()

# Добавление User-Agent и заголовка Accept в настройки (в настоящий момент закомментировано)
# options.add_argument(f"user-agent={useragent.chrome},Accept=*/*")

# Отключение режима webdriver
options.add_argument('--disable-blink-features=AutomationControlled')

# Указываем путь к исполняемому файлу драйвера Chrome и передаем настройки
driver = webdriver.Chrome(
    executable_path='/usr/local/bin/chromedriver',
    options=options
)

# Посещение URL
try:
    driver.get(url=url)
    time.sleep(5)

    # Находим элемент меню
    menu = driver.find_element(by=By.ID, value='link_2')

    # Наводим указатель на элемент меню
    ActionChains(driver).move_to_element(menu).perform()

    # Указываем URL подменю, по которому нужно щелкнуть
    url = '/market-data/pre-open-market-cm-and-emerge-market'

    # Находим элемент подменю
    sub_menu = driver.find_element(by=By.XPATH, value='//a[@href="'+url+'"]')

    # Наводим указатель на элемент подменю
    ActionChains(driver).move_to_element(sub_menu).perform()

    # Щелкаем по элементу подменю
    ActionChains(driver).click(sub_menu).perform()

    # Находим элемент загрузки
    download = driver.find_element(by=By.ID, value='dwldcsv')

    # Наводим указатель на элемент загрузки
    ActionChains(driver).move_to_element(download).perform()

    # Щелкаем по элементу загрузки
    ActionChains(driver).click(download).perform()

except Exception as ex:
    print(ex)
finally:
    time.sleep(5)
    driver.close()
    driver.quit()


import os
import pandas as pd

# Указываем путь к директории
directory = '/Users/denisermak/Downloads/'

# Получаем список файлов в директории
files = os.listdir(directory)

# Фильтруем файлы по расширению CSV
csv_files = [file for file in files if file.endswith('.csv')]

# Сортируем файлы по дате скачивания
sorted_files = sorted(csv_files, key=lambda x: os.path.getmtime(os.path.join(directory, x)))

# # Выводим отсортированный список файлов
# for file in sorted_files:
#     print(file)

# Получаем целевой файл (последний по дате)
target_file = sorted_files[-1]
print(target_file)

# Читаем данные из CSV-файла
data = pd.read_csv(directory+target_file)
# print(data.keys())

# Создаем DataFrame для результирующих данных
result_data = pd.DataFrame()
result_data['Name'] = data['SYMBOL \n']
result_data['Final_Price'] = data['FINAL \n']
result_data.to_csv('result.csv')


# --------------------------------------------------------
# Сценарий
# --------------------------------------------------------
# Посещение URL
try:
    driver.get(url=url)
    time.sleep(5)

    # Находим элемент меню
    menu = driver.find_element(by=By.ID, value='link_1')

    # Наводим указатель на элемент меню
    ActionChains(driver).move_to_element(menu).perform()

    time.sleep(1)
    # Находим элемент меню
    menu = driver.find_element(by=By.ID, value='link_2')


    # Наводим указатель на элемент меню
    ActionChains(driver).move_to_element(menu).perform()
    time.sleep(1)
    # Находим элемент меню
    menu = driver.find_element(by=By.ID, value='link_3')

    # Наводим указатель на элемент меню
    ActionChains(driver).move_to_element(menu).perform()
    time.sleep(1)
    # Находим элемент меню
    menu = driver.find_element(by=By.ID, value='link_4')

    # Наводим указатель на элемент меню
    ActionChains(driver).move_to_element(menu).perform()
    time.sleep(1)
    # Наводим указатель на элемент меню
    ActionChains(driver).move_to_element(menu).perform()
    # Находим элемент меню
    menu = driver.find_element(by=By.ID, value='link_3')
    # Наводим указатель на элемент меню
    ActionChains(driver).move_to_element(menu).perform()
    time.sleep(2)
    # Находим элемент подменю
    url = '/invest/investors-feedback-form'
    sub_menu = driver.find_element(by=By.XPATH, value='//a[@href="'+url+'"]')

    # Наводим указатель на элемент подменю
    ActionChains(driver).move_to_element(sub_menu).perform()
    time.sleep(1)
    # Щелкаем по элементу подменю
    ActionChains(driver).click(sub_menu).perform()


    # Заполняем форму
    name_input = driver.find_element(by=By.ID,value='name')
    name_input.clear()
    name_input.send_keys('DENIS ERMAK')
    time.sleep(3)
    mobile_input = driver.find_element(by=By.ID,value='investor_phone')
    mobile_input.clear()
    mobile_input.send_keys('+78002353535')
    time.sleep(3)
    email_input = driver.find_element(by=By.ID, value='investor_email')
    email_input.clear()
    email_input.send_keys('test@test.com')
    time.sleep(3)
    email_input.clear()
    email_input.send_keys('testtest@testtest.com')
    time.sleep(3)
    # Прокручиваем страницу вниз на 500 пикселей
    driver.execute_script('window.scrollBy(0, 2000)')

    # Прокручиваем страницу вниз на 500 пикселей
    driver.execute_script('window.scrollBy(0, -200)')

    text_input = driver.find_element(by=By.ID, value='complaint_resolution_suggestions')
    text_input.clear()
    text_input.send_keys('Буду очень рад с вами работать!!!')
    time.sleep(3)



except Exception as ex:
    print(ex)
finally:
    time.sleep(5)
    driver.close()
    driver.quit()
