---
title: Único para múltiplo
linktitle: Único para múltiplo
type: docs
weight: 60
url: /java/single-to-multiple/
description: Aprenda como converter um campo de texto de linha única em um campo de várias linhas em um documento PDF em Java usando a fachada FormEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Converta um campo PDF de linha única em multilinha em Java
Abstract: Este artigo mostra como vincular um PDF existente, converter um campo de linha única em um campo de várias linhas e salvar o documento atualizado usando a fachada FormEditor em Aspose.PDF para Java.
---
## Converter um campo de linha única em várias linhas

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Chame `single2Multiple(...)` para o nome do campo de destino.
3. Salve o documento atualizado.

```java
public static void singleToMultiple(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.single2Multiple("City");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
