---
title: Preencha os campos da caixa de seleção
linktitle: Preencha os campos da caixa de seleção
type: docs
weight: 20
url: /java/fill-check-box-fields/
description: Aprenda como preencher campos de caixa de seleção em um formulário PDF com Java usando a fachada do formulário em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Definir valores de campos de caixa de seleção em um formulário PDF com Java
Abstract: Este artigo mostra como vincular um formulário PDF, definir campos de caixa de seleção por nome e salvar o documento atualizado com a fachada do formulário em Aspose.PDF para Java.
---
Use `FormExamples.fillCheckBoxFields(...)` para definir valores de caixas de seleção em um formulário.

```java
public static void fillCheckBoxFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("subscribe_newsletter", "Yes");
        form.fillField("accept_terms", "Yes");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
