---
title: تصدير إلى XFDF
linktitle: تصدير إلى XFDF
type: docs
weight: 20
url: /ar/java/export-to-xfdf/
description: تعلم كيفية تصدير بيانات حقول نموذج PDF إلى XFDF في Java باستخدام واجهة Form في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: تصدير بيانات AcroForm إلى XFDF في Java
Abstract: توضح هذه المقالة كيفية ربط نموذج PDF وتصدير قيم حقوله إلى تدفق XFDF باستخدام واجهة Form في Aspose.PDF for Java.
---
استخدم `FormExamples.exportXfdf(...)` لكتابة بيانات حقل النموذج كـ XFDF.

```java
public static void exportXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream outputStream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(outputStream);
    } finally {
        form.close();
    }
}
```
