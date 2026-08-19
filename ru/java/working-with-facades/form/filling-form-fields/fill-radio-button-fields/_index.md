---
title: Заполнение полей радиокнопок
linktitle: Заполнение полей радиокнопок
type: docs
weight: 30
url: /ru/java/fill-radio-button-fields/
description: Узнайте, как выбрать значение радиокнопки в PDF-форме с помощью Java, используя фасад Form в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Выбор параметра поля радиокнопки в Java
Abstract: В этой статье показано, как привязать PDF-форму, выбрать параметр радиокнопки по индексу и сохранить обновлённый документ с помощью фасада Form в Aspose.PDF for Java.
---
Использовать `FormExamples.fillRadioButtonFields(...)` выбрать вариант радиокнопки.

```java
public static void fillRadioButtonFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("gender", 0);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

