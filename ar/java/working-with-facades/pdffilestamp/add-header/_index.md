---
title: إضافة رأس إلى PDF
linktitle: إضافة رأس إلى PDF
type: docs
weight: 20
url: /java/add-header/
description: تعرف على كيفية إضافة رؤوس النصوص والصور إلى صفحات PDF في Java باستخدام واجهة PdfFileStamp.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أضف رؤوس النص والصور إلى PDF في Java
Abstract: تعرف على كيفية إضافة محتوى رأس إلى مستندات PDF باستخدام Aspose.PDF لـ Java باستخدام واجهة PdfFileStamp. تغطي أمثلة Java رؤوس النص العادي، ورؤوس الصور المحملة من دفق، والرؤوس المصممة بقيم هامش واضحة.
---
## إضافة رأس إلى PDF

استخدم `PdfFileStamp` عندما تحتاج إلى محتوى رأس متكرر في كل صفحة.

### خطوات

1. قم بإنشاء مثيل `PdfFileStamp` واربط ملف PDF المصدر.
2. أنشئ محتوى الرأس كـ `FormattedText` أو قم بتحميله من دفق الصور.
3. اتصل بالحمل الزائد `addHeader` المناسب.
4. احفظ الإخراج وأغلق كائن الواجهة.

### أمثلة جافا

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
