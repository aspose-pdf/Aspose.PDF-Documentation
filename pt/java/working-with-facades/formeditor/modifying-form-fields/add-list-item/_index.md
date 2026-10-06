---
title: Adicionar item de lista
linktitle: Adicionar item de lista
type: docs
weight: 10
url: /pt/java/add-list-item/
description: Saiba como adicionar itens a um campo de lista em um documento PDF em Java usando a fachada FormEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Adicionar um item de lista a um campo de formulário PDF em Java
Abstract: Este artigo mostra como vincular um PDF existente, adicionar um novo item a um campo de lista e salvar o documento atualizado usando a fachada FormEditor no Aspose.PDF for Java.
---
## Adicionar um item a um campo de lista

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Chame `addListItem(...)` para o campo de destino e novo par de exibição/valor.
3. Salve o documento atualizado.

```java
public static void addListItem(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addListItem("Country", new String[] {"New Zealand", "New Zealand"});
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
