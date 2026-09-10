---
title: Diviser des fichiers PDF en Java
linktitle: Diviser des fichiers PDF
type: docs
weight: 60
url: /java/split-pdf-document/
description: Découvrez comment diviser des pages PDF en fichiers PDF distincts en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Divisez les documents PDF par pages, plages, groupes et modèles de noms de fichiers à l'aide de Java
Abstract: Cet article explique comment diviser des documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre la division en pages simples, en deux ou trois parties, les pages paires et impaires, les morceaux de taille fixe, les plages personnalisées, la première ou la dernière page plus le reste, les groupes de pages personnalisés et la génération de noms de fichiers stables.
---
Aspose.PDF pour Java prend en charge plusieurs modèles de fractionnement au-delà d'une sortie d'une page par fichier.


## 
Diviser un PDF en fichiers d'une seule page



Utilisez cette approche lorsque chaque page source doit devenir un document de sortie distinct.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) pour chaque [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) que vous souhaitez exporter.
1. Ajoutez la [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) sélectionnée au nouveau document.

1. 
Enregistrez chaque PDF de sortie [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).


```java
public static void splitDocuments(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            try (Document newDocument = new Document()) {
                newDocument.getPages().add(document.getPages().get_Item(pageNumber));
                newDocument.save(outputDir.resolve("Page_" + pageNumber + ".pdf").toString());
            }
        }
    }
}
```

## 
Diviser un PDF en deux parties



Cet exemple divise le document source en deux fichiers de sortie séquentiels en fonction du point médian.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Calculez le point médian de la collection [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) disponible.

1. 
Copiez la première moitié des pages dans un document de sortie et les pages restantes dans un autre.

1. 
Enregistrez les deux documents de résultats.


```java
public static void splitDocumentsIntoTwoParts(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        int midPoint = totalPages / 2;

        try (Document firstDocument = new Document()) {
            for (int pageNumber = 1; pageNumber <= midPoint; pageNumber++) {
                firstDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            firstDocument.save(outputDir.resolve("Part_1.pdf").toString());
        }

        try (Document secondDocument = new Document()) {
            for (int pageNumber = midPoint + 1; pageNumber <= totalPages; pageNumber++) {
                secondDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            secondDocument.save(outputDir.resolve("Part_2.pdf").toString());
        }
    }
}
```

## 
Diviser un PDF en groupes de pages de taille fixe



Utilisez ce modèle lorsque chaque fichier de sortie doit contenir le même nombre de pages, sauf éventuellement la dernière partie.

1. Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez la collection [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) par groupes de `pagesPerPart`.

1. 
Créez un nouveau document de sortie pour chaque groupe et copiez-y la plage de pages calculée.

1. 
Enregistrez chaque partie avec un nom de fichier généré.


```java
public static void splitDocumentsEveryNPages(Path inputFile, Path outputDir, int pagesPerPart) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        int partIndex = 1;

        for (int startPage = 1; startPage <= totalPages; startPage += pagesPerPart) {
            int endPage = Math.min(startPage + pagesPerPart - 1, totalPages);
            try (Document partDocument = new Document()) {
                for (int pageNumber = startPage; pageNumber <= endPage; pageNumber++) {
                    partDocument.getPages().add(document.getPages().get_Item(pageNumber));
                }
                partDocument.save(outputDir.resolve("Every_" + pagesPerPart + "_Part_" + partIndex + ".pdf").toString());
            }
            partIndex++;
        }
    }
}
```

## 
Diviser un PDF par plages de pages personnalisées

Cet exemple vous permet de définir des pages de début et de fin explicites pour chaque document de sortie.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Définissez les plages [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) requises dans un tableau ou une autre collection.

1. 
Validez chaque plage par rapport au nombre de pages source et copiez les pages correspondantes dans un nouveau document.

1. 
Enregistrez chaque fichier de sortie basé sur une plage.

```java
public static void splitDocumentsByPageRanges(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        Integer[][] ranges = {{1, 3}, {4, 6}, {7, null}};

        for (int index = 0; index < ranges.length; index++) {
            int startPage = ranges[index][0];
            Integer endPage = ranges[index][1];
            if (startPage > totalPages) {
                continue;
            }

            int effectiveEnd = endPage == null ? totalPages : Math.min(endPage, totalPages);
            if (startPage > effectiveEnd) {
                continue;
            }

            try (Document rangeDocument = new Document()) {
                for (int pageNumber = startPage; pageNumber <= effectiveEnd; pageNumber++) {
                    rangeDocument.getPages().add(document.getPages().get_Item(pageNumber));
                }
                rangeDocument.save(outputDir.resolve(
                        "Range_" + (index + 1) + "_" + startPage + "_to_" + effectiveEnd + ".pdf").toString());
            }
        }
    }
}
```

## Divisez la première page et les pages restantes



Utilisez cette approche lorsque la page de garde doit être exportée séparément du reste du document.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et confirmez qu'il contient des pages.

