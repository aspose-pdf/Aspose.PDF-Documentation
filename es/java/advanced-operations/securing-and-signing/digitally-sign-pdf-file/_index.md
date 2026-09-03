---
title: Agregar firma digital o firmar PDF digitalmente en Java
linktitle: Firmar PDF digitalmente
type: docs
weight: 10
url: /es/java/digitally-sign-pdf-file/
description: Aprende cómo firmar digitalmente y certificar documentos PDF en Java usando Aspose.PDF.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Firmar archivos PDF digitalmente con Java
Abstract: Esta guía explica cómo firmar digitalmente documentos PDF usando Aspose.PDF for Java. Cubre la firma con un objeto de certificado, la firma con parámetros básicos de certificado y la certificación de un documento con una firma DocMDP para controlar los cambios permitidos después de la firma.
---
Aspose.PDF for Java admite varios flujos de firma a través de `PdfFileSignature`.

## Firmar un PDF con un objeto de certificado

1. Crear el [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) fachada y vincular el documento PDF de origen.
1. Crear el [PKCS7](https://reference.aspose.com/pdf/java/com.aspose.pdf/pkcs7/) objeto de firma y configurar las opciones de firma.
1. Aplica la firma al documento PDF a través de [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. Guarda el documento PDF actualizado.

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

Este enfoque construye un `PKCS7` objeto de firma primero y luego lo aplica a la página 1.

## Firma un PDF con parámetros básicos del certificado

1. Crear el [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) fachada y vincular el documento PDF de origen.
1. Configura los parámetros del certificado requeridos por el ejemplo de firma.
1. Aplica la firma al documento PDF a través de [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. Guarda el documento PDF actualizado.

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

## Certificar un PDF con DocMDP

Utilice una firma de detección y prevención de modificaciones de documentos cuando necesite restricciones a nivel de certificación:

1. Crear el [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) fachada y vincular el documento PDF de origen.
1. Crear el [DocMDPSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpsignature/) objeto y configure el [DocMDPAccessPermissions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpaccesspermissions/) opciones de firma.
1. Aplique la firma de certificación y guarde el documento PDF actualizado.

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
