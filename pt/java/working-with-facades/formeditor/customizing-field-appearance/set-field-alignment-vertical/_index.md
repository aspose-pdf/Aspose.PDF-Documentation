---
title: Definir alinhamento vertical do campo
linktitle: Definir alinhamento vertical do campo
type: docs
weight: 30
url: /pt/java/set-field-alignment-vertical/
description: Aprenda como definir o alinhamento vertical para um campo de formulário PDF em Java usando a fachada FormEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Definir alinhamento vertical para um campo de formulário PDF em Java
Abstract: Este artigo mostra como vincular um PDF existente, definir o alinhamento vertical do campo e salvar o documento atualizado usando a fachada FormEditor no Aspose.PDF for Java.
---
## Definir alinhamento vertical do campo

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Chame `setFieldAlignmentV(...)` para o campo alvo e a constante de alinhamento vertical desejada.
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
