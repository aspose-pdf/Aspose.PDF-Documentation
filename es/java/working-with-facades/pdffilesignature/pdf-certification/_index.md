---
title: PDF Certification
linktitle: PDF Certification
type: docs
weight: 30
url: /java/pdf-certification/
description: Aprenda a certificar documentos PDF en Java con PdfFileSignature y DocMDPSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Certify PDF documents with DocMDP permissions in Java
Abstract: Aprenda a certificar documentos PDF con Aspose.PDF para Java. El ejemplo de Java utiliza PdfFileSignature junto con DocMDPSignature y DocMDPAccessPermissions para certificar un documento para completar y firmar formularios, al tiempo que restringe otros tipos de modificaciones.
---
## Certificar documentos PDF

Utilice la certificación cuando el documento deba seguir siendo confiable pero aún así permitir una clase definida de cambios después de la firma.

### Pasos

1. Cree una instancia `PdfFileSignature` y vincule el PDF de origen.
2. Build a `PKCS7` signature object with the certificate and certificate password.
3. Envuelva esa firma en un `DocMDPSignature` con el valor `DocMDPAccessPermissions` requerido.
4. Call `certify` with the target page, signature metadata, visible rectangle, and MDP signature.
5. Save the certified PDF and close the facade object.

### Java example

```java
public static void certifyPdfWithMdpSignature(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        DocMDPSignature signature = new DocMDPSignature(
                createPkcs7(certificateFile, "Certified for form filling and signing"),
                DocMDPAccessPermissions.FillingInForms);
        pdfSignature.certify(1, "Certified for form filling and signing", "security@example.com", "New York, USA", true, signatureRectangle(), signature);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```
