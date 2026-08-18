---
title: نقل الميدان
linktitle: نقل الميدان
type: docs
weight: 30
url: /java/move-field/
description: تعرف على كيفية نقل حقل نموذج موجود في مستند PDF في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: انقل حقل نموذج PDF إلى موضع جديد في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، ونقل حقل إلى إحداثيات جديدة، وحفظ المستند المحدث باستخدام واجهة FormEditor في Aspose.PDF لـ Java.
---
## نقل حقل

1. قم بربط ملف PDF المصدر بالواجهة `FormEditor`.
2. اتصل `moveField(...)` باسم الحقل الهدف وإحداثيات المستطيل الجديد.
3. احفظ المستند المحدث.

```java
public static void moveField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.moveField("Country", 200, 600, 280, 620);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
