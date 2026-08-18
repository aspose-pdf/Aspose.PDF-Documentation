---
title: تتسطح جميع الحقول
linktitle: تتسطح جميع الحقول
type: docs
weight: 10
url: /java/flatten-all-fields/
description: تعرف على كيفية تسوية جميع حقول نماذج PDF في Java باستخدام واجهة النموذج في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: تحويل كافة حقول النموذج التفاعلية إلى محتوى ثابت في Java
Abstract: توضح هذه المقالة كيفية ربط نموذج PDF، وتسوية كل حقل من حقول النموذج، وحفظ المستند المحدث باستخدام واجهة النموذج في Aspose.PDF لـ Java.
---
استخدم `FormExamples.flattenAllFields(...)` عندما تحتاج إلى تحويل كافة الحقول التفاعلية إلى محتوى صفحة ثابت.

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
