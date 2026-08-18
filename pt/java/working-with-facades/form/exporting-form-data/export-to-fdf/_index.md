---
title: Exportar para FDF
linktitle: Exportar para FDF
type: docs
weight: 10
url: /java/export-to-fdf/
description: Aprenda como exportar valores de campos de formulário PDF para FDF em Java usando a fachada do formulário em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Exportar dados do AcroForm para FDF em Java
Abstract: Este artigo mostra como vincular um formulário PDF e exportar seus dados de campo para um fluxo FDF com a fachada Form em Aspose.PDF para Java.
---
Use `FormExamples.exportFdf(...)` quando precisar serializar os dados do campo AcroForm como FDF.

```java
public static void exportFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream outputStream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(outputStream);
    } finally {
        form.close();
    }
}
```
