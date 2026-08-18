---
title: إنشاء حقل ListBox
linktitle: إنشاء حقل ListBox
type: docs
weight: 40
url: /java/create-listbox-field/
description: تعرف على كيفية إضافة حقل مربع قائمة إلى مستند PDF في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: قم بإنشاء حقل مربع قائمة في ملف PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وتحديد عناصر القائمة، وإضافة حقل مربع قائمة، وحفظ المستند المعدل باستخدام واجهة FormEditor في Aspose.PDF لـ Java.
---
استخدم `FormEditorExamples.createListBoxField(...)` لإنشاء مربع قائمة يحتوي على عناصر محددة مسبقًا.

## إنشاء حقل مربع قائمة

1. قم بربط ملف PDF المصدر بالواجهة `FormEditor`.
2. حدد عناصر القائمة المتوفرة باستخدام `setItems(...)`.
3. أضف حقل مربع القائمة بقيمته الافتراضية ومستطيله.
4. احفظ المستند المحدث.

```java
public static void createListBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setItems(new String[] {"Australia", "New Zealand", "Malaysia"});
        editor.addField(FieldType.ListBox, "listbox1", "Australia", 1, 230, 398, 350, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
