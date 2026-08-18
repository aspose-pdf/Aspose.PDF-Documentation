---
title: Renomear campo
linktitle: Renomear campo
type: docs
weight: 50
url: /java/rename-field/
description: Aprenda como renomear um campo de formulário existente em um documento PDF em Java usando a fachada FormEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Renomear um campo de formulário PDF em Java
Abstract: Este artigo mostra como vincular um PDF existente, renomear um campo especificado e salvar o documento atualizado usando a fachada FormEditor em Aspose.PDF para Java.
---
## Renomear um campo

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Chame `renameField(...)` com o nome do campo atual e o novo nome do campo.
3. Salve o documento atualizado.

```java
public static void renameField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.renameField("City", "Town");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