1. 
Créez un document de sortie pour la première [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Créez un autre document pour la plage de pages restante lorsque plusieurs pages sont disponibles.
1. Enregistrez les deux résultats.


```java
public static void splitDocumentsFirstPageAndRest(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        if (totalPages == 0) {
            return;
        }

        try (Document firstPageDocument = new Document()) {
            firstPageDocument.getPages().add(document.getPages().get_Item(1));
            firstPageDocument.save(outputDir.resolve("First_Page.pdf").toString());
        }

        if (totalPages == 1) {
            return;
        }

        try (Document remainingPagesDocument = new Document()) {
            for (int pageNumber = 2; pageNumber <= totalPages; pageNumber++) {
                remainingPagesDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            remainingPagesDocument.save(outputDir.resolve("Remaining_Pages.pdf").toString());
        }
    }
}
```

## 
Diviser la dernière page et les pages précédentes



Cet exemple sépare la page finale du reste du document, ce qui est utile pour extraire des pages de résumé ou de signature.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et vérifiez qu'il n'est pas vide.

1. 
Copiez la dernière [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) dans un nouveau document de sortie.
1. Supprimez cette page du document original lorsqu'il reste des pages antérieures.

1. 
Enregistrez la dernière page et les pages restantes dans des fichiers séparés.


```java
public static void splitDocumentsLastPageAndRest(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        if (totalPages == 0) {
            return;
        }

        try (Document lastPageDocument = new Document()) {
            lastPageDocument.getPages().add(document.getPages().get_Item(totalPages));
            lastPageDocument.save(outputDir.resolve("Last_Page.pdf").toString());
        }

        if (totalPages == 1) {
            return;
        }

        document.getPages().delete(totalPages);
        document.save(outputDir.resolve("Previous_Pages.pdf").toString());
    }
}
```

## 
Diviser un PDF en trois parties



Utilisez ce modèle lorsque le document doit être divisé en trois sections consécutives de taille à peu près égale.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et déterminez le nombre total de pages.
1. Calculez la taille approximative de chaque partie de sortie.

1. 
Créez jusqu'à trois documents et copiez les plages [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) correspondantes.

1. 
Enregistrez chaque pièce générée.


```java
public static void splitDocumentsIntoThreeParts(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        if (totalPages == 0) {
            return;
        }

        int partSize = Math.max(1, (totalPages + 2) / 3);
        for (int partIndex = 0; partIndex < 3; partIndex++) {
            int startPage = partIndex * partSize + 1;
            int endPage = Math.min((partIndex + 1) * partSize, totalPages);
            if (startPage > totalPages) {
                break;
            }

            try (Document partDocument = new Document()) {
                for (int pageNumber = startPage; pageNumber <= endPage; pageNumber++) {
                    partDocument.getPages().add(document.getPages().get_Item(pageNumber));
                }
                partDocument.save(outputDir.resolve("Three_Parts_" + (partIndex + 1) + ".pdf").toString());
            }
        }
    }
}
```

## 
Diviser un PDF en groupes de pages personnalisés



Cet exemple montre comment créer des fichiers de sortie à partir d'ensembles de pages non séquentiels au lieu de plages continues.

1. Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Définissez des groupes personnalisés de numéros [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Créez un nouveau document de sortie pour chaque groupe et ajoutez uniquement les pages valides de ce groupe.

1. 
Enregistrez chaque document de groupe non vide.


```java
public static void splitDocumentsCustomPageGroups(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        List<List<Integer>> groups = List.of(
                List.of(1, 2, 5),
                List.of(3, 4, 6, 7));

        int groupIndex = 1;
        for (List<Integer> group : groups) {
            try (Document groupDocument = new Document()) {
                for (Integer pageNumber : group) {
                    if (pageNumber >= 1 && pageNumber <= totalPages) {
                        groupDocument.getPages().add(document.getPages().get_Item(pageNumber));
                    }
                }
                if (groupDocument.getPages().size() > 0) {
                    groupDocument.save(outputDir.resolve("Custom_Group_" + groupIndex + ".pdf").toString());
                }
            }
            groupIndex++;
        }
    }
}
```

## 
Divisez un PDF en pages uniques avec des noms de fichiers stables

Utilisez cette version lorsque les noms de sortie doivent rester triables lexicalement, par exemple dans des pipelines automatisés.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un document de sortie pour chaque [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Enregistrez chaque fichier avec un numéro de page complété par des zéros.


```java
public static void splitDocumentsWithStableFilenames(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            try (Document newDocument = new Document()) {
                newDocument.getPages().add(document.getPages().get_Item(pageNumber));
                newDocument.save(outputDir.resolve(String.format("Page_%03d.pdf", pageNumber)).toString());
            }
        }
    }
}
```

## 
Diviser un PDF en pages paires et impaires

Cet exemple crée deux sorties en séparant les pages en fonction de leur parité de numéro de page.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un document de sortie pour les numéros de [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) impairs et un autre pour les numéros de page pairs.

1. 
Parcourez les pages sources avec l'incrément requis pour chaque document de sortie.

1. 
Enregistrez séparément les résultats des pages impaires et des pages paires.

```java
public static void splitDocumentsOddEvenPages(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();

        try (Document oddDocument = new Document()) {
            for (int pageNumber = 1; pageNumber <= totalPages; pageNumber += 2) {
                oddDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            oddDocument.save(outputDir.resolve("Odd_Pages.pdf").toString());
        }

        try (Document evenDocument = new Document()) {
            for (int pageNumber = 2; pageNumber <= totalPages; pageNumber += 2) {
                evenDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            evenDocument.save(outputDir.resolve("Even_Pages.pdf").toString());
        }
    }
}
```
