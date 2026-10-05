---
title: تصدير إلى FDF
linktitle: تصدير إلى FDF
type: docs
weight: 10
url: /ar/java/export-to-fdf/
description: تعرف على كيفية تصدير قيم حقول نموذج PDF إلى FDF باستخدام لغة Java ومن خلال واجهة Form في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: تصدير بيانات AcroForm إلى FDF باستخدام Java
Abstract: توضح هذه المقالة كيفية ربط نموذج PDF وتصدير بيانات حقوله إلى تدفق FDF باستخدام واجهة Form في Aspose.PDF for Java.
---
استخدام `FormExamples.exportFdf(...)` عند الحاجة إلى تسلسل بيانات حقول AcroForm كـ FDF.

```java
public static void exportFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream outputStream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(outputStream);
    } finally {
        form.close();
    }
}
```
