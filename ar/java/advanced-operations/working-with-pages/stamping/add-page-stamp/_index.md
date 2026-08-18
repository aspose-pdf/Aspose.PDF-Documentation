---
title: إضافة طوابع الصفحة إلى PDF في جافا
linktitle: إضافة طوابع الصفحة
type: docs
weight: 30
url: /java/page-stamps-in-the-pdf-file/
description: تعرف على كيفية إضافة طوابع صفحة PDF كتراكبات أو خلفيات في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أضف طوابع مستندة إلى الصفحة إلى ملفات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية إضافة طابع صفحة إلى مستند PDF باستخدام Aspose.PDF لـ Java. يقوم المثال بتحميل صفحة PDF أخرى كختم، وتكوينها كخلفية، وتطبيقها على الصفحة المستهدفة.
---
يمكن لـ Aspose.PDF لـ Java تطبيق صفحة من ملف PDF آخر كختم أو إضافة تراكبات ترقيم الصفحات.

## أضف طابع صفحة من ملف PDF آخر

استخدم هذا المثال عندما يجب استخدام صفحة من ملف PDF منفصل كختم خلفية.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfpagestamp/) من صفحة PDF الخارجية.
1. قم بتكوين الختم وإضافته إلى الصفحة المستهدفة، ثم احفظ النتيجة.

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

## أضف ختم رقم الصفحة القياسي

استخدم هذا المثال عندما يجب أن تعرض الصفحة المستهدفة الرقم الحالي بتنسيق نص مخصص.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء وتكوين [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/).
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

## أضف ختم رقم الصفحة بالأرقام الرومانية

استخدم هذا المثال عندما يجب أن يبدأ ترقيم الصفحات من قيمة مخصصة واستخدام الأرقام الرومانية الكبيرة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) وقم بتكوين ترقيم الأرقام الرومانية.
1. أضف الختم إلى جميع الصفحات واحفظ ملف PDF.

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
