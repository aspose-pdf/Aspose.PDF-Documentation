---
title: Сгладить все поля
linktitle: Сгладить все поля
type: docs
weight: 10
url: /java/flatten-all-fields/
description: Узнайте, как свести все поля формы PDF в Java с помощью фасада формы в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Преобразование всех полей интерактивной формы в статический контент в Java
Abstract: В этой статье показано, как связать форму PDF, сгладить каждое поле формы и сохранить обновленный документ с фасадом формы в Aspose.PDF для Java.
---
Используйте `FormExamples.flattenAllFields(...)`, когда вам нужно преобразовать все интерактивные поля в статическое содержимое страницы.

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
