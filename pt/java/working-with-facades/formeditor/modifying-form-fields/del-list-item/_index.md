---
title: Excluir item da lista
linktitle: Excluir item da lista
type: docs
weight: 20
url: /java/del-list-item/
description: Aprenda como remover um item de um campo de lista em um documento PDF em Java usando a fachada FormEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Exclua um item de lista de um campo de formulário PDF em Java
Abstract: Este artigo mostra como vincular um PDF existente, remover um item específico de um campo de lista e salvar o documento atualizado usando a fachada FormEditor em Aspose.PDF para Java.
---
## Excluir um item de um campo de lista

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Chame `delListItem(...)` para o campo de destino e o item a ser removido.
3. Salve o documento atualizado.

```java
public static void deleteListItem(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.delListItem("Country", "UK");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
