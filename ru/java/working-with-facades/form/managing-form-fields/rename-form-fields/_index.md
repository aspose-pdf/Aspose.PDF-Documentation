---
title: Переименование полей формы
linktitle: Переименование полей формы
type: docs
weight: 30
url: /java/rename-form-fields/
description: Узнайте, как переименовывать поля формы PDF в Java с помощью фасада формы в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Переименование полей формы в PDF-документе с помощью Java
Abstract: В этой статье показано, как связать форму PDF, переименовать существующие поля и сохранить обновленный документ с фасадом формы в Aspose.PDF для Java.
---
Используйте `FormExamples.renameFormFields(...)` для переименования полей в интерактивной форме PDF.

```java
public static void renameFormFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.renameField("First Name", "NewFirstName");
        form.renameField("Last Name", "NewLastName");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
