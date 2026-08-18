---
title: Установить флаг отправки
linktitle: Установить флаг отправки
type: docs
weight: 40
url: /java/set-submit-flag/
description: Ознакомьтесь с текущим описанием Java для установки флага отправки на кнопке формы PDF с фасадом FormEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Отправка конфигурации флага в примерах Java FormEditor
Abstract: Текущий набор примеров Java не представляет конфигурацию флага отправки в качестве отдельного автономного примера метода. Вместо этого это демонстрируется вместе с конфигурацией URL-адреса отправки в `setSubmitUrl(...)`.
---
Метод Java `FormEditorExamples.setSubmitUrl(...)` включает в себя:

## Настройте флаг отправки

1. Привяжите исходный PDF-файл к фасаду `FormEditor`.
2. Установите URL-адрес отправки для поля кнопки.
3. Установите флаг отправки для необходимого формата.
4. Сохраните обновленный документ.

```java
editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
```

Используйте этот объединенный пример в качестве рабочего процесса Java с исходным кодом для настройки флага отправки в этом репозитории.
