---
title: Aplanar Todos os Campos
linktitle: Aplanar Todos os Campos
type: docs
weight: 10
url: /pt/java/flatten-all-fields/
description: Saiba como aplanar todos os campos de formulário PDF em Java usando a fachada Form no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Converta todos os campos de formulário interativos em conteúdo estático em Java
Abstract: Este artigo mostra como vincular um formulário PDF, aplanar cada campo de formulário e salvar o documento atualizado com a fachada Form no Aspose.PDF for Java.
---
Usar `FormExamples.flattenAllFields(...)` quando você precisa converter todos os campos interativos em conteúdo estático da página.

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
