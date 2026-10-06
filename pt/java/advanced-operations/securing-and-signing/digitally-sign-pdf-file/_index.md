---
title: Adicionar assinatura digital ou assinar PDF digitalmente em Java
linktitle: Assinar PDF digitalmente
type: docs
weight: 10
url: /pt/java/digitally-sign-pdf-file/
description: Aprenda como assinar digitalmente e certificar documentos PDF em Java usando Aspose.PDF.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Assinar digitalmente arquivos PDF com Java
Abstract: Este guia explica como assinar digitalmente documentos PDF usando Aspose.PDF for Java. Ele abrange a assinatura com um objeto de certificado, a assinatura com parâmetros básicos de certificado e a certificação de um documento com uma assinatura DocMDP para controlar as alterações permitidas após a assinatura.
aliases:
    - /pt/java/assinar-arquivo-pdf-digitalmente/
---
Aspose.PDF for Java suporta vários fluxos de assinatura através de `PdfFileSignature`.

## Assine um PDF com um objeto de certificado

1. Crie o [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) fachada e vincule o documento PDF de origem.
1. Crie o [PKCS7](https://reference.aspose.com/pdf/java/com.aspose.pdf/pkcs7/) objeto de assinatura e configure as opções de assinatura.
1. Aplique a assinatura ao documento PDF por meio de [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. Salve o documento PDF atualizado.

```java
public static void signPdfWithCertificateObject(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        pdfSignature.sign(1, false, signatureRectangle(), createPkcs7(certificateFile, "Document approval"));
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```

Esta abordagem constrói um `PKCS7` objeto de assinatura primeiro e então aplicá‑lo à página 1.

## Assine um PDF com parâmetros de certificado básicos

1. Crie o [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) fachada e vincule o documento PDF de origem.
1. Configure os parâmetros de certificado necessários para o exemplo de assinatura.
1. Aplique a assinatura ao documento PDF por meio de [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. Salve o documento PDF atualizado.

```java
public static void signPdfWithBasicParameters(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        pdfSignature.setCertificate(certificateFile.toString(), CERTIFICATE_PASSWORD);
        pdfSignature.sign(1, "Document approval", "qa@example.com", "New York, USA", false, signatureRectangle());
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```

## Certificar um PDF com DocMDP

Use uma assinatura de detecção e prevenção de modificação de documento quando precisar de restrições em nível de certificação:

1. Crie o [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) fachada e vincule o documento PDF de origem.
1. Crie o [DocMDPSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpsignature/) objeto e configure o [DocMDPAccessPermissions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpaccesspermissions/) opções de assinatura.
1. Aplique a assinatura de certificação e salve o documento PDF atualizado.

```java
public static void certifyPdfWithMdpSignature(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        DocMDPSignature signature = new DocMDPSignature(
                createPkcs7(certificateFile, "Certified for form filling and signing"),
                DocMDPAccessPermissions.FillingInForms);
        pdfSignature.certify(1, "Certified for form filling and signing", "security@example.com",
                "New York, USA", true, signatureRectangle(), signature);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```
