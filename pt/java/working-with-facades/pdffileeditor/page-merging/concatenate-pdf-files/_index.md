---
title: Concatenar vários arquivos PDF
linktitle: Concatenar vários arquivos PDF
type: docs
weight: 20
url: /pt/java/concatenate-pdf-files/
description: Mesclar arquivos PDF em Java com o fluxo de trabalho concatenate baseado em array do PdfFileEditor.
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mesclar vários arquivos PDF em um único documento com Java
Abstract: Saiba como concatenar arquivos PDF com Aspose.PDF for Java. O exemplo do repositório usa a sobrecarga baseada em array `concatenate` com duas entradas, e o mesmo fluxo de trabalho pode ser estendido para listas de arquivos maiores porque o método aceita um array de strings com os caminhos de origem.
---
## Concatenar arquivos PDF

O exemplo Java mescla dois arquivos passando-os para o baseado em array `concatenate` sobrecarga.

### Passos

1. Criar um `PdfFileEditor` instância.
2. Construir um array de strings com os caminhos dos PDFs de entrada.
3. Chamada `concatenate` com a matriz de entrada e o caminho do arquivo de saída.
4. Salvar o documento mesclado.

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```

Para mesclar mais de dois arquivos, amplie o array de strings passado para `concatenate`.
