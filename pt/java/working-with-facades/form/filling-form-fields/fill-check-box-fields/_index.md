---
title: Preencher Campos de Caixa de Seleção
linktitle: Preencher Campos de Caixa de Seleção
type: docs
weight: 20
url: /pt/java/fill-check-box-fields/
description: Aprenda como preencher campos de caixa de seleção em um formulário PDF com Java usando a fachada Form em Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Definir valores de campos de caixa de seleção em um formulário PDF com Java
Abstract: Este artigo mostra como vincular um formulário PDF, definir campos de caixa de seleção por nome e salvar o documento atualizado com a fachada Form em Aspose.PDF for Java.
---
Usar `FormExamples.fillCheckBoxFields(...)` definir valores das caixas de seleção em um formulário.

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
