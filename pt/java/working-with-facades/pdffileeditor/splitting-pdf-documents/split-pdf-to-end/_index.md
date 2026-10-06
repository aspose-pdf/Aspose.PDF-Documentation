---
title: Dividir PDF até o Final
linktitle: Dividir PDF até o Final
type: docs
weight: 40
url: /pt/java/split-pdf-to-end/
description: Divida um PDF a partir de uma página escolhida até o final em Java com a fachada PdfFileEditor.
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extrair páginas de um ponto de início até o final de um PDF com Java
Abstract: Saiba como dividir um PDF até o final com Aspose.PDF for Java. O exemplo Java usa PdfFileEditor para extrair todas as páginas a partir da página 2 até o final do documento de origem.
---
## Dividir PDF até o final

O exemplo Java extrai todas as páginas a partir da página 2.

### Etapas

1. Criar um `PdfFileEditor` instância.
2. Chamar `splitToEnd` com o arquivo de origem, número da página inicial e arquivo de saída.
3. Salve o documento PDF resultante.

```java
public static void splitPdfToEnd(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToEnd(inputFile.toString(), 2, outputFile.toString());
}
```
