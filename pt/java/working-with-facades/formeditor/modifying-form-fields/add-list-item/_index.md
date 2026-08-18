---
title: Adicionar item da lista
linktitle: Adicionar item da lista
type: docs
weight: 10
url: /java/add-list-item/
description: Aprenda como adicionar itens a um campo de lista em um documento PDF em Java usando a fachada FormEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Adicione um item de lista a um campo de formulário PDF em Java
Abstract: Este artigo mostra como vincular um PDF existente, adicionar um novo item a um campo de lista e salvar o documento atualizado usando a fachada FormEditor em Aspose.PDF para Java.
---
## Adicionar um item a um campo de lista

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Chame `addListItem(...)` para o campo de destino e o novo par exibição/valor.
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
