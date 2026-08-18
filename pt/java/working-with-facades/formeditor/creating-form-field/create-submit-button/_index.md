---
title: Criar botão Enviar
linktitle: Criar botão Enviar
type: docs
weight: 60
url: /java/create-submit-button/
description: Aprenda como adicionar um botão de envio a um documento PDF em Java usando a fachada FormEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Crie um botão de envio de PDF em Java
Abstract: Este artigo mostra como vincular um PDF existente, adicionar um campo de botão de envio com um URL de destino e salvar o documento modificado usando a fachada FormEditor em Aspose.PDF para Java.
---
Use `FormEditorExamples.createSubmitButton(...)` para criar um botão que envia dados do formulário.

## Crie um botão de envio

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Chame `addSubmitBtn(...)` com o nome do botão, página, rótulo, URL de destino e retângulo.
3. Salve o documento atualizado.

```java
public static void createSubmitButton(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addSubmitBtn("submitbutton", 1, "Submit", "http://localhost/testing/show", 100, 450, 150, 475);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
