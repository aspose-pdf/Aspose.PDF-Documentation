---
title: إزالة المرفقات
linktitle: إزالة المرفقات
type: docs
weight: 50
url: /ar/java/remove-attachments/
description: تعلم كيفية إزالة جميع مرفقات المستند من ملف PDF باستخدام واجهة `PdfContentEditor` في Aspose.PDF للغة Java.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: إزالة جميع مرفقات PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF، حذف جميع مرفقات المستند، وحفظ الملف المحدث باستخدام واجهة `PdfContentEditor` في Aspose.PDF for Java.
---
## إزالة جميع المرفقات

1. اربط ملف PDF المصدر إلى `PdfContentEditor` واجهة.
2. اتصال `deleteAttachments()` لإزالة كل مرفق مدمج.
3. احفظ مستند PDF المحدث.

```java
public static void removeAttachments(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.deleteAttachments();
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
