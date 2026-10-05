---
title: إضافة إجراء المستند
linktitle: إضافة إجراء المستند
type: docs
weight: 10
url: /ar/java/add-document-action/
description: تعلم كيفية إضافة إجراء فتح المستند إلى ملف PDF في Java باستخدام الواجهة PdfContentEditor في Aspose.PDF.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: إضافة إجراء فتح المستند إلى ملف PDF في Java
Abstract: تُظهر هذه المقالة كيفية ربط ملف PDF، وإرفاق إجراء JavaScript بحدث فتح المستند، وحفظ المستند المحدث باستخدام الواجهة PdfContentEditor في Aspose.PDF for Java.
---
## إضافة إجراء فتح المستند

1. اربط ملف PDF المصدر إلى واجهة `PdfContentEditor`.
2. استدعِ `addDocumentAdditionalAction(...)` مع `DOCUMENT_OPEN` الحدث ونص إجراء JavaScript..
3. احفظ مستند PDF المحدث.

```java
public static void addDocumentAction(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addDocumentAdditionalAction(PdfContentEditor.DOCUMENT_OPEN, "app.alert('Document opened with PdfContentEditor action');");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
