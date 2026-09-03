---
title: Rellenar campos de código de barras
linktitle: Rellenar campos de código de barras
type: docs
weight: 50
url: /es/java/fill-barcode-fields/
description: Aprenda cómo rellenar un campo de formulario de código de barras en Java usando la fachada Form en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Rellene un campo de código de barras en un formulario PDF con Java
Abstract: Este artículo muestra cómo enlazar un formulario PDF, establecer el valor de un campo de código de barras y guardar el documento actualizado con la fachada Form en Aspose.PDF para Java.
---
Usar `FormExamples.fillBarcodeFields(...)` para rellenar un campo de código de barras en un formulario PDF.

```java
public static void fillBarcodeFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillBarcodeField("product_barcode", "123456789012");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
