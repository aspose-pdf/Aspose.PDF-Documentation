---
title: Заполнить List Box
linktitle: Заполнить List Box
type: docs
weight: 40
url: /ru/java/fill-list-box/
description: Узнайте, как заполнить поле списка в PDF-форме с помощью Java, используя фасад Form в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Установить значение поля списка в PDF-форме с помощью Java
Abstract: В этой статье показано, как привязать PDF-форму, установить значение поля списка и сохранить обновлённый документ с помощью фасада Form в Aspose.PDF for Java.
---
Использовать `FormExamples.fillListBoxFields(...)` для заполнения поля списка.

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

