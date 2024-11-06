---
title: Ajouter un tampon de texte et d'image
type: docs
weight: 20
url: fr/net/add-text-and-image-stamp/
description: Cette section explique comment ajouter un tampon de texte et d'image avec Aspose.PDF Facades en utilisant la classe PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Ajouter un tampon de texte sur toutes les pages d'un fichier PDF

La classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) vous permet d'ajouter un tampon de texte sur toutes les pages d'un fichier PDF. En ordre d'ajouter un tampon de texte, vous devez d'abord créer des objets des classes [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) et [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Vous devez également créer le tampon de texte en utilisant la méthode [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) de la classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Vous pouvez définir d'autres attributs comme l'origine, la rotation, l'arrière-plan, etc. en utilisant l'objet [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Ensuite, vous pouvez ajouter le tampon dans le fichier PDF en utilisant la méthode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Le code suivant vous montre comment ajouter un tampon de texte sur toutes les pages d'un fichier PDF.

```csharp
 public static void AddTextStampOnAllPagesInPdfFile()
        {
            // Créer un objet PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Ouvrir le document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Créer un tampon
            Stamp stamp = new Stamp();
            stamp.BindLogo(new FormattedText("Hello World!", System.Drawing.Color.Blue, System.Drawing.Color.Gray, Aspose.Pdf.Facades.FontStyle.Helvetica, EncodingType.Winansi, true, 14));
            stamp.SetOrigin(10, 400);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Ajouter le tampon au fichier PDF
            fileStamp.AddStamp(stamp);

            // Enregistrer le fichier PDF mis à jour
            fileStamp.Save(_dataDir + "AddTextStamp-All_out.pdf");

            // Fermer fileStamp
            fileStamp.Close();
        }
```
## Ajouter un Tampon de Texte sur des Pages Particulières dans un Fichier PDF

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) classe vous permet d'ajouter un tampon de texte sur des pages particulières d'un fichier PDF. In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

Afin d'ajouter un tampon de texte, vous devez d'abord créer des objets des classes [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) et [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). You also need to create the text stamp using [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) method of [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class. Vous devez également créer le tampon de texte en utilisant la méthode [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) de la classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Vous pouvez définir d'autres attributs tels que l'origine, la rotation, l'arrière-plan, etc. using [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) objet également. Comme vous souhaitez ajouter un tampon de texte sur des pages particulières du fichier PDF, vous devez également définir la propriété [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) de la classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Cette propriété nécessite un tableau d'entiers contenant les numéros des pages sur lesquelles vous souhaitez ajouter le tampon. Ensuite, vous pouvez ajouter le tampon dans le fichier PDF en utilisant la méthode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). L'extrait de code suivant vous montre comment ajouter un tampon de texte sur des pages particulières dans un fichier PDF.

```csharp
 public static void AddTextStampOnParticularPagesInPdfFile()
        {
            // Créer un objet PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Ouvrir le document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Créer un tampon
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindLogo(new FormattedText("Hello World!", System.Drawing.Color.Blue, System.Drawing.Color.Gray, Aspose.Pdf.Facades.FontStyle.Helvetica, EncodingType.Winansi, true, 14));
            stamp.SetOrigin(10, 400);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Définir des pages particulières
            stamp.Pages = new int[] { 2 };

            // Ajouter le tampon au fichier PDF
            fileStamp.AddStamp(stamp);

            // Enregistrer le fichier PDF mis à jour
            fileStamp.Save(_dataDir + "AddTextStamp-Page_out.pdf");

            // Fermer fileStamp
            fileStamp.Close();
        }
```
## Ajouter un Tampon d'Image sur Toutes les Pages d'un Fichier PDF

La classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) vous permet d'ajouter un tampon d'image sur toutes les pages d'un fichier PDF. In order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

Afin d'ajouter un tampon d'image, vous devez d'abord créer des objets des classes [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) et [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Vous devez également créer le tampon d'image en utilisant la méthode [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) de la classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Vous pouvez définir d'autres attributs comme l'origine, la rotation, l'arrière-plan, etc. en utilisant également l'objet [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Ensuite, vous pouvez ajouter le tampon dans le fichier PDF en utilisant la méthode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Le fragment de code suivant vous montre comment ajouter un tampon d'image sur toutes les pages d'un fichier PDF.

```csharp
public static void AddImageStampOnAllPagesInPdfFile()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create stamp
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindImage(_dataDir + "aspose-logo.png");
            stamp.SetOrigin(10, 200);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Set particular pages
            stamp.Pages = new int[] { 2 };

            // Add stamp to PDF file
            fileStamp.AddStamp(stamp);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "AddImageStamp-Page_out.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```
### Contrôler la qualité de l'image lors de l'ajout comme tampon

Lors de l'ajout d'une image en tant qu'objet tampon, vous pouvez également contrôler la qualité de l'image. Pour répondre à cette exigence, la propriété Quality est ajoutée à la classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Elle indique la qualité de l'image en pourcentage (les valeurs valides sont 0..100).

## Ajouter un tampon d'image sur des pages particulières dans un fichier PDF

La classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) vous permet d'ajouter un tampon d'image sur des pages particulières d'un fichier PDF. In order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

Afin d'ajouter un tampon d'image, vous devez d'abord créer des objets des classes [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) et [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). You also need to create the image stamp using [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) method of [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class.  

Vous devez également créer le tampon d'image en utilisant la méthode [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) de la classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). You can set other attributes like origin, rotation, background etc.  
Vous pouvez définir d'autres attributs tels que l'origine, la rotation, l'arrière-plan, etc. using [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) objet aussi. Comme vous souhaitez ajouter un tampon d'image sur des pages particulières du fichier PDF, vous devez également définir la propriété [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) de la classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Cette propriété nécessite un tableau d'entiers contenant les numéros des pages sur lesquelles vous souhaitez ajouter le tampon. Ensuite, vous pouvez ajouter le tampon dans le fichier PDF en utilisant la méthode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Le code suivant vous montre comment ajouter un tampon d'image sur des pages particulières dans un fichier PDF.

```csharp
 public static void AddImageStampOnParticularPagesInPdfFile()
        {
            // Créer un objet PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Ouvrir le document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Créer un tampon
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindImage(_dataDir + "aspose-logo.png");
            stamp.SetOrigin(10, 200);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Ajouter le tampon au fichier PDF
            fileStamp.AddStamp(stamp);

            // Enregistrer le fichier PDF mis à jour
            fileStamp.Save(_dataDir + "AddImageStamp-All_out.pdf");

            // Fermer fileStamp
            fileStamp.Close();
        }
```