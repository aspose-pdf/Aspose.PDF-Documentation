---
title: Gestión de firmas
linktitle: Gestión de firmas
type: docs
weight: 80
url: /java/signature-management/
description: Aprenda cómo eliminar una firma PDF existente en Java con la fachada PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar firmas de PDF en Java
Abstract: Aprenda cómo eliminar una firma de un PDF firmado con Aspose.PDF para Java. El conjunto de ejemplos de Java actual cubre la eliminación de una firma existente por nombre y el guardado del documento actualizado. No incluye una muestra separada para limpiar el campo de firma asociado.
---
## Eliminar una firma



Utilice este flujo de trabajo cuando deba eliminarse una firma digital existente del documento.


### 
Pasos


1. Cree una instancia `PdfFileSignature` y vincule el PDF firmado.

2. Lea la colección de firmas y seleccione un nombre de firma.
3. Llame a `removeSignature` con ese nombre.

4. Guarde el archivo actualizado y cierre el objeto de fachada.


### 
Ejemplo de Java


```java
public static void removeSignature(Path inputFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        pdfSignature.removeSignature(signatureName);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```


El conjunto de muestra de Java actual no incluye un método separado para eliminar el campo de firma asociado después de eliminar la firma.
