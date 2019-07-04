import requests
import logging


class TeamsNotifier:
    webhook_url = None

    def __init__(self, webhook_url):
        if webhook_url:
            self.webhook_url = webhook_url

    def notify(self, message: str):
        returned_data = requests.post(
            self.webhook_url,
            json={'text': message},
            headers={'Content-type': 'application/json'}
        )
        if returned_data.status_code != 200:
            logging.warning(returned_data.text)
        return returned_data.status_code

    def notify_advanced(self, message):
        returned_data = requests.post(
            self.webhook_url,
            json=message,
            headers={'Content-type': 'application/json'}
        )
        if returned_data.status_code != 200:
            logging.warning(returned_data.text)
        return returned_data.status_code
