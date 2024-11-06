---
title: Obtenir, Mettre à Jour et Développer un Signet 
linktitle: Obtenir, Mettre à Jour et Développer un Signet
type: docs
weight: 20
url: fr/java/get-update-and-expand-bookmark/
description: Cet article décrit comment utiliser les signets dans un fichier PDF. Avec notre bibliothèque Java, vous pouvez obtenir des signets à partir du fichier PDF, obtenir le numéro de page d'un signet, mettre à jour les signets dans un document PDF, et développer les signets lors de la visualisation d'un document.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtenir des Signets

La collection [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) contient tous les signets d'un fichier PDF. Cet article explique comment obtenir des signets à partir d'un fichier PDF, et comment obtenir sur quelle page se trouve un signet particulier.

Pour obtenir les signets, parcourez la collection [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) et obtenez chaque signet dans la OutlineItemCollection.
 L'OutlineItemCollection fournit l'accès à tous les attributs des signets. Le snippet de code suivant vous montre comment obtenir des signets à partir du fichier PDF.

```java
    public static void GettingBookmarks() {
        // Ouvrir le document
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // Parcourir tous les signets
        for (OutlineItemCollection outlineItem : (Iterable<OutlineItemCollection>) pdfDocument.getOutlines()) {
            System.out.println("Titre :- " + outlineItem.getTitle());
            System.out.println("Est Italique :- " + outlineItem.getItalic());
            System.out.println("Est Gras :- " + outlineItem.getBold());
            System.out.println("Couleur :- " + outlineItem.getColor());
        }
    }
```

## Obtenir le numéro de page d'un signet

Une fois que vous avez ajouté un signet, vous pouvez savoir sur quelle page il se trouve en obtenant le numéro de page de destination associé à l'objet Signet.

```java
    public static void GettingBookmarksPageNumber() {
        // Créer PdfBookmarkEditor
        PdfBookmarkEditor bookmarkEditor = new PdfBookmarkEditor();
        // Ouvrir le fichier PDF
        bookmarkEditor.bindPdf(GetDataDir() + "UpdateBookmarks.pdf");
        // Extraire les signets
        Bookmarks bookmarks = bookmarkEditor.extractBookmarks();
        for (Bookmark bookmark : (Iterable<Bookmark>) bookmarks) {
            String strLevelSeprator = "";
            for (int i = 1; i < bookmark.getLevel(); i++) {
                strLevelSeprator += "---- ";
            }
            System.out.println("Titre :- " + strLevelSeprator + bookmark.getTitle());
            System.out.println("Numéro de Page :- " + strLevelSeprator + bookmark.getPageNumber());
            System.out.println("Action de Page :- " + strLevelSeprator + bookmark.getAction());
        }
    }
```

## Mettre à jour les signets dans un document PDF

Pour mettre à jour un signet dans un fichier PDF, commencez par obtenir le signet particulier de la collection OutlineCollection de l'objet Document en spécifiant l'index du signet. Une fois que vous avez récupéré le signet dans l'objet [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection), vous pouvez mettre à jour ses propriétés puis enregistrer le fichier PDF mis à jour en utilisant la méthode Save. Les extraits de code suivants montrent comment mettre à jour les signets dans un document PDF.

```java
    public static void UpdateBookmarksInPDFDocument() {
        // Ouvrir le document
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // Obtenir un objet signet
        OutlineItemCollection pdfOutline = pdfDocument.getOutlines().get_Item(1);

        // Mettre à jour l'objet signet
        pdfOutline.setTitle("Outline mis à jour");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);
        // Définir la page cible comme 2
        pdfOutline.setDestination(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // Enregistrer la sortie
        pdfDocument.save(GetDataDir() + "Bookmarkupdated_output.pdf");
    }
```


## Mettre à jour les signets enfants dans un document PDF

Pour mettre à jour un signet enfant :

1. Récupérez le signet enfant que vous souhaitez mettre à jour à partir du fichier PDF en obtenant d'abord le signet parent, puis le signet enfant en utilisant les valeurs d'index appropriées.
2. Enregistrez le fichier PDF mis à jour en utilisant la méthode Save.

{{% alert color="primary" %}}

Obtenez un signet de la collection OutlineCollection de l'objet Document en spécifiant l'index du signet, puis obtenez le signet enfant en spécifiant l'index de ce signet parent.

{{% /alert %}}

L'extrait de code suivant vous montre comment mettre à jour les signets enfants dans un document PDF.

```java
    public static void UpdateChildBookmarksInPDFDocument() {
        // Ouvrir le document
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // Obtenir un objet signet
        OutlineItemCollection pdfOutline = pdfDocument.getOutlines().get_Item(1);
        // Obtenir l'objet signet enfant
        OutlineItemCollection childOutline = pdfOutline.get_Item(1);

        // Mettre à jour l'objet signet
        childOutline.setTitle("Updated Outline");
        childOutline.setItalic(true);
        childOutline.setBold(true);
        // Définir la page cible en tant que 2
        childOutline.setDestination(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // Enregistrer la sortie
        pdfDocument.save(GetDataDir() + "Bookmarkupdated_output.pdf");
    }
```


## Signets développés lors de la visualisation du document

Les signets sont conservés dans la collection [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) de l'objet Document, elle-même dans la collection [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection). Cependant, nous pouvons avoir besoin que tous les signets soient développés lors de la visualisation du fichier PDF.

Pour répondre à cette exigence, nous pouvons définir le statut d'ouverture pour chaque élément de plan/signet comme ouvert. Le code suivant vous montre comment définir le statut d'ouverture pour chaque signet comme développé dans un document PDF.

```java
    public static void ExpandedBookmarks() {    
        Document doc = new Document(GetDataDir()+"UpdateBookmarks.pdf");
        // définir le mode d'affichage de la page, c'est-à-dire montrer les vignettes, plein écran, montrer le panneau des pièces jointes
        doc.setPageMode(PageMode.UseOutlines);
        // imprimer le nombre total de signets dans le fichier PDF
        System.out.println(doc.getOutlines().size());
        // parcourir chaque élément de plan dans la collection de plans du fichier PDF
        for (int counter = 1; counter <= doc.getOutlines().size(); counter++) {
            // définir le statut d'ouverture pour l'élément de plan
            doc.getOutlines().get_Item(counter).setOpen(true);
        }
        // enregistrer le fichier PDF
        doc.save(_dataDir+"Bookmarks_Expanded.pdf");
    }
```