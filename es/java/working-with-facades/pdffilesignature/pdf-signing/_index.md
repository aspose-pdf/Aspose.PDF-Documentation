---
title: Firmar documentos PDF
linktitle: Firmar documentos PDF
type: docs
weight: 10
url: /es/java/pdf-signing/
description: Aprenda cómo firmar documentos PDF en Java con la fachada PdfFileSignature.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Firmar documentos PDF con firmas digitales en Java
Abstract: Aprenda cómo firmar documentos PDF con Aspose.PDF for Java. El conjunto de ejemplos Java cubre la firma con una ruta de certificado y contraseña configuradas, y la firma con un objeto de firma PKCS7 explícito que incluye metadatos de la firma como motivo, información de contacto, ubicación y autoridad.
---
## Firmar documentos PDF

Utilice `PdfFileSignature` cuando necesites aplicar una firma digital visible a un PDF.

### Pasos

1. Cree una instancia de `PdfFileSignature` y vincule el PDF de origen.
2. Cargue el certificado ya sea a través de `setCertificate` o creando un objeto `PKCS7`.
3. Llame `sign` con la página de destino, configuraciones de visibilidad, rectángulo de firma y datos de firma.
4. Guarde el PDF firmado y cierre el objeto fachada.

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
