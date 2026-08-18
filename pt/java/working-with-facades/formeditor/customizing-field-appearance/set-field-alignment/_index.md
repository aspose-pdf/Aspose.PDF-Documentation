---
title: Definir alinhamento de campo
linktitle: Definir alinhamento de campo
type: docs
weight: 20
url: /java/set-field-alignment/
description: Aprenda como definir o alinhamento horizontal do texto para um campo de formulário PDF em Java usando a fachada FormEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Definir o alinhamento dos campos do formulário PDF em Java
Abstract: Este artigo mostra como vincular um PDF existente, definir o alinhamento horizontal dos campos e salvar o documento atualizado usando a fachada FormEditor em Aspose.PDF para Java.
---
## Definir alinhamento de campo horizontal

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Chame `setFieldAlignment(...)` para o campo de destino e a constante de alinhamento desejada.
3. Salve o documento atualizado.

```java
public static void setFieldAlignment(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAlignment("First Name", FormFieldFacade.ALIGN_CENTER);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
