---
title: Eliminando adjuntos de un PDF
linktitle: Eliminando adjuntos de un PDF existente
type: docs
weight: 30
url: es/cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF para C++ puede eliminar adjuntos de sus documentos PDF. Use la API de PDF en C++ para eliminar adjuntos en archivos PDF usando la biblioteca Aspose.PDF.
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF puede eliminar adjuntos de archivos PDF. Los adjuntos de un documento PDF se encuentran en la colección EmbeddedFiles del objeto Document.

Para eliminar todos los adjuntos asociados a un archivo PDF:

1. Llame al método [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection#afff8b235b554a66c203464b61204b843) de la colección [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection).
1. Guarde el archivo actualizado usando el método Save del objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

El siguiente fragmento de código muestra cómo eliminar adjuntos de un documento PDF.

```cpp
void WorkingWithAttachments::RemovingAttachment() {

 String _dataDir("C:\\Samples\\");

 // Abrir documento
 auto pdfDocument = new Document(_dataDir + u"DeleteAllAttachments.pdf");

 // Eliminar todos los adjuntos
 pdfDocument->get_EmbeddedFiles()->Delete();

 // Guardar archivo actualizado
 pdfDocument->Save(_dataDir + u"DeleteAllAttachments_out.pdf");
}
```