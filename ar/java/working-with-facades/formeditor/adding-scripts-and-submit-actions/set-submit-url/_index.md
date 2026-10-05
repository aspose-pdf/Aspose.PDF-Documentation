---
title: تعيين عنوان URL للإرسال
linktitle: تعيين عنوان URL للإرسال
type: docs
weight: 30
url: /ar/java/set-submit-url/
description: تعرف على كيفية تعيين عنوان URL للإرسال لزر نموذج PDF في Java باستخدام واجهة `FormEditor` في Aspose.PDF.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: تكوين عنوان URL للإرسال لنموذج PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وتعيين عنوان URL للإرسال وعلم الإرسال لحقل الزر، وحفظ المستند المحدث باستخدام واجهة `FormEditor` في Aspose.PDF for Java.
---
## تعيين عنوان URL للإرسال

1. اربط ملف PDF المصدر بـ واجهة `FormEditor`.
2. استدعِ `setSubmitUrl(...)` لحقل الزر.
3. طبّق علم الإرسال لتنسيق الإرسال.
4. احفظ المستند المحدث.

```java
public static void setSubmitUrl(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
        editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
