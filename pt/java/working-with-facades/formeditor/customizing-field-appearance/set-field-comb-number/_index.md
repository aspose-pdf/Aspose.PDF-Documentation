---
title: Definir número de pente de campo
linktitle: Definir número de pente de campo
type: docs
weight: 60
url: /java/set-field-comb-number/
description: Aprenda como definir um número de pente para um campo de formulário PDF em Java usando a fachada FormEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Defina um número de pente para um campo de formulário PDF em Java
Abstract: Este artigo mostra como vincular um PDF existente, definir um número de pente para um campo e salvar o documento atualizado usando a fachada FormEditor em Aspose.PDF para Java.
---
## Definir um número de combinação de campo

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Chame `setFieldCombNumber(...)` para o campo de destino e o valor do pente.
3. Salve o documento atualizado.

```java
public static void setFieldCombNumber(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldCombNumber("textCombField", 5);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
