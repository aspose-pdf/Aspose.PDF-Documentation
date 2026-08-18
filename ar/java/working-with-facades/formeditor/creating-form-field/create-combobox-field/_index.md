---
title: إنشاء حقل ComboBox
linktitle: إنشاء حقل ComboBox
type: docs
weight: 30
url: /java/create-combobox-field/
description: تعرف على كيفية إضافة حقل تحرير وسرد إلى مستند PDF في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: قم بإنشاء حقل مربع التحرير والسرد في ملف PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود وإضافة حقل تحرير وسرد وتعبئته بالعناصر وحفظ المستند المعدل باستخدام واجهة FormEditor في Aspose.PDF لـ Java.
---
استخدم `FormEditorExamples.createComboBoxField(...)` لإنشاء مربع تحرير وسرد وإضافة عناصر قابلة للتحديد.

## إنشاء حقل مربع التحرير والسرد

1. قم بربط ملف PDF المصدر بالواجهة `FormEditor`.
2. أضف حقل مربع التحرير والسرد بقيمته الافتراضية والمستطيل المستهدف.
3. أضف عناصر مربع التحرير والسرد القابلة للتحديد.
4. احفظ المستند المحدث.

```java
public static void createComboBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.ComboBox, "combobox1", "Australia", 1, 230, 498, 350, 514);
        editor.addListItem("combobox1", new String[] {"Australia", "Australia"});
        editor.addListItem("combobox1", new String[] {"New Zealand", "New Zealand"});
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
