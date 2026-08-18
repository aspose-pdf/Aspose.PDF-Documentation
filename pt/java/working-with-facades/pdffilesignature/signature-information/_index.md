---
title: Informações de assinatura
linktitle: Informações de assinatura
type: docs
weight: 60
url: /java/signature-information/
description: Aprenda como ler nomes de assinaturas e detalhes de signatários de PDFs assinados em Java com PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Leia detalhes de assinatura de documentos PDF em Java
Abstract: Aprenda como inspecionar metadados de assinatura com Aspose.PDF para Java. O exemplo Java lê o primeiro nome de assinatura disponível e, em seguida, recupera o signatário, a data, o motivo e o local do PDF assinado.
---
## Obtenha informações de assinatura

Use este fluxo de trabalho quando precisar inspecionar quem assinou um PDF e quais metadados de assinatura foram armazenados.

### Passos

1. Crie uma instância `PdfFileSignature` e vincule o PDF assinado.
2. Leia a coleção de assinaturas e selecione um nome de assinatura.
3. Chame os acessadores de informações de assinatura para obter o nome, data, motivo e local do signatário.
4. Feche o objeto de fachada quando terminar.

### Exemplo Java

```java
public static void getSignatureInformation(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature Names: " + pdfSignature.getSignNames());
        System.out.println("Signer: " + pdfSignature.getSignerName(signatureName));
        System.out.println("Date: " + pdfSignature.getDateTime(signatureName));
        System.out.println("Reason: " + pdfSignature.getReason(signatureName));
        System.out.println("Location: " + pdfSignature.getLocation(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```
