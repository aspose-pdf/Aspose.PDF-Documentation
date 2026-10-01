---
title: إعادة تسمية حقول النموذج (Form)
linktitle: إعادة تسمية حقول النموذج (Form)
type: docs
weight: 30
url: /ar/java/rename-form-fields/
description: تعلم كيفية إعادة تسمية حقول نموذج PDF في Java باستخدام واجهة Form في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: إعادة تسمية حقول النموذج في مستند PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية ربط نموذج PDF، وإعادة تسمية الحقول الموجودة، وحفظ المستند المحدث باستخدام واجهة Form في Aspose.PDF for Java.
---
استخدام `FormExamples.renameFormFields(...)` لإعادة تسمية الحقول في نموذج PDF تفاعلي.

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
