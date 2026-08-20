---
title: Llenar campos de código de barras
linktitle: Llenar campos de código de barras
type: docs
weight: 50
url: /java/fill-barcode-fields/
description: Aprenda a completar un campo de formulario de código de barras en Java usando la fachada del formulario en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Complete un campo de código de barras en un formulario PDF con Java
Abstract: Este artículo muestra cómo vincular un formulario PDF, establecer un valor de campo de código de barras y guardar el documento actualizado con la fachada del formulario en Aspose.PDF para Java.
---
Utilice `FormExamples.fillBarcodeFields(...)` para completar un campo de código de barras en un formulario PDF.

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
