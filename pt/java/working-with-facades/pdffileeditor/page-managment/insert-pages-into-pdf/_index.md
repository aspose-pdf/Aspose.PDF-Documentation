---
title: Inserir páginas no PDF
linktitle: Inserir páginas no PDF
type: docs
weight: 40
url: /pt/java/insert-pages-into-pdf/
description: Inserir páginas selecionadas de um PDF em outro em Java com a fachada PdfFileEditor.
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inserir páginas de outro PDF em uma posição escolhida com Java
Abstract: Saiba como inserir páginas em um PDF com Aspose.PDF for Java. O exemplo em Java usa PdfFileEditor para inserir páginas selecionadas de um segundo documento após um número de página especificado no PDF de destino.
---
## Inserir páginas em um PDF

O exemplo Java insere as páginas 1 e 2 do documento secundário após a página 2 do PDF de destino.

### Etapas

1. Criar um `PdfFileEditor` instância.
2. Escolha o ponto de inserção no documento de destino.
3. Selecione os números de página a copiar do documento de origem.
4. Chamada `insert` com o arquivo de destino, ponto de inserção, arquivo de origem, matriz de páginas e arquivo de saída.
5. Salve o PDF atualizado.

### Exemplo Java

```java
public static void insertPagesIntoPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.insert(inputFile.toString(), 2, sampleFile.toString(), new int[] {1, 2}, outputFile.toString());
}
```
