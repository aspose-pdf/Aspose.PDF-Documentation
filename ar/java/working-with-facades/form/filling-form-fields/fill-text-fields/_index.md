---
title: ملء الحقول النصية
linktitle: ملء الحقول النصية
type: docs
weight: 10
url: /java/fill-text-fields/
description: تعرف على كيفية ملء الحقول النصية في نموذج PDF باستخدام Java باستخدام واجهة النموذج في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: تعبئة حقول النموذج النصي في ملف PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية ربط نموذج PDF، وتعيين قيم الحقول النصية حسب الاسم، وحفظ المستند المحدث باستخدام واجهة النموذج في Aspose.PDF لـ Java.
---
استخدم `FormExamples.fillTextFields(...)` لملء حقول النماذج النصية.

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
