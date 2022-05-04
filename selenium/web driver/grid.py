# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 20:13:22 2019

@author: Kadva Saach
"""

import unittest
import time
from selenium import webdriver

driver = webdriver.Firefox(executable_path= r'geckodriver')
    
base_url = "http://localhost:8080/LMS/"
uname = "j"
pwd   = "j"


class TestOne(unittest.TestCase):    
    def test_one(self):
        #-----------URL--------------
        driver.get(base_url)
        time.sleep(2)
        driver.implicitly_wait(2)
        #sdriver.maximize_window()
        
        #-----------login------
        uid = driver.find_element_by_name("user_name")
        print("username found")
        time.sleep(2)
        
        uid.send_keys(uname)
        print("username entered")
        time.sleep(2)
        
        password = driver.find_element_by_name("password")
        print("password element found")
        password.clear()
        
        password.send_keys(pwd)
        print("password entered")
        time.sleep(2)
        
        #----------Login btn-------
        signup_btn = driver.find_element_by_name("signin")
        print("btn found")
        time.sleep(2)
        
        signup_btn.click()
        print("signup btn clicked")
        driver.get_screenshot_as_file('ADM2.png')
        
        time.sleep(10)
        
    def Quit(self):
        driver.quit()
        
if __name__ == "__main__":
    unittest.main()