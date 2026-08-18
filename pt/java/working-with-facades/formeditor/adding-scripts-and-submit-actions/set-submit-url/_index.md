---
title: Definir URL de envio
linktitle: Definir URL de envio
type: docs
weight: 30
url: /java/set-submit-url/
description: Aprenda como definir um URL de envio para um botão de formulário PDF em Java usando a fachada FormEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Configure um URL de envio de formulário PDF em Java
Abstract: Este artigo mostra como vincular um PDF existente, definir um URL de envio e um sinalizador de envio para um campo de botão e salvar o documento atualizado usando a fachada FormEditor em Aspose.PDF para Java.
---
## Defina um URL de envio

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Chame `setSubmitUrl(...)` para o campo do botão.
3. Aplique o sinalizador de envio para o formato de envio.
4. Salve o documento atualizado.

```java
public static void setSubmitUrl(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
        editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
