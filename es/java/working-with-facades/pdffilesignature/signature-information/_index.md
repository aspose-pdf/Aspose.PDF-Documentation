---
title: Información de la firma
linktitle: Información de la firma
type: docs
weight: 60
url: /es/java/signature-information/
description: Aprenda cómo leer los nombres de firma y los detalles del firmante de los PDF firmados en Java con PdfFileSignature.
lastmod: "2026-09-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Leer los detalles de la firma de documentos PDF en Java
Abstract: Aprenda cómo inspeccionar los metadatos de la firma con Aspose.PDF for Java. El ejemplo en Java lee el primer nombre de firma disponible y luego recupera el firmante, la fecha, el motivo y la ubicación del PDF firmado.
---
## Obtener información de la firma

Utilice este flujo de trabajo cuando necesite inspeccionar quién firmó un PDF y qué metadatos de firma se almacenaron.

### Pasos

1. Crear un `PdfFileSignature` instancia y vincula el PDF firmado.
2. Leer la colección de firmas y seleccionar un nombre de firma.
3. Llamar a los accesores de información de la firma para el nombre del firmante, la fecha, el motivo y la ubicación.
4. Cerrar el objeto fachada cuando haya terminado.

### Ejemplo de Java

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
