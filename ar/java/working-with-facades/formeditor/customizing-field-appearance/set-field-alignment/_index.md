---
title: ضبط محاذاة الحقل
linktitle: ضبط محاذاة الحقل
type: docs
weight: 20
url: /java/set-field-alignment/
description: تعرف على كيفية ضبط محاذاة النص الأفقية لحقل نموذج PDF في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: ضبط محاذاة حقل نموذج PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وتعيين محاذاة الحقل الأفقي، وحفظ المستند المحدث باستخدام واجهة FormEditor في Aspose.PDF لـ Java.
---
## ضبط محاذاة الحقل الأفقي

1. قم بربط ملف PDF المصدر بالواجهة `FormEditor`.
2. اتصل `setFieldAlignment(...)` للحصول على الحقل الهدف وثابت المحاذاة المطلوب.
3. احفظ المستند المحدث.

```java
public static void setFieldAlignment(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAlignment("First Name", FormFieldFacade.ALIGN_CENTER);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
