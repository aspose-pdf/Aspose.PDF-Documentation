```
---
title: Ajout d'Images et de Texte
type: docs
weight: 10
url: /net/adding-images-and-text-using-pdffilemend-class/
description: Cette section explique comment ajouter des images et du texte en utilisant la classe PdfFileMend.
lastmod: "2021-06-05"
draft: false
---

[PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) class peut vous aider à ajouter des images et du texte dans un document PDF existant, à un emplacement spécifié.
``` It provides two methods with the names [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) and [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index).  

Il fournit deux méthodes avec les noms [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) et [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index). [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) méthode vous permet d'ajouter des images de type JPG, GIF, PNG et BMP. La méthode [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index) prend un argument de type [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) classe et l'ajoute dans le fichier PDF existant. Les images et le texte peuvent être ajoutés dans une région rectangulaire spécifiée par les coordonnées des points inférieur gauche et supérieur droit. Lors de l'ajout d'images, vous pouvez spécifier soit le chemin du fichier image, soit un flux de fichier image. Afin de spécifier le numéro de page auquel l'image ou le texte doit être ajouté, ces deux méthodes fournissent un argument de numéro de page. Ainsi, vous pouvez non seulement ajouter les images et le texte à l'emplacement spécifié, mais aussi sur une page spécifiée.

Les images sont une partie importante du contenu d'un document PDF. Manipuler des images dans un fichier PDF existant est une exigence courante pour les personnes travaillant avec des fichiers PDF. Dans cet article, nous allons explorer comment les images peuvent être manipulées, dans un fichier PDF existant, à l'aide de l'[espace de noms Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) d'[Aspose.PDF pour .NET](/pdf/net/). Toutes les opérations liées aux images de l'[espace de noms Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) ont été consolidées dans cet article.

## Détails de l'implémentation

[L'espace de noms Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) vous permet d'ajouter de nouvelles images dans un fichier PDF existant. Vous pouvez également remplacer ou supprimer une image existante. Un fichier PDF peut également être converti en images. Vous pouvez soit convertir chaque page individuelle en une seule image, soit un fichier PDF complet en une image. Il vous permet de formats c'est-à-dire JPEG, BMP, PNG et TIFF etc. Vous pouvez également extraire les images d'un fichier PDF. Vous pouvez utiliser quatre classes de [espace de noms Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) pour implémenter ces opérations c'est-à-dire [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend), [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor), [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) et [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter).

## Opérations d'image

Dans cette section, nous examinerons en détail ces opérations d'image. Nous verrons également des extraits de code pour montrer l'utilisation des classes et méthodes associées. Tout d'abord, examinons l'ajout d'une image dans un fichier PDF existant. Nous pouvons utiliser la méthode [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) de la classe [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) pour ajouter une nouvelle image. En utilisant cette méthode, vous pouvez non seulement spécifier le numéro de page sur lequel vous souhaitez ajouter l'image, mais aussi spécifier l'emplacement de l'image.

## Ajouter une image dans un fichier PDF existant (Facades)

Vous pouvez utiliser la méthode [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) de la classe [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend). Le [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) méthode nécessite l'image à ajouter, le numéro de page auquel l'image doit être ajoutée et les informations de coordonnées. Après cela, enregistrez le fichier PDF mis à jour en utilisant [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/close) méthode.

Dans l'exemple suivant, nous ajoutons l'image à la page en utilisant imageStream :

```csharp
public static void AddImage01()
        {
            Document document = new Document(_dataDir + "sample.pdf");
            PdfFileMend mender = new PdfFileMend();

            // Charger l'image dans le flux
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            mender.AddImage(imageStream, 1, 10, 650, 110, 750);

            // enregistrer le fichier de sortie
            mender.Save(_dataDir + "PdfFileMend04_output.pdf");
        }
```

![Ajouter une image](/pdf/net/images/add_image1.png)

Avec l'aide de [CompositingParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilemend/addimage/methods/1), nous pouvons superposer une image sur une autre :
```csharp
public static void AddImage02()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // Charger l'image dans le flux
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // enregistrer le fichier de sortie
            mender.Save(_dataDir + "PdfFileMend05_output.pdf");
        }
```

![Ajouter une Image](/pdf/net/images/add_image2.png)

Il existe plusieurs façons de stocker une image dans un fichier PDF. Nous allons en démontrer une dans l'exemple suivant :

```csharp
public static void AddImage03()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // Charger l'image dans le flux
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Exclusion, ImageFilterType.Flate);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // enregistrer le fichier de sortie
            mender.Save(_dataDir + "PdfFileMend06_output.pdf");
        }
```

```csharp
public static void AddImage04()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // Load image into stream
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply, ImageFilterType.Flate,false);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend07_output.pdf");
        }
```

## Ajouter du texte dans un fichier PDF existant (facades)

Nous pouvons ajouter du texte de plusieurs manières. Considérez le premier. Nous prenons le [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) et l'ajoutons à la Page. Ensuite, nous indiquons les coordonnées du coin inférieur gauche, puis nous ajoutons notre texte à la Page.

```csharp
public static void AddText01()
        {
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(_dataDir + "sample.pdf");
            FormattedText message = new FormattedText("Welcome to Aspose!");

            mender.AddText(message, 1, 10, 750);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend01_output.pdf");
        }
```

Vérifiez à quoi cela ressemble :

![Ajouter du Texte](/pdf/net/images/add_text.png)

La deuxième façon d'ajouter [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). De plus, nous indiquons un rectangle dans lequel notre texte doit s'adapter.

```csharp
public static void AddText02()
        {
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(_dataDir + "sample.pdf");
            FormattedText message = new FormattedText("Welcome to Aspose! Welcome to Aspose!");

            mender.AddText(message, 1, 10, 700, 55, 810);
            mender.WrapMode = WordWrapMode.ByWords;

            // save the output file
            mender.Save(_dataDir + "PdfFileMend02_output.pdf");
        }
```
Le troisième exemple offre la possibilité d'ajouter du texte aux pages spécifiées. Dans notre exemple, ajoutons une légende sur les pages 1 et 3 du document.

```csharp
public static void AddText03()
        {
            Document document = new Document(_dataDir + "sample.pdf");
            document.Pages.Add();
            document.Pages.Add();
            document.Pages.Add();
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(document);
            FormattedText message = new FormattedText("Welcome to Aspose!");
            int[] pageNums = new int[] { 1, 3 };
            mender.AddText(message, pageNums, 10, 750, 310, 760);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend03_output.pdf");
        }
```