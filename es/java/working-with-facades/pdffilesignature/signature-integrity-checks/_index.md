---
title: Verificaciones de integridad de firmas
linktitle: Verificaciones de integridad de firmas
type: docs
weight: 70
url: /es/java/signature-integrity-checks/
description: Aprenda cómo validar la cobertura e integridad de firmas en Java con la fachada PdfFileSignature.
lastmod: "2026-09-28"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Validar la cobertura e integridad de firmas PDF en Java
Abstract: Aprenda cómo inspeccionar la integridad de la firma con Aspose.PDF for Java. El conjunto actual de ejemplos Java utiliza `verifySignature` para validar la firma seleccionada y `coversWholeDocument` para determinar si la firma protege todo el PDF.
---
## Comprobar la integridad de la firma

Este artículo se asigna al mismo flujo de trabajo de verificación expuesto por `PdfFileSignatureExamples.java`.

### Pasos

1. Enlace el PDF firmado con `PdfFileSignature`.
2. Seleccione un nombre de firma del documento.
3. Llame a `verifySignature` para validar el contenido de la firma.
4. Llame a `coversWholeDocument` para confirmar la cobertura en todo el documento.
5. Cierre el objeto fachada.

### Ejemplo de Java

```java
public static void verifyPdfSignature(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature '" + signatureName + "' is valid: " + pdfSignature.verifySignature(signatureName));
        System.out.println("Signature covers whole document: " + pdfSignature.coversWholeDocument(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```
