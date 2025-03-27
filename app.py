from fastapi import FastAPI, Request
import requests
import logging
from datetime import datetime

app = FastAPI()

# Configuration des logs
logging.basicConfig(filename="access.log", level=logging.INFO)

# API pour obtenir les infos d'une IP
@app.get("/geolocate/ip/{ip}")
def get_ip_info(ip: str, request: Request):
    user_ip = request.client.host  # IP du visiteur
    logging.info(f"{datetime.now()} - Request from {user_ip} for {ip}")
    
    response = requests.get(f"http://ip-api.com/json/{ip}").json()
    return response

# API pour obtenir les infos d’un numéro de téléphone (exemple avec Numverify)
@app.get("/geolocate/phone/{number}")
def get_phone_info(number: str):
    API_KEY = "VOTRE_CLE_API_NUMVERIFY"
    url = f"http://apilayer.net/api/validate?access_key={API_KEY}&number={number}"
    
    response = requests.get(url).json()
    return response
