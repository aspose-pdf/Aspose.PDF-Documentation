---
title: تعيين محاذاة الحقل
linktitle: تعيين محاذاة الحقل
type: docs
weight: 20
url: /ar/java/set-field-alignment/
description: تعرف على كيفية تعيين محاذاة النص الأفقية لحقل نموذج PDF في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: تعيين محاذاة حقل نموذج PDF في Java
Abstract: تو�ضح هذه المقالة كيفية ربط ملف PDF موجود، وتعيين محاذاة الحقل الأفقية، وحفظ المستند المحدث باستخدام واجهة FormEditor في Aspose.PDF for Java.
---
## تعيين محاذاة الحقل الأفقية

1. اربط ملف PDF المصدر إلى واجهة `FormEditor`.
2. استدعِ `setFieldAlignment(...)` للحقل الهدف وثابت المحاذاة المطلوب.
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
