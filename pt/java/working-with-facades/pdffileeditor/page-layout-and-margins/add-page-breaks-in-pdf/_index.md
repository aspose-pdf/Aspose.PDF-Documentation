---
title: Adicionar Quebras de Página em PDF
linktitle: Adicionar Quebras de Página em PDF
type: docs
weight: 20
url: /pt/java/add-page-breaks-in-pdf/
description: Inserir quebras de página em um PDF em Java usando a fachada PdfFileEditor.
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inserir quebras de página em posições fixas em um documento PDF com Java
Abstract: Aprenda como adicionar quebras de página com Aspose.PDF for Java. O exemplo Java usa PdfFileEditor.PageBreak para dividir uma página em uma posição vertical específica e salvar o resultado como um novo PDF.
---
## Adicionar quebras de página em um PDF

Use este fluxo de trabalho quando uma página precisar ser dividida em várias páginas em uma posição Y conhecida.

### Etapas

1. Criar um `PdfFileEditor` instância.
2. Crie um ou mais `PdfFileEditor.PageBreak` entradas com o número da página e a posição de quebra.
3. Passe o array de quebras de página para `addPageBreak`.
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
