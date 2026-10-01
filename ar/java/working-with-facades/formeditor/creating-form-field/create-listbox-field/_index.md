---
title: إنشاء حقل ListBox
linktitle: إنشاء حقل ListBox
type: docs
weight: 40
url: /ar/java/create-listbox-field/
description: تعرّف على كيفية إضافة حقل ListBox إلى مستند PDF باستخدام Java وواجهة FormEditor في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: إنشاء حقل ListBox في ملف PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية ربط PDF موجود، تعريف عناصر القائمة، إضافة حقل ListBox، وحفظ المستند المعدل باستخدام واجهة FormEditor في Aspose.PDF for Java.
---
استخدام `FormEditorExamples.createListBoxField(...)` لإنشاء صندوق قائمة بعناصر محددة مسبقًا.

## إنشاء حقل ListBox

1. ربط ملف PDF المصدر بال `FormEditor` واجهة.
2. حدد عناصر القائمة المتاحة باستخدام `setItems(...)`.
3. إضافة حقل صندوق القائمة مع قيمته الافتراضية والمستطيل.
4. حفظ المستند المحدث.

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
