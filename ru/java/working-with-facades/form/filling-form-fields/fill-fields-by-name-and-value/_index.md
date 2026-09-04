---
title: Заполнение полей по имени и значению
linktitle: Заполнение полей по имени и значению
type: docs
weight: 60
url: /ru/java/fill-fields-by-name-and-value/
description: Узнайте, как адаптировать API заполнения полей фасада Form в Java для динамических обновлений формы по имени и значению.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Заполните несколько полей формы PDF из пар имя‑значение в Java
Abstract: Текущий набор Java‑примеров заполняет поля по отдельности с помощью повторяющихся вызовов `fillField(...)`. В этой статье показано, как применить тот же шаблон API к вашей собственной коллекции пар имя‑значение, не придумывая отдельную функцию фасада, которой нет в примерах репозитория.
---
Java `FormExamples` класс заполняет отдельные поля напрямую:

```java
form.fillField("name", "John Doe");
form.fillField("address", "123 Main St, Anytown, USA");
form.fillField("email", "john.doe@example.com");
```

Если ваше приложение уже имеет динамический набор имён полей и значений, примените то же самое `fillField(...)` вызов внутри вашего собственного цикла:

```java
for (Map.Entry<String, String> entry : values.entrySet()) {
    form.fillField(entry.getKey(), entry.getValue());
}
```

Это шаблон уровня приложения, полученный из того же Java API, который используется в `FormExamples.fillTextFields(...)`; текущий репозиторий не включает отдельный специализированный вспомогательный метод для заполнения на основе карты.


