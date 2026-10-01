---
title: إنشاء حقل ComboBox
linktitle: إنشاء حقل ComboBox
type: docs
weight: 30
url: /ar/java/create-combobox-field/
description: تعلم كيفية إضافة حقل صندوق اختيار إلى مستند PDF بلغة Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: إنشاء حقل صندوق اختيار في ملف PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وإضافة حقل صندوق اختيار، وتعبئته بالعناصر، وحفظ المستند المعدل باستخدام واجهة FormEditor في Aspose.PDF for Java.
---
استخدام `FormEditorExamples.createComboBoxField(...)` لإنشاء مربع اختيار وإضافة عناصر قابلة للتحديد.

## إنشاء حقل صندوق اختيار

1. ربط ملف PDF المصدر إلى `FormEditor` واجهة.
2. إضافة حقل مربع السرد مع القيمة الافتراضية والمستطيل الهدف.
3. إضافة العناصر القابلة للتحديد لمربع السرد.
4. حفظ المستند المحدث.

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
