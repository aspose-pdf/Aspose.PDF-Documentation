---
title: Limpar Metadados PDF
linktitle: Limpar Metadados PDF
type: docs
weight: 10
url: /pt/java/clear-pdf-metadata/
description: Aprenda como limpar metadados PDF em Java com a fachada PdfFileInfo.
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Limpando Metadados PDF Usando Aspose.PDF for Java
Abstract: Aprenda como limpar metadados PDF com Aspose.PDF for Java. O exemplo em Java usa PdfFileInfo para remover informações armazenadas do documento com `clearInfo()` e, em seguida, salva o PDF limpo em um novo arquivo.
---
## Limpar Metadados PDF

Use este fluxo de trabalho quando precisar remover informações armazenadas do documento antes de compartilhar ou arquivar um PDF.

### Passos

1. Criar um `PdfFileInfo` objeto para o PDF de entrada.
2. Chamar `clearInfo()` para remover os metadados do documento.
3. Salve o resultado em um novo arquivo com `save()`.
4. Fechar o `PdfFileInfo` instância.

### Exemplo em Java

```java
public static void clearPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.clearInfo();
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
