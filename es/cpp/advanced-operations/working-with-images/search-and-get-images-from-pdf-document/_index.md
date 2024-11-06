---
title: Buscar y Obtener Imágenes de un Documento PDF usando C++
linktitle: Buscar y Obtener Imágenes
type: docs
weight: 60
url: es/cpp/search-and-get-images-from-pdf-document/
description: Esta sección explica cómo buscar y obtener imágenes de un documento PDF con la biblioteca Aspose.PDF.
lastmod: "2021-12-18"
---

El ImagePlacementAbsorber te permite buscar entre las imágenes en todas las páginas de un documento PDF.

Para buscar imágenes en todo el documento:

1. Llama al método [Accept](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#ae71a2782e747936e3c14b7ded5c6dc3f) de la colección [Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection). El método Accept toma un objeto [ImagePlacementAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_absorber/) como parámetro. Esto devuelve una colección de objetos ImagePlacement.
1. Recorre los objetos ImagePlacements y obtén sus propiedades (Imagen, dimensiones, resolución, etc.).

El siguiente fragmento de código muestra cómo buscar un documento para todas sus imágenes.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void SearchAndGetImagesFromPDFDocument() {

    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + u"SearchAndGetImages.pdf");

    // Crear objeto ImagePlacementAbsorber para realizar la búsqueda de colocación de imágenes
    auto abs = MakeObject<ImagePlacementAbsorber>();

    // Aceptar el absorbedor para todas las páginas
    document->get_Pages()->Accept(abs);

    // Recorre todos los ImagePlacements, obtiene la imagen y las Propiedades de ImagePlacement
    for(auto imagePlacement : abs->get_ImagePlacements())
    {
        // Obtener la imagen usando el objeto ImagePlacement
        auto image = imagePlacement->get_Image();

        // Mostrar propiedades de colocación de imagen para todas las colocaciones
        Console::WriteLine(u"ancho de la imagen: {0}", imagePlacement->get_Rectangle()->get_Width());
        Console::WriteLine(u"altura de la imagen:{0}", imagePlacement->get_Rectangle()->get_Height());
        Console::WriteLine(u"LLX de la imagen:{0}", imagePlacement->get_Rectangle()->get_LLX());
        Console::WriteLine(u"LLY de la imagen:{0}", imagePlacement->get_Rectangle()->get_LLY());
        Console::WriteLine(u"resolución horizontal de la imagen:{0}", imagePlacement->get_Resolution()->get_X());
        Console::WriteLine(u"resolución vertical de la imagen:{0}", imagePlacement->get_Resolution()->get_Y());
    }
}
```