---
title: Criar campo ListBox
linktitle: Criar campo ListBox
type: docs
weight: 40
url: /java/create-listbox-field/
description: Aprenda como adicionar um campo de caixa de listagem a um documento PDF em Java usando a fachada FormEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Crie um campo de caixa de listagem em um PDF com Java
Abstract: Este artigo mostra como vincular um PDF existente, definir itens de lista, adicionar um campo de caixa de listagem e salvar o documento modificado usando a fachada FormEditor em Aspose.PDF para Java.
---
Use `FormEditorExamples.createListBoxField(...)` para criar uma caixa de listagem com itens predefinidos.

## Crie um campo de caixa de listagem

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Defina os itens da lista disponíveis com `setItems(...)`.
3. Adicione o campo da caixa de listagem com seu valor padrão e retângulo.
4. Salve o documento atualizado.

```java
public static void createListBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setItems(new String[] {"Australia", "New Zealand", "Malaysia"});
        editor.addField(FieldType.ListBox, "listbox1", "Australia", 1, 230, 398, 350, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
