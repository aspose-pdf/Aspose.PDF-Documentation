---
title: Redimensionar conteúdo da página PDF
linktitle: Redimensionar conteúdo da página PDF
type: docs
weight: 30
url: /pt/java/resize-pdf-page-contents/
description: Redimensionar conteúdo nas páginas PDF selecionadas em Java com a fachada PdfFileEditor.
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Redimensionar o conteúdo de páginas existentes em um documento PDF com Java
Abstract: Aprenda como redimensionar conteúdos de página com Aspose.PDF for Java. O exemplo em Java usa PdfFileEditor para direcionar páginas específicas, aplicar uma nova largura e altura de conteúdo e interromper o workflow se a operação de redimensionamento falhar.
---
## Redimensionar conteúdos da página PDF

O exemplo em Java redimensiona a área de conteúdo nas páginas 1 e 3 e verifica o valor booleano retornado.

### Etapas

1. Criar um `PdfFileEditor` instância.
2. Escolha as páginas cujo conteúdo deve ser redimensionado.
3. Chamar `resizeContents` com a largura e altura de destino.
4. Verifique o valor retornado e trate a falha antes de continuar.
5. Salve o documento atualizado.

### Exemplo Java

```java
public static void resizePdfPageContents(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    if (!pdfEditor.resizeContents(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 400, 750)) {
        throw new IllegalStateException("Failed to resize PDF page contents.");
    }
}
```
