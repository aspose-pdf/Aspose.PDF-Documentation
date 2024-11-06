---
title: Ajouter une Image au PDF en utilisant C++
linktitle: Ajouter Image
type: docs
weight: 10
url: fr/cpp/add-image-to-existing-pdf-file/
description: Cette section décrit comment ajouter une image à un fichier PDF existant en utilisant la bibliothèque C++.
lastmod: "2021-12-18"
---

## Ajouter une Image dans un Fichier PDF Existant

Chaque page PDF contient des propriétés Resources et Contents. Les ressources peuvent être des images et des formulaires par exemple, tandis que le contenu est représenté par un ensemble d'opérateurs PDF. Chaque opérateur a son nom et argument. Cet exemple utilise des opérateurs pour ajouter une image à un fichier PDF.

Pour ajouter une image à un fichier PDF existant :

- Créez un objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) et ouvrez le document PDF d'entrée.
- Obtenez la page à laquelle vous souhaitez ajouter une image.
- Ajoutez l'image dans la collection Resources de la page.
- Utilisez des opérateurs pour placer l'image sur la page :
- Utilisez l'opérateur [GSave](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save/) pour sauvegarder l'état graphique actuel.

- Utilisez l'opérateur [ConcatenateMatrix](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.concatenate_matrix#a40ca09b1fa45560d57a1fd042d3fbe96) pour spécifier où l'image doit être placée.
- Utilisez l'[opérateur Do](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.do/) pour dessiner l'image sur la page.
- Enfin, utilisez l'[opérateur GRestore](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore/) pour enregistrer l'état graphique mis à jour.
- Enregistrez le fichier.
L'extrait de code suivant montre comment ajouter l'image dans un document PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithImages::AddImageToExistingPDF()
{
    String _dataDir("C:\\Samples\\");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + u"AddImage.pdf");

    // Définir les coordonnées
    int lowerLeftX = 50;
    int lowerLeftY = 750;
    int upperRightX = 100;
    int upperRightY = 800;

    // Obtenez la page à laquelle vous souhaitez ajouter l'image
    auto page = document->get_Pages()->idx_get(1);

    // Charger l'image dans le flux
    auto imageStream = System::IO::File::OpenRead(_dataDir + u"logo.png");

    // Ajouter une image à la collection Images des ressources de la page
    page->get_Resources()->get_Images()->Add(imageStream);

    // Utilisation de l'opérateur GSave : cet opérateur enregistre l'état graphique actuel
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

    // Créer des objets Rectangle et Matrix
    auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);

    auto matrix = MakeObject<Matrix>(
        MakeArray<double>({
            rectangle->get_URX() - rectangle->get_LLX(),
            0,                  0,
            rectangle->get_URY() - rectangle->get_LLY(),
            rectangle->get_LLX(), rectangle->get_LLY() }));

    // Utilisation de l'opérateur ConcatenateMatrix (concaténer la matrice) :
    // définit comment l'image doit être placée
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
    auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());

    // Utilisation de l'opérateur Do : cet opérateur dessine l'image
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));

    // Utilisation de l'opérateur GRestore : cet opérateur restaure l'état graphique
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // Enregistrez le nouveau PDF
    document->Save(_dataDir + u"updated_document.pdf");

    // Fermer le flux d'image
    imageStream->Close();
}
```

## Ajouter la Référence d'une Image Unique Plusieurs Fois dans un Document PDF

Parfois, nous avons besoin d'utiliser la même image plusieurs fois dans un document PDF. Ajouter une nouvelle instance augmente la taille du document PDF résultant. La méthode [XImageCollection.Add(XImage)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image/) permet d'ajouter une référence au même objet PDF que l'image originale, ce qui optimise la taille du document PDF.

```cpp
void WorkingWithImages::AddReferenceOfaSingleImageMultipleTimes() {

    String _dataDir("C:\\Samples\\");
    auto imageRectangle = MakeObject<Rectangle>(0, 0, 30, 15);

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    document->get_Pages()->Add();
    document->get_Pages()->Add();

    auto imageStream = System::IO::File::OpenRead(_dataDir + u"aspose-logo.png");

    SharedPtr<Aspose::Pdf::XImage> image;

    for (auto page : document->get_Pages()) {
        auto annotation = MakeObject<Aspose::Pdf::Annotations::WatermarkAnnotation>(page, page->get_Rect());
        auto form = annotation->get_Appearance()->idx_get(u"N");
        form->set_BBox(page->get_Rect());
        String name;
        if (image != nullptr) {
            name = form->get_Resources()->get_Images()->Add(imageStream);
            image = form->get_Resources()->get_Images()->idx_get(name);
        }
        else {
            form->get_Resources()->get_Images()->AddWithName(image);
        }
        form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
        form->get_Contents()->Add(
            MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(
                MakeObject<Matrix>(imageRectangle->get_Width(), 0, 0, imageRectangle->get_Height(), 0, 0)));

        form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(name));
        form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());
        page->get_Annotations()->Add(annotation, false);
        imageRectangle = MakeObject<Rectangle>(0, 0, imageRectangle->get_Width() * 1.01, imageRectangle->get_Height() * 1.01);
    }
    document->Save(_dataDir + u"AddReferenceOfaSingleImageMultipleTimes_out.pdf");
}
```

## Placer une image sur la page et préserver (contrôler) le ratio d'aspect

Si nous ne connaissons pas les dimensions de l'image, il y a une forte probabilité d'obtenir une image déformée sur la page. L'exemple suivant montre l'une des façons d'éviter cela.

```cpp
void WorkingWithImages::AddingImageAndPreserveAspectRatioIntoPDF() {

    String _dataDir("C:\\Samples\\");

    auto bitmap = System::Drawing::Image::FromFile(_dataDir + u"3410492.jpg");

    int width;
    int height;

    width = bitmap->get_Width();
    height = bitmap->get_Height();

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    int scaledWidth = 400;
    int scaledHeight = scaledWidth * height / width;

    page->AddImage(_dataDir + u"3410492.jpg", new Rectangle(10, 10, scaledWidth, scaledHeight));
    document->Save(_dataDir + u"sample_image.pdf");
}
```

## Identifier si l'image dans le PDF est en couleur ou en noir et blanc

Pour réduire la taille de l'image, vous devez la compresser. Avant de pouvoir déterminer le type de compression d'une image, vous devez savoir si elle est en couleur ou en noir et blanc.

Le type de compression appliqué à l'image dépend de l'espace colorimétrique de l'image originale, c'est-à-dire si l'image est en couleur (RGB) alors utilisez la compression JPEG2000, et si elle est en noir et blanc alors utilisez la compression JBIG2 / JBIG2000.

Un fichier PDF peut contenir des éléments de texte, d'image, de graphique, de pièce jointe, d'annotation, etc., et si le fichier PDF source contient des images, nous pouvons déterminer l'espace colorimétrique de l'image et appliquer la compression appropriée pour l'image afin de réduire la taille du fichier PDF.

L'extrait de code suivant montre les étapes pour identifier si l'image à l'intérieur du PDF est en couleur ou en noir et blanc.

```cpp
void WorkingWithImages::CheckColors() {

    String _dataDir("C:\\Samples\\");
    auto document = MakeObject<Document>(_dataDir + u"test4.pdf");
    try {
        // itérer à travers toutes les pages du fichier PDF
        for (auto page : document->get_Pages()) {
            // créer une instance d'absorbeur de placement d'image
            auto abs = MakeObject<ImagePlacementAbsorber>();
            page->Accept(abs);

            for (auto ia : abs->get_ImagePlacements()) {
                /* ColorType */
                auto colorType = ia->get_Image()->GetColorType();
                switch (colorType) {
                case ColorType::Grayscale:
                    Console::WriteLine(u"Image en niveaux de gris");
                    break;
                case ColorType::Rgb:
                    Console::WriteLine(u"Image en couleur");
                    break;
                }
            }
        }
    }
    catch (Exception ex) {
        Console::WriteLine(u"Erreur de lecture du fichier = {0}", document->get_FileName());
    }
}
```
## Contrôler la Qualité de l'Image

Il est possible de contrôler la qualité d'une image qui est ajoutée à un fichier PDF. Utilisez la méthode surchargée [Replace](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection#a698b65051b073f0f4b84b1235889bd72) dans la classe [XImageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection).

L'extrait de code suivant démontre comment convertir toutes les images du document en JPEGs qui utilisent 80% de qualité pour la compression.

```cpp
void WorkingWithImages::ControlImageQuality() {

    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample_with_images.pdf");

    for (auto page : document->get_Pages())
    {
        int idx = 1;
        for (auto image : page->get_Resources()->get_Images())
        {
            auto imageStream = MakeObject<System::IO::MemoryStream>();
            image->Save(imageStream, System::Drawing::Imaging::ImageFormat::get_Jpeg());
            page->get_Resources()->get_Images()->Replace(idx, imageStream, 80);
            idx = idx + 1;
        }
    }

    document->Save(_dataDir + u"sample_with_images_out.pdf");
}
```