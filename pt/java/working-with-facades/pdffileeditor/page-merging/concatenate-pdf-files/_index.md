---
title: Concatenar vários arquivos PDF
linktitle: Concatenar vários arquivos PDF
type: docs
weight: 20
url: /java/concatenate-pdf-files/
description: Mesclar arquivos PDF em Java com o fluxo de trabalho de concatenação PdfFileEditor baseado em array.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mesclar vários arquivos PDF em um documento com Java
Abstract: Aprenda como concatenar arquivos PDF com Aspose.PDF para Java. A amostra do repositório usa a sobrecarga `concatenate` baseada em array com duas entradas, e o mesmo fluxo de trabalho pode ser estendido para listas de arquivos mais longas porque o método aceita uma matriz de strings de caminhos de origem.
---
## Concatenar arquivos PDF

A amostra Java mescla dois arquivos, passando-os para a sobrecarga `concatenate` baseada em array.

### Passos

1. Crie uma instância `PdfFileEditor`.
2. Crie uma matriz de strings com os caminhos do PDF de entrada.
3. Chame `concatenate` com a matriz de entrada e o caminho do arquivo de saída.
4. Salve o documento mesclado.

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```

Para mesclar mais de dois arquivos, estenda a matriz de strings passada para `concatenate`.
