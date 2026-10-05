---
title: الحصول على إصدار PDF
linktitle: الحصول على إصدار PDF
type: docs
weight: 20
url: /ar/java/get-pdf-version/
description: تعلم كيفية استرجاع إصدار مستند PDF في Java باستخدام واجهة PdfFileInfo.
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استرجاع إصدار PDF باستخدام Aspose.PDF for Java
Abstract: تعلم كيفية استرجاع إصدار PDF باستخدام Aspose.PDF for Java. ينشئ المثال في Java كائن PdfFileInfo، يقرأ سلسلة الإصدار باستخدام `getPdfVersion()`، يطبع النتيجة، ويغلق كائن معلومات الملف.
---
## الحصول على إصدار PDF

استخدم سير العمل هذا عندما تحتاج إلى التحقق من توافق الملف أو توجيه المستند عبر منطق معالجة محدد بالإصدار.

### الخطوات

1. أنشئ كائن `PdfFileInfo` لملف PDF..
2. استدعِ `getPdfVersion()` لاسترجاع النسخة المبلغ عنها.
3. استخدم أو طباعة قيمة الإصدار.
4. أغلق `PdfFileInfo` مثال.

### مثال Java

```java
public static void getPdfVersion(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println();
    System.out.println("PDF Version: " + pdfInfo.getPdfVersion());
    pdfInfo.close();
}
```
