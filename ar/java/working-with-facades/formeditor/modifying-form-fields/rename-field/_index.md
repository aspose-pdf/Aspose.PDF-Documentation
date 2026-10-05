---
title: إعادة تسمية الحقل
linktitle: إعادة تسمية الحقل
type: docs
weight: 50
url: /ar/java/rename-field/
description: تعلم كيفية إعادة تسمية حقل نموذج موجود في مستند PDF باستخدام Java عبر واجهة FormEditor في Aspose.PDF.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: إعادة تسمية حقل نموذج PDF بـ Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وإعادة تسمية الحقل المحدد، وحفظ المستند المحدث باستخدام واجهة FormEditor في Aspose.PDF for Java.
---
## إعادة تسمية حقل

1. اربط ملف PDF المصدر إلى واجهة `FormEditor`.
2. استدعِ `renameField(...)` مع اسم الحقل الحالي والاسم الجديد للحقل.
3. احفظ المستند المحدث.

```java
public static void renameField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.renameField("City", "Town");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
