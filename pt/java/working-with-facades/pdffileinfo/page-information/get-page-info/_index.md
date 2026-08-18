---
title: Obtenha informações da página
linktitle: Obtenha informações da página
type: docs
weight: 10
url: /java/get-page-info/
description: Aprenda como inspecionar a largura, altura e rotação da página em Java com a fachada PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtenha informações da página PDF usando Aspose.PDF para Java
Abstract: Aprenda como recuperar informações da página com Aspose.PDF para Java. O exemplo Java usa PdfFileInfo para ler a largura, a altura e a rotação da página 1 para que você possa inspecionar seu layout antes do processamento adicional.
---
## Obtenha informações da página

Este exemplo lê as principais propriedades geométricas da página 1.

### Passos

1. Crie um objeto `PdfFileInfo` para o PDF de origem.
2. Chame `getPageWidth`, `getPageHeight` e `getPageRotation` para a página que deseja inspecionar.
3. Use ou imprima os valores retornados.
4. Feche a instância `PdfFileInfo`.

### Exemplo Java

```java
public static void getPageInformation(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page Width: " + pdfInfo.getPageWidth(1));
    System.out.println("Page Height: " + pdfInfo.getPageHeight(1));
    System.out.println("Page Rotation: " + pdfInfo.getPageRotation(1));
    pdfInfo.close();
}
```
