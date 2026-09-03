---
title: Gestión de firmas
linktitle: Gestión de firmas
type: docs
weight: 80
url: /es/java/signature-management/
description: Aprenda cómo eliminar una firma PDF existente en Java con la fachada PdfFileSignature.
lastmod: "2026-09-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar firmas PDF en Java
Abstract: Aprenda cómo eliminar una firma de un PDF firmado con Aspose.PDF for Java. El conjunto de ejemplos actual de Java cubre la eliminación de una firma existente por nombre y la guardado del documento actualizado. No incluye un ejemplo separado para limpiar el campo de firma asociado.
---
## Eliminar una firma

Utilice este workflow cuando una firma digital existente debe eliminarse del documento.

### Pasos

1. Crear una `PdfFileSignature` instancia y vincula el PDF firmado.
2. Lee la colección de firmas y selecciona un nombre de firma.
3. Llamada `removeSignature` con ese nombre.
4. Guarda el archivo actualizado y cierra el objeto fachada.

### Ejemplo en Java

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

El conjunto actual de ejemplos en Java no incluye un método separado para eliminar el campo de firma asociado después de borrar la firma.
