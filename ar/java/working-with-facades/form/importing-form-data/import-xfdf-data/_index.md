---
title: استيراد بيانات XFDF
linktitle: استيراد بيانات XFDF
type: docs
weight: 20
url: /ar/java/import-xfdf-data/
description: تعلم كيفية استيراد بيانات نموذج XFDF إلى نموذج PDF باستخدام Java عبر واجهة Form في Aspose.PDF.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: استيراد بيانات AcroForm من XFDF في Java
Abstract: توضح هذه المقالة كيفية ربط نموذج PDF، استيراد قيم الحقول من تدفق XFDF، وحفظ المستند المحدث باستخدام واجهة Form في Aspose.PDF for Java.
---
استخدم `FormExamples.importXfdf(...)` لملء نموذج من بيانات XFDF.

```java
public static void importXfdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXfdf(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
