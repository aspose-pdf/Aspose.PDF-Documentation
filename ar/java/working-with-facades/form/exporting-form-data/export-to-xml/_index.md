---
title: تصدير إلى XML
linktitle: تصدير إلى XML
type: docs
weight: 40
url: /java/export-to-xml/
description: تعرف على كيفية تصدير بيانات نموذج PDF إلى XML في Java باستخدام واجهة النموذج في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: تصدير بيانات AcroForm إلى XML في Java
Abstract: توضح هذه المقالة كيفية ربط نموذج PDF وتصدير قيم الحقول الخاصة به إلى تدفق XML باستخدام واجهة النموذج في Aspose.PDF لـ Java.
---
استخدم `FormExamples.exportXml(...)` لحفظ بيانات حقل النموذج بتنسيق XML.

```java
public static void exportXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream outputStream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(outputStream);
    } finally {
        form.close();
    }
}
```
