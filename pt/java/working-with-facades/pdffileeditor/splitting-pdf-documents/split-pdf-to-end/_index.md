---
title: Dividir PDF até o final
linktitle: Dividir PDF até o final
type: docs
weight: 40
url: /java/split-pdf-to-end/
description: Divida um PDF de uma página escolhida até o final em Java com a fachada PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraia páginas do ponto inicial ao final de um PDF com Java
Abstract: Aprenda como dividir um PDF até o fim com Aspose.PDF para Java. O exemplo Java usa PdfFileEditor para extrair todas as páginas desde a página 2 até o final do documento de origem.
---
## Dividir PDF até o final

A amostra Java extrai todas as páginas começando na página 2.

### Passos

1. Crie uma instância `PdfFileEditor`.
2. Chame `splitToEnd` com o arquivo de origem, número da página inicial e arquivo de saída.
3. Salve o documento PDF resultante.

```java
public static void splitPdfToEnd(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToEnd(inputFile.toString(), 2, outputFile.toString());
}
```
