---
title: Extrair informações de assinatura de PDF em Java
linktitle: Extrair detalhes da Assinatura
type: docs
weight: 20
url: /pt/java/extract-image-and-signature-information/
description: Aprenda como extrair detalhes de certificado e assinatura digital de arquivos PDF em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extrair detalhes da assinatura e dados do certificado de PDFs assinados em Java
Abstract: Este artigo explica como inspecionar assinaturas digitais em documentos PDF usando Aspose.PDF for Java. Aprenda como ler detalhes do assinante, verificar uma assinatura, verificar se uma assinatura cobre todo o documento, extrair o certificado de assinatura incorporado e remover uma assinatura existente.
---
Usar `PdfFileSignature` para inspecionar e gerenciar assinaturas que já existem em um documento PDF.

## Ler informações da assinatura

1. Criar o [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) fachada e vincule o documento PDF de origem.
1. Acesse o nome da assinatura do documento e configure o fluxo de inspeção de assinatura exigido pelo exemplo.
1. Leia e verifique as informações da assinatura a partir do [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) fachada.
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

## Verificar uma assinatura

1. Criar o [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) fachada e vincule o documento PDF de origem.
1. Acesse o nome da assinatura do documento e configure o fluxo de verificação exigido pelo exemplo.
1. Leia e verifique as informações da assinatura a partir do [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) fachada.

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

## "Extrair o certificado de assinatura"

1. Criar o [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) fachada e vincule o documento PDF de origem.
1. "Acesse o nome da assinatura do documento necessário para a extração do certificado."
1. Escreva a saída extraída ou inspecione os valores retornados do [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) fachada.

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
