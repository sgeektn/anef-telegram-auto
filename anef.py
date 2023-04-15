from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import requests
from flask import Flask


TELEGRAM_TOKEN = "*******"
TELEGRAM_CHAT_ID = "******"
PASSWORD= "******"
LOGIN="*******"
def send_to_telegram(message):
    chat_id = TELEGRAM_CHAT_ID
    api_url = "https://api.telegram.org/bot{api_token}/sendMessage".format(api_token=TELEGRAM_TOKEN)
    response = requests.post(api_url, json={'chat_id': chat_id, 'text': message})
    print(response.text)

def get_status():
    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options)

    driver.get("https://sso.anef.dgef.interieur.gouv.fr/auth/realms/anef-usagers/protocol/openid-connect/auth?client_id=anef-usagers&redirect_uri=https%3A%2F%2Fadministration-etrangers-en-france.interieur.gouv.fr%2Fparticuliers%2F%23&response_mode=fragment&response_type=code&scope=openid&acr_values=eidas1")
    driver.find_element(By.ID,"login").send_keys(LOGIN)
    driver.find_element(By.ID,"password").send_keys(PASSWORD)
    driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/form/button").click()

    time.sleep(15)
    driver.get("https://administration-etrangers-en-france.interieur.gouv.fr/api/anf/dossier-stepper")
    time.sleep(1)
    status = driver.find_element(By.CLASS_NAME,"panelContent").text

    driver.close()
    send_to_telegram(status)

    return "ok"


app = Flask(__name__)

@app.route('/get_status')
def home():
    return get_status()