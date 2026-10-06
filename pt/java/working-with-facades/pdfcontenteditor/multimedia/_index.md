---
title: Multimídia
linktitle: Multimídia
type: docs
weight: 70
url: /pt/java/pdfcontenteditor-multimedia/
description: Aprenda a cobertura multimídia atual disponível na fachada Java PdfContentEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Fluxos de trabalho de anotação multimídia em Java com PdfContentEditor
Abstract: Esta seção cobre fluxos de trabalho relacionados a multimídia atualmente suportados pelo conjunto de exemplos Java PdfContentEditor. O repositório inclui um exemplo direto de anotação de filme, enquanto tópicos de som não suportados são mantidos como notas de escopo explícitas.
---
O Java atual `PdfContentEditorExamples` classe suporta diretamente `addMovieAnnotation(...)`.

## Adicionar uma anotação de filme

1. Vincule o PDF de origem à fachada `PdfContentEditor`.
2. Chame `createMovie(...)` com o retângulo de anotação, o caminho do arquivo de filme e o número da página.
3. Salve o documento PDF atualizado.

```java
public static void addMovieAnnotation(Path inputFile, Path movieFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.createMovie(new Rectangle(80, 500, 220, 120), movieFile.toString(), 1);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
