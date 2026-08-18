---
title: Extraia informações de assinatura de PDF em Java
linktitle: Extraia detalhes da assinatura
type: docs
weight: 20
url: /java/extract-image-and-signature-information/
description: Aprenda como extrair detalhes de certificados e assinaturas digitais de arquivos PDF em Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraia detalhes de assinatura e dados de certificado de PDFs assinados em Java
Abstract: Este artigo explica como inspecionar assinaturas digitais em documentos PDF usando Aspose.PDF para Java. Aprenda como ler os detalhes do signatário, verificar uma assinatura, verificar se uma assinatura cobre todo o documento, extrair o certificado de assinatura incorporado e remover uma assinatura existente.
---
Use `PdfFileSignature` para inspecionar e gerenciar assinaturas que já existem em um documento PDF.

## Ler informações de assinatura

1. Crie a fachada [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) e vincule o documento PDF de origem.
1. Acesse o nome da assinatura do documento e configure o fluxo de inspeção de assinatura exigido pelo exemplo.
1. Leia e verifique as informações de assinatura da fachada [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. Leia os valores retornados ou continue com a próxima etapa de processamento.

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

## Verifique uma assinatura

1. Crie a fachada [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) e vincule o documento PDF de origem.
1. Acesse o nome da assinatura do documento e configure o fluxo de verificação exigido pelo exemplo.
1. Leia e verifique as informações de assinatura da fachada [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).

```java
public static void verifyPdfSignature(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature '" + signatureName + "' is valid: "
                + pdfSignature.verifySignature(signatureName));
        System.out.println("Signature covers whole document: "
                + pdfSignature.coversWholeDocument(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```

## Extraia o certificado de assinatura

1. Crie a fachada [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) e vincule o documento PDF de origem.
1. Acesse o nome da assinatura do documento necessário para extração do certificado.
1. Escreva a saída extraída ou inspecione os valores retornados da fachada [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).

```java
public static void extractSignatureCertificate(Path inputFile, Path outputFile) throws Exception {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        try (InputStream inputStream = pdfSignature.extractCertificate(signatureName);
             OutputStream outputStream = Files.newOutputStream(outputFile)) {
            inputStream.transferTo(outputStream);
        }
    } finally {
        pdfSignature.close();
    }
}
```
