---
title: Eliminar Imágenes de un Archivo PDF usando C++
linktitle: Eliminar Imágenes
type: docs
weight: 20
url: es/cpp/delete-images-from-pdf-file/
description: Esta sección explica cómo eliminar imágenes de un archivo PDF usando Aspose.PDF para C++.
lastmod: "2021-12-18"
---

Para eliminar una imagen de un archivo PDF:

1. Cree un objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) y abra el archivo PDF de entrada.
1. Obtenga la página que contiene la imagen de la [colección de páginas](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) del objeto Document.
1. Las imágenes se mantienen en la colección de Imágenes, que se encuentra en la colección de Recursos de la página.
1. Elimine una imagen con el método Delete de la colección de Imágenes.
1. Guarde el resultado como usando el método Save del objeto Document.

El siguiente fragmento de código muestra cómo eliminar una imagen de un archivo PDF.

```cpp
void WorkingWithImages::DeleteImagesFromPDFFile()
{
    String _dataDir("C:\\Samples\\");

    // Open document
    auto document = MakeObject<Document>(_dataDir + u"DeleteImages.pdf");

    // Delete a particular image
    document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->Delete(1);

    // Save updated PDF file
    document->Save(_dataDir + u"DeleteImages_out.pdf");
}
```