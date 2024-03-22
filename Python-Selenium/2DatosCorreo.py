from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
import time
import tkinter as tk  # Importa tkinter para mostrar alertas

# Función para mostrar una alerta
def mostrar_alerta(mensaje):
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    tk.messagebox.showerror("Error", mensaje)

try:
    # Inicializar el navegador Chrome
    driver = Chrome()

    # Abre una página de ejemplo para verificar que funcione correctamente
    driver.get('https://gmail.com')

    # Espera 5 segundos para cargar la página
    time.sleep(5)

    # Ingresa el correo electrónico
    users = driver.find_element(By.ID, "identifierId")
    users.send_keys("mtomalaz@unemi.edu.ec")
    users.send_keys(Keys.ENTER)

    # Espera 3 segundos para cargar la página
    time.sleep(3)

    # Ingresa la contraseña
    password = driver.find_element(By.NAME, "Passwd")
    password.send_keys("5165468654564")
    password.send_keys(Keys.ENTER) 

    # Espera 5 segundos para verificar si el inicio de sesión fue exitoso
    time.sleep(5)

    # Verifica si hay un mensaje de error después de intentar iniciar sesión
    error_message = driver.find_elements(By.XPATH, "//div[@class='GQ8Pzc']//div[@class='LXRPh']//div[@class='dEOOab RxsGPe']")
    if error_message:
        # Si hay un mensaje de error, muestra una alerta con el mensaje
        mostrar_alerta("Contraseña incorrecta. Por favor, verifica tus credenciales.")
    else:
        print("Inicio de sesión exitoso")  # Puedes agregar acciones adicionales si el inicio de sesión fue exitoso

except Exception as e:
    # Si ocurre un error, muestra una alerta con el mensaje de error
    mostrar_alerta(str(e))
