```
title: Ajouter et Supprimer un Signet
linktitle: Ajouter et Supprimer un Signet
type: docs
weight: 10
url: /fr/cpp/add-and-delete-bookmark/
description: Ce sujet explique comment ajouter un signet à un document PDF avec la bibliothèque C++. Vous pouvez également supprimer tous les signets ou des signets particuliers d'un document PDF.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ajouter un Signet à un Document PDF

Les signets sont conservés dans la collection [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection/) de l'objet Document, elle-même dans la collection [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/).

Pour ajouter un signet à un PDF :

1. Ouvrez un document PDF en utilisant l'objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/).
1. Créez un signet et définissez ses propriétés.
1.
``` Ajoutez la collection [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) à la collection Outlines.

L'extrait de code suivant vous montre comment ajouter un signet dans un document PDF.

```cpp
void AddBookmarks() {


String _dataDir("C:\\Samples\\Bookmarks\\");

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddBookmark.pdf");


// Créez un objet signet

auto pdfOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfOutline->set_Title(u"Test Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);


// Définissez le numéro de page de destination

pdfOutline->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));


// Ajoutez un signet dans la collection d'aperçu du document.

pdfDocument->get_Outlines()->Add(pdfOutline);


// Enregistrez le document mis à jour

pdfDocument->Save(_dataDir + u"AddBookmark_out.pdf");
}
```

## Ajouter un Signet Enfant au Document PDF

Les signets peuvent être imbriqués, indiquant une relation hiérarchique avec des signets parents et enfants. Cet article explique comment ajouter un signet enfant, c'est-à-dire un signet de deuxième niveau, à un PDF.

Pour ajouter un signet enfant à un fichier PDF, ajoutez d'abord un signet parent :

1. Ouvrez un document.
1. Ajoutez un signet à la [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection/), en définissant ses propriétés.
1. Ajoutez l'OutlineItemCollection à la collection [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) de l'objet Document.

Le signet enfant est créé de la même manière que le signet parent, expliqué ci-dessus, mais est ajouté à la collection des signets du parent.

Les extraits de code suivants montrent comment ajouter un signet enfant à un document PDF.

```cpp
void AddChildBookmark() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Ouvrir le document

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddChildBookmark.pdf");


// Créer un objet signet parent

auto pdfOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfOutline->set_Title(u"Parent Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);


// Créer un objet signet enfant

auto pdfChildOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfChildOutline->set_Title(u"Child Outline");

pdfChildOutline->set_Italic(true);

pdfChildOutline->set_Bold(true);


// Ajouter le signet enfant dans la collection du signet parent

pdfOutline->Add(pdfChildOutline);

// Ajouter le signet parent dans la collection des signets du document.

pdfDocument->get_Outlines()->Add(pdfOutline);


// Sauvegarder le résultat

pdfDocument->Save(_dataDir + u"AddChildBookmark_out.pdf");
}
```
## Supprimer tous les signets d'un document PDF

Tous les signets d'un PDF sont contenus dans la collection [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/). Cet article explique comment supprimer tous les signets d'un fichier PDF.

Pour supprimer tous les signets d'un fichier PDF :

1. Appelez la méthode Delete de la collection [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/).
1. Enregistrez le fichier modifié à l'aide de la méthode Save de l'objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/).

Les extraits de code suivants montrent comment supprimer tous les signets d'un document PDF.

```cpp
void DeleteAllBookmarksFromPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Ouvrir le document

auto pdfDocument = MakeObject<Document>(_dataDir + u"DeleteAllBookmarks.pdf");


// Supprimer tous les signets

pdfDocument->get_Outlines()->Delete();


// Enregistrer le fichier mis à jour

pdfDocument->Save(_dataDir + u"DeleteAllBookmarks_out.pdf");
}
```


## Supprimer un signet particulier d'un document PDF

[Supprimer tous les pièces jointes du document PDF](https://docs.aspose.com/pdf/cpp/working-with-attachments/) a montré comment supprimer toutes les pièces jointes d'un fichier PDF. Il est également possible de supprimer uniquement des pièces jointes spécifiques.

Pour supprimer un signet particulier d'un fichier PDF :

1. Passez le titre du signet en tant que paramètre à la méthode Delete de la collection [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/).
2. Ensuite, enregistrez le fichier mis à jour avec la méthode Save de l'objet Document.

La classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) fournit la collection [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/). La méthode [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection#a04f36a1f4f7c4fde3189399eb046a98b) supprime tout signet avec le titre passé à la méthode.

Les extraits de code suivants montrent comment supprimer un signet particulier du document PDF.

```cpp
void DeleteParticularBookmarkPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Ouvrir le document

auto pdfDocument = MakeObject<Document>(_dataDir + u"DeleteParticularBookmark.pdf");


// Supprimer le signet particulier par titre

pdfDocument->get_Outlines()->Delete(u"Child Outline");


// Enregistrer le fichier mis à jour

pdfDocument->Save(_dataDir + u"DeleteParticularBookmark_out.pdf");
}
```