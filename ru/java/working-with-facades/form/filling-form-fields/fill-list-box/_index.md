---
title: Заполнить список
linktitle: Заполнить список
type: docs
weight: 40
url: /java/fill-list-box/
description: Узнайте, как заполнить поле списка в форме PDF с помощью Java, используя фасад формы в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Установите значение поля списка в форме PDF с помощью Java
Abstract: В этой статье показано, как связать форму PDF, установить значение поля списка и сохранить обновленный документ с фасадом формы в Aspose.PDF для Java.
---
Используйте `FormExamples.fillListBoxFields(...)`, чтобы заполнить поле списка.

```java
public static void fillListBoxFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("favorite_colors", "Red");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
