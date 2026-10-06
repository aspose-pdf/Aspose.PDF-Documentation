---
title: Excluir páginas de PDF
linktitle: Excluir páginas de PDF
type: docs
weight: 20
url: /pt/java/delete-pages-from-pdf/
description: Excluir páginas selecionadas de um PDF em Java com a fachada PdfFileEditor.
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remover páginas específicas de um documento PDF com Java
Abstract: Saiba como excluir páginas de um PDF com Aspose.PDF for Java. O exemplo em Java usa PdfFileEditor para remover um conjunto definido de números de página e salvar as páginas restantes como um novo documento.
---
## Excluir páginas de um PDF

O exemplo em Java remove as páginas 2 e 4 do documento original.

### Etapas

1. Crie uma instância de `PdfFileEditor`.
2. Crie um array com os números das páginas a serem removidas.
3. Chame `delete` com o arquivo de entrada, o array de páginas e o arquivo de saída.
4. Salve o PDF resultante.

### Exemplo Java

```java
public static void deletePagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.delete(inputFile.toString(), new int[] {2, 4}, outputFile.toString());
}
```
