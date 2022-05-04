import unittest
import time
from selenium import webdriver
#import org.openqa.selenium.firefox.FirefoxDrive
driver = webdriver.Firefox(executable_path= r'geckodriver')

base_url = "http://localhost:8080/LMS/"
uname = "j"
pwd   = "j"

class TestThree(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities={
                "browserName": "firefox",
            })
    def test_three(self):
        driver = self.driver
        driver.get(base_url)
        #time.sleep(5)
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
        
        #-----------------
        bk = driver.find_element_by_link_text('Book')
        bk.click()

        ab = driver.find_element_by_link_text('Add Book')
        ab.click()
        
        #----Add book----

        bt = driver.find_element_by_id('book_title')  #title
        bt.send_keys('zzzxz')
        print("title entered")
        time.sleep(3)

        ct = driver.find_element_by_id('category_name') #category_name
        ct.send_keys('asda')
        print("category_name entered")

        an = driver.find_element_by_name('author_name') #author_name
        an.send_keys('ere')
        print("author_name entered")
        time.sleep(3)


        pn = driver.find_element_by_name('publisher_name') #publisher_name
        pn.send_keys('jhk')
        print("publisher_name entered")
        time.sleep(3)

        ed = driver.find_element_by_name('edition')         #edition    
        ed.send_keys('89')
        print("edition entered")
        time.sleep(3)

        vm = driver.find_element_by_name('volume')          #volume
        vm.send_keys('56')
        print("volume entered")
        time.sleep(3)

        en = driver.find_element_by_name('ean_code')        #ean_code
        en.send_keys('AZS')
        print("ean_code entered")
        time.sleep(3)

        ib = driver.find_element_by_name('isbn')            #isbn
        ib.send_keys('854')
        print("isbn entered")
        time.sleep(3)

        pc = driver.find_element_by_name('price')           #price
        pc.send_keys('8008')
        print("price entered")
        time.sleep(3)

        lz = driver.find_element_by_name("language")        #language
        lz.send_keys('english')
        print("language entered")
        time.sleep(3)

        ds = driver.find_element_by_name('description')     #description
        ds.send_keys('asd zxcz dsfsfsddfs')
        print("description entered")
        time.sleep(3)

        k = driver.find_element_by_class_name('btn-default')    #add book btn
        k.click()
        print("add book btn clicked")
        
        zz = driver.find_element_by_link_text('Logout')
        zz.click()
        print("log out")
        
    def Quit(self):
        driver.quit()
        


    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    unittest.main()