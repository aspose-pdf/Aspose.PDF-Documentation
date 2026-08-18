---
title: الحصول على إزاحة الصفحة
linktitle: الحصول على إزاحة الصفحة
type: docs
weight: 20
url: /java/get-page-offset/
description: تعرف على كيفية فحص إزاحات الصفحة X وY في Java باستخدام واجهة PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: احصل على إزاحات صفحة PDF باستخدام Java
Abstract: تعرف على كيفية استرداد إزاحات الصفحة باستخدام Aspose.PDF لـ Java. يستخدم مثال Java PdfFileInfo لقراءة إزاحات X وY للصفحة 1 وتحويل قيم النقاط إلى بوصات لتسهيل تحليل التخطيط.
---
## الحصول على إزاحة الصفحة

استخدم سير العمل هذا عندما تحتاج إلى فهم كيفية وضع محتوى الصفحة بالنسبة إلى أصل PDF.

### خطوات

1. قم بإنشاء كائن `PdfFileInfo` لمدخل PDF.
2. اتصل بـ `getPageXOffset` و`getPageYOffset` للصفحة المستهدفة.
3. قم بتحويل قيم النقاط إلى بوصات عن طريق القسمة على `72.0`.
4. استخدم أو اطبع القيم المحولة.
5. أغلق المثيل `PdfFileInfo`.

### مثال جافا

```java
public static void getPageOffsets(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page X Offset: " + (pdfInfo.getPageXOffset(1) / 72.0) + " inches");
    System.out.println("Page Y Offset: " + (pdfInfo.getPageYOffset(1) / 72.0) + " inches");
    pdfInfo.close();
}
```
