---
title: إضافة أرقام الصفحات إلى PDF في Java
linktitle: إضافة رقم الصفحة
type: docs
weight: 30
url: /java/add-page-number/
description: تعرف على كيفية إضافة طوابع أرقام الصفحات إلى مستندات PDF في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أضف طوابع أرقام الصفحات إلى ملفات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية إضافة طوابع أرقام الصفحات باستخدام Aspose.PDF لـ Java. ويغطي ترقيم الصفحات القياسي مع تصميم خط مخصص وترقيم الأرقام الرومانية برقم بداية قابل للتكوين.
---
## إضافة ختم رقم الصفحة

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء كائن [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/).
1. قم بتكوين موضع الطوابع المطلوبة وخيارات الترقيم.
1. قم بتعيين خيارات تنسيق النص المطلوبة، بما في ذلك [FontRepository](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/) و[اللون](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. أضف [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) الذي تم تكوينه إلى [الصفحة] المستهدفة(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. احفظ ملف PDF المحدث [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
