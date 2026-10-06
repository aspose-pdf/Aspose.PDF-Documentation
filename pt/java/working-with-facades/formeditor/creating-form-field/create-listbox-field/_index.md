---
title: Criar campo ListBox
linktitle: Criar campo ListBox
type: docs
weight: 40
url: /pt/java/create-listbox-field/
description: Aprenda como adicionar um campo de caixa de lista a um documento PDF em Java usando a fachada FormEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Criar um campo de caixa de lista em um PDF com Java
Abstract: Este artigo mostra como vincular um PDF existente, definir itens de lista, adicionar um campo de caixa de lista e salvar o documento modificado usando a fachada FormEditor no Aspose.PDF for Java.
---
Use `FormEditorExamples.createListBoxField(...)` para criar uma caixa de lista com itens predefinidos.

## Criar um campo de caixa de lista

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Defina os itens de lista disponíveis com `setItems(...)`.
3. Adicione o campo de caixa de lista com seu valor padrão e retângulo.
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
