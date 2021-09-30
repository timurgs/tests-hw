import requests


class CreateFolderYaApi:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "OAuth {}".format(self.token)
        }
        return headers

    def create_folder(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {"path": "Test_folder"}
        response = requests.put(url, headers=headers, params=params)
        return response

    def check_create_folder(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {"path": "Test_folder"}
        response = requests.get(url, headers=headers, params=params)
        return response
