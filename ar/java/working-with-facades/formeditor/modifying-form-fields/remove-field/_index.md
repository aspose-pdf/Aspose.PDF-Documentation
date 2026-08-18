---
title: إزالة الحقل
linktitle: إزالة الحقل
type: docs
weight: 40
url: /java/remove-field/
description: تعرف على كيفية إزالة حقل نموذج موجود من مستند PDF في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: حذف حقل نموذج PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وإزالة حقل محدد، وحفظ المستند المحدث باستخدام واجهة FormEditor في Aspose.PDF لـ Java.
---
## إزالة حقل

1. قم بربط ملف PDF المصدر بالواجهة `FormEditor`.
2. اتصل `removeField(...)` للحصول على اسم الحقل الهدف.
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
