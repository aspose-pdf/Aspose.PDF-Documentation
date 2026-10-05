---
title: تزيين الحقل
linktitle: تزيين الحقل
type: docs
weight: 10
url: /ar/java/decorate-field/
description: تعلم كيفية تزيين حقل نموذج PDF بالألوان والمحاذاة في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: تزيين حقل نموذج PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، تكوين FormFieldFacade بألوان ومحاذاة، تزيين حقل، وحفظ المستند المحدّث باستخدام واجهة FormEditor في Aspose.PDF for Java.
---
## تزيين حقل

1. اربط ملف PDF المصدر بـ واجهة `FormEditor`.
2. اضبط `FormFieldFacade` مع الألوان المطلوبة والمحاذاة.
3. مرّر الواجهة إلى المحرر واستدعِ `decorateField(...)`.
4. احفظ المستند المحدث.

```java
public static void decorateField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        FormFieldFacade facade = new FormFieldFacade();
        facade.setBackgroundColor(Color.RED);
        facade.setTextColor(Color.BLUE);
        facade.setBorderColor(Color.GREEN);
        facade.setAlignment(FormFieldFacade.ALIGN_CENTER);
        editor.setFacade(facade);
        editor.decorateField("First Name");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
