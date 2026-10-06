---
title: Obter deslocamento da página
linktitle: Obter deslocamento da página
type: docs
weight: 20
url: /pt/java/get-page-offset/
description: Aprenda como inspecionar os offsets X e Y da página em Java com a fachada PdfFileInfo.
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obter offsets de página PDF usando Java
Abstract: Aprenda como recuperar os offsets de página com Aspose.PDF for Java. O exemplo em Java usa PdfFileInfo para ler os offsets X e Y da página 1 e converte os valores em pontos para polegadas, facilitando a análise de layout.
---
## Obter deslocamento da página

Use este fluxo de trabalho quando precisar entender como o conteúdo da página está posicionado em relação à origem do PDF.

### Etapas

1. Criar um `PdfFileInfo` objeto para o PDF de entrada.
2. Chamar `getPageXOffset` e `getPageYOffset` para a página de destino.
3. Converta os valores em pontos para polegadas dividindo por `72.0`.
4. Use ou imprima os valores convertidos.
5. Fechar o `PdfFileInfo` instância.

### Exemplo Java

```java
public static void getPageOffsets(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page X Offset: " + (pdfInfo.getPageXOffset(1) / 72.0) + " inches");
    System.out.println("Page Y Offset: " + (pdfInfo.getPageYOffset(1) / 72.0) + " inches");
    pdfInfo.close();
}
```
