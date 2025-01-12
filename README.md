# Домашняя работа Django REST framework
Работа над SPA веб-приложением.
Ожидание - бэкенд-сервер, который возвращает клиенту JSON-структуры
##   Урок 30.1: Вьюсеты и дженерики
### Задание:
1. Создайте новый Django-проект, подключите DRF в настройках проекта
2. Создайте следующие модели:

Пользователь:
- все поля от обычного пользователя, но авторизацию заменить на email;
- телефон;
- город;
- аватарка.
- Модель пользователя разместите в приложении users

Курс:
- название,
- превью (картинка),
- описание.

Урок:
- название,
- описание,
- превью (картинка),
- ссылка на видео.

Урок и курс - это связанные между собой сущности. Уроки складываются в курс, в одном курсе может быть много уроков. Реализуйте связь между ними.
Модель курса и урока разместите в отдельном приложении. Название для приложения выбирайте такое, чтобы оно описывало то, с какими сущностями приложение работает. Например, lms или materials - отличные варианты.

3. Опишите CRUD для моделей курса и урока. Для реализации CRUD для курса используйте Viewsets, а для урока - Generic-классы.
Для работы контроллеров опишите простейшие сериализаторы. Работу каждого эндпоинта необходимо проверять с помощью Postman

##   Урок 30.2: Сериализаторы
### Задание:
1. Для модели курса добавьте в сериализатор поле вывода количества уроков. Поле реализуйте с помощью 
SerializerMethodField()

2. Добавьте новую модель в приложение users:
- Платежи
- пользователь,
- дата оплаты,
- оплаченный курс или урок,
- сумма оплаты,
- способ оплаты: наличные или перевод на счет.
Поля пользователь , оплаченный курс и отдельно оплаченный урок должны быть ссылками на соответствующие модели.

Запишите в таблицу, соответствующую этой модели данные через инструмент фикстур или кастомную команду.
Если вы забыли как работать с фикстурами или кастомной командой - можете вернуться к уроку 20.1 Работа с ORM в Django чтобы вспомнить материал.

3. Для сериализатора для модели курса реализуйте поле вывода уроков. Вывод реализуйте с помощью сериализатора для связанной модели.
Один сериализатор должен выдавать и количество уроков курса и информацию по всем урокам курса одновременно.

4. Настроить фильтрацию для эндпоинта вывода списка платежей с возможностями:
- менять порядок сортировки по дате оплаты,
- фильтровать по курсу или уроку,
- фильтровать по способу оплаты.

##   Урок 31: Права доступа в DRF
### Задание:
1. Реализуйте CRUD для пользователей, в том числе регистрацию пользователей, настройте в проекте использование JWT-авторизации и закройте каждый эндпоинт авторизацией.
2. Заведите группу модераторов и опишите для нее права работы с любыми уроками и курсами, но без возможности их удалять и создавать новые. Заложите функционал такой проверки в контроллеры.
3. Опишите права доступа для объектов таким образом, чтобы пользователи, которые не входят в группу модераторов, могли видеть, редактировать и удалять только свои курсы и уроки.

##   Урок 32.1: Валидаторы, пагинация и тесты
### Задание:
1. Для сохранения уроков и курсов реализуйте дополнительную проверку на отсутствие в материалах ссылок на сторонние ресурсы, кроме youtube.com.
То есть ссылки на видео можно прикреплять в материалы, а ссылки на сторонние образовательные платформы или личные сайты — нельзя.
2. Добавьте модель подписки на обновления курса для пользователя.
3. Реализуйте пагинацию для вывода всех уроков и курсов.
4. Напишите тесты, которые будут проверять корректность работы CRUD уроков и функционал работы подписки на обновления курса.

##   Урок 32.2: Документирование и безопасность
### Задание:
1. Подключить и настроить вывод документации для проекта. Убедиться, что каждый из реализованных эндпоинтов описан в документации верно, при необходимости описать вручную.
Для работы с документацией проекта воспользуйтесь библиотекой drf-yasg или drf-spectacular.
2. Подключить возможность оплаты курсов через https://stripe.com/docs/api.
Доступы можно получить напрямую из документации, а также пройти простую регистрацию по адресу https://dashboard.stripe.com/register.
Для работы с запросами вам понадобится реализовать обращение к эндпоинтам:
https://stripe.com/docs/api/products/create — создание продукта;
https://stripe.com/docs/api/prices/create — создание цены;
https://stripe.com/docs/api/checkout/sessions/create — создание сессии для получения ссылки на оплату.
Для тестирования можно использовать номера карт из документации: https://stripe.com/docs/terminal/references/testing#standard-test-cards.

##   Урок 32.2: Celery
### Задание:
1. Настройте проект для работы с Celery. Также настройте приложение на работу с celery-beat для выполнения периодических задач.
2. Добавьте асинхронную рассылку писем пользователям об обновлении материалов курса.
Чтобы реализовать асинхронную рассылку, вызывайте специальную задачу по отправке письма в коде контроллера. То есть вызов задачи на отправку сообщения должен происходить в контроллере обновления курса: когда курс обновлен — тем, кто подписан на обновления именно этого курса, отправляется письмо на почту.
3. С помощью celery-beat реализуйте фоновую задачу, которая будет проверять пользователей по дате последнего входа по полю 
last_login и, если пользователь не заходил более месяца, блокировать его с помощью флага is_active.
Задачу сделайте периодической и запланируйте расписание в настройках celery-beat.
Обратите внимание на timezone вашего приложения и timezone в настройках celery: важно, чтобы они были одинаковыми, чтобы задачи запускались в корректное время.

##   Урок 34: Docker
### Задание:
1. Опишите Dockerfile для запуска контейнера с проектом.
2. Оберните в Docker Compose Django-проект с БД PostgreSQL.
3. Допишите в docker-compose.yaml работу с Redis.
4. Допишите в docker-compose.yaml работу с Celery.

##   Урок 35: CI/CD и GitHub Actions
### Задание:
1. Настройте удаленный сервер для работы с веб-приложением, которое вы разрабатывали в рамках домашних работ на курсе DRF.
2. Создайте и настройте файл GitHub Actions workflow, который будет:
- Запускать тесты проекта автоматически при каждом push в репозиторий.
- Автоматически деплоить проект на удаленный сервер после успешного прохождения тестов.