---
title: تزيين الميدان
linktitle: تزيين الميدان
type: docs
weight: 10
url: /java/decorate-field/
description: تعرف على كيفية تزيين حقل نموذج PDF بالألوان والمحاذاة في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: تزيين حقل نموذج PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وتكوين FormFieldFacade بالألوان والمحاذاة، وتزيين حقل، وحفظ المستند المحدث باستخدام واجهة FormEditor في Aspose.PDF لـ Java.
---
## تزيين الحقل

1. قم بربط ملف PDF المصدر بالواجهة `FormEditor`.
2. قم بتكوين `FormFieldFacade` بالألوان والمحاذاة المطلوبة.
3. قم بتمرير الواجهة إلى المحرر واتصل بـ `decorateField(...)`.
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
