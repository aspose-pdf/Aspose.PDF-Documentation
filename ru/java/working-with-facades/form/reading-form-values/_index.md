---
title: Чтение значений формы
linktitle: Чтение значений формы
type: docs
weight: 60
url: /java/reading-form-values/
description: Узнайте, как проверять имена и значения полей формы PDF в Java с помощью фасада формы в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Чтение имен и значений полей формы PDF в Java
Abstract: В этом разделе рассматриваются рабочие процессы чтения форм Java, реализованные в текущем наборе примеров фасада формы для Aspose.PDF для Java. В репозитории представлен общий пример проверки на месте и используются явные примечания по объему для специализированных страниц, на которых еще нет соответствующих примеров Java.
---
Класс Java `FormExamples` демонстрирует основные рабочие процессы обработки форм, предоставляемые API фасадов.

## Получите значения полей

Используйте `FormExamples.inspectFormFields(...)` для проверки имен полей и их текущих значений.

```java
public static void inspectFormFields(Path inputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        System.out.println("Field names: " + Arrays.toString(form.getFieldNames()));
        for (String fieldName : form.getFieldNames()) {
            System.out.println(fieldName + " = " + form.getField(fieldName));
        }
    } finally {
        form.close();
    }
}
```
