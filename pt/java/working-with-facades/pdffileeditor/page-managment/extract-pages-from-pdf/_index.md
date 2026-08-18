---
title: Extraia páginas de PDF
linktitle: Extraia páginas de PDF
type: docs
weight: 30
url: /java/extract-pages-from-pdf/
description: Extraia páginas selecionadas de um PDF em Java com a fachada PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraia páginas PDF selecionadas em um novo documento com Java
Abstract: Aprenda como extrair páginas de um PDF com Aspose.PDF para Java. O exemplo Java usa PdfFileEditor para coletar números de páginas específicos e gravá-los em um PDF de saída separado.
---
## Extraia páginas de um PDF

A amostra Java extrai as páginas 1, 4 e 3 em um novo documento PDF.

### Passos

1. Crie uma instância `PdfFileEditor`.
2. Defina os números das páginas a serem extraídas.
3. Chame `extract` com o arquivo de origem, matriz de páginas e arquivo de saída.
4. Salve as páginas extraídas como um novo PDF.

### Exemplo Java

```java
public static void extractPagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.extract(inputFile.toString(), new int[] {1, 4, 3}, outputFile.toString());
}
```
