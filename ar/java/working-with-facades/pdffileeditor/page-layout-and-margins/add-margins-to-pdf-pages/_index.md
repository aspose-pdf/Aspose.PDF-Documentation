---
title: إضافة هوامش إلى صفحات PDF
linktitle: إضافة هوامش إلى صفحات PDF
type: docs
weight: 10
url: /ar/java/add-margins-to-pdf-pages/
description: إضافة هوامش إلى صفحات PDF المحددة في Java باستخدام واجهة PdfFileEditor.
lastmod: "2026-10-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة هوامش إلى صفحات محددة في مستند PDF باستخدام Java
Abstract: تعرّف على كيفية إضافة هوامش إلى الصفحات المحددة باستخدام Aspose.PDF for Java. يستخدم مثال Java فئة PdfFileEditor لاستهداف أرقام الصفحات الفردية وتطبيق قيم هوامش متساوية من الأعلى والأسفل واليسار واليمين.
---
## إضافة هوامش إلى صفحات PDF

عينة Java تُضيف هوامش بقيمة 36 نقطة إلى الصفحتين 1 و 3 من المستند الأصلي.

### الخطوات

1. إنشاء `PdfFileEditor` مثال.
2. حدد أرقام الصفحات التي يجب أن تتلقى هوامش جديدة.
3. اتصال `addMargins` مع ملف الإدخال، ملف الإخراج، قائمة الصفحات، وقيم الهوامش.
4. احفظ ملف PDF المحدث.

### مثال Java

```java
public static void addMarginsToPdfPages(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addMargins(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 36, 36, 36, 36);
}
```
