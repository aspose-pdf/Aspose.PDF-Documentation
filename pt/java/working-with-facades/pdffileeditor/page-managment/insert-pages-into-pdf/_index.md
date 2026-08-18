---
title: Inserir páginas em PDF
linktitle: Inserir páginas em PDF
type: docs
weight: 40
url: /java/insert-pages-into-pdf/
description: Insira páginas selecionadas de um PDF em outro em Java com a fachada PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Insira páginas de outro PDF na posição escolhida com Java
Abstract: Aprenda como inserir páginas em um PDF com Aspose.PDF para Java. O exemplo Java usa PdfFileEditor para inserir páginas selecionadas de um segundo documento após um determinado número de página no PDF de destino.
---
## Inserir páginas em um PDF

A amostra Java insere as páginas 1 e 2 do documento secundário após a página 2 do PDF de destino.

### Passos

1. Crie uma instância `PdfFileEditor`.
2. Escolha o ponto de inserção no documento de destino.
3. Selecione os números de página a serem copiados do documento de origem.
4. Chame `insert` com o arquivo de destino, ponto de inserção, arquivo de origem, matriz de páginas e arquivo de saída.
5. Salve o PDF atualizado.

### Exemplo Java

```java
public static void insertPagesIntoPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.insert(inputFile.toString(), 2, sampleFile.toString(), new int[] {1, 2}, outputFile.toString());
}
```
