---
title: Ajouter et supprimer des signets PDF en Java
linktitle: Ajouter et supprimer un signet
type: docs
weight: 10
url: /java/add-and-delete-bookmark/
description: Découvrez comment ajouter et supprimer des signets dans des documents PDF à l'aide de Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter ou supprimer des signets dans des documents PDF avec Java
Abstract: Cet article montre comment créer et supprimer des signets à l'aide d'Aspose.PDF pour Java. Les exemples montrent l'ajout d'un signet de niveau supérieur, la création d'une hiérarchie de signets enfants, la suppression de tous les signets et la suppression d'un signet spécifique par titre.
---
Utilisez la collection de plans de documents pour gérer les signets par programmation.


## 
Ajouter un favori de niveau supérieur



Utilisez cet exemple lorsque le document doit inclure une seule entrée de plan de niveau supérieur.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [OutlineItemCollection] (https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) et configurez son titre, son style et son action.
1. Ajoutez le signet aux plans du document et enregistrez le fichier.


```java
public static void addBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection pdfOutline = new OutlineItemCollection(document.getOutlines());
        pdfOutline.setTitle("Test Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);
        pdfOutline.setAction(new GoToAction(document.getPages().get_Item(1)));

        document.getOutlines().add(pdfOutline);
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter un favori enfant



Cet exemple crée un signet parent et imbrique un signet enfant en dessous.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez des objets parent et enfant [OutlineItemCollection] (https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/).
1. Ajoutez l'enfant au parent, ajoutez le parent à la collection de plans et enregistrez le document.


```java
public static void addChildBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection pdfOutline = new OutlineItemCollection(document.getOutlines());
        pdfOutline.setTitle("Parent Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        OutlineItemCollection pdfChildOutline = new OutlineItemCollection(document.getOutlines());
        pdfChildOutline.setTitle("Child Outline");
        pdfChildOutline.setItalic(true);
        pdfChildOutline.setBold(true);

        pdfOutline.add(pdfChildOutline);
        document.getOutlines().add(pdfOutline);
        document.save(outputFile.toString());
    }
}
```

## 
Supprimer tous les favoris



Utilisez cette approche lorsque la totalité de la collection de plans doit être supprimée du document.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Supprimez la collection de contours complète.
1. Enregistrez le fichier de sortie nettoyé.


```java
public static void deleteBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete();
        document.save(outputFile.toString());
    }
}
```

## 
Supprimer un favori spécifique



Utilisez cet exemple lorsqu'un signet nommé doit être supprimé sans effacer toute l'arborescence.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Supprimez le signet par titre de la collection de plans.
1. Enregistrez le document mis à jour.

```java
public static void deleteBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete("Child Outline");
        document.save(outputFile.toString());
    }
}
```
