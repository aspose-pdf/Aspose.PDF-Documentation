---
title: Divida o PDF em páginas únicas
linktitle: Divida o PDF em páginas únicas
type: docs
weight: 30
url: /java/split-pdf-into-single-pages/
description: Divida um PDF em arquivos de saída de página única em Java com a fachada PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Exporte cada página de um PDF para seu próprio arquivo com Java
Abstract: Aprenda como dividir um PDF em arquivos de página única com Aspose.PDF para Java. O exemplo Java usa PdfFileEditor para gravar cada página em um PDF de saída individual com base em um padrão de nome de arquivo.
---
## Divida o PDF em páginas únicas

Use este fluxo de trabalho quando cada página de origem precisar se tornar seu próprio arquivo PDF.

### Passos

1. Crie uma instância `PdfFileEditor`.
2. Prepare um padrão de arquivo de saída que inclua um espaço reservado de página como `%NUM%`.
3. Chame `splitToPages` com o arquivo de origem e o padrão de saída.
4. Salve os arquivos de página única gerados.

```java
public static void splitPdfIntoSinglePages(Path inputFile, Path outputFilePattern) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToPages(inputFile.toString(), outputFilePattern.toString());
}
```
