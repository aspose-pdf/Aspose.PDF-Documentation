---
title: إضافة طوابع الصفحات إلى PDF في Java
linktitle: إضافة طوابع الصفحات
type: docs
weight: 30
url: /ar/java/page-stamps-in-the-pdf-file/
description: تعلم كيفية إضافة طوابع صفحات PDF كطبقات فوقية أو خلفيات في Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة طوابع مستندة إلى الصفحات إلى ملفات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية إضافة ختم صفحة إلى مستند PDF باستخدام Aspose.PDF for Java. يقوم المثال بتحميل صفحة PDF أخرى كختم، ويضبطها كخلفية، ويطبقها على الصفحة المستهدفة.
---
يمكن لـ Aspose.PDF for Java تطبيق صفحة من PDF آخر كختم أو إضافة تغطيات ترقيم الصفحات.

## إضافة ختم صفحة من PDF آخر

استخدم هذا المثال عندما يجب استخدام صفحة من PDF منفصل كختم خلفية.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfpagestamp/) من صفحة PDF الخارجية.
1. اضبط الطابع وأضفه إلى الصفحة المستهدفة، ثم احفظ النتيجة.

```java
public static void addPageStamp(Path inputFile, Path pageStampFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PdfPageStamp pageStamp = new PdfPageStamp(pageStampFile.toString(), 1);
        pageStamp.setBackground(true);
        document.getPages().get_Item(1).addStamp(pageStamp);
        document.save(outputFile.toString());
    }
}
```

## إضافة ختم رقم صفحة قياسي

استخدم هذا المثال عندما يجب أن تُظهر الصفحة المستهدفة الرقم الحالي مع تنسيق نص مخصص.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ واضبط a [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/).
1. أضف الطابع إلى الصفحة واحفظ المستند.

```java
public static void addPageNumStamp(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageNumberStamp pageNumberStamp = new PageNumberStamp();
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # of " + document.getPages().size());
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0f);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        pageNumberStamp.getTextState().setForegroundColor(Color.getBlueViolet());

        document.getPages().get_Item(1).addStamp(pageNumberStamp);
        document.save(outputFile.toString());
    }
}
```

## إضافة ختم رقم صفحة بالأرقام الرومانية

استخدم هذا المثال عندما يجب أن يبدأ ترقيم الصفحات من قيمة مخصصة ويستخدم الأرقام الرومانية الكبيرة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) وتهيئ ترقيم الأرقام الرومانية.
1. أضف العلامة إلى جميع الصفحات واحفظ ملف PDF..

```java
public static void addPageNumStampRoman(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageNumberStamp pageNumberStamp = new PageNumberStamp();
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(42);
        pageNumberStamp.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0f);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold);
        pageNumberStamp.getTextState().setForegroundColor(Color.getBlueViolet());

        for (Page page : document.getPages()) {
            page.addStamp(pageNumberStamp);
        }
        document.save(outputFile.toString());
    }
}
```
