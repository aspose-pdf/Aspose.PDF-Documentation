---
title: Obter deslocamento de página
linktitle: Obter deslocamento de página
type: docs
weight: 20
url: /java/get-page-offset/
description: Aprenda como inspecionar os deslocamentos das páginas X e Y em Java com a fachada PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtenha deslocamentos de página em PDF usando Java
Abstract: Aprenda como recuperar deslocamentos de página com Aspose.PDF para Java. O exemplo Java usa PdfFileInfo para ler os deslocamentos X e Y da página 1 e converte os valores dos pontos em polegadas para facilitar a análise do layout.
---
## Obter deslocamento de página

Use este fluxo de trabalho quando precisar entender como o conteúdo da página é posicionado em relação à origem do PDF.

### Passos

1. Crie um objeto `PdfFileInfo` para o PDF de entrada.
2. Chame `getPageXOffset` e `getPageYOffset` para a página de destino.
3. Converta os valores dos pontos em polegadas dividindo por `72.0`.
4. Use ou imprima os valores convertidos.
5. Feche a instância `PdfFileInfo`.

### Exemplo Java

```java
public static void getPageOffsets(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page X Offset: " + (pdfInfo.getPageXOffset(1) / 72.0) + " inches");
    System.out.println("Page Y Offset: " + (pdfInfo.getPageYOffset(1) / 72.0) + " inches");
    pdfInfo.close();
}
```
