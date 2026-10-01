---
title: إزالة الحقل
linktitle: إزالة الحقل
type: docs
weight: 40
url: /ar/java/remove-field/
description: تعلم كيفية إزالة حقل نموذج موجود من مستند PDF في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: حذف حقل نموذج PDF في Java
Abstract: توضح هذه المقالة كيفية ربط مستند PDF موجود، وإزالة حقل محدد، ثم حفظ المستند المحدث باستخدام واجهة FormEditor في Aspose.PDF for Java.
---
## إزالة حقل

1. ربط ملف PDF المصدر بـ `FormEditor` واجهة.
2. اتصال `removeField(...)` لاسم الحقل الهدف.
3. احفظ المستند المحدث.

```java
public static void removeField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeField("Country");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
