---
title: Trabajando con la Colocación de Imágenes usando C++
linktitle: Trabajando con la Colocación de Imágenes
type: docs
weight: 50
url: /es/cpp/working-with-image-placement/
description: Esta sección describe las características de trabajar con la colocación de imágenes en un archivo PDF usando la biblioteca C++.
lastmod: "2021-12-18"
---

**Aspose.PDF para C++** soporta [ImagePlacement](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement), [ImagePlacementAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_absorber) y [ImagePlacementCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_collection) que proporcionan una capacidad similar a las clases descritas anteriormente para obtener la resolución y posición de una imagen en un documento PDF.

- ImagePlacementAbsorber realiza la búsqueda de uso de imágenes como la colección de objetos ImagePlacement.
- ImagePlacement proporciona los miembros Resolution y Rectangle que devuelven los valores reales de colocación de la imagen.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithImagePlacement() {

    String _dataDir("C:\\Samples\\");

    // Cargar el documento PDF de origen
    auto document = MakeObject<Aspose::Pdf::Document>(_dataDir + u"ImagePlacement.pdf");

    auto abs = MakeObject<ImagePlacementAbsorber>();

    // Cargar el contenido de la primera página
    document->get_Pages()->idx_get(1)->Accept(abs);
    for(auto imagePlacement : abs->get_ImagePlacements())
    {
        // Obtener propiedades de la imagen
        Console::WriteLine(u"ancho de la imagen: {0}", imagePlacement->get_Rectangle()->get_Width());
        Console::WriteLine(u"altura de la imagen: {0}", imagePlacement->get_Rectangle()->get_Height());
        Console::WriteLine(u"LLX de la imagen: {0}", imagePlacement->get_Rectangle()->get_LLX());
        Console::WriteLine(u"LLY de la imagen: {0}", imagePlacement->get_Rectangle()->get_LLY());
        Console::WriteLine(u"resolución horizontal de la imagen: {0}", imagePlacement->get_Resolution()->get_X());
        Console::WriteLine(u"resolución vertical de la imagen: {0}", imagePlacement->get_Resolution()->get_Y());

        // Recuperar imagen con dimensiones visibles
        auto imageStream = MakeObject<System::IO::MemoryStream>();

        // Recuperar imagen de los recursos
        imagePlacement->get_Image()->Save(imageStream, System::Drawing::Imaging::ImageFormat::get_Png());
        auto resourceImage = System::DynamicCast< System::Drawing::Bitmap>(System::Drawing::Bitmap::FromStream(imageStream));

        // Crear bitmap con dimensiones reales
        auto scaledImage = MakeObject<System::Drawing::Bitmap>(resourceImage, (int)imagePlacement->get_Rectangle()->get_Width(), (int)imagePlacement->get_Rectangle()->get_Height());
        // ...

    }

}
```