---
title: تقسيم PDF إلى النهاية
linktitle: تقسيم PDF إلى النهاية
type: docs
weight: 40
url: /ar/java/split-pdf-to-end/
description: قسّم PDF من صفحة مختارة إلى النهاية في Java باستخدام واجهة PdfFileEditor.
lastmod: "2026-10-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخراج الصفحات من نقطة بدء إلى نهاية PDF باستخدام Java
Abstract: تعلم كيفية تقسيم PDF إلى النهاية باستخدام Aspose.PDF for Java. يستخدم المثال في Java أداة PdfFileEditor لاستخراج جميع الصفحات بدءًا من الصفحة 2 حتى نهاية المستند الأصلي.
---
## تقسيم PDF إلى النهاية

عينة Java تستخرج جميع الصفحات بدءًا من الصفحة 2.

### خطوات

1. إنشاء `PdfFileEditor` مثيل.
2. اتصال `splitToEnd` مع ملف المصدر، رقم الصفحة الابتدائي، وملف الإخراج.
3. احفظ مستند PDF الناتج.

```java
public static void splitPdfToEnd(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToEnd(inputFile.toString(), 2, outputFile.toString());
}
```
