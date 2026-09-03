---
title: Verificación de firma
linktitle: Verificación de firma
type: docs
weight: 90
url: /java/signature-verification/
description: Aprenda a verificar firmas de PDF en Java con la fachada PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Verificar firmas de PDF en Java
Abstract: Aprenda cómo verificar una firma de PDF con Aspose.PDF para Java. El ejemplo de Java selecciona la primera firma disponible, valida la firma y comprueba si cubre todo el documento.
---
## Verificar firma PDF



Utilice este flujo de trabajo cuando necesite una validación rápida de un PDF firmado existente.


### 
Pasos


1. Cree una instancia `PdfFileSignature` y vincule el PDF firmado.

2. Seleccione el nombre de la firma que desea inspeccionar.
3. Llame a `verifySignature` para validar la firma.

4. Llame a `coversWholeDocument` para verificar la cobertura.

5. Cierra el objeto de fachada.


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
