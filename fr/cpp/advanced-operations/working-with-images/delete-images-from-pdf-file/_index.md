---
title: Supprimer des Images d'un Fichier PDF en utilisant C++
linktitle: Supprimer des Images
type: docs
weight: 20
url: fr/cpp/delete-images-from-pdf-file/
description: Cette section explique comment supprimer des images d'un fichier PDF en utilisant Aspose.PDF pour C++.
lastmod: "2021-12-18"
---

Pour supprimer une image d'un fichier PDF :

1. Créez un objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) et ouvrez le fichier PDF d'entrée.
1. Obtenez la page qui contient l'image à partir de la [collection de pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) de l'objet Document.
1. Les images sont contenues dans la collection d'Images, qui se trouve dans la collection de Ressources de la page.
1. Supprimez une image avec la méthode Delete de la collection d'Images.
1. Enregistrez la sortie en utilisant la méthode Save de l'objet Document.

Le snippet de code suivant montre comment supprimer une image d'un fichier PDF.

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