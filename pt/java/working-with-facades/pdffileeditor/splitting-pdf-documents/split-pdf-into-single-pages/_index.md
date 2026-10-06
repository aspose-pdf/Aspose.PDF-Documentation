---
title: Dividir PDF em páginas Únicas
linktitle: Dividir PDF em páginas Únicas
type: docs
weight: 30
url: /pt/java/split-pdf-into-single-pages/
description: Divida um PDF em arquivos de saída de página única em Java com a fachada PdfFileEditor.
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Exportar cada página de um PDF para seu próprio arquivo com Java
Abstract: Saiba como dividir um PDF em arquivos de página única com Aspose.PDF for Java. O exemplo em Java usa PdfFileEditor para gravar cada página em um PDF de saída individual com base em um padrão de nome de arquivo.
---
## Dividir PDF em páginas individuais

Use este fluxo de trabalho quando cada página de origem precisar se tornar seu próprio arquivo PDF.

### Etapas

1. Crie uma instância de `PdfFileEditor`.
2. Prepare um padrão de arquivo de saída que inclua um marcador de página como `%NUM%`.
3. Chame `splitToPages` com o arquivo de origem e o padrão de saída.
4. Salve os arquivos de página única gerados.

```java
public static void splitPdfIntoSinglePages(Path inputFile, Path outputFilePattern) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToPages(inputFile.toString(), outputFilePattern.toString());
}
```
