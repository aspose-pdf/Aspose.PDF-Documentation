---
title: تصدير إلى XFDF
linktitle: تصدير إلى XFDF
type: docs
weight: 20
url: /java/export-to-xfdf/
description: تعرف على كيفية تصدير بيانات حقل نموذج PDF إلى XFDF في Java باستخدام واجهة النموذج في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: تصدير بيانات AcroForm إلى XFDF في Java
Abstract: توضح هذه المقالة كيفية ربط نموذج PDF وتصدير قيم الحقول الخاصة به إلى تدفق XFDF باستخدام واجهة النموذج في Aspose.PDF لـ Java.
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
