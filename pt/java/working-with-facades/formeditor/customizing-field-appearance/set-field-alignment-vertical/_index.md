---
title: Definir alinhamento de campo vertical
linktitle: Definir alinhamento de campo vertical
type: docs
weight: 30
url: /java/set-field-alignment-vertical/
description: Aprenda como definir o alinhamento vertical para um campo de formulário PDF em Java usando a fachada FormEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Defina o alinhamento vertical para um campo de formulário PDF em Java
Abstract: Este artigo mostra como vincular um PDF existente, definir o alinhamento vertical dos campos e salvar o documento atualizado usando a fachada FormEditor em Aspose.PDF para Java.
---
## Definir alinhamento vertical do campo

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Chame `setFieldAlignmentV(...)` para o campo de destino e a constante de alinhamento vertical desejada.
3. Salve o documento atualizado.

```java
public static void setFieldAlignmentVertical(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAlignmentV("First Name", FormFieldFacade.ALIGN_BOTTOM);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
