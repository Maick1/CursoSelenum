import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
import time

#Clase
class usar_unittest(unittest.TestCase):
    
    #Creo funcion driver
    def setUp(self):
        self.driver = Chrome()

    #funcion buscar por xpath
    def test_buscar_por_xpath(self):
        driver = self.driver
        driver.get('https://www.google.com')
        time.sleep(3)

        #instruccion por script para abrir una ventana
        driver.execute_script("window.open('');")
        time.sleep(3)

        #abro segunda pestaña con handles
        driver.switch_to.window(driver.window_handles[1])
        driver.get('https://github.com')
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(5)

if __name__ =='__main__':
    unittest.main()
