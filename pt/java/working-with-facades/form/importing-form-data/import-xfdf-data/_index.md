---
title: Importar Dados XFDF
linktitle: Importar Dados XFDF
type: docs
weight: 20
url: /pt/java/import-xfdf-data/
description: Aprenda como importar dados de formulário XFDF para um formulário PDF com Java usando a fachada Form no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Importar dados AcroForm de XFDF em Java
Abstract: Este artigo mostra como vincular um formulário PDF, importar valores de campo de um fluxo XFDF e salvar o documento atualizado com a fachada Form no Aspose.PDF for Java.
---
Usar `FormExamples.importXfdf(...)` para preencher um formulário a partir de dados XFDF.

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
