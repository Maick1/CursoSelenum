import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import cv2

# Comparación de imagen 
class usar_unittest(unittest.TestCase):
    
    # Creo función driver
    def setUp(self):
        self.driver = Chrome()

    def test_usando_opencv(self):
        driver = self.driver
        driver.get('https://www.google.com')
        # Función para capturar imagen
        driver.save_screenshot('img2.png')
        time.sleep(3)
      
        
    # Comparar imágenes
    def comparar_img(self):
        img1 = cv2.imread('../img1.png')
        img2 = cv2.imread('img2.png')

        #Modulo cv2
        diferencia = cv2.absdiff(img1,img2)
        imagen_gris = cv2.cvtColor(diferencia,cv2.COLOR_BGR2GRAY)  # Corrección en la conversión de color
        contours,_ = cv2.findContours(imagen_gris, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        # Lectura de imágenes
        for c in contours:
            if cv2.contourArea(c) >= 20:
                # Dimensiones de las imágenes
                posicion_x, posicion_y, ancho, alto = cv2.boundingRect(c)
                cv2.rectangle(img1, (posicion_x, posicion_y), (posicion_x + ancho, posicion_y + alto), (0, 0, 255), 2)
        
        # Mostrar imágenes
        while (1):
            cv2.imshow('Imagen1', img1)
            cv2.imshow('Imagen2', img2)
            cv2.imshow('Diferencia Detectadas', diferencia)
            teclado = cv2.waitKey(5) & 0xFF
            if teclado == 27:
                break
        cv2.destroyAllWindows()

if __name__ == '__main__':
    unittest.main()
