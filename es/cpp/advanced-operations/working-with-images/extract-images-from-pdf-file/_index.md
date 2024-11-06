---
title: Extraer Imágenes de Archivo PDF usando C++
linktitle: Extraer Imágenes
type: docs
weight: 30
url: es/cpp/extract-images-from-pdf-file/
description: Esta sección muestra cómo extraer imágenes de un archivo PDF usando la biblioteca C++.
lastmod: "2021-12-18"
---

Puede usar Aspose.PDF para C++ para extraer todas las imágenes de sus documentos PDF en archivos separados que se pueden reutilizar en otros programas.

Las imágenes se mantienen en la colección de Recursos de cada página en la colección de Imágenes. Para extraer una página en particular, obtenga la imagen de la colección de Imágenes usando el índice particular de la imagen.

El índice de la imagen devuelve un objeto [XImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image). Este objeto proporciona un método Save que se puede usar para guardar la imagen extraída.

El siguiente fragmento de código muestra cómo extraer imágenes de un archivo PDF.

```cpp
void WorkingWithImages::ExtractImages()
{
    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + u"ExtractImages.pdf");

    // Extraer una imagen particular
    auto xImage = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(1);

    auto outputImage = System::IO::File::OpenWrite(_dataDir + u"output.jpg");

    // Guardar imagen de salida
    xImage->Save(outputImage, System::Drawing::Imaging::ImageFormat::get_Jpeg());
    outputImage->Close();

    // Guardar archivo PDF actualizado
    document->Save(_dataDir + u"ExtractImages_out.pdf");
}
```