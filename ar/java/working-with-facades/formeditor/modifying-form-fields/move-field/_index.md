---
title: نقل الحقل
linktitle: نقل الحقل
type: docs
weight: 30
url: /ar/java/move-field/
description: تعلم كيفية نقل حقل نموذج موجود في مستند PDF باستخدام Java عبر واجهة FormEditor في Aspose.PDF.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: نقل حقل نموذج PDF إلى موضع جديد باستخدام Java.
Abstract: توضح هذه المقالة كيفية ربط مستند PDF موجود، نقل حقل إلى إحداثيات جديدة، وحفظ المستند المحدث باستخدام واجهة FormEditor في Aspose.PDF for Java.
---
## نقل حقل

1. اربط ملف PDF المصدر بـ واجهة `FormEditor`.
2. استدعِ `moveField(...)` مع اسم الحقل المستهدف وإحداثيات المستطيل الجديدة.
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
