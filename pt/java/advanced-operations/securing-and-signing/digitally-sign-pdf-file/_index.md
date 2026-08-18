---
title: Adicione assinatura digital ou assine digitalmente PDF em Java
linktitle: Assinar PDF digitalmente
type: docs
weight: 10
url: /java/digitally-sign-pdf-file/
description: Aprenda como assinar e certificar digitalmente documentos PDF em Java usando Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Assine digitalmente arquivos PDF com Java
Abstract: Este guia explica como assinar digitalmente documentos PDF usando Aspose.PDF para Java. Abrange a assinatura com um objeto de certificado, a assinatura com parâmetros básicos de certificado e a certificação de um documento com uma assinatura DocMDP para controlar as alterações pós-assinatura permitidas.
---
Aspose.PDF para Java oferece suporte a vários fluxos de assinatura por meio de `PdfFileSignature`.

## Assine um PDF com um objeto de certificado

1. Crie a fachada [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) e vincule o documento PDF de origem.
1. Crie o objeto de assinatura [PKCS7](https://reference.aspose.com/pdf/java/com.aspose.pdf/pkcs7/) e configure as opções de assinatura.
1. Aplique a assinatura ao documento PDF através de [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
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

Essa abordagem cria primeiro um objeto de assinatura `PKCS7` e depois o aplica à página 1.

## Assine um PDF com parâmetros básicos de certificado

1. Crie a fachada [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) e vincule o documento PDF de origem.
1. Configure os parâmetros de certificado exigidos pelo exemplo de assinatura.
1. Aplique a assinatura ao documento PDF através de [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
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

1. Crie a fachada [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) e vincule o documento PDF de origem.
1. Crie o objeto [DocMDPSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpsignature/) e configure as opções de assinatura [DocMDPAccessPermissions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpaccesspermissions/).
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
