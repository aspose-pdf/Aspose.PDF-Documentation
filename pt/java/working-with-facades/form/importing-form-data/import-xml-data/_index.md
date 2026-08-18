---
title: Importar dados XML
linktitle: Importar dados XML
type: docs
weight: 40
url: /java/import-xml-data/
description: Aprenda como importar dados de formulário XML para um formulário PDF com Java usando a fachada Form em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Importe dados AcroForm de XML em Java
Abstract: Este artigo mostra como vincular um formulário PDF, importar valores de campo de um fluxo XML e salvar o documento atualizado com a fachada Form em Aspose.PDF para Java.
---
Use `FormExamples.importXml(...)` para preencher um formulário a partir de dados XML.

```java
public static void importXml(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXml(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
