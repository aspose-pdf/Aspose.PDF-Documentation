---
title: Заполните поля флажка
linktitle: Заполните поля флажка
type: docs
weight: 20
url: /java/fill-check-box-fields/
description: Learn how to fill check box fields in a PDF form with Java using the Form facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Установите значения полей флажка в форме PDF с помощью Java
Abstract: В этой статье показано, как связать форму PDF, установить поля флажков по имени и сохранить обновленный документ с фасадом формы в Aspose.PDF для Java.
---
Используйте `FormExamples.fillCheckBoxFields(...)`, чтобы установить значения флажков в форме.

```java
public static void fillCheckBoxFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("subscribe_newsletter", "Yes");
        form.fillField("accept_terms", "Yes");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
