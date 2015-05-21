__author__ = 'paolo.degrazia'

from selenium import webdriver


class AutomationFramework():

    def __init__(self):
        pass

    @staticmethod
    def go():
        driver= webdriver.Firefox()
        driver.get('http://localhost:8080/index2.html')

    @staticmethod
    def quit():
        pass