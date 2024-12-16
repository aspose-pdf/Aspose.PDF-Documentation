---
title: Mettre à jour, Supprimer et Obtenir des Signets
type: docs
weight: 30
url: /fr/net/update-delete-and-get-bookmarks/
description: Cette section explique comment mettre à jour, supprimer et obtenir des signets avec Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

## Mettre à jour un Signet Existant dans le Fichier PDF

Pour mettre à jour un signet existant dans un fichier PDF, vous devez utiliser la méthode [ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks).
``` Ce document prend deux arguments : titre source (le titre du signet à modifier), titre de destination (le titre à remplacer). Vous devez créer un objet de la classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Ensuite, vous devez appeler la méthode [ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks), puis enregistrer le PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). L'extrait de code suivant vous montre comment modifier un signet existant dans un fichier PDF.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-UpdateBookmark-UpdateBookmark.cs" >}}

## Supprimer tous les signets du fichier PDF

Vous pouvez supprimer tous les signets du fichier PDF en utilisant la méthode [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) sans aucun paramètre. Tout d'abord, vous devez créer un objet de la classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Après cela, vous devez appeler la méthode [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) puis enregistrer le fichier PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). L'extrait de code suivant vous montre comment supprimer tous les signets du fichier PDF.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-DeleteAllBookmarks-DeleteAllBookmarks.cs" >}}

## Supprimer un Signet Particulier d'un Fichier PDF

Pour supprimer un signet particulier, vous devez appeler la méthode [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) avec un paramètre de type chaîne (titre). Le *titre* ici représente le signet à supprimer du PDF. Créez un objet de la classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) et liez le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Ensuite, appelez la méthode [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) et enregistrez le fichier PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Le code suivant vous montre comment supprimer un signet particulier d'un fichier PDF.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-DeleteABookmark-DeleteABookmark.cs" >}}

## Obtenez des signets à partir des façades de documents PDF

La classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) offre la possibilité de manipuler les signets dans un fichier PDF existant. Il fournit diverses propriétés pour obtenir/définir des informations concernant les signets. Le code suivant montre comment obtenir des informations relatives à chaque signet dans un fichier PDF.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-GetFromPDF-GetFromPDF.cs" >}}

## Extraire les signets d'un fichier PDF existant

La méthode [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) vous permet d'extraire des signets d'un fichier PDF. Afin d'extraire les signets, vous devez créer un objet [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) et lier le fichier PDF en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Après cela, vous devez appeler la méthode [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3). La méthode [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) retourne un objet [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks/methods/index). Vous pouvez ensuite parcourir ces signets et obtenir des objets [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) individuels. Enfin, enregistrez le fichier PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). L'extrait de code suivant vous montre comment exporter des signets vers un fichier XML.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ExtractBookmarks-ExtractBookmarks.cs" >}}