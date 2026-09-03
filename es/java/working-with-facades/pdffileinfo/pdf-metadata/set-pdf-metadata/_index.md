---
title: Establecer metadatos PDF
linktitle: Establecer metadatos PDF
type: docs
weight: 50
url: /es/java/set-pdf-metadata/
description: Aprenda cómo actualizar los metadatos PDF en Java con la fachada PdfFileInfo.
lastmod: "2026-09-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Actualizando metadatos PDF usando Aspose.PDF for Java
Abstract: Aprenda cómo actualizar los metadatos PDF con Aspose.PDF for Java. El ejemplo en Java usa PdfFileInfo para establecer campos estándar de metadatos como asunto, título, palabras clave y creador, agrega una entrada de metadatos personalizada y guarda el resultado en un nuevo PDF.
---
## Establecer metadatos PDF

Utilice este flujo de trabajo cuando necesite normalizar o enriquecer la información del documento antes de guardar el PDF.

### Pasos

1. Crear un `PdfFileInfo` objeto para el PDF de origen.
2. Establezca los campos de metadatos estándar que desea actualizar.
3. Agregue cualquier metadato personalizado con `setMetaInfo`.
4. Guardar el documento actualizado con `save()`.
5. Cerrar el `PdfFileInfo` instancia.

### Ejemplo de Java

```java
public static void setPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.setSubject("Aspose PDF for Java");
    pdfInfo.setTitle("Aspose PDF for Java");
    pdfInfo.setKeywords("Aspose, PDF, Java");
    pdfInfo.setCreator("Aspose Team");
    pdfInfo.setMetaInfo("CustomKey", "CustomValue");
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
