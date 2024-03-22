#Explicit Wait sirve para cargar ciertos componentes

import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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
        try:
            element = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located(By.XPATH,"//*[@id=\"APjFqb\"]"))
        finally:
            driver.quit()

    
if __name__ =='__main__':
    unittest.main()
