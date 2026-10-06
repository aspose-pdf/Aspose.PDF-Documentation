---
title: Definir Limite de Campo
linktitle: Definir Limite de Campo
type: docs
weight: 50
url: /pt/java/set-field-limit/
description: Saiba como definir um limite máximo de caracteres para um campo de formulário PDF em Java usando a fachada FormEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Definir um limite de caracteres para um campo de formulário PDF em Java
Abstract: Este artigo mostra como vincular um PDF existente, definir o limite máximo de caracteres de um campo e salvar o documento atualizado usando a fachada FormEditor no Aspose.PDF para Java.
---
## Definir um limite de caracteres de campo

1. Vincule o PDF de origem ao `FormEditor` fachada.
2. Chamar `setFieldLimit(...)` para o campo de destino e contagem máxima de caracteres.
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
