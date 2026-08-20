---
title: Установить флаг отправки
linktitle: Установить флаг отправки
type: docs
weight: 40
url: /ru/java/set-submit-flag/
description: Просмотрите текущую поддержку Java для установки флага отправки на кнопку PDF-формы с фасадом FormEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Конфигурация флага отправки в примерах FormEditor на Java
Abstract: Текущий набор Java‑примеров не раскрывает конфигурацию submit‑flag как отдельный самостоятельный пример метода. Вместо этого она демонстрируется совместно с конфигурацией submit URL в `setSubmitUrl(...)`.
---
Java `FormEditorExamples.setSubmitUrl(...)` метод включает:

## Настройте флаг отправки

1. Привяжите исходный PDF к `FormEditor` фасад.
2. Установите URL отправки для поля кнопки.
3. Установите флаг отправки для требуемого формата.
4. Сохраните обновлённый документ.

```java
editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
```

Используйте этот комбинированный пример в качестве Java‑workflow с поддержкой источника для настройки флага отправки в этом репозитории.


