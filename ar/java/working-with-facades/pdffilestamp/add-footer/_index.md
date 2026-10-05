---
title: إضافة تذييل إلى PDF
linktitle: إضافة تذييل إلى PDF
type: docs
weight: 10
url: /ar/java/add-footer/
description: تعرف على كيفية إضافة تذييلات نصية وصور إلى صفحات PDF في Java باستخدام واجهة PdfFileStamp.
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة تذييلات نصية وصور إلى PDF في Java
Abstract: تعرف على كيفية إضافة محتوى التذييل إلى مستندات PDF باستخدام Aspose.PDF for Java عبر واجهة PdfFileStamp. تغطي أمثلة Java تذييلات نصية عادية، وتذييلات صور محملة من تدفق، وتذييلات نصية مع هوامش صريحة اليسار، اليمن، والأسفل.
---
## إضافة تذييل إلى PDF

استخدم `PdfFileStamp` عندما تحتاج إلى محتوى تذييل مكرر في كل صفحة من المستند.

### خطوات

1. أنشئ `PdfFileStamp` إنشاء نسخة وربط ملف PDF المصدر.
2. أنشئ محتوى التذييل كإحدى `FormattedText` أو تدفق صورة.
3. استدعِ بالملائم `addFooter` تحميل زائد.
4. احفظ الملف المحدث وأغلق كائن الواجهة.

### أمثلة Java

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
