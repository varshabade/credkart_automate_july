import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Login():
    def test_login1(self,setup):
        self.driver = setup
        self.driver.get("https://automation.credence.in ")
        if self.driver.title=='CredKart':
            print("You are in credence.in")
            self.driver.save_screenshot("C:\\Users\\Ankush\\PycharmProjects\\Credkart_Automation\\Screenshots\\test_login1_Pass.PNG")
            assert True
        else:
            print("You are not  in credence.in")
            self.driver.save_screenshot("C:\\Users\\Ankush\\PycharmProjects\\Credkart_Automation\\Screenshots\\test_login1_faIL.PNG")
            assert False

    def test_login2(self,setup):
        self.driver=setup
        self.driver.get("https://automation.credence.in/login")
        self.driver.find_element(By.ID, "email").send_keys("Credencetest@test.com")
        self.driver.find_element(By.NAME, "password").send_keys("Credence@123")
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(3)
        try:
            self.driver.find_element(By.XPATH,"//h2[normalize-space()='CredKart']")
            print("login pass")
            self.driver.save_screenshot("C:\\Users\\Ankush\\PycharmProjects\\Credkart_Automation\\Screenshots\\test_login2Pass.PNG")
            assert True
        except:
            print("login Fail")
            self.driver.save_screenshot("C:\\Users\\Ankush\\PycharmProjects\\Credkart_Automation\\Screenshots\\test_login2fAIL.PNG")
            assert False
