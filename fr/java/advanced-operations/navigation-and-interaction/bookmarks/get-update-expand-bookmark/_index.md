---
title: Obtenir, mettre à jour et développer des signets PDF en Java
linktitle: Obtenir, mettre à jour et développer un signet
type: docs
weight: 20
url: /java/get-update-and-expand-bookmark/
description: Découvrez comment récupérer, mettre à jour et développer des signets dans des documents PDF à l'aide de Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inspectez les propriétés des signets et développez les contours dans les fichiers PDF avec Java
Abstract: Cet article explique comment lire, mettre à jour et développer des signets à l'aide d'Aspose.PDF pour Java. Il couvre l'itération des éléments du plan, l'extraction des numéros de page des signets avec PdfBookmarkEditor, la lecture des signets enfants, la mise à jour des titres et du style des signets et l'ouverture forcée des plans lorsque le document est affiché.
---
Aspose.PDF pour Java expose les signets à la fois via le modèle de plan de document et la façade `PdfBookmarkEditor`.


## 
Obtenir les propriétés des favoris



Utilisez cet exemple lorsque vous devez inspecter les entrées de signets de niveau supérieur dans le plan du document.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez la collection de contours.
1. Lisez et imprimez le titre, le style et les valeurs de couleur du signet.


```java
public static void getBookmarks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection outlineItem = document.getOutlines().get_Item(i);
            System.out.println(outlineItem.getTitle());
            System.out.println(outlineItem.getItalic());
            System.out.println(outlineItem.getBold());
            System.out.println(outlineItem.getColor());
        }
    }
}
```

## 
Obtenir les numéros de page des favoris



Cet exemple utilise `PdfBookmarkEditor` pour extraire les titres, les niveaux, les numéros de page et les actions des signets.


1. 
Liez le PDF source à [PdfBookmarkEditor] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdfbookmarkeditor/).

1. 
Extrayez la collection de signets et parcourez-la.
1. Imprimez le niveau, le titre, le numéro de page et les informations sur l'action pour chaque signet.


```java
public static void getBookmarkPageNumber(Path inputFile) {
    PdfBookmarkEditor bookmarkEditor = new PdfBookmarkEditor();
    try {
        bookmarkEditor.bindPdf(inputFile.toString());
        for (Bookmark bookmark : bookmarkEditor.extractBookmarks()) {
            String levelSeparator = "";
            for (int i = 0; i < bookmark.getLevel(); i++) {
                levelSeparator += "----";
            }

            System.out.println(levelSeparator + " Title: " + bookmark.getTitle());
            System.out.println(levelSeparator + " Page Number: " + bookmark.getPageNumber());
            System.out.println(levelSeparator + " Page Action: " + bookmark.getAction());
        }
    } finally {
        bookmarkEditor.close();
    }
}
```

## 
Obtenir des favoris pour enfants



Utilisez cet exemple lorsque vous devez inspecter à la fois les éléments de plan de niveau supérieur et imbriqués.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez les contours de niveau supérieur et imprimez leurs propriétés.
1. Détectez les signets enfants, puis parcourez-les et imprimez leurs propriétés.


```java
public static void getChildBookmarks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection outlineItem = document.getOutlines().get_Item(i);
            System.out.println(outlineItem.getTitle());
            System.out.println(outlineItem.getItalic());
            System.out.println(outlineItem.getBold());
            System.out.println(outlineItem.getColor());
            int count = outlineItem.size();
            if (count > 0) {
                System.out.println("Child Bookmarks");
                for (int j = 1; j <= outlineItem.size(); j++) {
                    OutlineItemCollection childOutlineItem = outlineItem.get_Item(j);
                    System.out.println(childOutlineItem.getTitle());
                    System.out.println(childOutlineItem.getItalic());
                    System.out.println(childOutlineItem.getBold());
                    System.out.println(childOutlineItem.getColor());
                }
            }
        }
    }
}
```

## 
Mettre à jour les favoris



Utilisez cet exemple lorsqu’un titre et un style de signet existant doivent être modifiés.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Accédez à l’élément de plan cible et à son signet enfant.
1. Mettez à jour les propriétés du signet et enregistrez le document.


```java
public static void updateBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection outline = document.getOutlines().get_Item(1);
        OutlineItemCollection childOutline = outline.get_Item(1);
        childOutline.setTitle("Updated Outline");
        childOutline.setItalic(true);
        childOutline.setBold(true);

        document.save(outputFile.toString());
    }
}
```

## 
Développer les favoris par défaut



Utilisez cet exemple lorsque le panneau de signets doit s'ouvrir et afficher les éléments de plan développés lorsque le document est affiché.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Définissez le mode page pour utiliser les contours et marquez chaque élément du plan comme ouvert.
1. Enregistrez le document mis à jour.

```java
public static void expandedBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setPageMode(PageMode.UseOutlines);
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection item = document.getOutlines().get_Item(i);
            item.setOpen(true);
        }
        document.save(outputFile.toString());
    }
}
```
