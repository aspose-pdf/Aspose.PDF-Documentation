---
title: Dividir PDF desde o início
linktitle: Dividir PDF desde o início
type: docs
weight: 10
url: /pt/java/split-pdf-from-beginning/
description: Divida um PDF desde o início em Java com a fachada PdfFileEditor.
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraia as primeiras páginas de um PDF para um novo documento com Java
Abstract: Saiba como dividir um PDF desde o início com Aspose.PDF for Java. O exemplo em Java usa PdfFileEditor para obter as três primeiras páginas de um documento e salvá‑las como um PDF separado.
---
## Dividir PDF desde o início

O exemplo em Java extrai as três primeiras páginas do documento de origem.

### Etapas

1. Criar um `PdfFileEditor` instância.
2. Chamar `splitFromFirst` com o arquivo fonte, número de páginas a manter e arquivo de saída.
3. Salve o novo documento PDF.

```java
public static void splitPdfFromBeginning(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitFromFirst(inputFile.toString(), 3, outputFile.toString());
}
```
