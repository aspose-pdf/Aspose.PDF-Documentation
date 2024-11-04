---
title: Ajouter un Timbre de Page PDF
type: docs
weight: 10
url: /java/add-pdf-page-stamp/
description: Cette section explique comment travailler avec Aspose.PDF Facades en utilisant la classe PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Ajouter un Timbre de Page PDF sur Toutes les Pages d'un Fichier PDF

La classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) vous permet d'ajouter un timbre de page PDF sur toutes les pages d'un fichier PDF.
 In order to add PDF page stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) et [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes. Vous devez également créer le tampon de page PDF en utilisant la méthode [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) de la classe [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Vous pouvez définir d'autres attributs comme l'origine, la rotation, l'arrière-plan, etc. en utilisant également l'objet [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Ensuite, vous pouvez ajouter le tampon dans le fichier PDF en utilisant la méthode [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Le extrait de code suivant vous montre comment ajouter un tampon de page PDF sur toutes les pages d'un fichier PDF.

```csharp
public static void AddPageStampOnAllPages()
        {
            // Créer un objet PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Ouvrir le document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Créer un tampon
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

La classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) vous permet d'ajouter un tampon de page PDF sur des pages particulières d'un fichier PDF.
 Afin d'ajouter un tampon de page PDF, vous devez d'abord créer des objets des classes [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) et [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Vous devez également créer le tampon de page PDF en utilisant la méthode [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) de la classe [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). You can set other attributes like origin, rotation, background etc.  
Vous pouvez définir d'autres attributs tels que l'origine, la rotation, l'arrière-plan, etc. using [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) objet aussi. Comme vous souhaitez ajouter un tampon de page PDF sur des pages particulières du fichier PDF, vous devez également définir la propriété [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) de la classe [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Cette propriété nécessite un tableau d'entiers contenant les numéros des pages sur lesquelles vous souhaitez ajouter le tampon. Ensuite, vous pouvez ajouter le tampon dans le fichier PDF en utilisant la méthode [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Le code suivant vous montre comment ajouter un tampon de page PDF sur des pages particulières dans un fichier PDF.

```csharp
public static void AddPageStampOnCertainPages()
        {
            // Créer un objet PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Ouvrir le document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Créer un tampon
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;
            stamp.Pages = new[] { 1, 3 };
            // Ajouter un tampon au fichier PDF
            fileStamp.AddStamp(stamp);

            // Enregistrer le fichier PDF mis à jour
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // Fermer fileStamp
            fileStamp.Close();
        }

        // Ajouter des numéros de page au PDF
        public enum PageNumPosition
        {
            PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
        }
```

## Ajouter un Numéro de Page dans un Fichier PDF (facades)

La classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) vous permet d'ajouter des numéros de page dans un fichier PDF.
 In order to add page numbers, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class.

Afin d'ajouter des numéros de page, vous devez d'abord créer un objet de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Si vous souhaitez afficher le numéro de page comme "Page X sur N", où X est le numéro de page actuel et N le nombre total de pages dans le fichier PDF, vous devez d'abord obtenir le nombre de pages en utilisant la propriété getNumberOfpages de la classe [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo). Pour obtenir le numéro de page actuel, vous pouvez utiliser le signe **#** dans votre texte où vous le souhaitez. Vous pouvez formater le texte du numéro de page en utilisant la classe [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText). Si vous voulez commencer la numérotation des pages à partir d'un numéro spécifique, vous pouvez définir la propriété setStartingNumber. Une fois que vous êtes prêt à ajouter un numéro de page dans le fichier, vous devez appeler la méthode addPageNumber de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode Save de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp).

Le fragment de code suivant vous montre comment ajouter un numéro de page dans un fichier PDF.
```java
 public static void AddPageNumberInPdfFile() {
        // Créer un objet PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Ouvrir le document
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Obtenir le nombre total de pages
        int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").getNumberOfPages();

        // Créer un texte formaté pour le numéro de page
        FormattedText formattedText = new FormattedText("Page # de " + totalPages, java.awt.Color.WHITE,
                java.awt.Color.GRAY, FontStyle.TimesBoldItalic, EncodingType.Winansi, false, 12);

        // Définir le numéro de départ pour la première page ; vous pourriez vouloir commencer à partir de 2 ou plus
        fileStamp.setStartingNumber(1);

        // Ajouter un numéro de page
        fileStamp.addPageNumber(formattedText, (int) PageNumPosition.PosUpperRight.ordinal());

        // Enregistrer le fichier PDF mis à jour
        fileStamp.save(_dataDir + "AddPageNumber_out.pdf");

        // Fermer fileStamp
        fileStamp.close();
    }
```


### Style de numérotation personnalisé

The [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) classe offre la fonctionnalité d'ajouter des informations de numéro de page en tant qu'objet tampon à l'intérieur d'un document PDF. Avant cette version, la classe ne supportait que 1,2,3,4 comme style de numérotation de page. Cependant, certains clients ont exprimé le besoin d'utiliser un style de numérotation personnalisé lors de l'ajout d'un tampon de numéro de page dans un document PDF. Pour répondre à ce besoin, la propriété [NumberingStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/numberingstyle) a été introduite, qui accepte les valeurs de l'énumération [NumberingStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/numberingstyle). Les valeurs spécifiées ci-dessous sont proposées dans cette énumération.

```java
 public static void AddCustomPageNumberInPdfFile() {
        // Créer un objet PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Ouvrir le document
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Obtenir le nombre total de pages
        int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").getNumberOfPages();

        // Créer un texte formaté pour le numéro de page
        FormattedText formattedText = new FormattedText("Page # sur " + totalPages, java.awt.Color.WHITE,
                java.awt.Color.GRAY, FontStyle.TimesBoldItalic, EncodingType.Winansi, false, 12);

        // Spécifier le style de numérotation comme Numéraux Romains Majuscules
        fileStamp.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);

        // Définir le numéro de départ pour la première page; vous pouvez vouloir commencer à partir de 2 ou plus
        fileStamp.setStartingNumber(1);

        // Ajouter le numéro de page
        fileStamp.addPageNumber(formattedText, PageNumPosition.PosUpperRight.ordinal());

        // Enregistrer le fichier PDF mis à jour
        fileStamp.save(_dataDir + "AddPageNumber_out.pdf");

        // Fermer fileStamp
        fileStamp.close();
    }
```