---
title: إضافة مرفق
linktitle: إضافة مرفق
type: docs
weight: 10
url: /java/add-attachment/
description: تعرف على كيفية إرفاق ملف خارجي بمستند PDF في Java باستخدام واجهة PdfContentEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: إضافة ملف مرفق إلى ملف PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF، وفتح المرفق كدفق، وإضافة مرفق المستند مع الوصف، وحفظ الملف المحدث باستخدام واجهة PdfContentEditor في Aspose.PDF لـ Java.
---
## إضافة مرفق مستند

1. قم بربط ملف PDF المصدر بالواجهة `PdfContentEditor`.
2. افتح الملف المرفق كدفق إدخال.
3. اتصل `addDocumentAttachment(...)` مع الدفق واسم الملف والوصف.
4. احفظ مستند PDF المحدث.

```java
public static void addAttachment(Path inputFile, Path attachmentFile, Path outputFile) throws Exception {
    PdfContentEditor editor = new PdfContentEditor();
    try (InputStream attachmentStream = Files.newInputStream(attachmentFile)) {
        editor.bindPdf(inputFile.toString());
        editor.addDocumentAttachment(attachmentStream, attachmentFile.getFileName().toString(), "Sample attachment.");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
