---
title: Remover ação de campo
linktitle: Remover ação de campo
type: docs
weight: 50
url: /java/remove-field-action/
description: Aprenda como remover uma ação de campo de um campo de formulário PDF em Java usando a fachada FormEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Remover uma ação de campo de formulário PDF em Java
Abstract: Este artigo mostra como vincular um PDF existente, remover a ação associada a um campo específico e salvar o documento atualizado usando a fachada FormEditor em Aspose.PDF para Java.
---
## Remover uma ação de campo

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Chame `removeFieldAction(...)` para o campo de destino.
3. Salve o documento atualizado.

```java
public static void removeFieldAction(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeFieldAction("Script_Demo_Button");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
