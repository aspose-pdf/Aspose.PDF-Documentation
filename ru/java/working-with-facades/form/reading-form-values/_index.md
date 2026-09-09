---
title: Чтение значений формы
linktitle: Чтение значений формы
type: docs
weight: 60
url: /ru/java/reading-form-values/
description: Узнайте, как просматривать имена полей формы PDF и их значения в Java с использованием фасада Form в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Чтение имен полей формы PDF и их значений в Java
Abstract: В этом разделе рассматриваются потоки чтения форм Java, реализованные в текущем наборе примеров фасада Form для Aspose.PDF for Java. Репозиторий предоставляет общий пример инспекции полей и использует явные примечания к области для специализированных страниц, для которых пока нет соответствующих примеров на Java.
---
Java `FormExamples` класс демонстрирует основные рабочие процессы обработки форм, предоставляемые Facades API.

## Получите значения полей

Использовать `FormExamples.inspectFormFields(...)` для проверки имен полей и их текущих значений.

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


