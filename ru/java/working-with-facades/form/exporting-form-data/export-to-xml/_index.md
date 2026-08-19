---
title: Экспорт в XML
linktitle: Экспорт в XML
type: docs
weight: 40
url: /ru/java/export-to-xml/
description: Узнайте, как экспортировать данные формы PDF в XML на Java, используя фасад Form в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Экспорт данных AcroForm в XML на Java
Abstract: В этой статье показано, как привязать форму PDF и экспортировать значения её полей в поток XML с помощью фасада Form в Aspose.PDF for Java.
---
Использовать `FormExamples.exportXml(...)` для сохранения данных полей формы в XML.

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

