---
title: Adicionar quebras de página em PDF
linktitle: Adicionar quebras de página em PDF
type: docs
weight: 20
url: /java/add-page-breaks-in-pdf/
description: Insira quebras de página em um PDF em Java com a fachada PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Insira quebras de página em posições fixas em um documento PDF com Java
Abstract: Aprenda como adicionar quebras de página com Aspose.PDF para Java. O exemplo Java usa PdfFileEditor.PageBreak para dividir uma página em uma posição vertical específica e salvar o resultado como um novo PDF.
---
## Adicione quebras de página em um PDF

Use este fluxo de trabalho quando uma página precisar ser dividida em várias páginas em uma posição Y conhecida.

### Passos

1. Crie uma instância `PdfFileEditor`.
2. Crie uma ou mais entradas `PdfFileEditor.PageBreak` com o número da página e a posição de quebra.
3. Passe a matriz de quebra de página para `addPageBreak`.
4. Salve o documento PDF atualizado.

### Exemplo Java

```java
public static void addPageBreaksInPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addPageBreak(inputFile.toString(), outputFile.toString(), new PdfFileEditor.PageBreak[] {
            new PdfFileEditor.PageBreak(1, 400)
    });
}
```
