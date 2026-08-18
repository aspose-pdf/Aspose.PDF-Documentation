---
title: Operações de imagem
linktitle: Operações de imagem
type: docs
weight: 50
url: /java/pdfcontenteditor-image-operations/
description: Aprenda a cobertura atual de operação de imagem Java disponível na fachada PdfContentEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Fluxos de trabalho de edição de imagens em Java com PdfContentEditor
Abstract: Esta seção aborda fluxos de trabalho relacionados a imagens atualmente suportados pelo conjunto de exemplos Java PdfContentEditor. O repositório inclui um exemplo direto para substituir uma imagem, enquanto os tópicos de exclusão de imagem não suportados são mantidos como notas de escopo explícitas.
---
A classe Java `PdfContentEditorExamples` atual suporta diretamente `replaceImage(...)`.

## Substituir uma imagem

1. Vincule o PDF de origem à fachada `PdfContentEditor`.
2. Chame `replaceImage(...)` com o número da página, o índice da imagem e o caminho da imagem de substituição.
3. Salve o documento PDF atualizado.

```java
public static void replaceImage(Path inputFile, Path imageFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.replaceImage(1, 1, imageFile.toString());
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
