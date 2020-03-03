import json

import requests

HOST = "https://sandbox.toloka.yandex.ru"  # Точка доступа к API
TOKEN = open("token", "r").read()  # Токен доступа для выполнения запросов к API Толоки
HEADER = {"Content-Type": "application/json", "Authorization": "OAuth " + TOKEN}  # Заголовки запросов API


def print_pretty_json(data):
    print(json.dumps(data, indent=2, sort_keys=False, ensure_ascii=False))


def create_pool():
    with open("json/create_pool.json", "r") as json_file:
        json_data = json.dumps(json.load(json_file))
    request = requests.post(f"{HOST}/api/v1/pools", headers=HEADER, data=json_data)
    request.raise_for_status()
    return request.json()


def create_task():
    with open("json/create_task.json", "r") as json_file:
        json_data = json.dumps(json.load(json_file))
    request = requests.post(f"{HOST}/api/v1/tasks", headers=HEADER, data=json_data)
    request.raise_for_status()
    return request.json()


def get_pool_results():
    request = requests.get(f"{HOST}/api/v1/assignments", headers=HEADER)
    request.raise_for_status()
    return request.json()


def get_pool_list():
    request = requests.get(f"{HOST}/api/v1/pools", headers=HEADER)
    request.raise_for_status()
    return request.json()


if __name__ == "__main__":
    pass
