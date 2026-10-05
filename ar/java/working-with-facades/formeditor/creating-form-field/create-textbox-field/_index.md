---
title: إنشاء حقل TextBox
linktitle: إنشاء حقل TextBox
type: docs
weight: 10
url: /ar/java/create-textbox-field/
description: تعرف على كيفية إضافة حقول TextBox إلى مستند PDF باستخدام Java من خلال واجهة FormEditor في Aspose.PDF.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: إنشاء حقول نموذج نصية في PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وإضافة حقول نصية بقيم افتراضية، وحفظ المستند المعدل باستخدام واجهة FormEditor في Aspose.PDF for Java.
---
استخدم `FormEditorExamples.createTextBoxField(...)` لإضافة حقول نصية إلى نموذج PDF.

## إنشاء حقول TextBox

1. اربط ملف PDF المصدر إلى واجهة `FormEditor`.
2. أضف كل حقل نص مع `FieldType.Text`، اسم الحقل، القيمة الافتراضية، رقم الصفحة، والمستطيل.
3. احفظ المستند المحدث.

```java
public static void createTextBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.Text, "first_name", "Alexander", 1, 50, 570, 150, 590);
        editor.addField(FieldType.Text, "last_name", "Smith", 1, 235, 570, 330, 590);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
