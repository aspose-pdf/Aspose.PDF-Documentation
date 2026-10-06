---
title: Exportar para XML
linktitle: Exportar para XML
type: docs
weight: 40
url: /pt/java/export-to-xml/
description: Aprenda como exportar os dados de formulário PDF para XML em Java usando a fachada Form no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Exportar dados do AcroForm para XML em Java
Abstract: Este artigo mostra como vincular um formulário PDF e exportar seus valores de campo para um fluxo XML com a fachada Form no Aspose.PDF for Java.
---
Usar `FormExamples.exportXml(...)` para salvar os dados do campo de formulário como XML.

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
