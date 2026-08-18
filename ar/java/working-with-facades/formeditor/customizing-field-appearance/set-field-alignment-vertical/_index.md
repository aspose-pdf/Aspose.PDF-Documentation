---
title: ضبط محاذاة الحقل عموديًا
linktitle: ضبط محاذاة الحقل عموديًا
type: docs
weight: 30
url: /java/set-field-alignment-vertical/
description: تعرف على كيفية تعيين المحاذاة الرأسية لحقل نموذج PDF في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: قم بتعيين المحاذاة الرأسية لحقل نموذج PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وتعيين محاذاة الحقل العمودي، وحفظ المستند المحدث باستخدام واجهة FormEditor في Aspose.PDF لـ Java.
---
## ضبط محاذاة المجال الرأسي

1. قم بربط ملف PDF المصدر بالواجهة `FormEditor`.
2. اتصل بـ`setFieldAlignmentV(...)` للحصول على الحقل الهدف وثابت المحاذاة الرأسية المطلوب.
3. احفظ المستند المحدث.

```java
public static void setFieldAlignmentVertical(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAlignmentV("First Name", FormFieldFacade.ALIGN_BOTTOM);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
