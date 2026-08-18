---
title: Adicionar carimbo de borracha
linktitle: Adicionar carimbo de borracha
type: docs
weight: 10
url: /java/add-rubber-stamp/
description: Aprenda como adicionar uma anotação de carimbo a um documento PDF em Java usando a fachada PdfContentEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Adicione um carimbo a um PDF em Java
Abstract: Este artigo mostra como vincular um PDF, criar uma anotação de carimbo com texto e cor do rótulo e salvar o documento atualizado usando a fachada PdfContentEditor em Aspose.PDF para Java.
---
## Adicione um carimbo de borracha

1. Vincule o PDF de origem à fachada `PdfContentEditor`.
2. Chame `createRubberStamp(...)` com o número da página, retângulo, título, conteúdo e cor.
3. Salve o documento PDF atualizado.

```java
public static void addRubberStamp(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.createRubberStamp(1, new Rectangle(120, 450, 180, 60), "Approved", "Approved by reviewer", Color.GREEN);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
