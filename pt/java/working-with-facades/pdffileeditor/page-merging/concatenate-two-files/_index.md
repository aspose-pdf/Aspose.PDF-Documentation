---
title: Concatenar dois arquivos PDF
linktitle: Concatenar dois arquivos PDF
type: docs
weight: 60
url: /java/concatenate-two-files/
description: Mesclar dois arquivos PDF em um documento em Java com a fachada PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Concatene dois arquivos PDF em um único documento de saída com Java
Abstract: Aprenda como concatenar dois arquivos PDF com Aspose.PDF para Java. O exemplo Java usa PdfFileEditor e a sobrecarga `concatenate` baseada em array para combinar dois documentos de origem em um PDF de saída.
---
## Concatenar dois arquivos PDF

Este artigo mapeia diretamente para o exemplo `mergePdfDocuments` em `PdfFileEditorExamples.java`.

### Passos

1. Crie uma instância `PdfFileEditor`.
2. Passe os dois caminhos do arquivo de entrada como uma matriz de strings.
3. Chame `concatenate` com o array e o caminho do arquivo de saída.
4. Salve o PDF mesclado.

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```
