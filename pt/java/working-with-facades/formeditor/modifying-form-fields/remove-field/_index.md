---
title: Remover campo
linktitle: Remover campo
type: docs
weight: 40
url: /java/remove-field/
description: Aprenda como remover um campo de formulário existente de um documento PDF em Java usando a fachada FormEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Excluir um campo de formulário PDF em Java
Abstract: Este artigo mostra como vincular um PDF existente, remover um campo especificado e salvar o documento atualizado usando a fachada FormEditor em Aspose.PDF para Java.
---
## Remover um campo

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Chame `removeField(...)` para o nome do campo de destino.
3. Salve o documento atualizado.

```java
public static void removeField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeField("Country");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
