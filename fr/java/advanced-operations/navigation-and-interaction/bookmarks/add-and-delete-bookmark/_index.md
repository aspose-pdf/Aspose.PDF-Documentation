---
title: Ajouter et Supprimer un Signet
linktitle: Ajouter et Supprimer un Signet
type: docs
weight: 10
url: fr/java/add-and-delete-bookmark/
description: Vous pouvez ajouter un signet à un document PDF avec Java. Il est possible de supprimer tous ou certains signets d'un document PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ajouter un Signet à un Document PDF

Les signets sont contenus dans la collection [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) de l'objet Document, elle-même dans la collection [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection).

Pour ajouter un signet à un PDF :

1. Ouvrez un document PDF en utilisant l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
2. Créez un signet et définissez ses propriétés.
3. Ajoutez la collection [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) à la collection Outlines.

Le fragment de code suivant vous montre comment ajouter un signet dans un document PDF.

```java
package com.aspose.pdf.examples;

import java.io.IOException;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.Bookmark;
import com.aspose.pdf.facades.Bookmarks;
import com.aspose.pdf.facades.PdfBookmarkEditor;

public class ExampleBookmarks {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Bookmarks/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Bookmarks\\";
        return _dataDir;
    }

    public static void AddBookmarks() throws IOException {

        Document pdfDocument = new Document(GetDataDir() + "AddBookmark.pdf");

        // Créer un objet signet
        OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfOutline.setTitle("Test Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        // Définir le numéro de page de destination
        pdfOutline.setAction(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // Ajouter un signet dans la collection des signets du document.
        pdfDocument.getOutlines().add(pdfOutline);

        // Enregistrer le document mis à jour
        pdfDocument.save(_dataDir + "AddBookmark_out.pdf");
    }
```


## Ajouter un Signet Enfant au Document PDF

Les signets peuvent être imbriqués, indiquant une relation hiérarchique avec des signets parent et enfant. Cet article explique comment ajouter un signet enfant, c'est-à-dire un signet de deuxième niveau, à un PDF.

Pour ajouter un signet enfant à un fichier PDF, ajoutez d'abord un signet parent :

1. Ouvrez un document.
1. Ajoutez un signet à la [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection), en définissant ses propriétés.
1. Ajoutez la OutlineItemCollection à la collection [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) de l'objet Document.

Le signet enfant est créé de la même manière que le signet parent, expliqué ci-dessus, mais est ajouté à la collection Outlines du signet parent.

Les extraits de code suivants montrent comment ajouter un signet enfant à un document PDF.

```java
    public static void AddChildBookmark() {
        // Ouvrir le document
        Document pdfDocument = new Document(GetDataDir() + "AddChildBookmark.pdf");

        // Créer un objet de signet parent
        OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfOutline.setTitle("Parent Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        // Créer un objet de signet enfant
        OutlineItemCollection pdfChildOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfChildOutline.setTitle("Child Outline");
        pdfChildOutline.setItalic(true);
        pdfChildOutline.setBold(true);

        // Ajouter le signet enfant dans la collection de signets du parent
        pdfOutline.add(pdfChildOutline);
        // Ajouter le signet parent dans la collection de signets du document.
        pdfDocument.getOutlines().add(pdfOutline);

        // Enregistrer la sortie
        pdfDocument.save(_dataDir + "AddChildBookmark_out.pdf");
    }
```


## Supprimer tous les signets d'un document PDF

Tous les signets dans un PDF sont contenus dans la collection [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection). Cet article explique comment supprimer tous les signets d'un fichier PDF.

Pour supprimer tous les signets d'un fichier PDF :

1. Appelez la méthode Delete de la collection [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection).
2. Enregistrez le fichier modifié en utilisant la méthode Save de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Les extraits de code suivants montrent comment supprimer tous les signets d'un document PDF.

```java
    public static void DeleteAllBookmarksFromPDFDocument() {
        // Ouvrir le document
        Document pdfDocument = new Document(GetDataDir() + "DeleteAllBookmarks.pdf");

        // Supprimer tous les signets
        pdfDocument.getOutlines().delete();

        // Enregistrer le fichier mis à jour
        pdfDocument.save(_dataDir + "DeleteAllBookmarks_out.pdf");
    }
```

## Supprimer un signet particulier d'un document PDF

[Supprimer toutes les pièces jointes d'un document PDF](https://docs.aspose.com/pdf/java/working-with-attachments/) a montré comment supprimer toutes les pièces jointes d'un fichier PDF. Il est également possible de supprimer uniquement des pièces jointes spécifiques.

Pour supprimer un signet particulier d'un fichier PDF :

1. Passez le titre du signet en tant que paramètre à la méthode [Delete](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection#delete--) de la collection [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection).
1. Ensuite, enregistrez le fichier mis à jour avec la méthode Save de l'objet Document.

La classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) fournit la collection [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection). La méthode [Delete](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection#delete--) supprime tout signet avec le titre passé à la méthode.

Les extraits de code suivants montrent comment supprimer un signet particulier du document PDF.

```java
    public static void DeleteParticularBookmarkPDFDocument() {
        // Ouvrir le document
        Document pdfDocument = new Document(GetDataDir() + "DeleteParticularBookmark.pdf");

        // Supprimer un signet particulier par titre
        pdfDocument.getOutlines().delete("Child Outline");

        // Enregistrer le fichier mis à jour
        pdfDocument.save(_dataDir + "DeleteParticularBookmark_out.pdf");
    }
```