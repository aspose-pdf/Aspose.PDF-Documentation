---
title: إنشاء زر إرسال
linktitle: إنشاء زر إرسال
type: docs
weight: 60
url: /ar/java/create-submit-button/
description: تعرف على كيفية إضافة زر إرسال إلى مستند PDF في Java باستخدام الواجهة FormEditor في Aspose.PDF.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: إنشاء زر إرسال PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وإضافة حقل زر إرسال مع عنوان URL المستهدف، وحفظ المستند المعدل باستخدام الواجهة FormEditor في Aspose.PDF for Java.
---
استخدم `FormEditorExamples.createSubmitButton(...)` لإنشاء زر يرسل بيانات النموذج.

## إنشاء زر إرسال

1. اربط ملف PDF المصدر بـ واجهة `FormEditor`.
2. استدعِ `addSubmitBtn(...)` مع اسم الزر، الصفحة، التسمية، عنوان URL المستهدف، والمستطيل.
3. احفظ المستند المُحدّث.

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
