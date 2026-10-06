---
title: Preencher caixa de lista
linktitle: Preencher caixa de lista
type: docs
weight: 40
url: /pt/java/fill-list-box/
description: Saiba como preencher um campo de caixa de lista em um formulário PDF com Java usando a fachada Form no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Definir o valor de um campo de caixa de lista em um formulário PDF com Java
Abstract: Este artigo mostra como vincular um formulário PDF, definir o valor de um campo de caixa de lista e salvar o documento atualizado com a fachada Form no Aspose.PDF for Java.
---
Use `FormExamples.fillListBoxFields(...)` para preencher um campo de caixa de lista.

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
