---
title: حذف الصفحات من PDF
linktitle: حذف الصفحات من PDF
type: docs
weight: 20
url: /ar/java/delete-pages-from-pdf/
description: حذف الصفحات المحددة من PDF في Java باستخدام واجهة PdfFileEditor.
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إزالة صفحات محددة من مستند PDF باستخدام Java
Abstract: تعلم كيفية حذف الصفحات من PDF باستخدام Aspose.PDF for Java. يستخدم المثال على Java أداة PdfFileEditor لإزالة مجموعة محددة من أرقام الصفحات وحفظ الصفحات المتبقية كمستند جديد.
---
## حذف الصفحات من PDF

العينة على Java تزيل الصفحات 2 و 4 من المستند الأصلي.

### خطوات

1. أنشئ مثيلًا من `PdfFileEditor`.
2. ابنِ مصفوفة بأرقام الصفحات التي تريد إزالتها.
3. استدعِ `delete` مع ملف الإدخال ومصفوفة الصفحات وملف الإخراج.
4. احفظ ملف PDF الناتج.

### مثال Java

```java
public static void deletePagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.delete(inputFile.toString(), new int[] {2, 4}, outputFile.toString());
}
```
