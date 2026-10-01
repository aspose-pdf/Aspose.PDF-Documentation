---
title: استيراد بيانات FDF
linktitle: استيراد بيانات FDF
type: docs
weight: 10
url: /ar/java/import-fdf-data/
description: تعلم كيفية استيراد بيانات نموذج FDF إلى نموذج PDF باستخدام Java عبر واجهة Form في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: استيراد بيانات AcroForm من FDF باستخدام Java
Abstract: توضح هذه المقالة كيفية ربط نموذج PDF، واستيراد قيم الحقول من تدفق FDF، وحفظ المستند المحدث باستخدام واجهة Form في Aspose.PDF for Java.
---
استخدام `FormExamples.importFdf(...)` لتطبيق قيم الحقول من ملف FDF.

```java
public static void importFdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importFdf(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
