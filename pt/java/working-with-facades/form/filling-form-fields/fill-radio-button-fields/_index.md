---
title: Preencher campos de botão de rádio
linktitle: Preencher campos de botão de rádio
type: docs
weight: 30
url: /pt/java/fill-radio-button-fields/
description: Saiba como selecionar um valor de botão de rádio em um formulário PDF com Java usando a fachada Form no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Selecionar uma opção de campo de botão de rádio em Java
Abstract: Este artigo mostra como vincular um formulário PDF, selecionar uma opção de botão de rádio por índice e salvar o documento atualizado com a fachada Form no Aspose.PDF for Java.
---
Usar `FormExamples.fillRadioButtonFields(...)` para selecionar uma opção de botão de rádio.

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
