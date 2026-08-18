---
title: Criar campo TextBox
linktitle: Criar campo TextBox
type: docs
weight: 10
url: /java/create-textbox-field/
description: Aprenda como adicionar campos de caixa de texto a um documento PDF em Java usando a fachada FormEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Crie campos de formulário de texto em um PDF com Java
Abstract: Este artigo mostra como vincular um PDF existente, adicionar campos de texto com valores padrão e salvar o documento modificado usando a fachada FormEditor em Aspose.PDF para Java.
---
Use `FormEditorExamples.createTextBoxField(...)` para adicionar campos de texto a um formulário PDF.

## Crie campos de caixa de texto

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Adicione cada campo de texto com `FieldType.Text`, o nome do campo, o valor padrão, o número da página e o retângulo.
3. Salve o documento atualizado.

```java
public static void createTextBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.Text, "first_name", "Alexander", 1, 50, 570, 150, 590);
        editor.addField(FieldType.Text, "last_name", "Smith", 1, 235, 570, 330, 590);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
