---
title: Fusionner des fichiers PDF en Java
linktitle: Fusionner des fichiers PDF
type: docs
weight: 50
url: /java/merge-pdf-documents/
description: Découvrez comment fusionner plusieurs fichiers PDF en un seul document en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Combinez des documents complets, des plages sélectionnées et des pages alternées avec Java
Abstract: Cet article explique comment fusionner des documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre la combinaison de deux fichiers, la fusion de plusieurs documents, la sélection de plages de pages, l'insertion d'un document dans un autre à une position spécifique, l'alternance de pages et la création d'une sortie fusionnée avec des signets de section.
---
Aspose.PDF pour Java prend en charge plusieurs stratégies de fusion en fonction de la manière dont la sortie doit être assemblée.


## 
Fusionner deux documents PDF



Utilisez cette approche lorsque vous avez besoin du flux de fusion le plus simple et que vous souhaitez ajouter un document complet à un autre.


1. 
Ouvrez les deux objets PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Ajoutez la collection [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) du deuxième document au premier document.
1. Enregistrez le [Document] PDF mis à jour (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).


```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```

## 
Copier une plage de pages sélectionnée entre des documents



Cette méthode d'assistance conserve la logique de fusion de plages de pages au même endroit afin que d'autres exemples puissent réutiliser la même routine de copie validée.


1. 
Ouvrez ou recevez les objets PDF [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) source et destination.

1. 
Normalisez la plage de pages demandée afin qu’elle reste dans la collection [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) disponible.
1. Ajoutez chaque page de la plage validée au document de destination.


```java
private static void appendPageRange(Document sourceDocument, Document destinationDocument, int startPage, int endPage) {
    int totalPages = sourceDocument.getPages().size();
    if (totalPages == 0) {
        return;
    }

    int start = Math.max(1, startPage);
    int end = Math.min(endPage, totalPages);
    if (start > end) {
        return;
    }

    for (int pageNumber = start; pageNumber <= end; pageNumber++) {
        destinationDocument.getPages().add(sourceDocument.getPages().get_Item(pageNumber));
    }
}
```

## 
Fusionner plusieurs documents PDF en un seul fichier



Utilisez ce modèle lorsque vous devez combiner une liste de fichiers d’entrée en un seul document de sortie en séquence.


