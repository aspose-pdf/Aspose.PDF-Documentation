---
title: Agregue firma digital o firme digitalmente PDF en Java
linktitle: Firmar PDF digitalmente
type: docs
weight: 10
url: /java/digitally-sign-pdf-file/
description: Aprenda a firmar y certificar digitalmente documentos PDF en Java utilizando Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Firmar digitalmente archivos PDF con Java
Abstract: Esta guía explica cómo firmar digitalmente documentos PDF usando Aspose.PDF para Java. Cubre la firma con un objeto de certificado, la firma con parámetros básicos de certificado y la certificación de un documento con una firma DocMDP para controlar los cambios permitidos posteriores a la firma.
---
Aspose.PDF para Java admite múltiples flujos de firma a través de `PdfFileSignature`.


## 
Firmar un PDF con un objeto de certificado


1. 
Cree la fachada [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) y vincule el documento PDF de origen.

1. 
Cree el objeto de firma [PKCS7](https://reference.aspose.com/pdf/java/com.aspose.pdf/pkcs7/) y configure las opciones de firma.

1. 
Aplique la firma al documento PDF a través de [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. Guarde el documento PDF actualizado.


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


Este enfoque crea primero un objeto de firma `PKCS7` y luego lo aplica a la página 1.


## 
Firmar un PDF con parámetros básicos de certificado


1. 
Cree la fachada [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) y vincule el documento PDF de origen.

1. 
Configure los parámetros del certificado requeridos por el ejemplo de firma.
1. Aplique la firma al documento PDF a través de [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).

1. 
Guarde el documento PDF actualizado.


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

## 
Certificar un PDF con DocMDP



Utilice una firma de prevención y detección de modificaciones de documentos cuando necesite restricciones de nivel de certificación:


1. 
Cree la fachada [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) y vincule el documento PDF de origen.
1. Cree el objeto [DocMDPSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpsignature/) y configure las opciones de firma [DocMDPAccessPermissions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpaccesspermissions/).

1. 
Aplique la firma de certificación y guarde el documento PDF actualizado.

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
