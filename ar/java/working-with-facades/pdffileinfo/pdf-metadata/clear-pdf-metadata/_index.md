---
title: مسح بيانات تعريف PDF
linktitle: مسح بيانات تعريف PDF
type: docs
weight: 10
url: /java/clear-pdf-metadata/
description: تعرف على كيفية مسح بيانات تعريف PDF في Java باستخدام واجهة PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: مسح بيانات تعريف PDF باستخدام Aspose.PDF لـ Java
Abstract: تعرف على كيفية مسح بيانات تعريف PDF باستخدام Aspose.PDF لـ Java. يستخدم مثال Java PdfFileInfo لإزالة معلومات المستند المخزنة باستخدام `clearInfo()` ثم يحفظ ملف PDF الذي تم تنظيفه في ملف جديد.
---
## مسح البيانات التعريفية لملف PDF

استخدم سير العمل هذا عندما تحتاج إلى إزالة معلومات المستند المخزنة قبل مشاركة ملف PDF أو أرشفته.

### خطوات

1. قم بإنشاء كائن `PdfFileInfo` لمدخل PDF.
2. اتصل بـ `clearInfo()` لإزالة بيانات تعريف المستند.
3. احفظ النتيجة في ملف جديد باستخدام `save()`.
4. أغلق المثيل `PdfFileInfo`.

### مثال جافا

```java
public static void clearPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.clearInfo();
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
