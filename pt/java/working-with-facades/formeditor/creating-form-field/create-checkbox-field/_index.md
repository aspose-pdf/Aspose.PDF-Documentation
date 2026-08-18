---
title: Criar campo CheckBox
linktitle: Criar campo CheckBox
type: docs
weight: 20
url: /java/create-checkbox-field/
description: Aprenda como adicionar um campo de formulário de caixa de seleção a um documento PDF em Java usando a fachada FormEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Crie um campo de caixa de seleção em um PDF com Java
Abstract: Este artigo mostra como vincular um PDF existente, adicionar um campo de caixa de seleção em uma posição especificada e salvar o documento modificado usando a fachada FormEditor em Aspose.PDF para Java.
---
Use `FormEditorExamples.createCheckBoxField(...)` para adicionar um campo de caixa de seleção a um formulário PDF.

## Crie um campo de caixa de seleção

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Adicione o campo da caixa de seleção com `FieldType.CheckBox`, o nome do campo, legenda, página e retângulo.
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
