---
title: Sign PDF Documents
linktitle: Firmar documentos PDF
type: docs
weight: 10
url: /java/pdf-signing/
description: Aprenda a firmar documentos PDF en Java con la fachada PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Firmar documentos PDF con firmas digitales en Java
Abstract: Aprenda a firmar documentos PDF con Aspose.PDF para Java. El conjunto de ejemplos de Java cubre la firma con una ruta de certificado y una contraseña configuradas, y la firma con un objeto de firma PKCS7 explícito que incluye metadatos de firma como motivo, información de contacto, ubicación y autoridad.
---
## Firmar documentos PDF

Utilice `PdfFileSignature` cuando necesite aplicar una firma digital visible a un PDF.

### Pasos

1. Create a `PdfFileSignature` instance and bind the source PDF.
2. Load the certificate either through `setCertificate` or by creating a `PKCS7` object.
3. Call `sign` with the target page, visibility settings, signature rectangle, and signature data.
4. Save the signed PDF and close the facade object.

### Ejemplos de Java

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
