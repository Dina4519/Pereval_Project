![image](https://github.com/user-attachments/assets/2b82f50c-30c7-4116-acb6-ed0faa82955e)

# Виртуальная стажировка 

## Pereval Rest API 

Федерации спортивного туризма России [pereval.online](https://pereval.online/) (далее - ФСТР) заказала студентам SkillFactory разработать мобильное приложение для Android и IOS, которое упростило бы туристам задачу по отправке данных о перевале и сократило время обработки запроса до трёх дней.

Пользоваться мобильным приложением будут туристы. В горах они будут вносить данные о перевале в приложение и отправлять их в ФСТР, как только появится доступ в Интернет.

Модератор из федерации будет верифицировать и вносить в базу данных информацию, полученную от пользователей, а те в свою очередь смогут увидеть в мобильном приложении статус модерации и просматривать базу с объектами, внесёнными другими.

___

*Турист с помощью мобильного приложения будет передавать в ФСТР следующие данные о перевале:
+ ***Информацию о себе:***
  + ***Фамилия;***
  + ***Имя;***
  + ***Отчество;***
  + ***Электронная почта;***
  + ***Номер телефона.***
+ ***Название объекта;***
+ ***Координаты объекта и его высоту;***
+ ***Уровень сложности в зависимости от времени года;***
+ ***Несколько фотографий.***

*После этого турист нажимает кнопку «Отправить» в мобильном приложении. Мобильное приложение вызовет метод ***Pereval.***

***Метод:***

```
POST/Pereval/
```

*принимает JSON в теле запроса с информацией о перевале. Пример JSON-а:*

```
{
  "beauty_title": "пер. ",
  "title": "Пхия",
  "other_titles": "Триев",
  "connect": "", //что соединяет, текстовое поле
 
  "add_time": "2021-09-22 13:18:13",
  "user": {"email": "qwerty@mail.ru", 		
        "fam": "Пупкин",
		 "name": "Василий",
		 "otc": "Иванович",
        "phone": "+7 555 55 55"}, 
 
   "coords":{
  "latitude": "45.3842",
  "longitude": "7.1525",
  "height": "1200"}
 
 
  level:{"winter": "", //Категория трудности. В разное время года перевал может иметь разную категорию трудности
  "summer": "1А",
  "autumn": "1А",
  "spring": ""},
 
   images: [{data:"<картинка1>", title:"Седловина"}, {data:"<картинка>", title:"Подъём"}]
}
```

***Результат метода: JSON***

+ *status — код HTTP, целое число:*

  *500 — ошибка при выполнении операции;*

  *400 — Bad Request (при нехватке полей);*

  *200 — успех.*

+ *message — строка:*

*Причина ошибки (если она была);*

Отправлено успешно;

Если отправка успешна, дополнительно возвращается id вставленной записи.

id — идентификатор, который был присвоен объекту при добавлении в базу данных.

***Примеры oтветов:***

`{ "status": 500, "message": "Ошибка подключения к базе данных","id": null}`

`{ "status": 200, "message": null, "id": 42 }`

*После того, как турист добавит в базу данных информацию о новом перевале, сотрудники ФСТР проведут модерацию для каждого нового объекта и поменяют поле status.*

***Допустимые значения поля status:***

+ *'new';*
+ *'pending' — модератор взял в работу;*
+ *'accepted' — модерация прошла успешно;*
+ *'rejected' — модерация прошла, информация не принята.*

___

***Метод:***

```
GET /Pereval/<id>
```

*получает одну запись (перевал) по её id с выведением всей информацию об перевале, в том числе статус модерации.*

___

***Метод:***

```
PATCH /Pereval/<id>
```

*позволяет отредактировать существующую запись (замена), при условии что она в статусе "new". При этом редактировать можно все поля, кроме тех, что содержат ФИО, адрес почты и номер телефона. В качестве результата изменения приходит ответ содержащий следующие данные:*

*state: 1 — если успешно удалось отредактировать запись в базе данных. 0 — в отредактировать запись не удалось.*

*message: сообщение о причине неудачного обновления записи.*

___

***Метод:***

```
GET /Pereval/?user_id__email=<email>
```

*позволяет получить данные всех объектов, отправленных на сервер пользователем с почтой.*

В качестве реализации использована фильтрация по адресу электронной почты пользователя с помощью пакета **django-filter**

___

***Документация сгенерирована с помощью пакета drf-yasg***

 *Документация ***swagger***: http://127.0.0.1:8000/swagger/*
 
 *Документация ***redoc***: http://127.0.0.1:8000/redoc/*

___

***Дополнительно:***

   1.*Реализовано повторное использование существующего объекта модели `PassUser` при создания нового объекта модели `Pereval`. Если запрос (метод `POST/Pereval/`) на добавление записи отправляет пользователь, ранее уже отправлявший такой запрос (определяется по `email`), то для текущей записи используются ранее записанные данные пользователя, а не создается новый пользователь (объект модели `PassUser`).*
   
   2.*Для создания и изменения объектов моделей со связанными данными вложенных сериализаторов использован пакет `drf-writable-nested`*

___

*Проект опубликован на хостинге ***pythonanywhere.com***

*API ***Pereval***: https://Dina47.pythonanywhere.com/Pereval/*

