---
title: Operações de imagem
linktitle: Operações de imagem
type: docs
weight: 50
url: /pt/java/pdfcontenteditor-image-operations/
description: Conheça a cobertura atual de operações de imagem em Java disponível na fachada PdfContentEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Fluxos de trabalho de edição de imagem em Java com PdfContentEditor
Abstract: Esta seção cobre fluxos de trabalho relacionados a imagens atualmente suportados pelo conjunto de exemplos Java PdfContentEditor. O repositório inclui um exemplo direto para substituir uma imagem, enquanto tópicos de exclusão de imagens não suportados são mantidos como notas de escopo explícitas.
---
O Java atual `PdfContentEditorExamples` classe suporta diretamente `replaceImage(...)`.

## Substituir uma imagem

1. Vincule o PDF de origem à fachada `PdfContentEditor`.
2. Chame `replaceImage(...)` com o número da página, índice da imagem e caminho da imagem de substituição.
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
