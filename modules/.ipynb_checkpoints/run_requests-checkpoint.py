import time
import requests
import json
from typing import List
from tqdm.notebook import tqdm

# Создаем пустые списки для значений
success_inn: List[str] = []
fail_inn: List[str] = []

"""
Функция выполнения запросов в веб-странице
Аргументы: 
    inn : string
Возвращает:
    responce : json (ответ)
"""
def run_request(inn):
    # URL для запроса
    url = "https://websbor.rosstat.gov.ru/webstat/api/gs/organizations"
    
    # Заголовки запроса
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://websbor.rosstat.gov.ru",
        "Referer": "https://websbor.rosstat.gov.ru/online/info",
    }
    
    # Тело запроса (данные для отправки)
    data = {
        "okpo": "",
        "inn": f"{inn}",  # ИНН
        "ogrn": ""
    }
    
    # Куки (замените своими значениями, если они необходимы для сессии)
    cookies = {
        "ASP.NET_SessionId": "5usinsgoc0t5qcsewidexcuy",
        "SERVERID_ONLINE": "online_03"
    }
    
    try:
        # Выполнение запроса
        response = requests.post(url, headers=headers, json=data, cookies=cookies, verify=False)
        response.raise_for_status()  # Проверка на HTTP ошибки
        return response
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса для ИНН {inn}: {e}")
        time.sleep(20)
        return None
"""
Функция сохраняет результат парсинга в json файл в директории
"""
def check_request(inn):
    response = run_request(inn)
    if response is not None:
        try:
            # Сохранение JSON-данных в файл с названием по ИНН
            file_name = f"jsons/{inn}.json"
            with open(file_name, "w", encoding="utf-8") as file:
                json.dump(response.json(), file, ensure_ascii=False, indent=4)
            # Сохранение ИНН в список успешных запросов
            success_inn.append(inn)  
        except (json.JSONDecodeError, IOError) as e:
            print(f"Ошибка при сохранении данных для ИНН {inn}: {e}")
            # Сохранение ИНН в список неудачных запросов
            fail_inn.append(inn)  
    else:
        # Сохранение ИНН в список неудачных запросов, если запрос не удался
        fail_inn.append(inn)

"""
Функция запускает парсинг заданной ИНН
"""
def run_parser(inn_lst):
    inn_list = inn_lst
    # В цикле парсим все ИНН
    while len(inn_list) > 0:
        inn_list = list(set(inn_list) - set(success_inn))
        # Перебор ИНН из списка и выполнение запроса
        for inn in tqdm(inn_list):
            check_request(inn)
            time.sleep(5)