---
title: Définir la Préférence du Lecteur de PDF
type: docs
weight: 60
url: /net/set-viewer-preference-of-an-existing-pdf-file/
description: Cette section montre comment définir la préférence du lecteur d'un fichier PDF existant en utilisant la classe PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

## Définir la Préférence du Lecteur d'un Fichier PDF Existant

La classe [ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) représente les modes d'affichage des fichiers PDF ; par exemple, positionner la fenêtre du document au centre de l'écran, masquer la barre de menu de l'application du lecteur, etc.

La méthode [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) dans la classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) vous permet de changer la préférence du lecteur. Pour ce faire, vous devez créer un objet de la classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/bindpdf/index).

Après cela, vous pouvez appeler la méthode [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) pour définir n'importe quelle préférence. Enfin, vous devez enregistrer le fichier PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index). L'extrait de code suivant vous montre comment changer la préférence du visualiseur dans un fichier PDF existant.

Par exemple, nous spécifions le paramètre [CenterWindow](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/centerwindow) avec lequel nous centrons la fenêtre, après avoir retiré la barre d'outils supérieure avec [HideMenubar](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/hidemenubar) et avec [PageModeUseNone](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/pagemodeusenone) ouvrir le mode plein écran.
```csharp
 public static void SetViewerPreference()
        {
            var document = new Document(_dataDir + "Exemple.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // Changer les préférences du visualiseur
            editor.ChangeViewerPreference(ViewerPreference.CenterWindow);
            editor.ChangeViewerPreference(ViewerPreference.HideMenubar);
            editor.ChangeViewerPreference(ViewerPreference.PageModeFullScreen);
            // Enregistre le fichier PDF résultant
            editor.Save(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            GetViewerPreference();
        }
```