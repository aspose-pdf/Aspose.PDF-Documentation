---
title: Ajouter des pages PDF en Java
linktitle: Ajout de pages
type: docs
weight: 10
url: /java/add-pages/
description: Découvrez comment ajouter ou insérer des pages dans des documents PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter ou insérer des pages PDF avec Java
Abstract: Cet article explique comment ajouter des pages aux fichiers PDF à l'aide d'Aspose.PDF pour Java. Il couvre l'insertion d'une page vierge à un emplacement spécifique, l'ajout d'une page à la fin d'un document et l'importation d'une page à partir d'un autre PDF.
---
Aspose.PDF pour Java vous permet d'insérer des pages vierges ou d'importer des pages à partir d'un autre document.


## 
Insérer une page vide à un emplacement spécifique



Utilisez cet exemple lorsque vous devez ajouter une page vierge au milieu d'un PDF existant.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Insérez une nouvelle page dans la position cible dans la collection de pages.
1. Enregistrez le document mis à jour.


```java
public static void insertEmptyPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().insert(2);
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter une page vide à la fin



Utilisez cet exemple lorsque vous devez étendre le document avec une nouvelle dernière page vierge.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Ajoutez une nouvelle page à la fin de la collection de pages.
1. Enregistrez le PDF modifié.


```java
public static void addEmptyPageToEnd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().add();
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter une page d'un autre document



Utilisez cet exemple lorsque vous souhaitez importer une page d'un PDF dans un autre PDF.


1. 
Créez la destination [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ouvrez le document source.

1. 
Ajoutez tout contenu de destination requis et importez la page cible à partir du PDF source.
1. Enregistrez le document résultant.

```java
public static void addPageFromAnotherDocument(Path inputFile, Path outputFile) {
    try (Document document = new Document();
         Document anotherDocument = new Document(inputFile.toString())) {
        document.getPages().add().getParagraphs().add(new TextFragment("This is first page!"));
        document.getPages().add(anotherDocument.getPages().get_Item(1));
        document.save(outputFile.toString());
    }
}
```
