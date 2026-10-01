---
title: ضبط مظهر الحقل
linktitle: ضبط مظهر الحقل
type: docs
weight: 40
url: /ar/java/set-field-appearance/
description: تعرف على كيفية تغيير علامات المظهر البصري لحقل نموذج PDF في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: تغيير علامات مظهر حقل نموذج PDF في Java
Abstract: توضح هذه المقالة كيفية ربط PDF موجود، وتطبيق علامة مظهر على حقل، وحفظ المستند المحدث باستخدام واجهة FormEditor في Aspose.PDF for Java.
---
## ضبط علامات مظهر الحقل

1. ربط ملف PDF المصدر بـ `FormEditor` واجهة.
2. مكالمة `setFieldAppearance(...)` لحقل الهدف وعلم التعليق المختار.
3. احفظ المستند المحدث.

```java
public static void setFieldAppearance(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAppearance("First Name", AnnotationFlags.Hidden);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
