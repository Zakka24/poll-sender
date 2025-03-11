from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# poll_options può avere al massimo 12 elementi, limitazione di whatsapp web
numero_sondaggi = 1

options = webdriver.ChromeOptions()
# Directory per il profilo, così non bisogna sempre scannerizzare il qr code
options.add_argument("user-data-dir=/Users/zakariaaoukaili/Desktop/WhatsApp Session")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.google.com")
print("Chrome avviato con successo!!")

# nome del gruppo
group_name = "Navetta TN BZ" 

# apri WhatsApp Web
driver.get("https://web.whatsapp.com")
print("Scansiona il codice QR con il tuo telefono e premi invio qui quando sei loggato")
input()

time.sleep(3)

# cerca e apri il gruppo
search_box = driver.find_element(By.XPATH, "//div[@aria-placeholder='Cerca']")
search_box.click()
search_box.send_keys(group_name)
time.sleep(2)
# print("Gruppo trovato")

group = driver.find_element(By.XPATH, f"//span[@title='{group_name}']")
group.click()
time.sleep(2)
# print("Gruppo aperto")

while(numero_sondaggi < 3):

    if(numero_sondaggi == 1): # invio il primo sondaggio
        poll_question = "Organizzativo Settimana (Presenze)"
        poll_options = ["Presente lunedì", "Presente martedì", "Presente mercoledì", "Presente giovedì", "Presente venerdì"]

    else: # invio il secondo sondaggio
        poll_question = "Organizzativo Settimana (Uscita)"
        poll_options = ["Lu 17:10", "Lu 17:40", "Ma 17:10", "Ma 17:40", "Me 17:10", "Me 17:40", "Gi 17:10", "Gi 17:40", "Ve 17:10", "Ve 17:40"]
        
# clicca sull'icona allegati per aprire il menu degli allegati
    attachment_box = driver.find_element(By.XPATH, "//button[@title='Allega']")
    attachment_box.click()
    time.sleep(2)
    # print("Sezione allegati aperta")

    # clicca sull'icona Sondaggio
    poll_button = driver.find_element(By.XPATH, "//span[contains(text(),'Sondaggio')]")
    poll_button.click()
    time.sleep(2)
    # print("Sondaggio aperto")

    # inserisci la domanda del sondaggio
    question_box = driver.find_element(By.XPATH, "//div[@style='max-height: 7.35em; min-height: 1.47em; user-select: text; white-space: pre-wrap; word-break: break-word;']")
    question_box.click()
    question_box.send_keys(poll_question)
    time.sleep(2)
    # print("Domanda scritta")

    # inserisci le opzioni del sondaggio
    for idx, option in enumerate(poll_options):
        # trova lo span
        span_element = driver.find_element(By.XPATH, "//span[contains(text(),'Aggiungi')]")

        # trova il contenitore
        div_container = span_element.find_element(By.XPATH, "..")

        # all'interno del div_container, cerca l'elemento specifico.
        specific_element = div_container.find_element(By.XPATH, ".//div[@data-lexical-editor='true']")

        specific_element.send_keys(option)

        time.sleep(2)
        # print(f"Opzione {option} scritta")

    # clicca sul pulsante invia per mandare il sondaggio
    send_button = driver.find_element(By.XPATH, "//div[@aria-label='Invia']")
    send_button.click()

    print(f"Sondaggio {numero_sondaggi} inviato!")
    numero_sondaggi +=1
    time.sleep(2)

driver.quit()

