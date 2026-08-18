---
title: إضافة تذييل إلى PDF
linktitle: إضافة تذييل إلى PDF
type: docs
weight: 10
url: /java/add-footer/
description: تعرف على كيفية إضافة تذييلات نصية وصورية إلى صفحات PDF في Java باستخدام واجهة PdfFileStamp.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أضف تذييلات نصية وصورية إلى PDF في Java
Abstract: تعرف على كيفية إضافة محتوى تذييل إلى مستندات PDF باستخدام Aspose.PDF لـ Java باستخدام واجهة PdfFileStamp. تغطي أمثلة Java تذييلات النص العادي، وتذييلات الصور المحملة من الدفق، وتذييلات النص ذات الهوامش اليسرى واليمنى والسفلية الصريحة.
---
## إضافة تذييل إلى PDF

استخدم `PdfFileStamp` عندما تحتاج إلى محتوى تذييل متكرر في كل صفحة من المستند.

### خطوات

1. قم بإنشاء مثيل `PdfFileStamp` واربط ملف PDF المصدر.
2. أنشئ محتوى التذييل كـ `FormattedText` أو دفق صور.
3. اتصل بالحمل الزائد `addFooter` المناسب.
4. احفظ الملف المحدث وأغلق كائن الواجهة.

### أمثلة جافا

```java
public static void addTextFooter(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("Sample Footer");
        pdfStamper.addFooter(text, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addImageFooter(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addFooter(imageStream, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addFooterWithMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("This footer has margins on all sides.");
        pdfStamper.addFooter(text, 20, 20, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
