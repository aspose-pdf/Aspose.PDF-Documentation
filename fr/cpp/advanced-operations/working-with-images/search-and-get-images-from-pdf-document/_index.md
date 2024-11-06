---
title: Rechercher et Obtenir des Images à partir d'un Document PDF en C++
linktitle: Rechercher et Obtenir des Images
type: docs
weight: 60
url: fr/cpp/search-and-get-images-from-pdf-document/
description: Cette section explique comment rechercher et obtenir des images à partir d'un document PDF avec la bibliothèque Aspose.PDF.
lastmod: "2021-12-18"
---

L'ImagePlacementAbsorber vous permet de rechercher parmi les images sur toutes les pages d'un document PDF.

Pour rechercher des images dans un document entier :

1. Appelez la méthode [Accept](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#ae71a2782e747936e3c14b7ded5c6dc3f) de la collection [Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection). La méthode Accept prend un objet [ImagePlacementAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_absorber/) comme paramètre. Cela renvoie une collection d'objets ImagePlacement.
1. Parcourez les objets ImagePlacements et obtenez leurs propriétés (Image, dimensions, résolution, etc.).

Le fragment de code suivant montre comment rechercher un document pour toutes ses images.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void SearchAndGetImagesFromPDFDocument() {

    String _dataDir("C:\\Samples\\");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + u"SearchAndGetImages.pdf");

    // Créer un objet ImagePlacementAbsorber pour effectuer une recherche de placement d'image
    auto abs = MakeObject<ImagePlacementAbsorber>();

    // Accepter l'absorbeur pour toutes les pages
    document->get_Pages()->Accept(abs);

    // Boucler à travers tous les ImagePlacements, obtenir l'image et les propriétés de ImagePlacement
    for(auto imagePlacement : abs->get_ImagePlacements())
    {
        // Obtenir l'image en utilisant l'objet ImagePlacement
        auto image = imagePlacement->get_Image();

        // Afficher les propriétés de placement d'image pour tous les placements
        Console::WriteLine(u"largeur de l'image: {0}", imagePlacement->get_Rectangle()->get_Width());
        Console::WriteLine(u"hauteur de l'image:{0}", imagePlacement->get_Rectangle()->get_Height());
        Console::WriteLine(u"image LLX:{0}", imagePlacement->get_Rectangle()->get_LLX());
        Console::WriteLine(u"image LLY:{0}", imagePlacement->get_Rectangle()->get_LLY());
        Console::WriteLine(u"résolution horizontale de l'image:{0}", imagePlacement->get_Resolution()->get_X());
        Console::WriteLine(u"résolution verticale de l'image:{0}", imagePlacement->get_Resolution()->get_Y());
    }
}
```