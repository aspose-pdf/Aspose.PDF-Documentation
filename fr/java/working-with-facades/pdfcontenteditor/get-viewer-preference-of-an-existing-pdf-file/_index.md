---
title: Obtenir la préférence de visualisation d'un fichier PDF existant
type: docs
weight: 70
url: fr/java/get-viewer-preference-of-an-existing-pdf-file/
description: Cette section montre comment travailler avec Aspose.PDF Facades en utilisant la classe PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

## Obtenir la préférence de visualisation d'un fichier PDF existant

La classe [ViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/viewerpreference) représente les modes d'affichage des fichiers PDF ; par exemple, positionner la fenêtre du document au centre de l'écran, masquer la barre de menu de l'application de visualisation, etc.

Pour lire les paramètres, nous utilisons 'getViewerPreference'. Cette méthode retourne une variable où tous les paramètres sont sauvegardés.

```java
 public static void GetViewerPreference()
        {
            var document = new Document(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // Modifier les préférences de visualisation
            var preferences = editor.getViewerPreference();
            if ((preferences & ViewerPreference.CENTER_WINDOW) != 0)
                System.out.println("Fenêtre centrée");
            if ((preferences & ViewerPreference.HIDE_MENUBAR) != 0)
                System.out.println("Barre de menu masquée");
        }
```