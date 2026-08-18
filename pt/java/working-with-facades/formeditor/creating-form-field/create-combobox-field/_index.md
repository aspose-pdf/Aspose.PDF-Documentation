---
title: Criar campo ComboBox
linktitle: Criar campo ComboBox
type: docs
weight: 30
url: /java/create-combobox-field/
description: Aprenda como adicionar um campo de caixa de combinação a um documento PDF em Java usando a fachada FormEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Crie um campo de caixa de combinação em um PDF com Java
Abstract: Este artigo mostra como vincular um PDF existente, adicionar um campo de caixa de combinação, preenchê-lo com itens e salvar o documento modificado usando a fachada FormEditor em Aspose.PDF para Java.
---
Use `FormEditorExamples.createComboBoxField(...)` para criar uma caixa de combinação e adicionar itens selecionáveis.

## Crie um campo de caixa de combinação

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Adicione o campo da caixa de combinação com seu valor padrão e retângulo de destino.
3. Adicione os itens selecionáveis ​​da caixa de combinação.
4. Salve o documento atualizado.

```java
public static void createComboBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.ComboBox, "combobox1", "Australia", 1, 230, 498, 350, 514);
        editor.addListItem("combobox1", new String[] {"Australia", "Australia"});
        editor.addListItem("combobox1", new String[] {"New Zealand", "New Zealand"});
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
