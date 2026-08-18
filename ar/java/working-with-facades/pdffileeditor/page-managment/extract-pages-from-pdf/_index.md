---
title: استخراج الصفحات من PDF
linktitle: استخراج الصفحات من PDF
type: docs
weight: 30
url: /java/extract-pages-from-pdf/
description: قم باستخراج الصفحات المحددة من ملف PDF في Java باستخدام واجهة PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم باستخراج صفحات PDF المحددة إلى مستند جديد باستخدام Java
Abstract: تعرف على كيفية استخراج الصفحات من ملف PDF باستخدام Aspose.PDF لـ Java. يستخدم مثال Java PdfFileEditor لجمع أرقام صفحات محددة وكتابتها في ملف PDF منفصل.
---
## استخراج الصفحات من ملف PDF

يقوم نموذج Java باستخراج الصفحات 1 و4 و3 في مستند PDF جديد.

### خطوات

1. قم بإنشاء مثيل `PdfFileEditor`.
2. تحديد أرقام الصفحات المراد استخراجها.
3. اتصل `extract` بالملف المصدر، ومصفوفة الصفحات، وملف الإخراج.
4. احفظ الصفحات المستخرجة كملف PDF جديد.

### مثال جافا

```java
public static void extractPagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.extract(inputFile.toString(), new int[] {1, 4, 3}, outputFile.toString());
}
```
