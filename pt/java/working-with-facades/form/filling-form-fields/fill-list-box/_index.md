---
title: Preencher caixa de listagem
linktitle: Preencher caixa de listagem
type: docs
weight: 40
url: /java/fill-list-box/
description: Aprenda como preencher um campo de caixa de listagem em um formulário PDF com Java usando a fachada do formulário em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Defina um valor de campo de caixa de listagem em um formulário PDF com Java
Abstract: Este artigo mostra como vincular um formulário PDF, definir um valor de campo de caixa de listagem e salvar o documento atualizado com a fachada Form em Aspose.PDF para Java.
---
Use `FormExamples.fillListBoxFields(...)` para preencher um campo de caixa de listagem.

```java
public static void fillListBoxFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("favorite_colors", "Red");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
