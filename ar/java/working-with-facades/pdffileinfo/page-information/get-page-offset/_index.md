---
title: احصل على إزاحة الصفحة
linktitle: احصل على إزاحة الصفحة
type: docs
weight: 20
url: /ar/java/get-page-offset/
description: تعرّف على كيفية فحص إزاحات X و Y للصفحة في جافا باستخدام واجهة PdfFileInfo.
lastmod: "2026-10-01"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: احصل على إزاحات صفحات PDF باستخدام جافا
Abstract: تعرّف على كيفية استرجاع إزاحات الصفحات باستخدام Aspose.PDF for Java. يستخدم المثال في جافا PdfFileInfo لقراءة إزاحات X و Y للصفحة 1 ويحوّل قيم النقاط إلى بوصات لتسهيل تحليل التخطيط.
---
## احصل على إزاحة الصفحة

استخدم سير العمل هذا عندما تحتاج إلى فهم كيفية وضع محتوى الصفحة بالنسبة إلى أصل PDF.

### خطوات

1. إنشاء `PdfFileInfo` كائن لملف PDF المُدخل.
2. اتصال `getPageXOffset` و `getPageYOffset` لصفحة الهدف.
3. حوّل قيم النقاط إلى بوصات بقسمة على `72.0`.
4. استخدم أو اطبع القيم المحوّلة.
5. إغلاق `PdfFileInfo` مثال.

### مثال Java

```java
public static void getPageOffsets(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page X Offset: " + (pdfInfo.getPageXOffset(1) / 72.0) + " inches");
    System.out.println("Page Y Offset: " + (pdfInfo.getPageYOffset(1) / 72.0) + " inches");
    pdfInfo.close();
}
```
