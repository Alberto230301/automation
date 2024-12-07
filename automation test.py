from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login_to_webapp(driver, username, password, username_field_id, password_field_id, submit_button_id):
    """
    Funzione per accedere a un'applicazione web inserendo username e password.
    """
    try:
        # Trova i campi e il pulsante usando i loro ID
        username_field = driver.find_element(By.ID, username_field_id)
        password_field = driver.find_element(By.ID, password_field_id)
        submit_button = driver.find_element(By.ID, submit_button_id)

        # Inserisce username e password
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Clicca sul pulsante di login
        submit_button.click()

        # Attendi che la pagina si carichi dopo il login (opzionale)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='media-body media-middle']"))
        )
        print("Login completato.")
    except Exception as e:
        print(f"Errore durante il login: {e}")


def notam_quey(driver):
    """
    Funzione per navigare nella sezione NOTAM Office.
    """
    try:
        # Trova l'elemento NOTAM Office e cliccalo
        notam_office = driver.find_element(By.XPATH, "//div[@class='media-body media-middle']//span[text()='NOTAM Office']")
        notam_office.click()
        print("Navigazione alla sezione NOTAM completata.")
    except Exception as e:
        print(f"Errore durante la navigazione a NOTAM Office: {e}")


# Parametri
url = 'http://172.21.197.196/cronos-portal/'
username = 'admin'
password = 'aftn'
username_field_id = 'userLogin'
password_field_id = 'password'
submit_button_id = 'doLogin'

# Inizializza il driver (usa Chrome come esempio)
driver = webdriver.Chrome()  # Assicurati che chromedriver sia nella tua PATH
driver.get(url)  # Accedi all'URL

# Attendi il caricamento della pagina iniziale
time.sleep(15)

# Funzioni principali
login_to_webapp(driver, username, password, username_field_id, password_field_id, submit_button_id)
notam_quey(driver)

# Termina il driver
input('Premi Invio per uscire.')
driver.quit()
