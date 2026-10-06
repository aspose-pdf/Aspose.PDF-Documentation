---
title: Definir metadados PDF
linktitle: Definir metadados PDF
type: docs
weight: 50
url: /pt/java/set-pdf-metadata/
description: Saiba como atualizar metadados PDF em Java com a fachada PdfFileInfo.
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Atualizando metadados PDF usando Aspose.PDF for Java
Abstract: Saiba como atualizar metadados PDF com Aspose.PDF for Java. O exemplo em Java usa PdfFileInfo para definir campos padrão de metadados, como assunto, título, palavras‑chave e criador, adiciona uma entrada de metadados personalizada e salva o resultado em um novo PDF.
---
## Definir metadados PDF

Use este fluxo de trabalho quando precisar normalizar ou enriquecer as informações do documento antes de salvar o PDF.

### Etapas

1. Crie um objeto `PdfFileInfo` para o PDF de origem.
2. Defina os campos de metadados padrão que deseja atualizar.
3. Adicione quaisquer metadados personalizados com `setMetaInfo`.
4. Salve o documento atualizado com `save()`.
5. Feche o `PdfFileInfo` instância.

### Exemplo Java

```java
public static void setPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.setSubject("Aspose PDF for Java");
    pdfInfo.setTitle("Aspose PDF for Java");
    pdfInfo.setKeywords("Aspose, PDF, Java");
    pdfInfo.setCreator("Aspose Team");
    pdfInfo.setMetaInfo("CustomKey", "CustomValue");
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
