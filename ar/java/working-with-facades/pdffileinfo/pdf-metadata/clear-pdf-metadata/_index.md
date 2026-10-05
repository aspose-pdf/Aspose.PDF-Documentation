---
title: مسح بيانات تعريف PDF
linktitle: مسح بيانات تعريف PDF
type: docs
weight: 10
url: /ar/java/clear-pdf-metadata/
description: تعلم كيفية مسح بيانات تعريف PDF في Java باستخدام واجهة PdfFileInfo.
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: مسح بيانات تعريف PDF باستخدام Aspose.PDF for Java
Abstract: تعلم كيفية مسح بيانات تعريف PDF باستخدام Aspose.PDF for Java. يستخدم مثال Java فئة PdfFileInfo لإزالة معلومات المستند المخزنة باستخدام `clearInfo()` ثم يحفظ ملف PDF المنقى إلى ملف جديد.
---
## مسح بيانات تعريف PDF

استخدم سير العمل هذا عندما تحتاج إلى إزالة معلومات المستند المخزنة قبل مشاركة أو أرشفة ملف PDF.

### خطوات

1. أنشئ كائن `PdfFileInfo` للملف PDF المدخل.
2. استدعِ `clearInfo()` لإزالة البيانات التعريفية للمستند.
3. احفظ النتيجة في ملف جديد مع `save()`.
4. أغلق `PdfFileInfo` مثال.

### مثال Java

```java
public static void clearPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.clearInfo();
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
