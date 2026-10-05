---
title: إضافة مرفق
linktitle: إضافة مرفق
type: docs
weight: 10
url: /ar/java/add-attachment/
description: تعرّف على كيفية إرفاق ملف خارجي بمستند PDF في Java باستخدام واجهة PdfContentEditor في Aspose.PDF.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: إضافة مرفق ملف إلى PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF، فتح مرفق كدفق، إضافة مرفق المستند مع وصف، وحفظ الملف المحدث باستخدام واجهة PdfContentEditor في Aspose.PDF for Java.
---
## إضافة مرفق مستند

1. اربط ملف PDF المصدر بـ `PdfContentEditor` الواجهة.
2. افتح ملف المرفق كدفق إدخال.
3. استدعِ `addDocumentAttachment(...)` مع الدفق، اسم الملف، والوصف.
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
