---
title: Definir número de Comb de campo
linktitle: Definir número de Comb de campo
type: docs
weight: 60
url: /pt/java/set-field-comb-number/
description: Saiba como definir um número de comb para um campo de formulário PDF em Java usando a fachada FormEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Definir um número de comb para um campo de formulário PDF em Java
Abstract: Este artigo mostra como vincular um PDF existente, definir um número de comb para um campo e salvar o documento atualizado usando a fachada FormEditor no Aspose.PDF para Java.
---
## Definir um número de comb de campo

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Chame `setFieldCombNumber(...)` para o campo de destino e valor comb.
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
