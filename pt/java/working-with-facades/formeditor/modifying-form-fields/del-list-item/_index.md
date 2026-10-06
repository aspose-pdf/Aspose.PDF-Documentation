---
title: Excluir item da lista
linktitle: Excluir item da lista
type: docs
weight: 20
url: /pt/java/del-list-item/
description: Saiba como remover um item de um campo de lista em um documento PDF em Java usando a fachada FormEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Excluir um item de lista de um campo de formulário PDF em Java
Abstract: Este artigo mostra como vincular um PDF existente, remover um item específico de um campo de lista e salvar o documento atualizado usando a fachada FormEditor no Aspose.PDF for Java.
---
## Excluir um item de um campo de lista

1. Vincular o PDF de origem ao `FormEditor` fachada.
2. Chamar `delListItem(...)` para o campo de destino e o item a remover.
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
