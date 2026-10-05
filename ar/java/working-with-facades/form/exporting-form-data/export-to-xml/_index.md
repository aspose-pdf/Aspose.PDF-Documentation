---
title: تصدير إلى XML
linktitle: تصدير إلى XML
type: docs
weight: 40
url: /ar/java/export-to-xml/
description: تعرف على كيفية تصدير بيانات نموذج PDF إلى XML في Java باستخدام واجهة Form في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: تصدير بيانات AcroForm إلى XML في Java
Abstract: توضح هذه المقالة كيفية ربط نموذج PDF وتصدير قيم حقوله إلى تدفق XML باستخدام واجهة Form في Aspose.PDF for Java.
---
استخدام `FormExamples.exportXml(...)` لحفظ بيانات حقل النموذج كملف XML.

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
