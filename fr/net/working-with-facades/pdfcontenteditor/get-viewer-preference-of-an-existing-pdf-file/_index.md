---
title: Obtenir la Préférence du Visionneur d'un Fichier PDF
type: docs
weight: 70
url: /fr/net/get-viewer-preference-of-an-existing-pdf-file/
description: Cette section montre comment obtenir la préférence du visionneur d'un fichier PDF existant en utilisant la Classe PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

## Obtenir la Préférence du Visionneur d'un Fichier PDF existant

La classe [ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) représente les modes d'affichage des fichiers PDF; par exemple, positionner la fenêtre du document au centre de l'écran, masquer la barre de menu de l'application du visionneur, etc.

Afin de lire les paramètres, nous utilisons la classe [GetViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/getviewerpreference). Cette méthode retourne une variable où tous les paramètres sont enregistrés.

```csharp
      public static void GetViewerPreference()
        {
            var document = new Document(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // Change Viewer Preferences
            var preferences = editor.GetViewerPreference();
            if ((preferences & ViewerPreference.CenterWindow) != 0)
                Console.WriteLine("CenterWindow");
            if ((preferences & ViewerPreference.HideMenubar) != 0)
                Console.WriteLine("Menu bar hided");
            if ((preferences & ViewerPreference.PageModeFullScreen) != 0)
                Console.WriteLine("Page Mode Full Screen");
        }
```