1. 
Créez un PDF de sortie vide [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Ouvrez chaque fichier d'entrée un par un et copiez sa plage complète de [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) dans le document de sortie.
1. Enregistrez le résultat fusionné une fois que tous les fichiers sources ont été traités.


```java
public static void mergeMultipleDocuments(List<Path> inputFiles, Path outputFile) {
    try (Document outputDocument = new Document()) {
        for (Path inputFile : inputFiles) {
            try (Document sourceDocument = new Document(inputFile.toString())) {
                appendPageRange(sourceDocument, outputDocument, 1, sourceDocument.getPages().size());
            }
        }
        outputDocument.save(outputFile.toString());
    }
}
```

## 
Fusionner les plages de pages sélectionnées à partir de deux documents



Cet exemple crée un fichier de sortie personnalisé en prenant uniquement des plages de pages spécifiques de chaque document source.


1. 
Ouvrez les deux objets PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et créez un nouveau document de sortie.

1. 
Ajoutez uniquement les plages [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) requises de chaque document source.
1. Enregistrez le document de sortie assemblé.


```java
public static void mergeSelectedPageRanges(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString());
         Document outputDocument = new Document()) {
        appendPageRange(document1, outputDocument, 1, 2);
        appendPageRange(document2, outputDocument, 2, 3);
        outputDocument.save(outputFile.toString());
    }
}
```

## 
Insérer un document PDF dans un autre à une position spécifique



Utilisez cette approche lorsqu'un document doit apparaître dans un autre plutôt que seulement avant ou après.


1. 
Ouvrez la base et les objets PDF [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) insérés et créez un nouveau document de sortie.

1. 
Copiez la première partie du document de base, puis ajoutez le document inséré dans son intégralité et enfin ajoutez la plage de base restante [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Enregistrez le résultat réorganisé dans un nouveau fichier.


```java
public static void mergeInsertDocumentAtPosition(Path inputFile1, Path inputFile2, int insertAfterPage, Path outputFile) {
    try (Document baseDocument = new Document(inputFile1.toString());
         Document insertDocument = new Document(inputFile2.toString());
         Document outputDocument = new Document()) {
        int baseTotalPages = baseDocument.getPages().size();
        int insertIndex = Math.max(0, Math.min(insertAfterPage, baseTotalPages));

        appendPageRange(baseDocument, outputDocument, 1, insertIndex);
        appendPageRange(insertDocument, outputDocument, 1, insertDocument.getPages().size());
        appendPageRange(baseDocument, outputDocument, insertIndex + 1, baseTotalPages);

        outputDocument.save(outputFile.toString());
    }
}
```

## 
Fusionner deux documents PDF en alternant les pages



Cet exemple entrelace les pages de deux documents, ce qui est utile lorsque les deux entrées doivent contribuer page par page au résultat final.


1. 
Ouvrez les deux objets PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et créez un nouveau document de sortie.

1. 
Parcourez le nombre maximum de pages disponibles et ajoutez tour à tour chaque [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) disponible du premier et du deuxième documents.
1. Enregistrez le document de sortie entrelacé.


```java
public static void mergeAlternatingPages(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString());
         Document outputDocument = new Document()) {
        int document1Pages = document1.getPages().size();
        int document2Pages = document2.getPages().size();
        int maxPages = Math.max(document1Pages, document2Pages);

        for (int pageNumber = 1; pageNumber <= maxPages; pageNumber++) {
            if (pageNumber <= document1Pages) {
                outputDocument.getPages().add(document1.getPages().get_Item(pageNumber));
            }
            if (pageNumber <= document2Pages) {
                outputDocument.getPages().add(document2.getPages().get_Item(pageNumber));
            }
        }

        outputDocument.save(outputFile.toString());
    }
}
```

## 
Fusionner des documents avec des pages de séparation et des signets



Utilisez ce modèle lorsque le fichier fusionné doit rester facile à naviguer et montrer clairement où commence chaque document source.


1. 
Créez un PDF de sortie vide [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ouvrez chaque fichier source tour à tour.

1. 
Ajoutez un séparateur [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) avec un en-tête, puis créez un signet [OutlineItemCollection] (https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) pour cette section.
1. Ajoutez les pages sources, ajoutez éventuellement un signet qui pointe vers la première page de contenu et enregistrez le document final fusionné.

```java
public static void mergeWithSectionSeparatorsAndBookmarks(List<Path> inputFiles, Path outputFile) {
    try (Document outputDocument = new Document()) {
        int sectionIndex = 1;
        for (Path inputFile : inputFiles) {
            try (Document sourceDocument = new Document(inputFile.toString())) {
                int sourcePageCount = sourceDocument.getPages().size();

                Page separatorPage = outputDocument.getPages().add();
                separatorPage.getParagraphs().add(new TextFragment(
                        "Section " + sectionIndex + ": " + inputFile.getFileName()));

                OutlineItemCollection sectionBookmark = new OutlineItemCollection(outputDocument.getOutlines());
                sectionBookmark.setTitle("Section " + sectionIndex);
                sectionBookmark.setAction(new GoToAction(separatorPage));
                outputDocument.getOutlines().add(sectionBookmark);

                int firstContentPageNumber = outputDocument.getPages().size() + 1;
                appendPageRange(sourceDocument, outputDocument, 1, sourcePageCount);

                if (sourcePageCount > 0 && firstContentPageNumber <= outputDocument.getPages().size()) {
                    OutlineItemCollection contentBookmark = new OutlineItemCollection(outputDocument.getOutlines());
                    contentBookmark.setTitle("Section " + sectionIndex + " Content");
                    contentBookmark.setAction(new GoToAction(outputDocument.getPages().get_Item(firstContentPageNumber)));
                    sectionBookmark.add(contentBookmark);
                }
            }
            sectionIndex++;
        }

        outputDocument.save(outputFile.toString());
    }
}
```
