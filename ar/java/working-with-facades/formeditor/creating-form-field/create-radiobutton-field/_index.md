---
title: إنشاء حقل RadioButton
linktitle: إنشاء حقل RadioButton
type: docs
weight: 50
url: /ar/java/create-radiobutton-field/
description: تعلم كيفية إضافة حقل radio button إلى مستند PDF بلغة Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: إنشاء حقل radio button في PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وتكوين إعدادات تخطيط زر الراديو، وإنشاء حقل radio button، وحفظ المستند المعدل باستخدام واجهة FormEditor في Aspose.PDF for Java.
---
استخدم `FormEditorExamples.createRadioButtonField(...)` لإنشاء حقل زر اختيار مع خيارات محددة مسبقًا.

## إنشاء حقل radio button

1. اربط ملف PDF المصدر بـ واجهة `FormEditor`.
2. اضبط الفجوة بين أزرار الراديو، الاتجاه، وحجم العنصر.
3. عرّف عناصر زر الراديو.
4. أضف حقل زر الراديو مع الاختيار الافتراضي والمستطيل.
5. احفظ المستند المحدث.

```java
public static void createRadioButtonField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setRadioGap(4);
        editor.setRadioHoriz(false);
        editor.setRadioButtonItemSize(20);
        editor.setItems(new String[] {"Australia", "New Zealand", "Malaysia"});
        editor.addField(FieldType.Radio, "radiobutton1", "Malaysia", 1, 240, 498, 256, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
