---
title: Establecer metadatos PDF
linktitle: Establecer metadatos PDF
type: docs
weight: 50
url: /java/set-pdf-metadata/
description: Aprenda a actualizar metadatos de PDF en Java con la fachada PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Actualización de metadatos PDF utilizando Aspose.PDF para Java
Abstract: Aprenda a actualizar metadatos de PDF con Aspose.PDF para Java. El ejemplo de Java utiliza PdfFileInfo para configurar campos de metadatos estándar como asunto, título, palabras clave y creador, agrega una entrada de metadatos personalizada y guarda el resultado en un nuevo PDF.
---
## Establecer metadatos PDF



Utilice este flujo de trabajo cuando necesite normalizar o enriquecer la información del documento antes de guardar el PDF.


### 
Pasos


1. Cree un objeto `PdfFileInfo` para el PDF de origen.

2. Configure los campos de metadatos estándar que desea actualizar.
3. Agregue cualquier metadato personalizado con `setMetaInfo`.

4. Guarde el documento actualizado con `save()`.

5. Cierre la instancia `PdfFileInfo`.


### 
Ejemplo de Java

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
