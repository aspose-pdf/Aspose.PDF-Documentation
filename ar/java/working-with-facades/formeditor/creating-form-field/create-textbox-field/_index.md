---
title: إنشاء حقل مربع نص
linktitle: إنشاء حقل مربع نص
type: docs
weight: 10
url: /java/create-textbox-field/
description: تعرف على كيفية إضافة حقول مربع النص إلى مستند PDF في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: قم بإنشاء حقول نموذج نصية في ملف PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود وإضافة حقول نصية بقيم افتراضية وحفظ المستند المعدل باستخدام واجهة FormEditor في Aspose.PDF لـ Java.
---
استخدم `FormEditorExamples.createTextBoxField(...)` لإضافة حقول نصية إلى نموذج PDF.

## إنشاء حقول مربع النص

1. قم بربط ملف PDF المصدر بالواجهة `FormEditor`.
2. أضف كل حقل نصي باستخدام `FieldType.Text` واسم الحقل والقيمة الافتراضية ورقم الصفحة والمستطيل.
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
