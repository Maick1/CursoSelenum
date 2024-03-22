
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
        driver.get('https://www.gmail.com')
        time.sleep(3)
        driver.get('https://www.google.com')
        time.sleep(3)
        driver.get('https://www.youtube.com')
        time.sleep(3)
       
       #Hacia atras
        driver.back()
        time.sleep(3)
        driver.back()
        time.sleep(3)

    #Siguente
        driver.forward()
        time.sleep(5)

#aplico selenium para regresar o siguiente
        
if __name__ =='__main__':
    unittest.main()
