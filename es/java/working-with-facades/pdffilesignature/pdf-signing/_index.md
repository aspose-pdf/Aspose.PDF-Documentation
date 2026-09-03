---
title: Firmar documentos PDF
linktitle: Firmar documentos PDF
type: docs
weight: 10
url: /es/java/pdf-signing/
description: Aprenda cómo firmar documentos PDF en Java con la fachada PdfFileSignature.
lastmod: "2026-09-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Firmar documentos PDF con firmas digitales en Java
Abstract: Aprenda cómo firmar documentos PDF con Aspose.PDF for Java. El conjunto de ejemplos de Java cubre la firma con una ruta de certificado configurada y contraseña, y la firma con un objeto de firma PKCS7 explícito que incluye metadatos de la firma como motivo, información de contacto, ubicación y autoridad.
---
## Firmar documentos PDF

Usar `PdfFileSignature` cuando necesites aplicar una firma digital visible a un PDF.

### Pasos

1. Crear un `PdfFileSignature` instancia y enlaza el PDF de origen.
2. Cargue el certificado ya sea a través de `setCertificate` o creando un `PKCS7` objeto.
3. Llamar `sign` con la página objetivo, configuraciones de visibilidad, rectángulo de firma y datos de firma.
4. Guarda el PDF firmado y cierra el objeto fachada.

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
