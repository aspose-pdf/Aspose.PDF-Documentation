---
title: Ajouter des tampons d'image dans un PDF par programmation
linktitle: Tampons d'image dans un fichier PDF
type: docs
weight: 10
url: /cpp/image-stamps-in-pdf-page/
description: Ajoutez le tampon d'image dans votre document PDF en utilisant la classe ImageStamp avec la bibliothèque Aspose.PDF pour C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ajouter un tampon d'image dans un fichier PDF

Vous pouvez utiliser la classe ImageStamp pour ajouter un tampon d'image à un fichier PDF. La classe ImageStamp fournit les propriétés nécessaires pour créer un tampon basé sur une image, telles que la hauteur, la largeur, l'opacité, etc.

Pour ajouter un tampon d'image :

1. Créez un objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) et un objet ImageStamp en utilisant les propriétés requises.
1. Appelez la méthode [AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) de la classe [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) pour ajouter le tampon au PDF.

Le code suivant montre comment ajouter un tampon d'image dans le fichier PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddImageStampToPDFFile()
{    
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier d'entrée
    String inputFileName("AddImageStamp.pdf");

    String outputFileName("AddImageStamp_out.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Créer un tampon d'image
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");
    imageStamp->set_Background(true);
    imageStamp->set_XIndent(100);
    imageStamp->set_YIndent(100);
    imageStamp->set_Height(48);
    imageStamp->set_Width(225);
    imageStamp->set_Rotate(Rotation::on270);
    imageStamp->set_Opacity(0.5);
   
    // Ajouter le tampon à une page particulière    
    document->get_Pages()->idx_get(1)->AddStamp(imageStamp);

    // Enregistrer le document de sortie
    document->Save(_dataDir + outputFileName);
}
```

## Contrôler la qualité de l'image lors de l'ajout de tampon

Lors de l'ajout d'une image en tant qu'objet tampon, vous pouvez contrôler la qualité de l'image. La propriété Quality de la classe [ImageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_stamp) est utilisée à cette fin. Elle indique la qualité de l'image en pourcentage (les valeurs valides sont 0..100).

```cpp
void ControlImageQualityWhenAddingStamp() {
    
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier d'entrée
    String inputFileName("AddImageStamp.pdf");
    String outputFileName("ControlImageQuality_out.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Créer un tampon d'image
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    imageStamp->set_Quality(10);
    document->get_Pages()->idx_get(1)->AddStamp(imageStamp);    
    document->Save(_dataDir + u"ControlImageQuality_out.pdf");
}
```

## Tampon d'image comme arrière-plan dans une boîte flottante

L'API Aspose.PDF vous permet d'ajouter un tampon d'image comme arrière-plan dans une boîte flottante. La propriété BackgroundImage de la classe FloatingBox peut être utilisée pour définir l'image de fond d'un bloc flottant comme montré dans l'exemple de code suivant.

```cpp
void ImageStampAsBackgroundInFloatingBox() {
    
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier d'entrée
    String inputFileName("AddImageStamp.pdf");
    String outputFileName("AddImageStampAsBackgroundInFloatingBox_out.pdf");

    // Instancier l'objet Document
    auto document = MakeObject<Document>();

    // Ajouter une page au document PDF
    auto page = document->get_Pages()->Add();

    // Créer l'objet FloatingBox
    auto aBox = MakeObject<FloatingBox>(200, 100);

    // Définir la position gauche pour le FloatingBox
    aBox->set_Left(40);
    // Définir la position supérieure pour le FloatingBox
    aBox->set_Top(80);
    // Définir l'alignement horizontal pour le FloatingBox
    aBox->set_HorizontalAlignment(HorizontalAlignment::Center);
    
    // Ajouter un fragment de texte à la collection de paragraphes du FloatingBox    
    aBox->get_Paragraphs()->Add(MakeObject<TextFragment>(u"main text"));

    // Définir la bordure pour le FloatingBox
    aBox->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));

    // Ajouter l'image de fond
    auto image = MakeObject<Image>();
    image->set_File(_dataDir + u"aspose-logo.png");
    aBox->set_BackgroundImage(image);

    // Définir la couleur de fond pour le FloatingBox
    aBox->set_BackgroundColor(Color::get_Yellow());

    // Ajouter le FloatingBox à la collection de paragraphes de l'objet page
    page->get_Paragraphs()->Add(aBox);
    // Enregistrer le document PDF
    document->Save(_dataDir + outputFileName);
}
```