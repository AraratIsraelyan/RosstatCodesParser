"""
Модуль current_datetime.py.
Функция возвращает текущую дату и время в строковом формате
"""

import datetime

def get_current_datetime() -> str:
    """
    Возвращает текущую дату и время в строковом формате.
    
    Формат вывода: ГГГГ_ММ_ДД_ЧЧ_ММ_СС.
    Пример: '2025_03_11_15_30_45'
    """
    return str(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
