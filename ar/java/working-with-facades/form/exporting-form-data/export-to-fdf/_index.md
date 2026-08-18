---
title: تصدير إلى قوات الدفاع الشعبي
linktitle: تصدير إلى قوات الدفاع الشعبي
type: docs
weight: 10
url: /java/export-to-fdf/
description: تعرف على كيفية تصدير قيم حقول نموذج PDF إلى FDF في Java باستخدام واجهة النموذج في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: تصدير بيانات AcroForm إلى FDF في Java
Abstract: توضح هذه المقالة كيفية ربط نموذج PDF وتصدير بيانات الحقل الخاصة به إلى دفق FDF باستخدام واجهة النموذج في Aspose.PDF لـ Java.
---
استخدم `FormExamples.exportFdf(...)` عندما تحتاج إلى إجراء تسلسل لبيانات حقل AcroForm كـ FDF.

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
