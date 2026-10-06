---
title: Definir alinhamento de campo
linktitle: Definir alinhamento de campo
type: docs
weight: 20
url: /pt/java/set-field-alignment/
description: Saiba como definir o alinhamento de texto horizontal para um campo de formulário PDF em Java usando a fachada FormEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Definir alinhamento de campo de formulário PDF em Java
Abstract: Este artigo mostra como vincular um PDF existente, definir o alinhamento horizontal do campo e salvar o documento atualizado usando a fachada FormEditor no Aspose.PDF for Java.
---
## Definir alinhamento horizontal do campo

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
