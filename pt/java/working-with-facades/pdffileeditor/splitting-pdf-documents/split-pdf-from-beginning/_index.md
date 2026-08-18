---
title: Dividir PDF desde o início
linktitle: Dividir PDF desde o início
type: docs
weight: 10
url: /java/split-pdf-from-beginning/
description: Divida um PDF desde o início em Java com a fachada PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraia as primeiras páginas de um PDF em um novo documento com Java
Abstract: Aprenda como dividir um PDF desde o início com Aspose.PDF para Java. O exemplo Java usa PdfFileEditor para pegar as três primeiras páginas de um documento e salvá-las como um PDF separado.
---
## Dividir PDF desde o início

A amostra Java extrai as três primeiras páginas do documento de origem.

### Passos

1. Crie uma instância `PdfFileEditor`.
2. Chame `splitFromFirst` com o arquivo de origem, número de páginas a serem mantidas e arquivo de saída.
3. Salve o novo documento PDF.

```java
public static void splitPdfFromBeginning(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitFromFirst(inputFile.toString(), 3, outputFile.toString());
}
```
