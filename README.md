# Чат-бот для сообщества "Привет, Логопед!"

## Описание
Проект по созданию чат-ботов для Telegram и Вконтакте. Бот предоставляет следующие возможности:
1. Автоматизация ответа на простые вопросы пользователей;
2. Отслеживание результата работы с ребенком;
3. Получение информации об оплате;
4. Настройка уведомлений;
6. Возможность связаться с логопедом через бота;
7. Настройка бота администратором (изменение контента):


## Основные возможности админки

- Управление пользователями:

1. Просмотр списка пользователей: Вы можете просматривать полный список всех пользователей, которые взаимодействовали с ботом. Каждая учетная запись отображается с указанием имени пользователя (username), роли (role), платформы (platform).

3. Фильтрация и поиск пользователей: В админке вы можете использовать фильтры для упрощения поиска нужных пользователей.

4. Фильтрация по роли: Вы можете отфильтровать пользователей по их роли, чтобы, например, увидеть всех Логопедов или всех Родителей.

5. Фильтрация по платформе: Вы можете отфильтровать пользователей по платформе (Telegram или VK).


- Управление уведомлениями (Notification):

1. Просмотр списка уведомлений: Вы можете просматривать полный список всех созданных уведомлений. Каждое уведомление отображается с указанием пользователя, платформы, дней недели, времени отправки и разницы во времени с UTC.

2. Фильтрация уведомлений: В админке вы можете использовать фильтры для упрощения поиска нужных уведомлений.

3. Фильтрация по платформе: Вы можете отфильтровать уведомления по платформе (Telegram или VK).

4. Фильтрация по дням недели: Вы можете отфильтровать уведомления по дням недели, чтобы, например, увидеть все уведомления, отправляемые по понедельникам.

5. Поиск уведомлений: Вы можете искать уведомления по имени пользователя или дням недели. Это удобно, если вам нужно найти конкретное уведомление для редактирования или удаления.


- Управление контентом (Content):

1. Просмотр списка контента: Вы можете просматривать полный список всех созданных единиц контента.

2. Редактирование существующего контента: Вы можете редактировать уже созданный контент, обновляя ссылки, коды подарков или файлы. Это полезно, если вам нужно обновить материалы или добавить новые.


### Описание директорий проекта
- Backend - Модели базы данных, API, админка, маршруты и настройки сервера(админки);
- Telegram_bot - Приложение для запуска чат-бота на платформе Telegram;
- Vk_bot - Приложение для запуска чат-бота на платформе Вконтакте.

### Функциональные цели проекта:
Проект направлен на создание удобного и функционального чат-бота для сообщества “Привет, Логопед!”. Основные цели включают:

- Обеспечение поддержки пользователей(автоматизация ответов на вопросы).
- Предоставление инструментов для отслеживания прогресса работы с детьми.
- Обеспечение удобного доступа к информации об оплате приложения.
- Настройка и управление уведомлениями для пользователей.
- Обеспечение возможности связи с логопедом через бота.
- Предоставление администратору инструментов для настройки и управления ботом.

### Достигнутые и запланированные требования

* Достигнутые требования:
    1. Реализованы основные функции бота для Telegram и Вконтакте.
    2. Настроена админка для управления пользователями, уведомлениями и контентом.
    3. Обеспечена возможность создания уведомлений.
    4. Реализована функция связи с логопедом через бота.
* Запланированные требования:
    1. Добавление новых функций для улучшения взаимодействия с пользователями.
    2. Оптимизация производительности и безопасности бота.
    3. Расширение функционала админки для более гибкого управления ботом.
    4. Доработка рассылки новостей.
    5. Расширение функционала создания уведомлений.


## Запуск


## Договорённости именования веток, стиль кода и т.п.

### Правила использования веток.

Правила использования веток
* Основная ветка (develop):
    - Содержит стабильную версию проекта.
    - Все изменения в develop должны проходить через пул-реквесты и быть одобрены ревьюерами.
* Ветки для разработки и исправления ошибок:
    - Используются для разработки новых функций или исправления ошибок.
    - Создаются от develop.

### Порядок принятия пул-реквестов.
* Создание пул-реквеста:
    - Убедитесь, что все изменения закоммичены и запушены в соответствующую ветку.
    - Создайте пул-реквест в ветку main.
* Проверка и тестирование:
    - Убедитесь, что все тесты проходят успешно.
    - Проверьте, что код соответствует стилю кодирования проекта.
* Ревью кода:
    - Запросите ревью у одного или нескольких участников команды.
    - Внесите изменения по результатам ревью, если это необходимо.
Убедитесь, что все изменения корректно интегрированы и проект работает стабильно.

## Инструменты
- Aiogram;
- Vkbottle;
- Python;
- SQLAlchemy;
- Pydantic;
- SQLite.

## Команда
* Владислав Слепов - Тимлид
* Константин Гурашкин - Разработчик
* Ксения Катречко - Разработчик
* Виктор Рябов - Разработчик

