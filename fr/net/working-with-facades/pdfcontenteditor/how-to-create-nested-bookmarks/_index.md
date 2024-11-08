---
title: Ajout de signets au fichier PDF
type: docs
weight: 20
url: /fr/net/how-to-create-nested-bookmarks/
description: Cette section explique comment créer des signets imbriqués avec la classe PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

Les signets vous offrent la possibilité de suivre/lier à une page spécifique à l'intérieur du document PDF. La classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor) dans l'[espace de noms Aspose.Pdf.Facades](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace) fournit une fonctionnalité qui vous permet de créer votre propre signet de manière sophistiquée mais intuitive dans un fichier PDF existant, à une page donnée ou à toutes les pages.

## Détails de l'implémentation

En dehors de la création de signets simples, il arrive parfois que vous deviez créer un signet sous forme de chapitres où vous imbriquez les signets individuels à l'intérieur des signets de chapitre afin que lorsque vous cliquez sur le signe + d'un chapitre, vous puissiez voir les pages à l'intérieur lorsque les signets s'étendent, comme montré sur l'image ci-dessous.
```csharp
   public static void AddBookmarksAction()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            editor.CreateBookmarksAction("Signet 1", System.Drawing.Color.Green, true, false, string.Empty, "GoTo", "2");

            // Enregistre le PDF de résultat dans un fichier
            editor.Save(_dataDir + "PdfContentEditorDemo_Bookmark.pdf");
        }
```