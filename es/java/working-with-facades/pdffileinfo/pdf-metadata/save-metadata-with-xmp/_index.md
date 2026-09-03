---
title: Guardar metadatos con XMP
linktitle: Guardar metadatos con XMP
type: docs
weight: 30
url: /es/java/save-metadata-with-xmp/
description: Aprenda cómo guardar los metadatos PDF con XMP en Java usando la fachada PdfFileInfo.
lastmod: "2026-09-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guardando metadatos PDF con XMP usando Aspose.PDF for Java
Abstract: Aprenda cómo guardar los metadatos PDF con XMP usando Aspose.PDF for Java. El ejemplo en Java actualiza los campos de metadatos principales con PdfFileInfo y los escribe de nuevo usando `saveNewInfoWithXmp()` para que el documento de salida almacene la información en formato XMP.
---
## Guardar metadatos con XMP

Utilice este flujo de trabajo cuando necesite que la información actualizada del documento se almacene en formato XMP.

### Pasos

1. Crear un `PdfFileInfo` objeto para el PDF de origen.
2. Establece los campos de metadatos que deseas actualizar, como asunto, título, palabras clave y creador.
3. Llamar `saveNewInfoWithXmp()` con la ruta del archivo de salida.
4. Cerrar el `PdfFileInfo` instancia.

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
