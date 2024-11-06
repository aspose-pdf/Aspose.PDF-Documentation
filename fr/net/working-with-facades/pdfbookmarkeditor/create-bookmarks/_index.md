---
title: Créer des Signets
type: docs
weight: 10
url: fr/net/create-bookmarks/
description: Cette section explique comment créer des signets pour votre fichier PDF avec Aspose.PDF Facades en utilisant la classe PdfBookmarkEditor.
lastmod: "2021-06-05"
draft: false
---

## Créer des Signets de Toutes les Pages

Pour créer des signets de toutes les pages, vous devez utiliser la méthode [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) sans aucun paramètre. La classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) vous permet de créer des signets pour toutes les pages d'un fichier PDF. Tout d'abord, vous devez créer un objet de la classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) et lier le PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Ensuite, vous devez appeler la méthode [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) et enregistrer le fichier PDF de sortie en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Le code suivant vous montre comment créer des signets.


{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarksAll-CreateBookmarksAll.cs" >}}

## Créer des signets de toutes les pages avec des propriétés

La classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) vous permet de créer des signets de toutes les pages d'un fichier PDF et de spécifier les propriétés (Couleur, Gras, Italique). Vous pouvez le faire à l'aide de la méthode [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2). Tout d'abord, vous devez créer un objet de la classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) et lier le PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Ensuite, vous devez appeler la méthode [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) et enregistrer le fichier PDF de sortie en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). L'extrait de code suivant vous montre comment créer des signets pour toutes les pages avec des propriétés.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarksPagesProperties-CreateBookmarksPagesProperties.cs" >}}

## Créer un signet d'une page particulière

Vous pouvez créer un signet d'une page particulière dans un fichier PDF existant en utilisant la méthode [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1). Ce document décrit la méthode qui prend deux arguments : le titre du signet et le numéro de page. Tout d'abord, vous devez créer un objet de la classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Ensuite, vous devez appeler la méthode [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) et enregistrer le fichier PDF de sortie en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Le fragment de code suivant vous montre comment créer un signet d'une page particulière.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarkPage-CreateBookmarkPage.cs" >}}

## Créer des signets pour une plage de pages

La classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) vous permet de créer des signets pour une plage de pages. Vous pouvez utiliser la méthode [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) avec deux paramètres : la liste des signets (la liste des titres des signets) et la liste des pages (la liste des pages à marquer). Tout d'abord, vous devez créer un objet de la classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Ensuite, vous devez appeler la méthode [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) et enregistrer le PDF de sortie en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Le code suivant vous montre comment créer des signets pour une plage de pages.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarkPageRange-CreateBookmarkPageRange.cs" >}}
## Ajouter un Favori dans un Fichier PDF Existant

Vous pouvez ajouter un favori dans un fichier PDF existant en utilisant la classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor). Pour créer le favori, vous devez créer un objet [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) et définir les attributs requis du favori. Ensuite, vous devez passer l'objet [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) à la méthode [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) de la classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor). Enfin, vous devez enregistrer le fichier PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Le fragment de code suivant vous montre comment ajouter le favori dans un fichier PDF existant.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-AddBookmark-AddBookmark.cs" >}}

## Ajouter un Signet Enfant dans un Fichier PDF Existant

Vous pouvez ajouter des signets enfants dans un fichier PDF existant en utilisant la classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor). In order to add child bookmarks, you need to create [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) objets. You can add individual [Signet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) objects into [Signets](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks) object. Vous devez également créer un objet [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) et définir sa propriété [ChildItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem) sur l'objet [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks). Vous devez ensuite passer cet objet [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) avec [ChildItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem) à la méthode [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2). Enfin, vous devez enregistrer le PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) de la classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor). Le snippet de code suivant vous montre comment ajouter des signets enfants dans un fichier PDF existant.
## Voir aussi

Essayez de comparer et de trouver un moyen de travailler avec les signets qui vous convient. Apprenons la section [Travailler avec les signets dans PDF](/pdf/net/bookmarks/).