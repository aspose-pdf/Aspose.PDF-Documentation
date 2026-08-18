---
title: Exportar para XML
linktitle: Exportar para XML
type: docs
weight: 40
url: /java/export-to-xml/
description: Aprenda como exportar dados de formulário PDF para XML em Java usando a fachada do formulário em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Exporte dados do AcroForm para XML em Java
Abstract: Este artigo mostra como vincular um formulário PDF e exportar seus valores de campo para um fluxo XML com a fachada Form em Aspose.PDF para Java.
---
Use `FormExamples.exportXml(...)` para salvar os dados do campo do formulário como XML.

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
