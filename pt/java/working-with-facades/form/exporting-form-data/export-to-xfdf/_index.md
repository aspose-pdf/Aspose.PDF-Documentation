---
title: Exportar para XFDF
linktitle: Exportar para XFDF
type: docs
weight: 20
url: /pt/java/export-to-xfdf/
description: Saiba como exportar os dados de campos de formulário PDF para XFDF em Java usando a fachada Form no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Exportar dados AcroForm para XFDF em Java
Abstract: Este artigo mostra como vincular um formulário PDF e exportar seus valores de campo para um fluxo XFDF com a fachada Form no Aspose.PDF for Java.
---
Use `FormExamples.exportXfdf(...)` para escrever dados de campo de formulário como XFDF.

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
