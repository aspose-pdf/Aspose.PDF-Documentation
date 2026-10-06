---
title: Definir URL de Envio
linktitle: Definir URL de Envio
type: docs
weight: 30
url: /pt/java/set-submit-url/
description: Saiba como definir uma URL de envio para um botão de formulário PDF em Java usando a fachada FormEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Configure a URL de envio de um formulário PDF em Java
Abstract: Este artigo mostra como vincular um PDF existente, definir uma URL de envio e a bandeira de envio para um campo de botão, e salvar o documento atualizado usando a fachada FormEditor no Aspose.PDF for Java.
---
## Definir uma URL de envio

1. Vincule o PDF de origem ao `FormEditor` fachada.
2. Chamar `setSubmitUrl(...)` para o campo de botão.
3. Aplique o sinalizador de envio para o formato de submissão.
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
