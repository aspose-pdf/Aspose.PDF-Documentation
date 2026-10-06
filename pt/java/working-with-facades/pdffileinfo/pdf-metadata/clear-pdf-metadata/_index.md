---
title: Limpar metadados PDF
linktitle: Limpar metadados PDF
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
AlternativeHeadline: Limpando metadados PDF usando Aspose.PDF for Java
Abstract: Aprenda como limpar metadados PDF com Aspose.PDF for Java. O exemplo em Java usa PdfFileInfo para remover informações armazenadas do documento com `clearInfo()` e, em seguida, salva o PDF limpo em um novo arquivo.
---
## Limpar metadados PDF

Use este fluxo de trabalho quando precisar remover informações armazenadas do documento antes de compartilhar ou arquivar um PDF.

### Etapas

1. Crie um objeto `PdfFileInfo` para o PDF de entrada.
2. Chame `clearInfo()` para remover os metadados do documento.
3. Salve o resultado em um novo arquivo com `save()`.
4. Feche o `PdfFileInfo` instância.

### Exemplo em Java

```java
public static void clearPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.clearInfo();
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
