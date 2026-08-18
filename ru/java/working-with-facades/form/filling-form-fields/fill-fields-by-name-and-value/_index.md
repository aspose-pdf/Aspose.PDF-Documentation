---
title: Заполните поля по имени и значению
linktitle: Заполните поля по имени и значению
type: docs
weight: 60
url: /java/fill-fields-by-name-and-value/
description: Узнайте, как адаптировать API заполнения полей фасада формы на Java для динамических обновлений форм с использованием значений имен.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Заполнение нескольких полей формы PDF из пар имя-значение в Java
Abstract: Текущий набор примеров Java заполняет поля индивидуально с помощью повторяющихся вызовов `fillField(...)`. В этой статье показано, как применить тот же шаблон API к вашей собственной коллекции значений имени, не изобретая отдельную функцию фасада, которой нет в примерах репозитория.
---
Класс Java `FormExamples` заполняет отдельные поля напрямую:

```java
form.fillField("name", "John Doe");
form.fillField("address", "123 Main St, Anytown, USA");
form.fillField("email", "john.doe@example.com");
```

Если в вашем приложении уже есть динамический набор имен и значений полей, примените тот же вызов `fillField(...)` внутри собственного цикла:

```java
for (Map.Entry<String, String> entry : values.entrySet()) {
    form.fillField(entry.getKey(), entry.getValue());
}
```

Это шаблон уровня приложения, полученный на основе того же API Java, который используется в `FormExamples.fillTextFields(...)`; текущий репозиторий не включает отдельный специальный вспомогательный метод для заполнения на основе карты.
