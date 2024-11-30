# Домашняя работа Django REST frameworm
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
Реализуйте CRUD для пользователей, в том числе регистрацию пользователей, настройте в проекте использование JWT-авторизации и закройте каждый эндпоинт авторизацией.

### Задание:
Заведите группу модераторов и опишите для нее права работы с любыми уроками и курсами, но без возможности их удалять и создавать новые. Заложите функционал такой проверки в контроллеры.

### Задание:
Опишите права доступа для объектов таким образом, чтобы пользователи, которые не входят в группу модераторов, могли видеть, редактировать и удалять только свои курсы и уроки.