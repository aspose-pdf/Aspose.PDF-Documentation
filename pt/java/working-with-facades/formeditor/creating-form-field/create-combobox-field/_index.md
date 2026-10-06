---
title: Criar Campo ComboBox
linktitle: Criar Campo ComboBox
type: docs
weight: 30
url: /pt/java/create-combobox-field/
description: Saiba como adicionar um campo combo box a um documento PDF em Java usando a fachada FormEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Criar um campo combo box em um PDF com Java
Abstract: Este artigo mostra como vincular um PDF existente, adicionar um campo combo box, preenchê-lo com itens e salvar o documento modificado usando a fachada FormEditor no Aspose.PDF for Java.
---
Usar `FormEditorExamples.createComboBoxField(...)` para criar uma caixa de combinação e adicionar itens selecionáveis.

## Criar um campo combo box

1. Vincule o PDF de origem ao `FormEditor` fachada.
2. Adicione o campo de caixa de combinação com seu valor padrão e retângulo de destino.
3. Adicione os itens selecionáveis da caixa de combinação.
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
