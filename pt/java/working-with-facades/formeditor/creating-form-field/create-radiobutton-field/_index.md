---
title: Criar campo RadioButton
linktitle: Criar campo RadioButton
type: docs
weight: 50
url: /java/create-radiobutton-field/
description: Aprenda como adicionar um campo de botão de opção a um documento PDF em Java usando a fachada FormEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Crie um campo de botão de opção em um PDF com Java
Abstract: Este artigo mostra como vincular um PDF existente, definir as configurações de layout do botão de opção, criar um campo de botão de opção e salvar o documento modificado usando a fachada FormEditor no Aspose.PDF para Java.
---
Use `FormEditorExamples.createRadioButtonField(...)` para criar um campo de botão de opção com opções predefinidas.

## Crie um campo de botão de opção

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Configure a lacuna, a orientação e o tamanho do item do botão de opção.
3. Defina os itens do botão de opção.
4. Adicione o campo do botão de opção com sua seleção e retângulo padrão.
5. Salve o documento atualizado.

```java
public static void createRadioButtonField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setRadioGap(4);
        editor.setRadioHoriz(false);
        editor.setRadioButtonItemSize(20);
        editor.setItems(new String[] {"Australia", "New Zealand", "Malaysia"});
        editor.addField(FieldType.Radio, "radiobutton1", "Malaysia", 1, 240, 498, 256, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
