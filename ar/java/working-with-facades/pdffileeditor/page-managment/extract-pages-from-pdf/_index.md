---
title: استخراج الصفحات من PDF
linktitle: استخراج الصفحات من PDF
type: docs
weight: 30
url: /ar/java/extract-pages-from-pdf/
description: استخراج الصفحات المحددة من ملف PDF في Java باستخدام واجهة PdfFileEditor.
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخراج صفحات PDF المحددة إلى مستند جديد باستخدام Java
Abstract: تعلم كيفية استخراج الصفحات من ملف PDF باستخدام Aspose.PDF for Java. يستخدم المثال بلغة Java أداة PdfFileEditor لجمع أرقام صفحات معينة وكتابتها في ملف PDF ناتج منفصل.
---
## استخراج الصفحات من PDF

العينة بلغة Java تستخرج الصفحات 1 و 4 و 3 إلى مستند PDF جديد.

### خطوات

1. أنشئ مثيلًا `PdfFileEditor`.
2. حدّد أرقام الصفحات المراد استخراجها.
3. استدعِ `extract` مع ملف المصدر، ومصفوفة الصفحات، وملف الإخراج.
4. احفظ الصفحات المستخرجة كملف PDF جديد.

### مثال Java

```java
public static void extractPagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.extract(inputFile.toString(), new int[] {1, 4, 3}, outputFile.toString());
}
```
