---
title: Créer des Signets pour Toutes les Pages (facades)
type: docs
weight: 10
url: /java/create-bookmark/
description: Cette section explique comment créer des signets avec Aspose.PDF Facades en utilisant la classe PdfBookmarEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Créer des Signets pour Toutes les Pages (facades)

Pour créer des signets pour toutes les pages, vous devez utiliser la méthode createBookmarks sans aucun paramètre. La classe PdfBookmarEditor vous permet de créer des signets pour toutes les pages d'un fichier PDF. Tout d'abord, vous devez créer un objet de la classe PdfBookmarkEditor et lier le PDF d'entrée en utilisant la méthode bindPdf. Ensuite, vous devez appeler la méthode createBookmarks et sauvegarder le fichier PDF de sortie en utilisant la méthode save.

L'extrait de code suivant vous montre :

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-CreateBookmarksOfAllPages-.java" >}}

## Créer des Signets pour Toutes les Pages avec Propriétés (facades)

La classe PdfBookmarEditor vous permet de créer des signets pour toutes les pages d'un fichier PDF et de spécifier les propriétés (Couleur, Gras, Italique).
 Vous pouvez faire cela à l'aide de la méthode createBookmarks. Tout d'abord, vous devez créer un objet de la classe PdfBookmarkEditor et lier le PDF d'entrée en utilisant la méthode bindPdf. Ensuite, vous devez appeler la méthode createBookmarks et enregistrer le fichier PDF de sortie en utilisant la méthode save.

Le snippet de code suivant vous montre comment créer des signets de toutes les pages avec des propriétés.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-CreateBookmarksOfAllPagesWithProperties-.java" >}}