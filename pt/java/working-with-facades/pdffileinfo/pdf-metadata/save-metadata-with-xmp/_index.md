---
title: Salvar metadados com XMP
linktitle: Salvar metadados com XMP
type: docs
weight: 30
url: /java/save-metadata-with-xmp/
description: Aprenda como salvar metadados PDF com XMP em Java com a fachada PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Salvando metadados PDF com XMP usando Aspose.PDF para Java
Abstract: Aprenda como salvar metadados PDF com XMP usando Aspose.PDF para Java. O exemplo Java atualiza os principais campos de metadados com PdfFileInfo e os grava usando `saveNewInfoWithXmp()` para que o documento de saída armazene as informações no formato XMP.
---
## Salve metadados com XMP

Use este fluxo de trabalho quando precisar que as informações atualizadas do documento sejam armazenadas no formato XMP.

### Passos

1. Crie um objeto `PdfFileInfo` para o PDF de origem.
2. Defina os campos de metadados que deseja atualizar, como assunto, título, palavras-chave e criador.
3. Chame `saveNewInfoWithXmp()` com o caminho do arquivo de saída.
4. Feche a instância `PdfFileInfo`.

### Exemplo Java

```java
public static void saveInfoWithXmp(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.setSubject("Aspose PDF for Java");
    pdfInfo.setTitle("Aspose PDF for Java");
    pdfInfo.setKeywords("Aspose, PDF, Java");
    pdfInfo.setCreator("Aspose Team");
    pdfInfo.saveNewInfoWithXmp(outputFile.toString());
    pdfInfo.close();
}
```
