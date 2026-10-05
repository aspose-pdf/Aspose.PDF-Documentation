---
title: إضافة أرقام الصفحات إلى PDF باستخدام Java
linktitle: إضافة رقم الصفحة
type: docs
weight: 30
url: /ar/java/add-page-number/
description: تعرف على كيفية إضافة طوابع رقم الصفحة إلى مستندات PDF باستخدام Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة طوابع رقم الصفحة إلى ملفات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية إضافة طوابع رقم الصفحة باستخدام Aspose.PDF for Java. وتغطي ترقيم الصفحات القياسي مع تخصيص نمط الخط وترقيم الأرقام الرومانية مع رقم بدء قابل للتكوين.
---
## إضافة طابع رقم الصفحة

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/).
1. اضبط خيارات وضع الختم المطلوبة وخيارات الترقيم.
1. عيّن خيارات تنسيق النص المطلوبة، بما في ذلك [FontRepository](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/) و [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. أضف المُكوَّن المُعد [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) إلى الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. احفظ ملف PDF المحدث [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
