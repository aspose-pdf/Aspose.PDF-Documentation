---
title: Extrair Páginas de PDF
linktitle: Extrair Páginas de PDF
type: docs
weight: 30
url: /pt/java/extract-pages-from-pdf/
description: Extrair páginas selecionadas de um PDF em Java com a fachada PdfFileEditor.
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extrair páginas PDF selecionadas em um novo documento com Java
Abstract: Aprenda como extrair páginas de um PDF com Aspose.PDF for Java. O exemplo em Java usa PdfFileEditor para coletar números de página específicos e gravá-los em um PDF de saída separado.
---
## Extrair páginas de um PDF

O exemplo em Java extrai as páginas 1, 4 e 3 em um novo documento PDF.

### Etapas

1. Criar um `PdfFileEditor` instância.
2. Defina os números das páginas a serem extraídas.
3. Ligar `extract` com o arquivo de origem, o array de páginas e o arquivo de saída.
4. Salve as páginas extraídas como um novo PDF.

### Exemplo Java

```java
public static void extractPagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.extract(inputFile.toString(), new int[] {1, 4, 3}, outputFile.toString());
}
```
