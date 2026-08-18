---
title: إضافة رقم الصفحة إلى PDF
linktitle: إضافة رقم الصفحة إلى PDF
type: docs
weight: 30
url: /java/page-number/
description: تعرف على كيفية إضافة أرقام الصفحات إلى مستندات PDF في Java باستخدام واجهة PdfFileStamp.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة أرقام الصفحات إلى PDF في Java
Abstract: تعرف على كيفية إضافة أرقام الصفحات إلى مستندات PDF باستخدام Aspose.PDF لـ Java باستخدام واجهة PdfFileStamp. تغطي أمثلة Java الموضع الافتراضي، والإحداثيات الصريحة، والموضع المحاذي مع الهوامش، ومخرجات الترقيم الروماني برقم بداية مخصص.
---
## إضافة رقم الصفحة إلى PDF

استخدم `PdfFileStamp` عندما يجب تطبيق ترقيم الصفحات بعد إنشاء محتوى PDF بالفعل.

### خطوات

1. قم بإنشاء مثيل `PdfFileStamp` واربط ملف PDF المصدر.
2. اختر استراتيجية وضع رقم الصفحة التي تحتاجها.
3. اختياريًا، قم بتعيين نمط الترقيم ورقم البداية قبل الختم.
4. اتصل `addPageNumber` بالحمل الزائد المطلوب.
5. احفظ الإخراج وأغلق كائن الواجهة.

### أمثلة جافا

```java
public static void addPageNumbersDefault(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #");
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersAtCoordinates(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #", 300, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersWithPositionAndMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #", PdfFileStamp.POS_BOTTOM_RIGHT, 10, 10, 10, 10);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersWithRomanStyle(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);
        pdfStamper.setStartingNumber(42);
        pdfStamper.addPageNumber("Page #", PdfFileStamp.POS_UPPER_RIGHT);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
