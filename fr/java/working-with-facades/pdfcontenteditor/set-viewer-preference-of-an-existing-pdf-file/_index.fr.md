---
title: Définir la Préférence de Visionneuse d'un Fichier PDF Existant
type: docs
weight: 60
url: /java/set-viewer-preference-of-an-existing-pdf-file/
description: Cette section montre comment travailler avec Aspose.PDF Facades en utilisant la classe PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

## Définir la Préférence de Visionneuse d'un Fichier PDF Existant

La classe [ViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/viewerpreference) représente les modes d'affichage des fichiers PDF ; par exemple, positionner la fenêtre du document au centre de l'écran, masquer la barre de menu de l'application visionneuse, etc.

La méthode [ChangeViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#changeViewerPreference-int-) dans la classe [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) vous permet de changer la préférence de visionneuse.
 Afin de faire cela, vous devez créer un objet de la classe [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) et lier le fichier PDF d'entrée en utilisant la méthode [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#bindPdf-java.lang.String-).

Après cela, vous pouvez appeler la méthode [ChangeViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#changeViewerPreference-int-) pour définir toute préférence. Enfin, vous devez enregistrer le fichier PDF mis à jour en utilisant la méthode Save. Le fragment de code suivant vous montre comment changer la préférence du visualiseur dans un fichier PDF existant.

Par exemple, nous spécifions le paramètre [CENTER WINDOW](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#CENTER_WINDOW) avec lequel nous centrons la fenêtre, après avoir retiré la barre d'outils supérieure avec [HIDE MENUBAR](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#HIDE_MENUBAR) et avec [PAGE MODE USE NONE](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#PAGE_MODE_USE_NONE) ouvrir le mode plein écran.
```java
public static void SetViewerPreference()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // Modifier les préférences de visualisation
            editor.changeViewerPreference(ViewerPreference.CENTER_WINDOW);
            editor.changeViewerPreference(ViewerPreference.HIDE_MENUBAR);
            editor.changeViewerPreference(ViewerPreference.PAGE_MODE_USE_NONE);
            
            editor.save(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            GetViewerPreference();
        }
```