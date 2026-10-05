---
title: ملء حقول النص
linktitle: ملء حقول النص
type: docs
weight: 10
url: /ar/java/fill-text-fields/
description: تعلم كيفية ملء حقول النص في نموذج PDF باستخدام Java وباستخدام واجهة Form في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: ملء حقول النموذج النصية في PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية ربط نموذج PDF، وتعيين قيم حقول النص حسب الاسم، وحفظ المستند المحدث باستخدام واجهة Form في Aspose.PDF for Java.
---
استخدام `FormExamples.fillTextFields(...)` لملء حقول النموذج النصية.

```java
public static void fillTextFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("name", "John Doe");
        form.fillField("address", "123 Main St, Anytown, USA");
        form.fillField("email", "john.doe@example.com");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
