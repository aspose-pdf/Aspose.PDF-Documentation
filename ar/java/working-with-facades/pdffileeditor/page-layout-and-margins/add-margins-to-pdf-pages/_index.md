---
title: إضافة هوامش إلى صفحات PDF
linktitle: إضافة هوامش إلى صفحات PDF
type: docs
weight: 10
url: /java/add-margins-to-pdf-pages/
description: أضف هوامش إلى صفحات PDF محددة في Java باستخدام واجهة PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أضف هوامش إلى صفحات محددة في مستند PDF باستخدام Java
Abstract: تعرف على كيفية إضافة هوامش إلى الصفحات المحددة باستخدام Aspose.PDF لـ Java. يستخدم مثال Java PdfFileEditor لاستهداف أرقام الصفحات الفردية وتطبيق قيم متساوية للهامش العلوي والسفلي واليسار والأيمن.
---
## إضافة هوامش إلى صفحات PDF

تضيف عينة Java هوامش مكونة من 36 نقطة إلى الصفحتين 1 و3 من المستند المصدر.

### خطوات

1. قم بإنشاء مثيل `PdfFileEditor`.
2. حدد أرقام الصفحات التي يجب أن تتلقى هوامش جديدة.
3. اتصل `addMargins` باستخدام ملف الإدخال وملف الإخراج وقائمة الصفحات وقيم الهامش.
4. احفظ ملف PDF المحدث.

### مثال جافا

```java
public static void addMarginsToPdfPages(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addMargins(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 36, 36, 36, 36);
}
```
