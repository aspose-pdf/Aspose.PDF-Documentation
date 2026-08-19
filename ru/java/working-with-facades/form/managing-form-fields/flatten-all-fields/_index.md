---
title: Свести все поля
linktitle: Свести все поля
type: docs
weight: 10
url: /ru/java/flatten-all-fields/
description: Узнайте, как сплющить все поля формы PDF в Java с использованием фасада Form в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Преобразуйте все интерактивные поля формы в статический контент в Java
Abstract: В этой статье показано, как привязать форму PDF, сплющить каждое поле формы и сохранить обновленный документ с помощью фасада Form в Aspose.PDF for Java.
---
Использовать `FormExamples.flattenAllFields(...)` когда вам нужно преобразовать все интерактивные поля в статическое содержимое страницы.

```java
public static void flattenAllFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.flattenAllFields();
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

