---
title: تقسيم ملف PDF إلى النهاية
linktitle: تقسيم ملف PDF إلى النهاية
type: docs
weight: 40
url: /java/split-pdf-to-end/
description: قم بتقسيم ملف PDF من الصفحة المختارة إلى النهاية في Java باستخدام واجهة PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم باستخراج الصفحات من نقطة البداية إلى نهاية ملف PDF باستخدام Java
Abstract: تعرف على كيفية تقسيم ملف PDF إلى النهاية باستخدام Aspose.PDF لـ Java. يستخدم مثال Java PdfFileEditor لاستخراج كافة الصفحات بدءًا من الصفحة 2 وحتى نهاية المستند المصدر.
---
## تقسيم ملف PDF إلى النهاية

يستخرج نموذج Java جميع الصفحات بدءًا من الصفحة 2.

### خطوات

1. قم بإنشاء مثيل `PdfFileEditor`.
2. اتصل `splitToEnd` بالملف المصدر ورقم صفحة البداية وملف الإخراج.
3. احفظ مستند PDF الناتج.

```java
public static void splitPdfToEnd(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToEnd(inputFile.toString(), 2, outputFile.toString());
}
```
