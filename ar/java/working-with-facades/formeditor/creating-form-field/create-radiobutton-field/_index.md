---
title: إنشاء حقل زر الراديو
linktitle: إنشاء حقل زر الراديو
type: docs
weight: 50
url: /java/create-radiobutton-field/
description: تعرف على كيفية إضافة حقل زر اختيار إلى مستند PDF في Java باستخدام واجهة FormEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: قم بإنشاء حقل زر اختيار في ملف PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF موجود، وتكوين إعدادات تخطيط زر الاختيار، وإنشاء حقل زر اختيار، وحفظ المستند المعدل باستخدام واجهة FormEditor في Aspose.PDF لـ Java.
---
استخدم `FormEditorExamples.createRadioButtonField(...)` لإنشاء حقل زر اختيار بخيارات محددة مسبقًا.

## قم بإنشاء حقل زر الاختيار

1. قم بربط ملف PDF المصدر بالواجهة `FormEditor`.
2. قم بتكوين فجوة زر الاختيار والاتجاه وحجم العنصر.
3. تحديد عناصر زر الاختيار.
4. أضف حقل زر الاختيار مع التحديد الافتراضي والمستطيل.
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
