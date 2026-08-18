---
title: إنشاء زر إرسال
linktitle: إنشاء زر إرسال
type: docs
weight: 60
url: /java/create-submit-button/
description: تعرف على كيفية إضافة زر إرسال إلى مستند PDF في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: قم بإنشاء زر إرسال PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وإضافة حقل زر إرسال بعنوان URL مستهدف، وحفظ المستند المعدل باستخدام واجهة FormEditor في Aspose.PDF لـ Java.
---
استخدم `FormEditorExamples.createSubmitButton(...)` لإنشاء زر يرسل بيانات النموذج.

## إنشاء زر إرسال

1. قم بربط ملف PDF المصدر بالواجهة `FormEditor`.
2. اتصل بـ `addSubmitBtn(...)` باستخدام اسم الزر والصفحة والتسمية وعنوان URL المستهدف والمستطيل.
3. احفظ المستند المحدث.

```java
public static void createSubmitButton(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addSubmitBtn("submitbutton", 1, "Submit", "http://localhost/testing/show", 100, 450, 150, 475);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
