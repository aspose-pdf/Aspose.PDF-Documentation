---
title: إنشاء حقل خانة الاختيار
linktitle: إنشاء حقل خانة الاختيار
type: docs
weight: 20
url: /java/create-checkbox-field/
description: تعرف على كيفية إضافة حقل نموذج خانة اختيار إلى مستند PDF في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: قم بإنشاء حقل خانة اختيار في ملف PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود وإضافة حقل خانة اختيار في موضع محدد وحفظ المستند المعدل باستخدام واجهة FormEditor في Aspose.PDF لـ Java.
---
استخدم `FormEditorExamples.createCheckBoxField(...)` لإضافة حقل خانة اختيار إلى نموذج PDF.

## قم بإنشاء حقل خانة الاختيار

1. قم بربط ملف PDF المصدر بالواجهة `FormEditor`.
2. أضف حقل خانة الاختيار باستخدام `FieldType.CheckBox` واسم الحقل والتسمية التوضيحية والصفحة والمستطيل.
3. احفظ المستند المحدث.

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
