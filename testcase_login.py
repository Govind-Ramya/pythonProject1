import pytest
from selenium import webdriver
from Pageobject.login import loginpage
from utilities.readdataconf import dataread
from utilities.customelogger import loggen

class test_01_loginpage:
    baseurl = dataread.geturl()
    emailid = dataread.getemailid()
    password = dataread.getpassword()
    logger = loggen.loggenr()

    def test_homepagetitle(self,setup):
        self.logger.info("*****test01******")
        self.logger.info("****verifying home page title*****")
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Your store. Login":
            assert True
            self.driver.close
            self.logger.info("**** home page title is passed *****")
        else:
            self.driver.save_screenshot(".//screenshots"+"test_homepagetitle.png")
            self.driver.close
            assert False
            self.logger.error("****home page title is failed*****")
    def test_login(self,setup):
        self.logger.info("****verifying login credential*****")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.obj = loginpage(self.driver)
        self.obj.setusername(self.emailid)
        self.obj.setpassword(self.password)
        self.obj.click()
        new_title = self.driver.title
        if new_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close
            self.logger.info("****verifying login credential is passed *****")

        else:
            self.driver.save_screenshot(".//screenshot"+"test_login.png")
            self.driver.close
            assert False
            self.logger.error("****verifying login credential is failed*****")
