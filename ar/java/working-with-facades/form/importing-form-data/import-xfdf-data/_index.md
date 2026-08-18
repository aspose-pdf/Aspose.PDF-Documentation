---
title: استيراد بيانات XFDF
linktitle: استيراد بيانات XFDF
type: docs
weight: 20
url: /java/import-xfdf-data/
description: تعرف على كيفية استيراد بيانات نموذج XFDF إلى نموذج PDF باستخدام Java باستخدام واجهة النموذج في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: استيراد بيانات AcroForm من XFDF في Java
Abstract: توضح هذه المقالة كيفية ربط نموذج PDF، واستيراد قيم الحقول من تدفق XFDF، وحفظ المستند المحدث باستخدام واجهة النموذج في Aspose.PDF لـ Java.
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
