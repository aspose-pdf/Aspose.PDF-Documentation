---
title: Certificación PDF
linktitle: Certificación PDF
type: docs
weight: 30
url: /es/java/pdf-certification/
description: Aprenda cómo certificar documentos PDF en Java con PdfFileSignature y DocMDPSignature.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Certificar documentos PDF con permisos DocMDP en Java
Abstract: Aprenda cómo certificar documentos PDF con Aspose.PDF for Java. El ejemplo en Java utiliza PdfFileSignature junto con DocMDPSignature y DocMDPAccessPermissions para certificar un documento para rellenar formularios y firmar, mientras restringe otros tipos de modificaciones.
---
## Certificar documentos PDF

Utilice la certificación cuando el documento debe permanecer confiable pero aún permitir una clase definida de cambios después de la firma.

### Pasos

1. Cree una instancia de `PdfFileSignature` y enlace el PDF de origen.
2. Construya un objeto `PKCS7` de firma con el certificado y la contraseña del certificado.
3. Envuelva esa firma en un `DocMDPSignature` con el valor `DocMDPAccessPermissions` requerido.
4. Llame `certify` con la página de destino, los metadatos de la firma, el rectángulo visible y la firma MDP.
5. Guarde el PDF certificado y cierre el objeto fachada.

### Ejemplo Java

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
