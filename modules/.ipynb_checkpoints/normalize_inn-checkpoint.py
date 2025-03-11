from typing import List

def normalize_inn_list(inn_list: List[str]) -> List[str]:
    """
    Дополняет номера ИНН ведущими нулями до длины 10 символов.

    Параметры:
    inn_list (List[str]): Список ИНН в строковом формате.

    Возвращает:
    List[str]: Список ИНН с дополненными нулями.
    """
    return list(set([inn.zfill(10) for inn in inn_list]))