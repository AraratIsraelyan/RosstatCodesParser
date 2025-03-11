"""
Этот модуль предназначен для управления директорией jsons/, 
которая используется для хранения JSON-файлов данных по ИНН.

Функции модуля:
create_directory() — создает папку jsons/, если ее нет.
delete_directory() — удаляет папку jsons/ вместе со всеми файлами.
"""

import os
import shutil

def create_directory() -> None:
    """
    Создает директорию для сохранения JSON-файлов данных по ИНН.
    Если директория уже существует, ничего не делает.
    Исключения:
        OSError: Если не удается создать директорию.
    """
    directory = "jsons/"
    try:
        os.mkdir(directory)
    except OSError as e:
        raise OSError(f"""Не удалось создать директорию {directory}.
        Причина: {e.strerror}""")


def delete_directory() -> None:
    """
    Удаляет директорию с JSON-файлами.
    Исключения:
        OSError: Если не удается удалить директорию.
    """
    directory = "jsons/"
    try:
        shutil.rmtree(directory)
    except OSError as e:
        raise OSError(f"""Не удалось удалить директорию {directory}.
        Причина: {e.strerror}""")