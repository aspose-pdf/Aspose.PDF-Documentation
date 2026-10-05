---
title: إدراج صفحات في PDF
linktitle: إدراج صفحات في PDF
type: docs
weight: 40
url: /ar/java/insert-pages-into-pdf/
description: إدراج الصفحات المحددة من PDF واحد إلى آخر في Java باستخدام واجهة PdfFileEditor.
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إدراج صفحات من PDF آخر في موضع مختار باستخدام Java
Abstract: تعرف على كيفية إدراج صفحات في PDF باستخدام Aspose.PDF for Java. يستخدم مثال Java أداة PdfFileEditor لإدراج الصفحات المحددة من مستند ثانٍ بعد رقم صفحة معين في PDF المستهدف.
---
## إدراج صفحات في PDF

يقوم مثال Java بإدراج الصفحات 1 و 2 من المستند الثانوي بعد الصفحة 2 من PDF المستهدف.

### خطوات

1. أنشئ مثيلًا من `PdfFileEditor`.
2. اختر نقطة الإدراج في المستند الهدف.
3. حدّد أرقام الصفحات لنسخها من المستند المصدر.
4. استدعِ `insert` مع ملف الهدف، نقطة الإدراج، ملف المصدر، مصفوفة الصفحات، وملف الإخراج.
5. احفظ ملف PDF المحدّث.

### مثال Java

```java
public static void insertPagesIntoPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.insert(inputFile.toString(), 2, sampleFile.toString(), new int[] {1, 2}, outputFile.toString());
}
```
