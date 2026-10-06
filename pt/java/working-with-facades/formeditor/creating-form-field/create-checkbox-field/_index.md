---
title: Criar Campo CheckBox
linktitle: Criar Campo CheckBox
type: docs
weight: 20
url: /pt/java/create-checkbox-field/
description: Saiba como adicionar um campo de formulário de caixa de seleção a um documento PDF em Java usando a fachada FormEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Criar um campo de checkbox em um PDF com Java
Abstract: Este artigo mostra como vincular um PDF existente, adicionar um campo de caixa de seleção em uma posição especificada e salvar o documento modificado usando a fachada FormEditor no Aspose.PDF for Java.
---
Usar `FormEditorExamples.createCheckBoxField(...)` para adicionar um campo de caixa de seleção a um formulário PDF.

## Criar um campo de caixa de seleção

1. Vincule o PDF de origem ao `FormEditor` fachada.
2. Adicionar o campo de caixa de seleção com `FieldType.CheckBox`, o nome do campo, legenda, página e retângulo.
3. Salve o documento atualizado.

```java
public static void createCheckBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.CheckBox, "checkbox1", "Check Box 1", 1, 240, 498, 256, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
