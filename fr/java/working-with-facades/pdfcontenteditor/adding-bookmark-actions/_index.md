---
title: Ajout d'actions de signet à un fichier PDF existant
type: docs
weight: 20
url: /fr/java/adding-bookmark-actions/
description: Cette section explique comment ajouter des actions de signet à un fichier PDF existant avec Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

La classe [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) présente dans le package com.aspose.pdf.facades offre la flexibilité d'ajouter des actions de signet à un fichier PDF. Vous pouvez créer un lien avec les actions en série correspondant à l'exécution d'un élément de menu dans le visualiseur PDF. Cette classe offre également la possibilité de créer des actions supplémentaires pour les événements de document.

L'exemple de code suivant démontre comment ajouter une action de signet à un document PDF.
 Si vous cliquez sur cet onglet, l'action souhaitée est effectuée. Avec l'aide d'un signet, en cliquant dessus, nous effectuons l'action souhaitée. Ensuite, créez un [CreateBookmarkAction](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createBookmarksAction-java.lang.String-java.awt.Color-boolean-boolean-java.lang.String-java.lang.String-java.lang.String-), définissez les paramètres du texte, les couleurs, indiquez le nom du signet, et indiquez également le numéro de page. La dernière action est effectuée avec "GoTo", elle vous permet d'aller de n'importe où à la page dont nous avons besoin.

```java
public static void AddBookmarksAction()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            editor.createBookmarksAction("Bookmark 1", java.awt.Color.GREEN, true, false, "", "GoTo", "2");

            // Sauvegarde le PDF résultant dans un fichier
            editor.save(_dataDir + "PdfContentEditorDemo_Bookmark.pdf");
        }
```