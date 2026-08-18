---
title: Redimensionar o conteúdo da página PDF
linktitle: Redimensionar o conteúdo da página PDF
type: docs
weight: 30
url: /java/resize-pdf-page-contents/
description: Redimensione o conteúdo de páginas PDF selecionadas em Java com a fachada PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Redimensione o conteúdo da página existente em um documento PDF com Java
Abstract: Aprenda como redimensionar o conteúdo da página com Aspose.PDF para Java. O exemplo Java usa PdfFileEditor para direcionar páginas específicas, aplicar uma nova largura e altura de conteúdo e interromper o fluxo de trabalho se a operação de redimensionamento falhar.
---
## Redimensionar o conteúdo da página PDF

A amostra Java redimensiona a área de conteúdo nas páginas 1 e 3 e verifica o valor de retorno booleano.

### Passos

1. Crie uma instância `PdfFileEditor`.
2. Escolha as páginas cujo conteúdo deve ser redimensionado.
3. Chame `resizeContents` com a largura e altura do alvo.
4. Verifique o valor de retorno e trate a falha antes de continuar.
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
