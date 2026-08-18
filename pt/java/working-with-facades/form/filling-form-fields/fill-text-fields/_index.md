---
title: Preencher campos de texto
linktitle: Preencher campos de texto
type: docs
weight: 10
url: /java/fill-text-fields/
description: Aprenda como preencher campos de texto em um formulário PDF com Java usando a fachada do formulário em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Preencher campos de formulário de texto em um PDF com Java
Abstract: Este artigo mostra como vincular um formulário PDF, definir valores de campos de texto por nome e salvar o documento atualizado com a fachada Form em Aspose.PDF para Java.
---
Use `FormExamples.fillTextFields(...)` para preencher campos de formulário baseados em texto.

```java
public static void fillTextFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("name", "John Doe");
        form.fillField("address", "123 Main St, Anytown, USA");
        form.fillField("email", "john.doe@example.com");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
