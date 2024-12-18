---
title: Définir les Informations du Fichier PDF
type: docs
weight: 40
url: /fr/net/set-pdf-file-information/
description: Cette section explique comment définir les informations du fichier PDF avec Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

La classe [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) vous permet de définir des informations spécifiques à un fichier PDF. Vous devez créer un objet de la classe [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) puis définir différentes propriétés spécifiques au fichier comme Auteur, Titre, Mot-clé, et Créateur, etc. Enfin, enregistrez le fichier PDF mis à jour en utilisant la méthode [SaveNewInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileinfo/savenewinfo/methods/1) de l'objet [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo).

L'extrait de code suivant vous montre comment définir les informations du fichier PDF.

```csharp
 public static void SetPdfInfo()
        {
            PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf")
            {
                // Définir les informations PDF
                Author = "Aspose",
                Title = "Hello World!",
                Keywords = "Peace and Development",
                Creator = "Aspose"
            };
            // Enregistrer le fichier mis à jour
            fileInfo.SaveNewInfo(_dataDir + "SetFileInfo_out.pdf");
        }
```

## Définir les informations méta

La méthode [SetMetaInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/methods/setmetainfo) vous permet d'ajouter n'importe quelle information. Dans notre exemple, nous avons ajouté un champ. Vérifiez le code suivant :

```csharp
 public static void SetMetaInfo()
        {
            // Créer une instance de l'objet PdfFileInfo
            Aspose.Pdf.Facades.PdfFileInfo fInfo = new Aspose.Pdf.Facades.PdfFileInfo(_dataDir + "sample.pdf");

            // Définir un nouvel attribut client comme info méta
            fInfo.SetMetaInfo("Reviewer", "utilisateur Aspose.PDF");

            // Enregistrer le fichier mis à jour
            fInfo.SaveNewInfo(_dataDir + "SetMetaInfo_out.pdf");
```