---
title: إزالة المرفقات
linktitle: إزالة المرفقات
type: docs
weight: 50
url: /java/remove-attachments/
description: تعرف على كيفية إزالة جميع مرفقات المستندات من ملف PDF في Java باستخدام واجهة PdfContentEditor في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: قم بإزالة جميع مرفقات PDF في Java
Abstract: توضح هذه المقالة كيفية ربط ملف PDF، وحذف جميع مرفقات المستندات، وحفظ الملف المحدث باستخدام واجهة PdfContentEditor في Aspose.PDF لـ Java.
---
## قم بإزالة كافة المرفقات

1. قم بربط ملف PDF المصدر بالواجهة `PdfContentEditor`.
2. اتصل بـ `deleteAttachments()` لإزالة كل المرفقات المضمنة.
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
