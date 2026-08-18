---
title: Copiar campo interno
linktitle: Copiar campo interno
type: docs
weight: 70
url: /java/copy-inner-field/
description: Aprenda como copiar um campo de formulário para uma nova posição dentro do mesmo documento PDF em Java usando a fachada FormEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Copie um campo de formulário PDF dentro do mesmo documento em Java
Abstract: Este artigo mostra como vincular um PDF existente, duplicar um campo para outra página e posição e salvar o documento atualizado usando a fachada FormEditor em Aspose.PDF para Java.
---
## Copie um campo dentro do mesmo PDF

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Chame `copyInnerField(...)` com o nome do campo de origem, novo nome de campo, página e coordenadas.
3. Salve o documento atualizado.

```java
public static void copyInnerField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.copyInnerField("First Name", "First Name Copy", 2, 200, 600);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
