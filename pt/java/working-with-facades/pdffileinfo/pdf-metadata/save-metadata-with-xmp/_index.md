---
title: Salvar Metadados com XMP
linktitle: Salvar Metadados com XMP
type: docs
weight: 30
url: /pt/java/save-metadata-with-xmp/
description: Aprenda como salvar metadados PDF com XMP em Java usando a fachada PdfFileInfo.
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Salvando Metadados PDF com XMP Usando Aspose.PDF for Java
Abstract: Aprenda como salvar metadados PDF com XMP usando Aspose.PDF for Java. O exemplo em Java atualiza os campos de metadados principais com PdfFileInfo e os grava novamente usando `saveNewInfoWithXmp()` para que o documento de saída armazene as informações no formato XMP.
---
## Salvar metadados com XMP

Use este fluxo de trabalho quando precisar que as informações atualizadas do documento sejam armazenadas no formato XMP.

### Passos

1. Criar um `PdfFileInfo` objeto para o PDF de origem.
2. Defina os campos de metadados que deseja atualizar, como assunto, título, palavras‑chave e criador.
3. Chamar `saveNewInfoWithXmp()` com o caminho do arquivo de saída.
4. Fechar o `PdfFileInfo` instância.

### Exemplo em Java

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
