---
title: Exportar para FDF
linktitle: Exportar para FDF
type: docs
weight: 10
url: /pt/java/export-to-fdf/
description: Aprenda como exportar os valores dos campos de formulário PDF para FDF em Java usando a fachada Form na Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Exportar dados do AcroForm para FDF em Java
Abstract: Este artigo mostra como vincular um formulário PDF e exportar seus dados de campo para um fluxo FDF com a fachada Form na Aspose.PDF for Java.
---
Use `FormExamples.exportFdf(...)` quando precisar serializar os dados de campo AcroForm como FDF.

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
