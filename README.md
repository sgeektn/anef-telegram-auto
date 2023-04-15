# Config

open anef.py and change the following variables:

TELEGRAM_TOKEN = "*******"
TELEGRAM_CHAT_ID = "******"
PASSWORD= "******"
LOGIN="*******"

# Launch application

➜  anef export FLASK_APP=anef.py
➜  anef nohup flask run --host=0.0.0.0 &

# Crontab 

0 */11 * * * curl http://161.35.109.90:5000/get_status
# anef-telegram-auto
