---
title: Signature Information
linktitle: Información de firma
type: docs
weight: 60
url: /java/signature-information/
description: Aprenda a leer nombres de firmas y detalles del firmante de archivos PDF firmados en Java con PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Leer detalles de firma de documentos PDF en Java
Abstract: Aprenda a inspeccionar metadatos de firmas con Aspose.PDF para Java. El ejemplo de Java lee el primer nombre de firma disponible y luego recupera el firmante, la fecha, el motivo y la ubicación del PDF firmado.
---
## Obtener información de firma

Utilice este flujo de trabajo cuando necesite inspeccionar quién firmó un PDF y qué metadatos de firma se almacenaron.

### Pasos

1. Cree una instancia `PdfFileSignature` y vincule el PDF firmado.
2. Lea la colección de firmas y seleccione un nombre de firma.
3. Call the signature-information accessors for signer name, date, reason, and location.
4. Close the facade object when finished.

### Java example

```java
public static void getSignatureInformation(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature Names: " + pdfSignature.getSignNames());
        System.out.println("Signer: " + pdfSignature.getSignerName(signatureName));
        System.out.println("Date: " + pdfSignature.getDateTime(signatureName));
        System.out.println("Reason: " + pdfSignature.getReason(signatureName));
        System.out.println("Location: " + pdfSignature.getLocation(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```
