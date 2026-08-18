---
title: الحصول على نسخة PDF
linktitle: الحصول على نسخة PDF
type: docs
weight: 20
url: /java/get-pdf-version/
description: تعرف على كيفية استرداد نسخة مستند PDF في Java باستخدام واجهة PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استرداد نسخة PDF باستخدام Aspose.PDF لجافا
Abstract: تعرف على كيفية استرداد نسخة PDF باستخدام Aspose.PDF لـ Java. يقوم مثال Java بإنشاء كائن PdfFileInfo، وقراءة سلسلة الإصدار باستخدام `getPdfVersion()`، وطباعة النتيجة، وإغلاق كائن معلومات الملف.
---
## احصل على نسخة PDF

استخدم سير العمل هذا عندما تحتاج إلى التحقق من توافق الملف أو توجيه مستند من خلال منطق المعالجة الخاص بالإصدار.

### خطوات

1. قم بإنشاء كائن `PdfFileInfo` لملف PDF.
2. اتصل بـ `getPdfVersion()` لاسترداد الإصدار الذي تم الإبلاغ عنه.
3. استخدم أو اطبع قيمة الإصدار.
4. أغلق المثيل `PdfFileInfo`.

### مثال جافا

```java
public static void getPdfVersion(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println();
    System.out.println("PDF Version: " + pdfInfo.getPdfVersion());
    pdfInfo.close();
}
```
