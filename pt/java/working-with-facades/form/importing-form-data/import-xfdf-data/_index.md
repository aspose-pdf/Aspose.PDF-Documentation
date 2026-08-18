---
title: Importar dados XFDF
linktitle: Importar dados XFDF
type: docs
weight: 20
url: /java/import-xfdf-data/
description: Aprenda como importar dados de formulário XFDF para um formulário PDF com Java usando a fachada Form em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Importe dados AcroForm do XFDF em Java
Abstract: Este artigo mostra como vincular um formulário PDF, importar valores de campo de um fluxo XFDF e salvar o documento atualizado com a fachada Form em Aspose.PDF para Java.
---
Use `FormExamples.importXfdf(...)` para preencher um formulário a partir de dados XFDF.

```java
public static void importXfdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXfdf(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
