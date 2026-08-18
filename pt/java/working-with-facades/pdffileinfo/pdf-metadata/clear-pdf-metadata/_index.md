---
title: Limpar metadados de PDF
linktitle: Limpar metadados de PDF
type: docs
weight: 10
url: /java/clear-pdf-metadata/
description: Aprenda como limpar metadados de PDF em Java com a fachada PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Limpando metadados de PDF usando Aspose.PDF para Java
Abstract: Aprenda como limpar metadados de PDF com Aspose.PDF para Java. O exemplo Java usa PdfFileInfo para remover informações de documentos armazenados com `clearInfo()` e depois salva o PDF limpo em um novo arquivo.
---
## Limpar metadados de PDF

Use este fluxo de trabalho quando precisar remover informações de documentos armazenados antes de compartilhar ou arquivar um PDF.

### Passos

1. Crie um objeto `PdfFileInfo` para o PDF de entrada.
2. Chame `clearInfo()` para remover metadados do documento.
3. Salve o resultado em um novo arquivo com `save()`.
4. Feche a instância `PdfFileInfo`.

### Exemplo Java

```java
public static void clearPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.clearInfo();
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
