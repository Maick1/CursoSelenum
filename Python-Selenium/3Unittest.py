import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
import time
import tkinter as tk

#Clase
class usar_unittest(unittest.TestCase):
    
    #Creo funcion driver
    def setUp(self):
        self.driver = Chrome()

    #funcion carga pagina, usar siempre (test_nombre) unittest
    def test_buscar(self):
        driver = self.driver
        driver.get('https://www.google.com')
        #asserIn
        self.assertIn("Google", driver.title)
        #busco un elemento
        elemento = driver.find_element(By.ID,"APjFqb")
        elemento.send_keys("Selenium")
        elemento.send_keys(Keys.RETURN)
        time.sleep(5)

        #Verifico el assert
        assert "No se encontro el elemento" not in driver.page_source

    #TearDown cerrar driver
    def tearDown(self):
        self.driver.close()

if __name__ =='__main__':
    unittest.main()

