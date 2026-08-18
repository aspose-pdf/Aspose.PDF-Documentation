---
title: Заполнить поля переключателей
linktitle: Заполнить поля переключателей
type: docs
weight: 30
url: /java/fill-radio-button-fields/
description: Узнайте, как выбрать значение переключателя в форме PDF с помощью Java, используя фасад формы в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Выберите параметр поля переключателя в Java
Abstract: В этой статье показано, как привязать форму PDF, выбрать параметр переключателя по индексу и сохранить обновленный документ с фасадом формы в Aspose.PDF для Java.
---
Используйте `FormExamples.fillRadioButtonFields(...)`, чтобы выбрать опцию переключателя.

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
