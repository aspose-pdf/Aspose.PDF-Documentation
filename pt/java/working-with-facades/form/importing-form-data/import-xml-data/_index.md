---
title: Importar dados XML
linktitle: Importar dados XML
type: docs
weight: 40
url: /pt/java/import-xml-data/
description: Saiba como importar dados de formulário XML para um formulário PDF com Java usando a fachada Form no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Importar dados AcroForm de XML em Java
Abstract: Este artigo mostra como vincular um formulário PDF, importar valores de campos de um fluxo XML e salvar o documento atualizado com a fachada Form no Aspose.PDF for Java.
---
Usar `FormExamples.importXml(...)` para preencher um formulário a partir de dados XML.

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
