---
title: Mover campo
linktitle: Mover campo
type: docs
weight: 30
url: /java/move-field/
description: Aprenda como mover um campo de formulário existente em um documento PDF em Java usando a fachada FormEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Mova um campo de formulário PDF para uma nova posição em Java
Abstract: Este artigo mostra como vincular um PDF existente, mover um campo para novas coordenadas e salvar o documento atualizado usando a fachada FormEditor em Aspose.PDF para Java.
---
## Mover um campo

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Chame `moveField(...)` com o nome do campo de destino e as novas coordenadas do retângulo.
3. Salve o documento atualizado.

```java
public static void moveField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.moveField("Country", 200, 600, 280, 620);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
