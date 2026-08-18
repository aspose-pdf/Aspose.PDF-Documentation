---
title: Obtenha metadados de PDF
linktitle: Obtenha metadados de PDF
type: docs
weight: 20
url: /java/get-pdf-metadata/
description: Aprenda como ler metadados PDF em Java com a fachada PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Recuperando metadados de PDF usando Aspose.PDF para Java.
Abstract: Aprenda como recuperar metadados PDF com Aspose.PDF para Java. O exemplo Java lê campos padrão como assunto, título, palavras-chave, criador, data de criação e data de modificação, junto com sinalizadores de status de arquivo e uma entrada de metadados `Reviewer` personalizada.
---
## Obtenha metadados de PDF

Este exemplo lê informações padrão do documento, sinalizadores de status de arquivo e uma chave de metadados personalizada.

### Passos

1. Crie um objeto `PdfFileInfo` para o PDF de origem.
2. Leia os campos de metadados padrão, como assunto, título, palavras-chave e criador.
3. Inspecione os sinalizadores de estado do arquivo, como se o arquivo é válido, criptografado, protegido por senha ou um portfólio.
4. Leia um valor de metadados personalizado com `getMetaInfo`.
5. Feche a instância `PdfFileInfo`.

### Exemplo Java

```java
public static void getPdfMetadata(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Subject: " + pdfInfo.getSubject());
    System.out.println("Title: " + pdfInfo.getTitle());
    System.out.println("Keywords: " + pdfInfo.getKeywords());
    System.out.println("Creator: " + pdfInfo.getCreator());
    System.out.println("Creation Date: " + pdfInfo.getCreationDate());
    System.out.println("Modification Date: " + pdfInfo.getModDate());
    System.out.println("Is Valid PDF: " + pdfInfo.isPdfFile());
    System.out.println("Is Encrypted: " + pdfInfo.isEncrypted());
    System.out.println("Has Open Password: " + pdfInfo.hasOpenPassword());
    System.out.println("Has Edit Password: " + pdfInfo.hasEditPassword());
    System.out.println("Is Portfolio: " + pdfInfo.hasCollection());
    String reviewer = pdfInfo.getMetaInfo("Reviewer");
    System.out.println("Reviewer: " + (reviewer == null || reviewer.isBlank() ? "No Reviewer metadata found." : reviewer));
    pdfInfo.close();
}
```
