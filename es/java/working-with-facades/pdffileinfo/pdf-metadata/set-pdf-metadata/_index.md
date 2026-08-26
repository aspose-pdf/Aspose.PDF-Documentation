---
title: Set PDF Metadata
linktitle: Set PDF Metadata
type: docs
weight: 50
url: /java/set-pdf-metadata/
description: Learn how to update PDF metadata in Java with the PdfFileInfo facade.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Actualización de metadatos PDF utilizando Aspose.PDF para Java
Abstract: Aprenda cómo actualizar metadatos de PDF con Aspose.PDF para Java. El ejemplo de Java utiliza PdfFileInfo para configurar campos de metadatos estándar como asunto, título, palabras clave y creador, agrega una entrada de metadatos personalizada y guarda el resultado en un nuevo PDF.
---
## Establecer metadatos PDF

Utilice este flujo de trabajo cuando necesite normalizar o enriquecer la información del documento antes de guardar el PDF.

### Steps

1. Cree un objeto `PdfFileInfo` para el PDF de origen.
2. Set the standard metadata fields you want to update.
3. Add any custom metadata with `setMetaInfo`.
4. Save the updated document with `save()`.
5. Cierre la instancia `PdfFileInfo`.

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
