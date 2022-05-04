# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 21:01:57 2019

@author: Kadva Saach
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Firefox(executable_path= r'geckodriver')

base_url = "http://localhost:8080/LMS/"
p_uid = "j"   #p stands for parameter
p_pass = "j"

# create a new Firefox session
driver.set_page_load_timeout(30)
driver.maximize_window()
driver.implicitly_wait(5)

# Navigate to the application home page
driver.get(base_url)

# Clicking a screenshot of the login page
driver.get_screenshot_as_file('ADM1.png')

uid = driver.find_element_by_name("user_name")
print("username element found")
uid.clear()
uid.send_keys(p_uid)
print("username entered")

password = driver.find_element_by_name("password")
print("password element found")
password.clear()
password.send_keys(p_pass)
print("password entered")
signup_btn = driver.find_element_by_name("signin")
print("signup btn found")


signup_btn.click()
print("signup btn clicked")
driver.get_screenshot_as_file('ADM2.png')

bk = driver.find_element_by_link_text('Book')
bk.click()

ab = driver.find_element_by_link_text('Add Book')
ab.click()


#----Add book----

bt = driver.find_element_by_id('book_title')  #title
bt.send_keys('qwasr')
print("title entered")
sleep(3)

ct = driver.find_element_by_id('category_name') #category_name
ct.send_keys('asdzxcz')
print("category_name entered")

an = driver.find_element_by_name('author_name') #author_name
an.send_keys('zxcggg')
print("author_name entered")
sleep(3)


pn = driver.find_element_by_name('publisher_name') #publisher_name
pn.send_keys('tyu')
print("publisher_name entered")
sleep(3)

ed = driver.find_element_by_name('edition')         #edition    
ed.send_keys('46')
print("edition entered")
sleep(3)

vm = driver.find_element_by_name('volume')          #volume
vm.send_keys('87')
print("volume entered")
sleep(3)

en = driver.find_element_by_name('ean_code')        #ean_code
en.send_keys('AQC5')
print("ean_code entered")
sleep(3)

ib = driver.find_element_by_name('isbn')            #isbn
ib.send_keys('8554')
print("isbn entered")
sleep(3)

pc = driver.find_element_by_name('price')           #price
pc.send_keys('8800')
print("price entered")
sleep(3)

lz = driver.find_element_by_name("language")        #language
lz.send_keys('english')
print("language entered")
sleep(3)

ds = driver.find_element_by_name('description')     #description
ds.send_keys('asd zxcz dsfsfsddfs')
print("description entered")
sleep(3)

k = driver.find_element_by_class_name('btn-default')    #add book btn
k.click()
print("add book btn clicked")
sleep(3)






sleep(10)
driver.quit()
