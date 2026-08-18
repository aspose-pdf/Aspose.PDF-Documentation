---
title: إضافة إجراء مستند
linktitle: إضافة إجراء مستند
type: docs
weight: 10
url: /java/add-document-action/
description: تعرف على كيفية إضافة إجراء فتح مستند إلى ملف PDF في Java باستخدام واجهة PdfContentEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: أضف إجراء فتح المستند إلى ملف PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF، وإرفاق إجراء JavaScript بحدث فتح المستند، وحفظ المستند المحدث باستخدام واجهة PdfContentEditor في Aspose.PDF لـ Java.
---
## إضافة إجراء فتح المستند

1. قم بربط ملف PDF المصدر بالواجهة `PdfContentEditor`.
2. اتصل بـ `addDocumentAdditionalAction(...)` باستخدام الحدث `DOCUMENT_OPEN` ونص إجراء JavaScript.
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
