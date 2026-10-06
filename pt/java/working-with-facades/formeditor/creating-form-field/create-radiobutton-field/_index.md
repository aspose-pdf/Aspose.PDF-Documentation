---
title: Criar campo RadioButton
linktitle: Criar campo RadioButton
type: docs
weight: 50
url: /pt/java/create-radiobutton-field/
description: Saiba como adicionar um campo RadioButton a um documento PDF em Java usando a fachada FormEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Criar um campo RadioButton em um PDF com Java
Abstract: Este artigo mostra como vincular um PDF existente, configurar as definições de layout do botão de opção, criar um campo RadioButton e salvar o documento modificado usando a fachada FormEditor no Aspose.PDF for Java.
---
Usar `FormEditorExamples.createRadioButtonField(...)` para criar um campo de botão de opção com opções predefinidas.

## Criar um campo RadioButton

1. Vincule o PDF de origem ao `FormEditor` fachada.
2. Configure o espaçamento, a orientação e o tamanho dos itens do botão de opção.
3. Defina os itens do botão de opção.
4. Adicione o campo do botão de opção com sua seleção padrão e retângulo.
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
