# Инструкция по использованию скрипта для парсинга данных

## Описание
Этот скрипт предназначен для выполнения запросов к веб-сервису, получения данных по ИНН (Идентификационный номер налогоплательщика), их сохранения в JSON-файлы, преобразования этих данных в таблицу и сохранения в Excel-файл. Также он поддерживает создание и удаление директорий для временного хранения файлов.

## Установка
1. Убедитесь, что у вас установлен Python версии 3.9 или выше.
2. Установите необходимые библиотеки, выполнив следующую команду:
   ```bash
   pip install requests pandas openpyxl
   ```

## Структура скрипта

### Основные функции

#### 1. `create_directory()`
Создаёт директорию `jsons/` для хранения JSON-файлов.
- **Возвращаемое значение**: None

#### 2. `delete_directory()`
Удаляет директорию `jsons/` вместе со всеми файлами внутри.
- **Возвращаемое значение**: None

#### 3. `run_request(inn)`
Выполняет запрос к веб-сервису для получения данных по ИНН.
- **Параметры**:
  - `inn` (str): ИНН для запроса.
- **Возвращаемое значение**: JSON-ответ от сервиса.

#### 4. `check_request(inn)`
Сохраняет ответ от веб-сервиса в файл JSON и обновляет списки успешных и неудачных запросов.
- **Параметры**:
  - `inn` (str): ИНН для запроса.
- **Возвращаемое значение**: None

#### 5. `create_dataframe()`
Создаёт Excel-файл на основе данных, сохранённых в JSON-файлах.
- **Возвращаемое значение**: None

### Основной сценарий работы
1. Создаётся директория для хранения JSON-файлов (`create_directory`).
2. Загружается список ИНН из Excel-файла (`input_inn.xlsx`).
3. Выполняются запросы для каждого ИНН (`run_request`, `check_request`).
4. JSON-файлы преобразуются в Excel-таблицу (`create_dataframe`).
5. Директория с временными файлами удаляется (`delete_directory`).

## Использование

1. Подготовьте файл `input_inn.xlsx` в следующем формате:
   - Должен содержать колонку `inn` с ИНН для обработки.

2. Запустите jupyterlab и скрипт в файле main:
   ```bash
   python -m jupyterlab
   ```

4. Скрипт создаст Excel-файл с результатами в формате `ГГГГ_ММ_ДД_Парсинг_ИНН.xlsx` в текущей директории.

## Логика обработки
- Если запрос к веб-сервису выполнен успешно, JSON-файл сохраняется в директорию `jsons/`.
- Если запрос не удался, ИНН добавляется в список неудачных запросов (`fail_inn`).
- Скрипт повторяет попытки для всех ИНН из списка, которые не удалось обработать.

## Требования
- Интернет-соединение.
- Доступ к веб-сервису: https://websbor.rosstat.gov.ru/webstat/api/gs/organizations.

## Возможные ошибки и их обработка
1. Ошибки создания или удаления директории:
   - Проверяйте права доступа к файловой системе.
2. Ошибки выполнения запросов:
   - Убедитесь, что URL и параметры запроса корректны.
   - Проверьте заголовки и куки.
3. Ошибки чтения/записи файлов:
   - Убедитесь, что файлы не заняты другими процессами.

## Советы по настройке
- **Задержка между запросами**:
  Установите паузу между запросами с помощью функции `time.sleep()` для предотвращения блокировки IP-адреса.
- **Логирование**:
  Добавьте дополнительные логи для удобства отладки.

## Контакты
Если у вас возникли вопросы или проблемы, свяжитесь с автором скрипта ararat.israelyan@mail.ru Арарат Исраелян