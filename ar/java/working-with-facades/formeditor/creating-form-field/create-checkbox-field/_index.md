---
title: إنشاء حقل CheckBox
linktitle: إنشاء حقل CheckBox
type: docs
weight: 20
url: /ar/java/create-checkbox-field/
description: تعرف على كيفية إضافة حقل نموذج مربع اختيار إلى مستند PDF باستخدام Java عبر واجهة FormEditor في Aspose.PDF.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: إنشاء حقل مربع اختيار في ملف PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وإضافة حقل مربع اختيار في موضع محدد، وحفظ المستند المعدل باستخدام واجهة FormEditor في Aspose.PDF for Java.
---
استخدام `FormEditorExamples.createCheckBoxField(...)` لإضافة حقل خانة اختيار إلى نموذج PDF.

## إنشاء حقل مربع اختيار

1. اربط ملف PDF المصدر إلى واجهة `FormEditor`.
2. أضف حقل مربع الاختيار مع `FieldType.CheckBox`، اسم الحقل، التسمية، الصفحة، والمستطيل.
3. احفظ المستند المُحدَّث.

```java
public static void createCheckBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.CheckBox, "checkbox1", "Check Box 1", 1, 240, 498, 256, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
