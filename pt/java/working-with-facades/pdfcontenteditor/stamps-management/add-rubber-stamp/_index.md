---
title: Adicionar carimbo de Borracha
linktitle: Adicionar carimbo de Borracha
type: docs
weight: 10
url: /pt/java/add-rubber-stamp/
description: Aprenda como adicionar uma anotação de carimbo de borracha a um documento PDF em Java usando a fachada PdfContentEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Adicionar um carimbo de borracha a um PDF em Java
Abstract: Este artigo mostra como vincular um PDF, criar uma anotação de carimbo de borracha com texto de rótulo e cor, e salvar o documento atualizado usando a fachada PdfContentEditor no Aspose.PDF for Java.
---
## Adicionar um carimbo de borracha

1. Vincule o PDF de origem à fachada `PdfContentEditor`.
2. Chame `createRubberStamp(...)` com o número da página, retângulo, título, conteúdos e cor.
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
