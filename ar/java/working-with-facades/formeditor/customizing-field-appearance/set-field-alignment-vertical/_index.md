---
title: تعيين محاذاة الحقل عموديًا
linktitle: تعيين محاذاة الحقل عموديًا
type: docs
weight: 30
url: /ar/java/set-field-alignment-vertical/
description: تعرّف على كيفية ضبط المحاذاة العمودية لحقل نموذج PDF في Java باستخدام الواجهة FormEditor في Aspose.PDF.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: ضبط المحاذاة العمودية لحقل نموذج PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وضبط المحاذاة العمودية للحقل، وحفظ المستند المحدث باستخدام الواجهة FormEditor في Aspose.PDF for Java.
---
## ضبط المحاذاة العمودية للحقل

1. اربط ملف PDF المصدر بـ واجهة `FormEditor`.
2. استدعِ `setFieldAlignmentV(...)` للحقل الهدف وثابت المحاذاة العمودية المطلوب.
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
