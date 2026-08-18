---
title: استيراد بيانات FDF
linktitle: استيراد بيانات FDF
type: docs
weight: 10
url: /java/import-fdf-data/
description: تعرف على كيفية استيراد بيانات نموذج FDF إلى نموذج PDF باستخدام Java باستخدام واجهة النموذج في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: استيراد بيانات AcroForm من FDF في Java
Abstract: توضح هذه المقالة كيفية ربط نموذج PDF، واستيراد قيم الحقول من تدفق FDF، وحفظ المستند المحدث باستخدام واجهة النموذج في Aspose.PDF لـ Java.
---
استخدم `FormExamples.importFdf(...)` لتطبيق قيم الحقول من ملف FDF.

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
