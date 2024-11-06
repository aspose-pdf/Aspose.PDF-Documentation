---
title: Gérer l'en-tête et le pied de page
type: docs
weight: 40
url: fr/net/manage-header-and-footer/
description: Cette section explique comment gérer l'en-tête et le pied de page avec Aspose.PDF Facades en utilisant la classe PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Ajouter un en-tête dans un fichier PDF

La classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) vous permet d'ajouter un en-tête dans un fichier PDF. In order to add header, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class.

Afin d'ajouter un en-tête, vous devez d'abord créer un objet de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Vous pouvez formater le texte de l'en-tête en utilisant la classe [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). Une fois que vous êtes prêt à ajouter un en-tête dans le fichier, vous devez appeler la méthode [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/constructors/main). Vous devez également spécifier au moins la marge supérieure dans la méthode [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/constructors/main). L'extrait de code suivant vous montre comment ajouter un en-tête dans un fichier PDF.

```csharp
 public static void AddHeader()
        {
            // Créer un objet PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Ouvrir le document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Créer un texte formaté pour le numéro de page
            FormattedText formattedText = new FormattedText("Aspose - Vos experts en format de fichier !",
                System.Drawing.Color.Yellow,
                System.Drawing.Color.Black,
                FontStyle.Courier,
                EncodingType.Winansi, false, 14);

            // Ajouter un en-tête
            fileStamp.AddHeader(formattedText, 10);

            // Enregistrer le fichier PDF mis à jour
            fileStamp.Save(_dataDir + "AddHeader_out.pdf");

            // Fermer fileStamp
            fileStamp.Close();
        }
```
## Ajouter un pied de page dans un fichier PDF

La classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) vous permet d'ajouter un pied de page dans un fichier PDF. ```
In order to add footer, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class.

Pour ajouter un pied de page, vous devez d'abord créer un objet de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main).
``` Vous pouvez formater le texte du pied de page en utilisant la classe [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). Une fois que vous êtes prêt à ajouter un pied de page dans le fichier, vous devez appeler la méthode [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Vous devez également spécifier au moins la marge inférieure dans la méthode [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Le code suivant vous montre comment ajouter un pied de page dans un fichier PDF.

```csharp
 public static void AddFooter()
        {
            // Créer l'objet PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Ouvrir le document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Créer un texte formaté pour le numéro de page
            FormattedText formattedText = new FormattedText("Aspose - Vos experts en format de fichiers!",
                System.Drawing.Color.Blue,
                System.Drawing.Color.Gray,
                FontStyle.Courier,
                EncodingType.Winansi, false, 14);

            // Ajouter un pied de page
            fileStamp.AddFooter(formattedText, 10);

            // Enregistrer le fichier PDF mis à jour
            fileStamp.Save(_dataDir + "AddFooter_out.pdf");

            // Fermer fileStamp
            fileStamp.Close();
        }
```
## Ajouter une Image dans l'En-tête d'un Fichier PDF Existant

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) classe vous permet d'ajouter une image dans l'en-tête d'un fichier PDF. Afin d'ajouter une image dans l'en-tête, vous devez d'abord créer un objet de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Après cela, vous devez appeler la méthode [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Vous pouvez passer l'image à la méthode [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Le code suivant vous montre comment ajouter une image dans l'en-tête d'un fichier PDF.

```csharp
public static void AddImageHeader()
        {
            // Créer un objet PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Ouvrir le document
            fileStamp.BindPdf(_dataDir + "sample.pdf");
            using (var fs = new FileStream(_dataDir + "aspose-logo.png", FileMode.Open))
            {
                // Ajouter l'en-tête
                fileStamp.AddHeader(fs, 10);

                // Enregistrer le fichier PDF mis à jour
                fileStamp.Save(_dataDir + "AddImage-Header_out.pdf");
                // Fermer fileStamp
                fileStamp.Close();
            }
        }
```
## Ajouter une Image dans le Pied de Page d'un Fichier PDF Existant

La classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) vous permet d'ajouter une image dans le pied de page d'un fichier PDF. Afin d'ajouter une image dans le pied de page, vous devez d'abord créer un objet de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Ensuite, vous devez appeler la méthode [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Vous pouvez passer l'image à la méthode [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Le code suivant vous montre comment ajouter une image dans le pied de page d'un fichier PDF.

```csharp
public static void AddImageFooter()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");
            using (var fs = new FileStream(_dataDir + "aspose-logo.png", FileMode.Open))
            {
                // Add footer
                fileStamp.AddFooter(fs, 10);

                // Save updated PDF file
                fileStamp.Save(_dataDir + "AddImage-Footer_out.pdf");

                // Close fileStamp
                fileStamp.Close();
            }
        }
```