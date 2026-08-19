---
title: Переименовать поля формы
linktitle: Переименовать поля формы
type: docs
weight: 30
url: /ru/java/rename-form-fields/
description: Узнайте, как переименовать поля формы PDF на Java с использованием фасада Form в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Переименовать поля формы в PDF‑документе с помощью Java
Abstract: В этой статье показано, как привязать форму PDF, переименовать существующие поля и сохранить обновленный документ с помощью фасада Form в Aspose.PDF for Java.
---
Использовать `FormExamples.renameFormFields(...)` переименовать поля в интерактивной PDF-форме.

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

