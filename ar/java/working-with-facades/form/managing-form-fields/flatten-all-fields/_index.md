---
title: تسوية جميع الحقول
linktitle: تسوية جميع الحقول
type: docs
weight: 10
url: /ar/java/flatten-all-fields/
description: تعلم كيفية تسوية جميع حقول نماذج PDF في Java باستخدام الواجهة Form في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: تحويل جميع حقول النموذج التفاعلية إلى محتوى ثابت في Java
Abstract: توضح هذه المقالة كيفية ربط نموذج PDF، تسوية كل حقل نموذج، وحفظ المستند المُحدَّث باستخدام الواجهة Form في Aspose.PDF for Java.
---
استخدام `FormExamples.flattenAllFields(...)` عندما تحتاج إلى تحويل جميع الحقول التفاعلية إلى محتوى صفحة ثابت.

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
