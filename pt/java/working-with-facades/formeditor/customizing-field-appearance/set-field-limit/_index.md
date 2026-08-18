---
title: Definir limite de campo
linktitle: Definir limite de campo
type: docs
weight: 50
url: /java/set-field-limit/
description: Aprenda como definir um limite máximo de caracteres para um campo de formulário PDF em Java usando a fachada FormEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Defina um limite de caracteres para um campo de formulário PDF em Java
Abstract: Este artigo mostra como vincular um PDF existente, definir o limite máximo de caracteres de um campo e salvar o documento atualizado usando a fachada FormEditor em Aspose.PDF para Java.
---
## Definir um limite de caracteres de campo

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Chame `setFieldLimit(...)` para o campo de destino e a contagem máxima de caracteres.
3. Salve o documento atualizado.

```java
public static void setFieldLimit(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldLimit("First Name", 15);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
