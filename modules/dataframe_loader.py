import os
import json
import pandas as pd
from typing import List, Dict

def create_dataframe() -> pd.DataFrame:
    """
    Создаёт pandas DataFrame из JSON-файлов, находящихся в папке "jsons".
    
    JSON-файлы содержат данные об организациях. Функция загружает их,
    извлекает необходимые поля и формирует DataFrame.
    
    Возвращает:
        pd.DataFrame: Таблица с данными организаций, без дубликатов.
    """
    folder_path: str = "jsons"
    data: List[Dict[str, str]] = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path: str = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                json_data = json.load(file)

                for obj in json_data:
                    data.append({
                        "ОКПО / Идентификационный номер ТОСП": obj.get("okpo", ""),
                        "ОГРН / ОГРНИП": obj.get("ogrn", ""),
                        "Дата регистрации": obj.get("date_reg", ""),
                        "ИНН": obj.get("inn", ""),
                        "ОКАТО фактический": (
                            f"{obj['okato_fact']['code']} - {obj['okato_fact']['name']}"
                            if obj.get("okato_fact") else ""
                        ),
                        "ОКАТО регистрации": (
                            f"{obj['okato_reg']['code']} - {obj['okato_reg']['name']}"
                            if obj.get("okato_reg") else ""
                        ),
                        "ОКТМО фактический": (
                            f"{obj['oktmo_fact']['code']} - {obj['oktmo_fact']['name']}"
                            if obj.get("oktmo_fact") else ""
                        ),
                        "ОКТМО регистрации": (
                            f"{obj['oktmo_reg']['code']} - {obj['oktmo_reg']['name']}"
                            if obj.get("oktmo_reg") else ""
                        ),
                        "ОКОГУ": (
                            f"{obj['okogu']['code']} - {obj['okogu']['name']}"
                            if obj.get("okogu") else ""
                        ),
                        "ОКФС": (
                            f"{obj['okfs']['code']} - {obj['okfs']['name']}"
                            if obj.get("okfs") else ""
                        ),
                        "ОКОПФ": (
                            f"{obj['okopf']['code']} - {obj['okopf']['name']}"
                            if obj.get("okopf") else ""
                        )
                    })

    df = pd.DataFrame(data)
    return df.drop_duplicates()