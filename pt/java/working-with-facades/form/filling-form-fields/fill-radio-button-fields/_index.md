---
title: Preencher campos de botão de opção
linktitle: Preencher campos de botão de opção
type: docs
weight: 30
url: /java/fill-radio-button-fields/
description: Aprenda como selecionar um valor de botão de opção em um formulário PDF com Java usando a fachada do formulário em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Selecione uma opção de campo de botão de opção em Java
Abstract: Este artigo mostra como vincular um formulário PDF, selecionar uma opção de botão de opção por índice e salvar o documento atualizado com a fachada Form em Aspose.PDF para Java.
---
Use `FormExamples.fillRadioButtonFields(...)` para selecionar uma opção de botão de opção.

```java
public static void fillRadioButtonFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("gender", 0);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
