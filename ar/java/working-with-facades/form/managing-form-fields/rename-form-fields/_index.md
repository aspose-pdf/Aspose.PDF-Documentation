---
title: إعادة تسمية حقول النموذج
linktitle: إعادة تسمية حقول النموذج
type: docs
weight: 30
url: /java/rename-form-fields/
description: تعرف على كيفية إعادة تسمية حقول نموذج PDF في Java باستخدام واجهة النموذج في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: إعادة تسمية حقول النموذج في مستند PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية ربط نموذج PDF وإعادة تسمية الحقول الموجودة وحفظ المستند المحدث باستخدام واجهة النموذج في Aspose.PDF لـ Java.
---
استخدم `FormExamples.renameFormFields(...)` لإعادة تسمية الحقول في نموذج PDF تفاعلي.

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
