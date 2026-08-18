---
title: الحصول على معلومات الصفحة
linktitle: الحصول على معلومات الصفحة
type: docs
weight: 10
url: /java/get-page-info/
description: تعرف على كيفية فحص عرض الصفحة وارتفاعها وتدويرها في Java باستخدام واجهة PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: احصل على معلومات صفحة PDF باستخدام Aspose.PDF لـ Java
Abstract: تعرف على كيفية استرداد معلومات الصفحة باستخدام Aspose.PDF لـ Java. يستخدم مثال Java PdfFileInfo لقراءة عرض الصفحة 1 وارتفاعها وتدويرها حتى تتمكن من فحص تخطيطها قبل إجراء المزيد من المعالجة.
---
## الحصول على معلومات الصفحة

يقرأ هذا المثال الخصائص الهندسية الرئيسية للصفحة 1.

### خطوات

1. قم بإنشاء كائن `PdfFileInfo` لملف PDF المصدر.
2. اتصل بـ `getPageWidth` و`getPageHeight` و`getPageRotation` للصفحة التي تريد فحصها.
3. استخدم أو اطبع القيم التي تم إرجاعها.
4. أغلق المثيل `PdfFileInfo`.

### مثال جافا

```java
public static void getPageInformation(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page Width: " + pdfInfo.getPageWidth(1));
    System.out.println("Page Height: " + pdfInfo.getPageHeight(1));
    System.out.println("Page Rotation: " + pdfInfo.getPageRotation(1));
    pdfInfo.close();
}
```
