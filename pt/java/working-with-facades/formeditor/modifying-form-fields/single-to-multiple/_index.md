---
title: Único para Múltiplo
linktitle: Único para Múltiplo
type: docs
weight: 60
url: /pt/java/single-to-multiple/
description: Saiba como converter um campo de texto de linha única em um campo de múltiplas linhas em um documento PDF em Java usando a fachada FormEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Converter um campo PDF de linha única para múltiplas linhas em Java
Abstract: Este artigo mostra como vincular um PDF existente, converter um campo de linha única em um campo de múltiplas linhas e salvar o documento atualizado usando a fachada FormEditor no Aspose.PDF for Java.
---
## Converter um campo de linha única para múltiplas linhas

1. Vincular o PDF de origem ao `FormEditor` fachada.
2. Chamar `single2Multiple(...)` para o nome do campo de destino.
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
