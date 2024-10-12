---
title: Définir la Taille de l'Image avec C++
linktitle: Définir la Taille de l'Image
type: docs
weight: 80
url: /cpp/set-image-size/
description: Cette section décrit comment définir la taille de l'image dans un fichier PDF en utilisant la bibliothèque C++.
lastmod: "2021-12-18"
---

Il est possible de définir la taille d'une image qui est ajoutée à un fichier PDF. Pour définir la taille, vous pouvez utiliser les propriétés [FixWidth](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image#a08f2f92b184632385eab19fb96c6d40e) et [FixHeight](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image#aed67b52e058b97df6931c214d7092dfa) de la [Classe Aspose.Pdf.Image](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image).

Le code suivant démontre comment définir la taille d'une image :

```cpp
void WorkingWithImages::ExampleSetImageSize()
{
    String _dataDir("C:\\Samples\\");
    // Instancier l'objet Document
    auto document = MakeObject<Document>();
    // ajouter une page à la collection de pages du fichier PDF
    auto page = document->get_Pages()->Add();
    // Créer une instance d'image
    auto img = MakeObject<Image>();
    // Définir la largeur et la hauteur de l'image en points
    img->set_FixWidth(100);
    img->set_FixHeight(100);
    // Définir le type d'image en tant que SVG
    img->set_FileType(Aspose::Pdf::ImageFileType::Unknown);
    // Chemin pour le fichier source
    img->set_File(_dataDir + u"aspose-logo.jpg");
    page->get_Paragraphs()->Add(img);
    // Définir les propriétés de la page
    page->get_PageInfo()->set_Width(800);
    page->get_PageInfo()->set_Height(800);
    // enregistrer le fichier PDF résultant
    document->Save(_dataDir + u"SetImageSize_out.pdf");
}
```