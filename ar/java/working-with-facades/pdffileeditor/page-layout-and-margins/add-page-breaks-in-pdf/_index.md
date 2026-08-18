---
title: إضافة فواصل الصفحات في PDF
linktitle: إضافة فواصل الصفحات في PDF
type: docs
weight: 20
url: /java/add-page-breaks-in-pdf/
description: قم بإدراج فواصل الصفحات في ملف PDF في Java باستخدام واجهة PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإدراج فواصل الصفحات في مواضع ثابتة في مستند PDF باستخدام Java
Abstract: تعرف على كيفية إضافة فواصل الصفحات باستخدام Aspose.PDF لـ Java. يستخدم مثال Java PdfFileEditor.PageBreak لتقسيم الصفحة في موضع رأسي محدد وحفظ النتيجة كملف PDF جديد.
---
## إضافة فواصل الصفحات في ملف PDF

استخدم سير العمل هذا عندما يلزم تقسيم الصفحة إلى صفحات متعددة في موضع Y معروف.

### خطوات

1. قم بإنشاء مثيل `PdfFileEditor`.
2. قم بإنشاء إدخال واحد أو أكثر `PdfFileEditor.PageBreak` باستخدام رقم الصفحة وموضع الفاصل.
3. قم بتمرير صفيف فاصل الصفحات إلى `addPageBreak`.
4. احفظ مستند PDF المحدث.

### مثال جافا

```java
public static void addPageBreaksInPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addPageBreak(inputFile.toString(), outputFile.toString(), new PdfFileEditor.PageBreak[] {
            new PdfFileEditor.PageBreak(1, 400)
    });
}
```
