---
title: استيراد بيانات XML
linktitle: استيراد بيانات XML
type: docs
weight: 40
url: /java/import-xml-data/
description: تعرف على كيفية استيراد بيانات نموذج XML إلى نموذج PDF باستخدام Java باستخدام واجهة النموذج في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: استيراد بيانات AcroForm من XML في Java
Abstract: توضح هذه المقالة كيفية ربط نموذج PDF، واستيراد قيم الحقول من تدفق XML، وحفظ المستند المحدث باستخدام واجهة النموذج في Aspose.PDF لـ Java.
---
استخدم `FormExamples.importXml(...)` لملء نموذج من بيانات XML.

```java
public static void importXml(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXml(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
