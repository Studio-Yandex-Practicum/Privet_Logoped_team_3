# Чат-бот для сообщества "Привет, Логопед!"

## Описание
Проект по созданию чат-ботов для Telegram и Вконтакте. Бот предоставляет следующие возможности:
1. Помощь в работе с мобильным приложением;
2. Отслеживание результата работы с ребенком;
3. Получение информации об оплате приложения;
4. Настройка уведомлений;
5. Рассылка сообщений подписчикам;
6. Возможность связаться с логопедом через бота;
7. Настройка бота администратором (изменение ссылкок, настройка рассылки и т.д.):


## Основные возможности админки

- Управление пользователями:

1. Просмотр списка пользователей: Вы можете просматривать полный список всех пользователей, которые взаимодействовали с ботом. Каждая учетная запись отображается с указанием имени пользователя (username), роли (role), платформы (platform), а также статус активности (is_active) и наличие административных прав (is_staff).

2. Редактирование пользователей: Вы можете редактировать информацию о пользователе.

3. Активность учетной записи (is_active): Вы можете включать или отключать учетную запись. Отключенные учетные записи не смогут войти в систему (блокировка).

4. Фильтрация и поиск пользователей: В админке вы можете использовать фильтры для упрощения поиска нужных пользователей.

5. Фильтрация по роли: Вы можете отфильтровать пользователей по их роли, чтобы, например, увидеть всех Логопедов или всех Родителей.

6. Фильтрация по платформе: Вы можете отфильтровать пользователей по платформе (Telegram или VK).

7. Поиск пользователей: Вы можете искать пользователей по имени пользователя. Это удобно, если вам нужно найти конкретного пользователя.

- Управление уведомлениями (Notification):

1. Просмотр списка уведомлений: Вы можете просматривать полный список всех созданных уведомлений. Каждое уведомление отображается с указанием пользователя, платформы, дней недели, времени отправки и разницы во времени с московским временем.

2. Редактирование существующих уведомлений: Вы можете редактировать уже созданные уведомления, изменяя дни недели, время отправки и другие параметры.
Это полезно, если у пользователя изменился график или если вам нужно скорректировать настройки уведомлений.

3. Удаление уведомлений: Вы можете удалять уведомления, если они больше не нужны. Это предотвращает отправку ненужных или устаревших напоминаний.

4. Фильтрация уведомлений: В админке вы можете использовать фильтры для упрощения поиска нужных уведомлений.

5. Фильтрация по платформе: Вы можете отфильтровать уведомления по платформе (Telegram или VK).

6. Фильтрация по дням недели: Вы можете отфильтровать уведомления по дням недели, чтобы, например, увидеть все уведомления, отправляемые по понедельникам.

7. Поиск уведомлений: Вы можете искать уведомления по имени пользователя или дням недели. Это удобно, если вам нужно найти конкретное уведомление для редактирования или удаления.

- Управление контентом (Content):

1. Просмотр списка контента: Вы можете просматривать полный список всех созданных единиц контента.

2. Создание нового контента: Вы можете создавать новый контент, который будет отправляться пользователям.

    * Код подарка: Указываете уникальный код, который пользователи могут использовать для получения подарка.

    * URL подарка: Указываете ссылку на подарок, который пользователь получит, введя правильный код.

    * Полезная ссылка: Указываете полезную ссылку, которую пользователи могут использовать, например, для просмотра обучающих видео или получения дополнительной информации.

    * Файл для отслеживания: Загружаете файл, который поможет пользователям отслеживать прогресс. Это может быть таблица или другой документ.

    * URL оплаты: Указываете ссылку, по которой пользователи смогут оплатить услуги или приобрести дополнительные материалы.

    * Файл оплаты для iOS: Загружаете файл с инструкцией по оплате для пользователей устройств на iOS.

    * Файл помощи по установке: Загружаете файл с инструкцией по установке приложения или другого программного обеспечения.

    * Файл для ПК: Загружаете файл, который помогает пользователям вывести приложение или контент на ПК.

3. Редактирование существующего контента: Вы можете редактировать уже созданный контент, обновляя ссылки, коды подарков или файлы. Это полезно, если вам нужно обновить материалы или добавить новые.

4. Удаление контента: Вы можете удалять единицы контента, если они больше не актуальны. Это позволяет поддерживать базу контента актуальной и не перегруженной устаревшими материалами.

5. Фильтрация контента: В админке вы можете использовать фильтры для упрощения поиска нужного контента.

6. Фильтрация по коду подарка: Вы можете отфильтровать контент по коду подарка, чтобы увидеть все единицы, связанные с конкретным кодом.

7. Фильтрация по полезной ссылке: Вы можете отфильтровать контент по полезной ссылке, чтобы, например, найти все обучающие видео.

8. Поиск контента: Вы можете искать контент по коду подарка, полезной ссылке или ссылке для оплаты. Это удобно, если вам нужно быстро найти и отредактировать или удалить конкретный контент.


### Описание директорий проекта
### Функциональные цели проекта: 
### Достигнутые и запланированные требования


## Запуск


## Договорённости именования веток, стиль кода и т.п.

### Правила использования веток.
### Нейминг веток.
### Порядок принятия пул-реквестов.

## Инструменты
- SQLAlchemy;
- Aiogram;
- Vkbottle;
- Python;
- SQLite/MySql.
- AioSqlite
- Alembics

## Команда
Владислав Слепов - Тимлид
Константин Гурашкин - Разработчик
Ксения Катречко - Разработчик
Виктор Рябов - Разработчик

