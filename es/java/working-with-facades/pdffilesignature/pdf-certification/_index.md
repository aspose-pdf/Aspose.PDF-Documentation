---
title: Certificación PDF
linktitle: Certificación PDF
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
AlternativeHeadline: Certificar documentos PDF con permisos DocMDP en Java
Abstract: Aprenda a certificar documentos PDF con Aspose.PDF para Java. El ejemplo de Java utiliza PdfFileSignature junto con DocMDPSignature y DocMDPAccessPermissions para certificar un documento para completar y firmar formularios, al tiempo que restringe otros tipos de modificaciones.
---
## Certificar documentos PDF



Utilice la certificación cuando el documento deba seguir siendo confiable pero aún así permitir una clase definida de cambios después de la firma.


### 
Pasos


1. Cree una instancia `PdfFileSignature` y vincule el PDF de origen.

2. Cree un objeto de firma `PKCS7` con el certificado y la contraseña del certificado.
3. Envuelva esa firma en un `DocMDPSignature` con el valor `DocMDPAccessPermissions` requerido.

4. Llame a `certify` con la página de destino, los metadatos de la firma, el rectángulo visible y la firma MDP.

5. Guarde el PDF certificado y cierre el objeto de fachada.


### 
Ejemplo de Java

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
