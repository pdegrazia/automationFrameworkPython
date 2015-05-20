__author__ = 'paolo.degrazia'

from selenium import webdriver


class AutomationFramework():

    def __init__(self):
        pass

    @staticmethod
    def go():
        driver= webdriver.Firefox()
        driver.get('http://google.com')