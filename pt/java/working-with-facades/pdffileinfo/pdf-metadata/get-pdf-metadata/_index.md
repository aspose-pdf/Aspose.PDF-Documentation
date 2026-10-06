---
title: Obter metadados do PDF
linktitle: Obter metadados do PDF
type: docs
weight: 20
url: /pt/java/get-pdf-metadata/
description: Saiba como ler metadados de PDF em Java com a fachada PdfFileInfo.
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Recuperando metadados de PDF usando Aspose.PDF for Java
Abstract: Saiba como recuperar metadados de PDF com Aspose.PDF for Java. O exemplo Java lê campos padrão como assunto, título, palavras‑chave, criador, data de criação e data de modificação, junto com flags de status do arquivo e uma entrada de metadados personalizada `Reviewer`.
---
## Obter metadados do PDF

Este exemplo lê informações padrão do documento, flags de status do arquivo e uma chave de metadados personalizada.

### Etapas

1. Crie um objeto `PdfFileInfo` para o PDF de origem.
2. Leia os campos de metadados padrão, como assunto, título, palavras‑chave e criador.
3. Inspecione as sinalizações de estado do arquivo, como se o arquivo é válido, criptografado, protegido por senha ou um portfólio.
4. Leia um valor de metadados personalizado com `getMetaInfo`.
5. Feche o `PdfFileInfo` instância.

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
