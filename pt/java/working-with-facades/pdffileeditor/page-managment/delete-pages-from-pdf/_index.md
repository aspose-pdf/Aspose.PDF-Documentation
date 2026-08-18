---
title: Excluir páginas do PDF
linktitle: Excluir páginas do PDF
type: docs
weight: 20
url: /java/delete-pages-from-pdf/
description: Exclua páginas selecionadas de um PDF em Java com a fachada PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remova páginas específicas de um documento PDF com Java
Abstract: Aprenda como excluir páginas de um PDF com Aspose.PDF para Java. O exemplo Java usa PdfFileEditor para remover um conjunto definido de números de página e salvar as páginas restantes como um novo documento.
---
## Excluir páginas de um PDF

A amostra Java remove as páginas 2 e 4 do documento de origem.

### Passos

1. Crie uma instância `PdfFileEditor`.
2. Construa uma matriz com os números das páginas a serem removidas.
3. Chame `delete` com o arquivo de entrada, matriz de páginas e arquivo de saída.
4. Salve o PDF resultante.

### Exemplo Java

```java
public static void deletePagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.delete(inputFile.toString(), new int[] {2, 4}, outputFile.toString());
}
```
