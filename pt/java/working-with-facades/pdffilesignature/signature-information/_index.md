---
title: Informações de Assinatura
linktitle: Informações de Assinatura
type: docs
weight: 60
url: /pt/java/signature-information/
description: Aprenda a ler nomes de assinaturas e detalhes do assinante em PDFs assinados em Java com PdfFileSignature.
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ler detalhes da assinatura em documentos PDF em Java
Abstract: Aprenda a inspecionar os metadados da assinatura com Aspose.PDF for Java. O exemplo em Java lê o primeiro nome de assinatura disponível e, em seguida, recupera o assinante, a data, o motivo e a localização do PDF assinado.
---
## Obter informações de assinatura

Use este fluxo de trabalho quando precisar inspecionar quem assinou um PDF e quais metadados da assinatura foram armazenados.

### Etapas

1. Criar um `PdfFileSignature` instância e vincular o PDF assinado.
2. Leia a coleção de assinaturas e selecione um nome de assinatura.
3. Chame os acessadores de informações da assinatura para nome do assinante, data, motivo e local.
4. Feche o objeto facade quando terminar.

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
