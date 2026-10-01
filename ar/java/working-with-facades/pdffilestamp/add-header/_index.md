---
title: إضافة رأس إلى PDF
linktitle: إضافة رأس إلى PDF
type: docs
weight: 20
url: /ar/java/add-header/
description: تعرف على كيفية إضافة رؤوس نصية ورؤوس صورة إلى صفحات PDF في Java باستخدام واجهة PdfFileStamp.
lastmod: "2026-10-01"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة رؤوس نصية وصور إلى PDF في Java
Abstract: تعرف على كيفية إضافة محتوى رأس إلى مستندات PDF باستخدام Aspose.PDF for Java مع واجهة PdfFileStamp. تغطي أمثلة Java رؤوس نصية عادية، ورؤوس صور تم تحميلها من تدفق، ورؤوس منسقة ذات قيم هوامش صريحة.
---
## إضافة رأس إلى PDF

استخدام `PdfFileStamp` عندما تحتاج إلى تكرار محتوى الرأس في كل صفحة.

### خطوات

1. إنشاء `PdfFileStamp` مثيل وربط ملف PDF المصدر.
2. بناء محتوى الرأس كـ `FormattedText` أو تحميله من تدفق صورة.
3. اتصل بالملائم `addHeader` تحميل زائد.
4. حفظ الناتج وإغلاق كائن الواجهة.

### أمثلة Java

```java
public static void addTextHeader(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("Sample Header");
        pdfStamper.addHeader(text, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addImageHeader(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addHeader(imageStream, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addHeaderWithMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText(
                "Sample Header",
                Color.BLUE,
                FontStyle.Helvetica,
                EncodingType.Winansi,
                true,
                12.0f);
        pdfStamper.addHeader(text, 20, 20, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
