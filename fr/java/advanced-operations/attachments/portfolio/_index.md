---
title: Créer des portefeuilles PDF en Java
linktitle: Portefeuille
type: docs
weight: 20
url: /java/portfolio/
description: Découvrez comment créer et gérer des portefeuilles PDF en Java à l'aide d'Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Créez et modifiez des portefeuilles PDF avec des fichiers intégrés en Java
Abstract: Cet article explique comment créer et gérer des portefeuilles PDF à l'aide d'Aspose.PDF pour Java. Découvrez comment activer une collection sur un document, ajouter plusieurs types de fichiers au portefeuille et supprimer tous les éléments de collection d'un portefeuille PDF existant.
---
Un portfolio PDF peut regrouper plusieurs fichiers dans un seul conteneur PDF tout en préservant chaque fichier dans son format d'origine.


## 
Créer un portfolio PDF



Utilisez cet exemple lorsque vous devez regrouper plusieurs fichiers dans une collection de portfolio PDF.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et activez sa [Collection] (https://reference.aspose.com/pdf/java/com.aspose.pdf/collection/).

1. 
Créez des objets [FileSpecification] (https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) pour chaque fichier d'entrée et définissez leurs descriptions.
1. Ajoutez les fichiers à la collection de portfolio et enregistrez le document de sortie.


```java
public static void createPdfPortfolio(Path[] inputFiles, Path outputFile) {
    try (Document document = new Document()) {
        document.setCollection(new Collection());

        FileSpecification excel = new FileSpecification(inputFiles[0].toString());
        FileSpecification word = new FileSpecification(inputFiles[1].toString());
        FileSpecification image = new FileSpecification(inputFiles[2].toString());

        excel.setDescription("Excel File");
        word.setDescription("Word File");
        image.setDescription("Image File");

        document.getCollection().add(excel);
        document.getCollection().add(word);
        document.getCollection().add(image);

        document.save(outputFile.toString());
    }
}
```

## 
Supprimer des fichiers d'un portefeuille PDF



Utilisez cet exemple lorsqu'une collection de portfolio PDF existante doit être effacée.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Supprimez les entrées de la collection de documents.
1. Enregistrez le document de sortie nettoyé.

```java
public static void removeFilesFromPdfPortfolio(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getCollection().delete();
        document.save(outputFile.toString());
    }
}
```
