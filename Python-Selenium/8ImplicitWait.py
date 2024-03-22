#Implicit Wait buscar componente 
import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#Clase
class usar_unittest(unittest.TestCase):
    
    #Creo funcion driver
    def setUp(self):
        self.driver = Chrome()

    #Usar implicit Wait
    def test_implicit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5) #pausar
        driver.get('https://www.google.com')

        #carga en un componente dinalmico
        elemento = driver.find_element(By.ID,"APjFqb")

if __name__ =='__main__':
    unittest.main()
