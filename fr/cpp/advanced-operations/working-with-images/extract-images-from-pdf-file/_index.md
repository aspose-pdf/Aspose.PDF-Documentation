---
title: Extraire des images d'un fichier PDF en utilisant C++
linktitle: Extraire des images
type: docs
weight: 30
url: fr/cpp/extract-images-from-pdf-file/
description: Cette section montre comment extraire des images d'un fichier PDF en utilisant une bibliothèque C++.
lastmod: "2021-12-18"
---

Vous pouvez utiliser Aspose.PDF pour C++ pour extraire toutes les images de vos documents PDF en fichiers séparés qui peuvent être réutilisés dans d'autres programmes.

Les images sont contenues dans la collection Images de la collection Resources de chaque page. Pour extraire une page particulière, obtenez ensuite l'image de la collection Images en utilisant l'index particulier de l'image.

L'index de l'image renvoie un objet [XImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image). Cet objet fournit une méthode Save qui peut être utilisée pour enregistrer l'image extraite.

Le code suivant montre comment extraire des images d'un fichier PDF.

```cpp
void WorkingWithImages::ExtractImages()
{
    String _dataDir("C:\\Samples\\");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + u"ExtractImages.pdf");

    // Extraire une image particulière
    auto xImage = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(1);

    auto outputImage = System::IO::File::OpenWrite(_dataDir + u"output.jpg");

    // Enregistrer l'image de sortie
    xImage->Save(outputImage, System::Drawing::Imaging::ImageFormat::get_Jpeg());
    outputImage->Close();

    // Enregistrer le fichier PDF mis à jour
    document->Save(_dataDir + u"ExtractImages_out.pdf");
}
```