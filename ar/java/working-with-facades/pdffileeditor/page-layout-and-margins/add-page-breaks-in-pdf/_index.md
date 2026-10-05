---
title: إضافة فواصل صفحات في PDF
linktitle: إضافة فواصل صفحات في PDF
type: docs
weight: 20
url: /ar/java/add-page-breaks-in-pdf/
description: إدراج فواصل صفحات في ملف PDF باستخدام Java مع واجهة PdfFileEditor.
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إدراج فواصل صفحات في مواضع ثابتة داخل مستند PDF باستخدام Java
Abstract: تعلم كيفية إضافة فواصل صفحات باستخدام Aspose.PDF for Java. يستخدم مثال Java الكائن PdfFileEditor.PageBreak لتقسيم صفحة عند موضع عمودي محدد وحفظ النتيجة كملف PDF جديد.
---
## إضافة فواصل صفحات في PDF

استخدم سير العمل هذا عندما تحتاج صفحة إلى أن تُقسَّم إلى عدة صفحات عند موضع Y معروف.

### خطوات

1. أنشئ مثيلًا من `PdfFileEditor`.
2. أنشئ واحد أو أكثر `PdfFileEditor.PageBreak` الإدخالات مع رقم الصفحة وموقع الفاصل.
3. مرّر مصفوفة فاصل الصفحات إلى `addPageBreak`.
4. احفظ مستند PDF المحدث.

### مثال Java

```java
public static void addPageBreaksInPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addPageBreak(inputFile.toString(), outputFile.toString(), new PdfFileEditor.PageBreak[] {
            new PdfFileEditor.PageBreak(1, 400)
    });
}
```
