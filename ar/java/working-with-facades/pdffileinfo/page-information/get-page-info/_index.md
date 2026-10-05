---
title: الحصول على معلومات الصفحة
linktitle: الحصول على معلومات الصفحة
type: docs
weight: 10
url: /ar/java/get-page-info/
description: تعلم كيفية فحص عرض الصفحة وارتفاعها ودورها في Java باستخدام واجهة PdfFileInfo.
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: الحصول على معلومات صفحة PDF باستخدام Aspose.PDF for Java
Abstract: تعلم كيفية استرجاع معلومات الصفحة باستخدام Aspose.PDF for Java. يستخدم المثال في Java فئة PdfFileInfo لقراءة عرض الصفحة وارتفاعها ودورها للصفحة 1 حتى تتمكن من فحص تخطيطها قبل المعالجة الإضافية.
---
## الحصول على معلومات الصفحة

يقرأ هذا المثال الخصائص الهندسية الأساسية للصفحة 1.

### خطوات

1. أنشئ كائن `PdfFileInfo` لملف PDF المصدر.
2. استدعِ `getPageWidth`, `getPageHeight`، و `getPageRotation` للصفحة التي تريد فحصها.
3. استخدم القيم المسترجعة أو اطبعها.
4. أغلق `PdfFileInfo` مثال.

### مثال Java

```java
public static void getPageInformation(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page Width: " + pdfInfo.getPageWidth(1));
    System.out.println("Page Height: " + pdfInfo.getPageHeight(1));
    System.out.println("Page Rotation: " + pdfInfo.getPageRotation(1));
    pdfInfo.close();
}
```
