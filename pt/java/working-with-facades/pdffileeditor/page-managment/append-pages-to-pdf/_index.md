---
title: Anexar páginas ao PDF
linktitle: Anexar páginas ao PDF
type: docs
weight: 10
url: /pt/java/append-pages-to-pdf/
description: Anexar páginas de um PDF a outro em Java com a fachada PdfFileEditor.
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Anexar um intervalo de páginas de um documento PDF a outro com Java
Abstract: Aprenda como anexar páginas a um PDF com Aspose.PDF for Java. O exemplo em Java usa PdfFileEditor para anexar um intervalo de páginas selecionado de outro documento ao final do PDF atual.
---
## Anexar páginas a um PDF

O exemplo em Java anexa a página 1 de um segundo PDF ao final do primeiro documento.

### Passos

1. Criar um `PdfFileEditor` instância.
2. Vincule o PDF de entrada principal passando seu caminho para `append`.
3. Forneça a lista de arquivos fonte secundários e o intervalo de páginas a anexar.
4. Salve o resultado mesclado no arquivo de saída.

### Exemplo Java

```java
public static void appendPagesToPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.append(inputFile.toString(), new String[] {sampleFile.toString()}, 1, 1, outputFile.toString());
}
```
