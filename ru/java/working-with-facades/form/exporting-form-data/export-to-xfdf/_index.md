---
title: Экспорт в XFDF
linktitle: Экспорт в XFDF
type: docs
weight: 20
url: /java/export-to-xfdf/
description: Узнайте, как экспортировать данные полей формы PDF в XFDF на Java, используя фасад формы в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Экспорт данных AcroForm в XFDF на Java
Abstract: В этой статье показано, как связать форму PDF и экспортировать значения ее полей в поток XFDF с помощью фасада формы в Aspose.PDF для Java.
---
Используйте `FormExamples.exportXfdf(...)` для записи данных полей формы в формате XFDF.

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
