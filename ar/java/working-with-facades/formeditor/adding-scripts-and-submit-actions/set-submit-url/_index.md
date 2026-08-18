---
title: قم بتعيين عنوان URL للإرسال
linktitle: قم بتعيين عنوان URL للإرسال
type: docs
weight: 30
url: /java/set-submit-url/
description: تعرف على كيفية تعيين عنوان URL للإرسال لزر نموذج PDF في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: قم بتكوين نموذج PDF لإرسال عنوان URL في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وتعيين عنوان URL للإرسال وعلامة الإرسال لحقل الزر، وحفظ المستند المحدث باستخدام واجهة FormEditor في Aspose.PDF لـ Java.
---
## قم بتعيين عنوان URL للإرسال

1. قم بربط ملف PDF المصدر بالواجهة `FormEditor`.
2. اتصل `setSubmitUrl(...)` للحصول على حقل الزر.
3. قم بتطبيق علامة الإرسال على تنسيق الإرسال.
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
