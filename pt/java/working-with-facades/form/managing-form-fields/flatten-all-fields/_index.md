---
title: Achatar todos os campos
linktitle: Achatar todos os campos
type: docs
weight: 10
url: /java/flatten-all-fields/
description: Aprenda como nivelar todos os campos do formulário PDF em Java usando a fachada do formulário em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Converta todos os campos do formulário interativo em conteúdo estático em Java
Abstract: Este artigo mostra como vincular um formulário PDF, nivelar cada campo do formulário e salvar o documento atualizado com a fachada Form em Aspose.PDF para Java.
---
Use `FormExamples.flattenAllFields(...)` quando precisar converter todos os campos interativos em conteúdo de página estática.

```java
public static void flattenAllFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.flattenAllFields();
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
