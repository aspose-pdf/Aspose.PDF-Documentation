---
title: Экспорт в XFDF
linktitle: Экспорт в XFDF
type: docs
weight: 20
url: /ru/java/export-to-xfdf/
description: Узнайте, как экспортировать данные полей PDF‑формы в XFDF на Java, используя фасад Form в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Экспорт данных AcroForm в XFDF на Java
Abstract: В этой статье показано, как привязать PDF‑форму и экспортировать её значения полей в поток XFDF с помощью фасада Form в Aspose.PDF for Java.
---
Использовать `FormExamples.exportXfdf(...)` записать данные полей формы в виде XFDF.

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

