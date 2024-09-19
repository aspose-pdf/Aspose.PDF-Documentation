---
title: Extraire des images d'un PDF en C#
linktitle: Extraire des images d'un PDF
type: docs
weight: 20
url: /net/extract-images-from-the-pdf-file/
description: Comment extraire une partie de l'image d'un PDF en utilisant Aspose.PDF pour .NET en C#
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Les images sont stockées dans la collection [Images](https://reference.aspose.com/pdf/net/aspose.pdf/resources/properties/images) de la collection [Resources](https://reference.aspose.com/pdf/net/aspose.pdf/resources) de chaque page. Pour extraire une page spécifique, puis obtenir l'image de la collection Images en utilisant l'index spécifique de l'image.

L'index de l'image renvoie un objet [XImage](https://reference.aspose.com/pdf/net/aspose.pdf/ximage). Cet objet fournit une méthode Save qui peut être utilisée pour sauvegarder l'image extraite. Le fragment de code suivant montre comment extraire des images d'un fichier PDF.

Ce fragment de code fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
```

// Pour des exemples complets et des fichiers de données, veuillez consulter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Ouvrir le document
Document pdfDocument = new Document(dataDir+ "ExtractImages.pdf");

// Extraire une image particulière
XImage xImage = pdfDocument.Pages[1].Resources.Images[1];

FileStream outputImage = new FileStream(dataDir + "output.jpg", FileMode.Create);

// Sauvegarder l'image de sortie
xImage.Save(outputImage, ImageFormat.Jpeg);
outputImage.Close();

dataDir = dataDir + "ExtractImages_out.pdf";

// Sauvegarder le fichier PDF mis à jour
pdfDocument.Save(dataDir);
```
