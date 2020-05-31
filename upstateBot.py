import requests
import datetime

BOT_TOKEN = ""
BOT_CHAT_ID = ""

SERVICES = {
    "service": "https://www.example.com"
}

def telegram_bot_sendtext(message):
    requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={BOT_CHAT_ID}&parse_mode=Markdown&text={message}")


def service_down(url):
    return requests.get(url).status_code == 502

for service in SERVICES:
    if service_down(SERVICES[service]):
        telegram_bot_sendtext(
            f"{datetime.datetime.now().strftime('%H:%M, %B %d %Y')} - {service} is down")
