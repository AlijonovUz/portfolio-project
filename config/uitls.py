import requests

BOT_TOKEN = "7456811289:AAHrHCyXhLGk4EsHm-PkcNDEN85igR7pZpM"
ADMIN_ID = 6150504681


def send_message(name, email, message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        'chat_id': ADMIN_ID,
        'text': f"<b>Foydalanuvchi:</b> {name}\n"
                f"<b>Elektron pochta manzili:</b> {email}\n"
                f"<b>Xabar matni:</b> {message}",
        'parse_mode': "HTML"
    }

    response = requests.get(url=url, data=data)

    if response.status_code == 200:
        return True
    else:
        return False