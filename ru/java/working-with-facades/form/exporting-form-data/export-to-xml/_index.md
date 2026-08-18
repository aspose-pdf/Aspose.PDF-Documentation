---
title: Экспорт в XML
linktitle: Экспорт в XML
type: docs
weight: 40
url: /java/export-to-xml/
description: Узнайте, как экспортировать данные формы PDF в XML на Java, используя фасад формы в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Экспорт данных AcroForm в XML на Java
Abstract: В этой статье показано, как связать форму PDF и экспортировать значения ее полей в поток XML с помощью фасада формы в Aspose.PDF для Java.
---
Используйте `FormExamples.exportXml(...)`, чтобы сохранить данные полей формы в формате XML.

```java
public static void exportXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream outputStream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(outputStream);
    } finally {
        form.close();
    }
}
```
