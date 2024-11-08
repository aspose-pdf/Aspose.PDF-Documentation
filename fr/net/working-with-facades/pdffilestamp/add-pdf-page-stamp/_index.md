---
title: Ajouter un Timbre de Page PDF
type: docs
weight: 10
url: /fr/net/add-pdf-page-stamp/
description: Cette section explique comment travailler avec Aspose.PDF Facades en utilisant la classe PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Ajouter un Timbre de Page PDF sur Toutes les Pages d'un Fichier PDF

La classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) vous permet d'ajouter un timbre de page PDF sur toutes les pages d'un fichier PDF. In order to add PDF page stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) et des classes [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Vous devez également créer le tampon de page PDF en utilisant la méthode [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) de la classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Vous pouvez définir d'autres attributs comme l'origine, la rotation, l'arrière-plan, etc. en utilisant également l'objet [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Ensuite, vous pouvez ajouter le tampon dans le fichier PDF en utilisant la méthode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Le code suivant vous montre comment ajouter un tampon de page PDF sur toutes les pages d'un fichier PDF.

```csharp
public static void AddPageStampOnAllPages()
        {
            // Créer un objet PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Ouvrir le document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Créer le tampon
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Ajouter le tampon au fichier PDF
            fileStamp.AddStamp(stamp);

            // Enregistrer le fichier PDF mis à jour
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // Fermer fileStamp
            fileStamp.Close();
        }
```
## Ajouter un Tampon de Page PDF sur des Pages Particulières dans un Fichier PDF

La classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) vous permet d'ajouter un tampon de page PDF sur des pages particulières d'un fichier PDF. In order to add PDF page stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

Afin d'ajouter un tampon de page PDF, vous devez d'abord créer des objets des classes [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) et [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). You also need to create the PDF page stamp using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method of [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class.

Vous devez également créer le tampon de page PDF à l'aide de la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) de la classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). You can set other attributes like origin, rotation, background etc.

Vous pouvez définir d'autres attributs comme l'origine, la rotation, l'arrière-plan, etc. using [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) objet également. Comme vous souhaitez ajouter un tampon de page PDF sur des pages particulières du fichier PDF, vous devez également définir la propriété [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) de la classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Cette propriété nécessite un tableau d'entiers contenant les numéros des pages sur lesquelles vous souhaitez ajouter le tampon. Ensuite, vous pouvez ajouter le tampon dans le fichier PDF en utilisant la méthode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). L'extrait de code suivant vous montre comment ajouter un tampon de page PDF sur des pages particulières dans un fichier PDF.

```csharp
public static void AddPageStampOnCertainPages()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create stamp
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;
            stamp.Pages = new[] { 1, 3 };
            // Add stamp to PDF file
            fileStamp.AddStamp(stamp);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // Close fileStamp
            fileStamp.Close();
        }

        // Add PDF Page Numbers
        public enum PageNumPosition
        {
            PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
        }
```
## Ajouter un Numéro de Page dans un Fichier PDF

La classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) vous permet d'ajouter des numéros de page dans un fichier PDF. In order to add page numbers, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class.

Pour ajouter des numéros de page, vous devez d'abord créer un objet de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). If you want to show page number like “Page X of N” while X being the current page number and N the total number of pages in the PDF file then you first need to get the page count using [NumberOfpages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages) property of [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) class.

Si vous voulez afficher le numéro de page comme “Page X sur N” où X est le numéro de la page actuelle et N le nombre total de pages dans le fichier PDF, vous devez d'abord obtenir le nombre de pages en utilisant la propriété [NumberOfpages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages) de la classe [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo). Afin d'obtenir le numéro de page actuel, vous pouvez utiliser le signe **#** dans votre texte où vous le souhaitez. Vous pouvez formater le texte du numéro de page en utilisant la classe [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). Si vous souhaitez commencer la numérotation des pages à partir d'un numéro spécifique, vous pouvez définir la propriété [StartingNumber](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/properties/startingnumber). Une fois que vous êtes prêt à ajouter le numéro de page dans le fichier, vous devez appeler la méthode [AddPageNumber](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addpagenumber/methods/7) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Le code suivant vous montre comment ajouter un numéro de page dans un fichier PDF.

```csharp
 public static void AddPageNumberInPdfFile()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Get total number of pages
            int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").NumberOfPages;

            // Create formatted text for page number
            FormattedText formattedText = new FormattedText($"Page # of {totalPages}",
                System.Drawing.Color.AntiqueWhite,
                System.Drawing.Color.Gray,
                FontStyle.TimesBoldItalic,
                EncodingType.Winansi, false, 12);

            // Set starting number for first page; you might want to start from 2 or more
            fileStamp.StartingNumber = 1;

            // Add page number
            fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "AddPageNumber_out.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```
### Style de Numérotation Personnalisée

La classe PdfFileStamp offre la fonctionnalité d'ajouter des informations de numéro de page en tant qu'objet de tampon à l'intérieur d'un document PDF. Avant cette version, la classe ne supportait que 1,2,3,4 comme style de numérotation de page. Cependant, certains clients ont exprimé le besoin d'utiliser un style de numérotation personnalisé lors de l'ajout d'un tampon de numéro de page dans un document PDF. Pour répondre à cette exigence, la propriété [NumberingStyle](https://reference.aspose.com/pdf/net/aspose.pdf/numberingstyle) a été introduite, qui accepte les valeurs de l'énumération [NumberingStyle](https://reference.aspose.com/pdf/net/aspose.pdf/numberingstyle). Les valeurs proposées dans cette énumération sont spécifiées ci-dessous.

- LettresMinuscules
- LettresMajuscules
- ChiffresArabes
- ChiffresRomainsMinuscules
- ChiffresRomainsMajuscules

```csharp
 public static void AddCustomPageNumberInPdfFile()
        {
            // Créer un objet PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Ouvrir le document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Obtenir le nombre total de pages
            int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").NumberOfPages;

            // Créer un texte formaté pour le numéro de page
            FormattedText formattedText = new FormattedText($"Page # of {totalPages}",
                System.Drawing.Color.AntiqueWhite,
                System.Drawing.Color.Gray,
                FontStyle.TimesBoldItalic,
                EncodingType.Winansi, false, 12);

            // Spécifier le style de numérotation comme Chiffres Romains Majuscules
            fileStamp.NumberingStyle = Aspose.Pdf.NumberingStyle.NumeralsRomanUppercase;

            // Définir le numéro de départ pour la première page; vous pourriez vouloir commencer à partir de 2 ou plus
            fileStamp.StartingNumber = 1;

            // Ajouter le numéro de page
            fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

            // Enregistrer le fichier PDF mis à jour
            fileStamp.Save(_dataDir + "AddPageNumber_out.pdf");

            // Fermer le fileStamp
            fileStamp.Close();
        }
```