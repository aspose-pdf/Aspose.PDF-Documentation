---
title: Obtenir, Mettre à Jour et Développer un Signet
linktitle: Obtenir, Mettre à Jour et Développer un Signet
type: docs
weight: 20
url: fr/cpp/get-update-and-expand-bookmark/
description: La bibliothèque Aspose.PDF pour C++ vous permet d'obtenir ? mettre à jour dans un fichier PDF avec notre.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtenir des Signets

La collection [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection) de l'objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) contient tous les signets d'un fichier PDF. Cet article explique comment obtenir des signets à partir d'un fichier PDF, et comment déterminer sur quelle page se trouve un signet particulier.

Pour obtenir les signets, parcourez la collection [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection) et obtenez chaque signet dans l'OutlineItemCollection. L'OutlineItemCollection fournit un accès à tous les attributs du signet. Le fragment de code suivant vous montre comment obtenir des signets à partir du fichier PDF.

```cpp
void GettingBookmarks() {

String _dataDir("C:\\Samples\\Bookmarks\\");

// Ouvrir le document

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// Boucle à travers tous les signets

for (auto outlineItem : pdfDocument->get_Outlines()) {


Console::WriteLine(u"Titre :- " + outlineItem->get_Title());


Console::WriteLine(u"Est Italique :- " + outlineItem->get_Italic());


Console::WriteLine(u"Est Gras :- " + outlineItem->get_Bold());


Console::WriteLine(u"Couleur :- {0}", outlineItem->get_Color());

}
}
```

## Obtenir le numéro de page d'un signet

Une fois que vous avez ajouté un signet, vous pouvez savoir sur quelle page il se trouve en obtenant le numéro de page de destination associé à l'objet signet.

```cpp
void GettingBookmarksPageNumber() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Créer PdfBookmarkEditor

auto bookmarkEditor = MakeObject<Aspose::Pdf::Facades::PdfBookmarkEditor>();

// Ouvrir le fichier PDF

bookmarkEditor->BindPdf(_dataDir + u"UpdateBookmarks.pdf");

// Extraire les signets

auto bookmarks = bookmarkEditor->ExtractBookmarks();

for (auto bookmark : bookmarks) {


String strLevelSeprator("");


for (int i = 1; i < bookmark->get_Level(); i++) {



strLevelSeprator += u"---- ";


}


Console::WriteLine(u"Titre :- " + strLevelSeprator + bookmark->get_Title());


Console::WriteLine(u"Numéro de page :- " + strLevelSeprator + bookmark->get_PageNumber());


Console::WriteLine(u"Action de la page :- " + strLevelSeprator + bookmark->get_Action());

}
}
```
## Mettre à jour les signets dans un document PDF

Pour mettre à jour un signet dans un fichier PDF, d'abord, obtenez le signet particulier de la collection OutlineColletion de l'objet Document en spécifiant l'indice du signet. Une fois que vous avez récupéré le signet dans l'objet [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection), vous pouvez mettre à jour ses propriétés, puis enregistrer le fichier PDF mis à jour en utilisant la méthode Save. Les extraits de code suivants montrent comment mettre à jour les signets dans un document PDF.

```cpp
void UpdateBookmarksInPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Ouvrir le document

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// Obtenir un objet signet

auto pdfOutline = pdfDocument->get_Outlines()->idx_get(1);


// Mettre à jour l'objet signet

pdfOutline->set_Title(u"Updated Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);

// Définir la page cible comme 2

pdfOutline->set_Destination(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));


// Enregistrer la sortie

pdfDocument->Save(_dataDir + u"Bookmarkupdated_output.pdf");
}
```

## Mettre à Jour les Signets Enfants dans un Document PDF

Pour mettre à jour un signet enfant :

1. Récupérez le signet enfant que vous souhaitez mettre à jour à partir du fichier PDF en obtenant d'abord le signet parent, puis le signet enfant en utilisant les valeurs d'index appropriées.
1. Enregistrez le fichier PDF mis à jour en utilisant la méthode Save.

{{% alert color="primary" %}}

Obtenez un signet de la collection OutlineCollection de l'objet Document en spécifiant l'index du signet, puis obtenez le signet enfant en spécifiant l'index de ce signet parent.

{{% /alert %}}

L'extrait de code suivant montre comment mettre à jour les signets enfants dans un document PDF.

```cpp
void UpdateChildBookmarksInPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Ouvrir le document

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// Obtenir un objet signet

auto pdfOutline = pdfDocument->get_Outlines()->idx_get(1);

// Obtenir l'objet signet enfant

auto childOutline = pdfOutline->idx_get(1);


// Mettre à jour l'objet signet

childOutline->set_Title(u"Updated Outline");

childOutline->set_Italic(true);

childOutline->set_Bold(true);

// Définir la page cible comme 2

childOutline->set_Destination(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));


// Enregistrer le résultat

pdfDocument->Save(_dataDir + u"Bookmarkupdated_output.pdf");
}
```

## Signets développés lors de la visualisation du document

Les signets sont contenus dans la collection [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection) de l'objet Document, elle-même dans la collection [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection). Cependant, nous pouvons avoir besoin que tous les signets soient développés lors de la visualisation du fichier PDF.

Afin de répondre à cette exigence, nous pouvons définir le statut d'ouverture pour chaque élément de plan/signet comme Ouvert. Le code suivant montre comment définir le statut d'ouverture pour chaque signet comme développé dans un document PDF.

```cpp
void ExpandedBookmarks() {


String _dataDir("C:\\Samples\\Bookmarks\\");


auto doc = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// définir le mode d'affichage de la page, c'est-à-dire afficher les vignettes, en plein écran, afficher le panneau des pièces jointes

doc->set_PageMode(PageMode::UseOutlines);

// imprimer le nombre total de signets dans le fichier PDF

Console::WriteLine(doc->get_Outlines()->get_Count());

// parcourir chaque élément de plan dans la collection de plans du fichier PDF

for (int counter = 1; counter <= doc->get_Outlines()->get_Count(); counter++) {


// définir le statut d'ouverture pour l'élément de plan


doc->get_Outlines()->idx_get(counter)->set_Open(true);

}

// enregistrer le fichier PDF

doc->Save(_dataDir + u"Bookmarks_Expanded.pdf");
}
```