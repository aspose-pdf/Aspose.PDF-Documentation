---
title: Extraire des images d'un PDF 
linktitle: Extraire des images d'un PDF
type: docs
weight: 20
url: fr/cpp/extract-images-from-the-pdf-file/
description: Comment extraire une partie de l'image d'un PDF en utilisant Aspose.PDF pour C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aussi, une tâche demandée lors du travail avec des documents PDF est d'extraire des images d'un fichier PDF. Par exemple, vous avez reçu un e-mail PDF avec beaucoup de belles images que vous souhaitez extraire en tant que fichiers séparés.

La bibliothèque Aspose.PDF vous permet d'extraire des images d'un PDF avec le code suivant :

```cpp
void ExtractImage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Parsing\\");

    // Chaîne pour le nom du fichier
    String infilename("sample-image.pdf");
    String outfilename("extracted_image.jpeg");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Extraire une image particulière
    auto xImage = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(1);

    auto outputImage = System::IO::File::OpenWrite(_dataDir + outfilename);

    // Sauvegarder l'image de sortie
    xImage->Save(outputImage, System::Drawing::Imaging::ImageFormat::get_Jpeg());
    outputImage->Close();

    std::clog << __func__ << ": Finish" << std::endl;
}
```