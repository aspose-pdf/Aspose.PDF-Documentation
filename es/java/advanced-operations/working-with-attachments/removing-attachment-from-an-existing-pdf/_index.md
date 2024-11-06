---
title: Eliminando adjunto de un PDF existente
linktitle: Eliminando adjunto de un PDF existente
type: docs
weight: 30
url: es/java/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF puede eliminar adjuntos de tus documentos PDF. Usa la API de PDF de Java para eliminar adjuntos en archivos PDF con la biblioteca Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF puede eliminar adjuntos de archivos PDF. Los adjuntos de un documento PDF se mantienen en la colección EmbeddedFiles del objeto Document.

Los adjuntos de un documento PDF se mantienen en la colección [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Para eliminar todos los adjuntos asociados con un archivo PDF:

1. Llama al método delete(..) de la colección [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection).

1. Guarde el archivo actualizado usando el método save del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

El siguiente fragmento de código muestra cómo eliminar todos los adjuntos de un documento PDF.

```java
   public static void DeleteAllAttachmentsFromPDF(){
  // Abrir un documento
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // Eliminar todos los adjuntos
  pdfDocument.getEmbeddedFiles().delete();
  // Guardar el archivo actualizado
  pdfDocument.save("output.pdf");

    }
```