---
title: Save Metadata with XMP
linktitle: Save Metadata with XMP
type: docs
weight: 30
url: /java/save-metadata-with-xmp/
description: Learn how to save PDF metadata with XMP in Java with the PdfFileInfo facade.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Saving PDF Metadata with XMP Using Aspose.PDF for Java
Abstract: Learn how to save PDF metadata with XMP using Aspose.PDF for Java. The Java example updates core metadata fields with PdfFileInfo and writes them back using `saveNewInfoWithXmp()` so the output document stores the information in XMP form.
---
## Guardar metadatos con XMP

Utilice este flujo de trabajo cuando necesite que la información actualizada del documento se almacene en formato XMP.

### Pasos

1. Cree un objeto `PdfFileInfo` para el PDF de origen.
2. Set the metadata fields you want to update, such as subject, title, keywords, and creator.
3. Llame a `saveNewInfoWithXmp()` con la ruta del archivo de salida.
4. Close the `PdfFileInfo` instance.

### Ejemplo de Java

```java
public static void saveInfoWithXmp(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.setSubject("Aspose PDF for Java");
    pdfInfo.setTitle("Aspose PDF for Java");
    pdfInfo.setKeywords("Aspose, PDF, Java");
    pdfInfo.setCreator("Aspose Team");
    pdfInfo.saveNewInfoWithXmp(outputFile.toString());
    pdfInfo.close();
}
```
