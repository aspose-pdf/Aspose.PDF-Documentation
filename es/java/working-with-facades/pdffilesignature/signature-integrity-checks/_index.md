---
title: Verificaciones de integridad de firma
linktitle: Verificaciones de integridad de firma
type: docs
weight: 70
url: /java/signature-integrity-checks/
description: Aprenda a validar la cobertura e integridad de la firma en Java con la fachada PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Validar la cobertura e integridad de la firma de PDF en Java
Abstract: Aprenda a inspeccionar la integridad de la firma con Aspose.PDF para Java. El conjunto de ejemplos de Java actual utiliza `verifySignature` para validar la firma seleccionada y `coversWholeDocument` para determinar si la firma protege todo el PDF.
---
## Verificar la integridad de la firma



Este artículo se corresponde con el mismo flujo de trabajo de verificación expuesto por `PdfFileSignatureExamples.java`.


### 
Pasos


1. 
Enlaza el PDF firmado con `PdfFileSignature`.

2. 
Seleccione un nombre de firma del documento.
3. Llame a `verifySignature` para validar el contenido de la firma.

4. 
Llame a `coversWholeDocument` para confirmar la cobertura de todo el documento.

5. 
Cierra el objeto de fachada.


### 
Ejemplo de Java

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
