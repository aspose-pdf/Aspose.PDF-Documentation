---
title: Importar dados FDF
linktitle: Importar dados FDF
type: docs
weight: 10
url: /pt/java/import-fdf-data/
description: Saiba como importar dados de formulário FDF em um formulário PDF com Java usando a fachada Form no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Importar dados AcroForm de FDF em Java
Abstract: Este artigo mostra como vincular um formulário PDF, importar valores de campo de um fluxo FDF e salvar o documento atualizado com a fachada Form no Aspose.PDF for Java.
---
Use `FormExamples.importFdf(...)` para aplicar valores de campo de um arquivo FDF.

```java
public static void importFdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importFdf(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
