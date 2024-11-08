---
title: Ajouter et Supprimer des Signets
type: docs
weight: 10
url: /fr/cpp/add-and-delete-bookmarks/
---

## <ins>**Ajouter un Signet**
La classe PdfBookmarkEditor vous permet d'ajouter des signets dans un document PDF. La méthode CreateBookmarkOfPage offerte par cette classe vous permet de créer un signet qui ciblera le numéro de page spécifié. L'extrait de code suivant démontre cette fonctionnalité de l'API Aspose.PDF pour C++ :



{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Bookmarks-CreateBookmark-1.cpp" >}}
## <ins>**Ajouter un Signet Enfant dans un document existant**
Vous pouvez ajouter des signets enfants dans un fichier PDF existant en utilisant la classe **PdfBookmarkEditor**. Afin d'ajouter des signets enfants, vous devez créer des objets **Bookmarks** et *Bookmark*. Vous pouvez ajouter des objets **Bookmark** individuels dans l'objet **Bookmarks**. Vous devez également créer un objet **Bookmark** et définir sa propriété **ChildItem** sur l'objet **Bookmarks**. Vous devez ensuite passer cet objet **Bookmark** avec **ChildItem** à la méthode **CreateBookmarks**. Enfin, vous devez enregistrer le PDF mis à jour en utilisant la méthode **Save** de la classe **PdfBookmarkEditor**. Le fragment de code suivant vous montre comment ajouter des signets enfants dans un fichier PDF existant.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Bookmarks-CreateChildBookmark-1.cpp" >}}
## <ins>**Supprimer tous les signets du fichier PDF**
Vous pouvez supprimer tous les signets du fichier PDF en utilisant la méthode **DeleteBookmarks** sans aucun paramètre. Tout d'abord, vous devez créer un objet de la classe **PdfBookmarkEditor** et lier le fichier PDF d'entrée à l'aide de la méthode **BindPdf**. Après cela, vous devez appeler la méthode **DeleteBookmarks** puis enregistrer le fichier PDF mis à jour en utilisant la méthode **Save**. Le fragment de code suivant vous montre comment supprimer tous les signets du fichier PDF.

## <ins>**Supprimer un Signet Particulier d'un Fichier PDF**
Afin de supprimer un signet particulier, vous devez appeler la méthode **DeleteBookmarks** avec un paramètre de type chaîne (titre). Le **titre** ici représente le signet à supprimer du PDF. Créez un objet de la classe **PdfBookmarkEditor** et liez le fichier PDF d'entrée en utilisant la méthode **BindPdf**. Après cela, appelez la méthode **DeleteBookmarks** puis enregistrez le fichier PDF mis à jour en utilisant la méthode **Save**. Le fragment de code suivant vous montre comment supprimer un signet particulier d'un fichier PDF.