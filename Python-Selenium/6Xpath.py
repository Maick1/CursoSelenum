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
        buscar_por_xpath = driver.find_element(By.XPATH, "//*[@id=\"APjFqb\"]")
        #ARROW.DOWN busca y baja
        buscar_por_xpath.send_keys("Selenium",Keys.ARROW_DOWN)
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ =='__main__':
    unittest.main()


#xpatch es una estructura de objetos
        #xpath Relativo.- parte de un nodo
        #xpath abosulto.- se usa cuando el componente no va a cambiar