# -*- coding: utf-8 -*-
# Required Python 3.6+

import ssl
import json
import codecs
import requests
import warnings

warnings.filterwarnings('ignore', message='Unverified HTTPS request')
ssl._create_default_https_context = ssl._create_unverified_context

# Глобальные параметры (боевые)
PROJECT_ID = 0000 # Идентификатор проекта в Толоке
HOST = "https://toloka.yandex.ru" # Точка доступа к API
TOKEN = "AQAD-qJSJrptAAAHdfJJpzljxxxxXXXXXxxx" # Токен доступа для выполнения запросов к API Толоки
HEADER = {"Content-Type": "application/json", "Authorization": "OAuth " + TOKEN} # Заголовки запросов API

def print_pretty_json(data):
    print(json.dumps(data, indent=2, sort_keys=False, ensure_ascii=False))

# 1) Получение свойств проекта и обновление приватного комментария
def get_project_and_update_private_comment(private_comment):
    try:
        # запрашиваем свойства проекта
        request = requests.get(f"{HOST}/api/v1/projects/{PROJECT_ID}",
                               headers=HEADER,
                               verify=False)
        request.raise_for_status()
        project = request.json()

        # получаем приватный комментарий
        origin_private_comment = project["private_comment"] if "private_comment" in project and project["private_comment"] else ""

        # выводим на экран ID, имя и приватный комментарий
        print()
        print(f"Проект {project['id']}")
        print(project["public_name"])
        print(origin_private_comment if len(origin_private_comment) > 0 else "[Приватный комментарий отсутствует]")

        if private_comment:

            # добавляем к приватному комментарию с новой строки private_comment
            project["private_comment"] = (f"{origin_private_comment}\n" if len(origin_private_comment) > 0 else "") + private_comment
            request = requests.put(f"{HOST}/api/v1/projects/{PROJECT_ID}",
                                   data=json.dumps(project, ensure_ascii=False).encode('utf8'),
                                   headers=HEADER,
                                   verify=False)
            project = request.json()
            print()
            if "id" in project: # выводим обновлённый приватный комментарий
                print("Обновлённый приватный комментарий:")
                print(project["private_comment"])
            else: # выводим весь ответ, если произошла ошибка
                print("Не удалось обновить приватный комментарий:")
                print_pretty_json(project)

    except Exception as exc:

        # выводим информацию об ошибке
        print()
        print(exc)



# Главный метод (точка входа)
if __name__ == '__main__':

    get_project_and_update_private_comment("My login is UserX")