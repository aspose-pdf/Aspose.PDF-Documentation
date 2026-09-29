---
title: Guardar metadatos con XMP
linktitle: Guardar metadatos con XMP
type: docs
weight: 30
url: /es/java/save-metadata-with-xmp/
description: Aprenda cómo guardar metadatos de PDF con XMP en Java usando la fachada PdfFileInfo.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guardando metadatos de PDF con XMP usando Aspose.PDF for Java
Abstract: Aprenda cómo guardar metadatos de PDF con XMP usando Aspose.PDF for Java. El ejemplo en Java actualiza los campos de metadatos principales con PdfFileInfo y los escribe de nuevo usando `saveNewInfoWithXmp()` para que el documento de salida almacene la información en forma XMP.
---
## Guardar metadatos con XMP

Utilice este flujo de trabajo cuando necesite que la información actualizada del documento se almacene en formato XMP.

### Pasos

1. Cree un objeto `PdfFileInfo` para el PDF de origen.
2. Establezca los campos de metadatos que desea actualizar, como asunto, título, palabras clave y creador.
3. Llame a `saveNewInfoWithXmp()` con la ruta del archivo de salida.
4. Cierre la instancia de `PdfFileInfo`.

### Ejemplo en Java

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
