---
title: Definir aparência do campo
linktitle: Definir aparência do campo
type: docs
weight: 40
url: /pt/java/set-field-appearance/
description: Aprenda como alterar os indicadores de aparência visual de um campo de formulário PDF em Java usando a fachada FormEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Alterar indicadores de aparência de campo de formulário PDF em Java
Abstract: Este artigo mostra como vincular um PDF existente, aplicar um indicador de aparência a um campo e salvar o documento atualizado usando a fachada FormEditor no Aspose.PDF for Java.
---
## Definir indicadores de aparência do campo

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Chame `setFieldAppearance(...)` para o campo de destino e a bandeira de anotação escolhida.
3. Salve o documento atualizado.

```java
public static void setFieldAppearance(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAppearance("First Name", AnnotationFlags.Hidden);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
