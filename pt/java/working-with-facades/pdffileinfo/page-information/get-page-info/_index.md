---
title: Obter informações da página
linktitle: Obter informações da página
type: docs
weight: 10
url: /pt/java/get-page-info/
description: Aprenda como inspecionar a largura, altura e rotação da página em Java com a fachada PdfFileInfo.
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obter informações da página PDF usando Aspose.PDF for Java
Abstract: Aprenda como recuperar informações da página com Aspose.PDF for Java. O exemplo em Java usa PdfFileInfo para ler a largura, altura e rotação da página 1, para que você possa inspecionar seu layout antes de prosseguir com o processamento.
---
## Obter informações da página

Este exemplo lê as principais propriedades geométricas da página 1.

### Etapas

1. Criar um `PdfFileInfo` objeto para o PDF de origem.
2. Chamada `getPageWidth`, `getPageHeight`, e `getPageRotation` para a página que você deseja inspecionar.
3. Use ou imprima os valores retornados.
4. Fechar o `PdfFileInfo` instância.

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
