---
title: Travailler avec le Placement d'Image en utilisant C++
linktitle: Travailler avec le Placement d'Image
type: docs
weight: 50
url: fr/cpp/working-with-image-placement/
description: Cette section décrit les fonctionnalités du travail avec le placement d'image dans un fichier PDF en utilisant la bibliothèque C++.
lastmod: "2021-12-18"
---

**Aspose.PDF pour C++** supporte les [ImagePlacement](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement), [ImagePlacementAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_absorber) et [ImagePlacementCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_collection) qui fournissent des capacités similaires aux classes décrites ci-dessus pour obtenir la résolution et la position d'une image dans un document PDF.

- ImagePlacementAbsorber effectue une recherche d'utilisation d'image en tant que collection d'objets ImagePlacement.
- ImagePlacement fournit les membres Resolution et Rectangle qui renvoient les valeurs réelles de placement d'image.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithImagePlacement() {

    String _dataDir("C:\\Samples\\");

    // Charger le document PDF source
    auto document = MakeObject<Aspose::Pdf::Document>(_dataDir + u"ImagePlacement.pdf");

    auto abs = MakeObject<ImagePlacementAbsorber>();

    // Charger le contenu de la première page
    document->get_Pages()->idx_get(1)->Accept(abs);
    for(auto imagePlacement : abs->get_ImagePlacements())
    {
        // Obtenir les propriétés de l'image
        Console::WriteLine(u"largeur de l'image: {0}", imagePlacement->get_Rectangle()->get_Width());
        Console::WriteLine(u"hauteur de l'image:{0}", imagePlacement->get_Rectangle()->get_Height());
        Console::WriteLine(u"LLX de l'image:{0}", imagePlacement->get_Rectangle()->get_LLX());
        Console::WriteLine(u"LLY de l'image:{0}", imagePlacement->get_Rectangle()->get_LLY());
        Console::WriteLine(u"résolution horizontale de l'image:{0}", imagePlacement->get_Resolution()->get_X());
        Console::WriteLine(u"résolution verticale de l'image:{0}", imagePlacement->get_Resolution()->get_Y());

        // Récupérer l'image avec des dimensions visibles
        auto imageStream = MakeObject<System::IO::MemoryStream>();

        // Récupérer l'image depuis les ressources
        imagePlacement->get_Image()->Save(imageStream, System::Drawing::Imaging::ImageFormat::get_Png());
        auto resourceImage = System::DynamicCast< System::Drawing::Bitmap>(System::Drawing::Bitmap::FromStream(imageStream));

        // Créer un bitmap avec des dimensions réelles
        auto scaledImage = MakeObject<System::Drawing::Bitmap>(resourceImage, (int)imagePlacement->get_Rectangle()->get_Width(), (int)imagePlacement->get_Rectangle()->get_Height());
        // ...

    }

}
```