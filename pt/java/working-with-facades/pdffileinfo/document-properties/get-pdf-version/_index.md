---
title: Obtenha a versão em PDF
linktitle: Obtenha a versão em PDF
type: docs
weight: 20
url: /java/get-pdf-version/
description: Aprenda como recuperar a versão de um documento PDF em Java com a fachada PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Recuperar a versão em PDF usando Aspose.PDF para Java
Abstract: Aprenda como recuperar a versão PDF com Aspose.PDF para Java. O exemplo Java cria um objeto PdfFileInfo, lê a string da versão com `getPdfVersion()`, imprime o resultado e fecha o objeto de informações do arquivo.
---
## Obtenha a versão em PDF

Use esse fluxo de trabalho quando precisar verificar a compatibilidade de arquivos ou rotear um documento por meio de lógica de processamento específica de versão.

### Passos

1. Crie um objeto `PdfFileInfo` para o arquivo PDF.
2. Ligue para `getPdfVersion()` para recuperar a versão relatada.
3. Use ou imprima o valor da versão.
4. Feche a instância `PdfFileInfo`.

### Exemplo Java

```java
public static void getPdfVersion(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println();
    System.out.println("PDF Version: " + pdfInfo.getPdfVersion());
    pdfInfo.close();
}
```
