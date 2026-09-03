---
title: Verificación de firmas
linktitle: Verificación de firmas
type: docs
weight: 90
url: /es/java/signature-verification/
description: Aprenda cómo verificar firmas PDF en Java con la fachada PdfFileSignature.
lastmod: "2026-09-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Verifique firmas PDF en Java
Abstract: Aprenda cómo verificar una firma PDF con Aspose.PDF for Java. El ejemplo en Java selecciona la primera firma disponible, valida la firma y verifica si cubre todo el documento.
---
## Verificar firma PDF

Utilice este workflow cuando necesite una validación rápida de un PDF firmado existente.

### Pasos

1. Crear un `PdfFileSignature` instancia y enlaza el PDF firmado.
2. Selecciona el nombre de la firma que deseas inspeccionar.
3. Llamar `verifySignature` para validar la firma.
4. Llamar `coversWholeDocument` para verificar la cobertura.
5. Cierra el objeto fachada.

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
