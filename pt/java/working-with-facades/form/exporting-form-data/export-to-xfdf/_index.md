---
title: Exportar para XFDF
linktitle: Exportar para XFDF
type: docs
weight: 20
url: /java/export-to-xfdf/
description: Aprenda como exportar dados de campo de formulário PDF para XFDF em Java usando a fachada do formulário em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Exporte dados do AcroForm para XFDF em Java
Abstract: Este artigo mostra como vincular um formulário PDF e exportar seus valores de campo para um fluxo XFDF com a fachada Form em Aspose.PDF para Java.
---
Use `FormExamples.exportXfdf(...)` para gravar dados de campo de formulário como XFDF.

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
