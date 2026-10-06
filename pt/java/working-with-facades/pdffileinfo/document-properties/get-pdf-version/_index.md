---
title: Obter versão do PDF
linktitle: Obter versão do PDF
type: docs
weight: 20
url: /pt/java/get-pdf-version/
description: Saiba como recuperar a versão de um documento PDF em Java com a fachada PdfFileInfo.
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Recuperar versão do PDF usando Aspose.PDF for Java
Abstract: Saiba como recuperar a versão do PDF com Aspose.PDF for Java. O exemplo Java cria um objeto PdfFileInfo, lê a string de versão com `getPdfVersion()`, imprime o resultado e fecha o objeto de informação de arquivo.
---
## Obter versão do PDF

Use este fluxo de trabalho quando precisar verificar a compatibilidade do arquivo ou encaminhar um documento por meio de lógica de processamento específica por versão.

### Passos

1. Criar um `PdfFileInfo` objeto para o arquivo PDF.
2. Chamada `getPdfVersion()` para recuperar a versão relatada.
3. Use ou imprima o valor da versão.
4. Fechar o `PdfFileInfo` instância.

### Exemplo em Java

```java
public static void getPdfVersion(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println();
    System.out.println("PDF Version: " + pdfInfo.getPdfVersion());
    pdfInfo.close();
}
```
