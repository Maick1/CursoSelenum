from selenium import webdriver

# Inicializar el navegador Brave con las opciones y el servicio
driver = webdriver.Chrome()

# Abre una página de ejemplo para verificar que funcione correctamente
driver.get('https://www.google.com')

# Espera un momento para ver los resultados antes de cerrar el navegador
input('Presiona enter para cerrar el navegador...')

# Cierra el navegador
driver.quit() 

