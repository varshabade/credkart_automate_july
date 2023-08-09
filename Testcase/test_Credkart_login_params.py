import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By


class Test_CredKart_Login_params:
    def test_CredKart_Login_params_003(self, setup, getdataForLogin):
        self.driver=setup
        self.driver.get("https://automation.credence.in/login")
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(getdataForLogin[0])
        self.driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys(getdataForLogin[1])
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(3)
        try:
            self.driver.find_element(By.XPATH,"//h2[normalize-space()='CredKart']")
            print("login pass")
            self.driver.save_screenshot("C:\\Users\\Ankush\\PycharmProjects\\Credkart_Automation_practice\\Screenshots\\"+getdataForLogin[0]+"_"+getdataForLogin[1]+"_"+"test_login2Pass.PNG")
            self.driver.close()
            assert True

        except:
            print("login Fail")
            self.driver.save_screenshot("C:\\Users\\Ankush\\PycharmProjects\\Credkart_Automation_practice\\Screenshots\\"+getdataForLogin[0]+"_"+getdataForLogin[1]+"_"+"test_login2Pass.PNG")
            self.driver.close()
            assert False





