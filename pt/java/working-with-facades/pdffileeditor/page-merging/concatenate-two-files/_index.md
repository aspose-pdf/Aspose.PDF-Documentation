---
title: Concatenar Dois Arquivos PDF
linktitle: Concatenar Dois Arquivos PDF
type: docs
weight: 60
url: /pt/java/concatenate-two-files/
description: Mesclar dois arquivos PDF em um único documento em Java com a fachada PdfFileEditor.
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Concatenar dois arquivos PDF em um único documento de saída com Java
Abstract: Aprenda como concatenar dois arquivos PDF com Aspose.PDF for Java. O exemplo em Java usa PdfFileEditor e a sobrecarga baseada em array `concatenate` para combinar dois documentos de origem em um único PDF de saída.
---
## Concatenar dois arquivos PDF

Este artigo corresponde diretamente ao `mergePdfDocuments` exemplo em `PdfFileEditorExamples.java`.

### Etapas

1. Criar um `PdfFileEditor` instância.
2. Passe os dois caminhos de arquivo de entrada como um array de strings.
3. Chamada `concatenate` com o array e o caminho do arquivo de saída.
4. Salve o PDF mesclado.

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```
