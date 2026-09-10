---
title: Comparer des documents PDF en Java
linktitle: Comparer le PDF
type: docs
weight: 130
url: /java/compare-pdf-documents/
description: Apprenez à comparer des documents PDF en Java à l'aide d'une sortie côte à côte et de différences graphiques avec Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comparez les pages PDF et les documents complets avec une sortie de différence visuelle en Java
Abstract: Cet article explique comment comparer des documents PDF à l'aide d'Aspose.PDF pour Java. Découvrez comment comparer des pages spécifiques ou des fichiers PDF entiers avec une sortie côte à côte, générer des rapports de différences PDF graphiques et exporter les différences d'images au niveau de la page.
---
Aspose.PDF pour Java fournit des API de comparaison côte à côte et graphiques pour détecter les différences entre les fichiers PDF.


## 
Comparez les pages et exportez les images de différence



Utilisez cet exemple lorsque vous avez besoin d’une sortie de différence basée sur une image pour une paire spécifique de pages PDF.


1. 
Ouvrez les deux objets PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Utilisez [GraphicalPdfComparer] (https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/) pour obtenir la [ImagesDifference] (https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/imagesdifference/) au niveau de la page.
1. Utilisez « GraphicalPdfComparer » pour obtenir la « ImagesDifference » au niveau de la page.

1. 
Exportez les images de différence générées et supprimez le résultat de la comparaison.


```java
public static void comparePdfWithGetDifferenceMethod(
        Path inputFile1, Path inputFile2, Path diffOutputFile, Path destinationOutputFile) throws Exception {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        GraphicalPdfComparer comparer = new GraphicalPdfComparer();
        ImagesDifference imagesDifference = comparer.getDifference(document1.getPages().get_Item(1),
                document2.getPages().get_Item(1));

        ImageIO.write(imagesDifference.differenceToImage(Color.getRed(), Color.getWhite()),
                "png", diffOutputFile.toFile());
        ImageIO.write(imagesDifference.getDestinationImage(), "png", destinationOutputFile.toFile());
        imagesDifference.dispose();
    }
    System.out.println("Difference images saved to " + diffOutputFile + " and " + destinationOutputFile);
}
```

## 
Comparez des pages spécifiques côte à côte



Utilisez cet exemple lorsque seules les pages sélectionnées doivent être comparées et enregistrées sous forme de résultat PDF côte à côte.


1. 
Ouvrez les deux objets PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Configurez [SideBySideComparisonOptions] (https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) pour le mode de comparaison requis.

1. 
Comparez les pages sélectionnées et enregistrez le PDF de sortie.


```java
public static void comparingSpecificPages(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        SideBySideComparisonOptions options = new SideBySideComparisonOptions();
        options.setAdditionalChangeMarks(true);
        options.setComparisonMode(ComparisonMode.IgnoreSpaces);

        SideBySidePdfComparer.compare(document1.getPages().get_Item(1), document2.getPages().get_Item(1),
                outputFile.toString(), options);
    }
    System.out.println("Specific pages comparison saved to " + outputFile);
}
```

## 
Comparez graphiquement les documents PDF complets



Cet exemple génère un rapport PDF graphique qui met en évidence les différences visuelles dans l'ensemble des documents.


1. 
Ouvrez les deux objets PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Configurez le seuil, la couleur et la résolution de [GraphicalPdfComparer] (https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/).

1. 
Comparez les documents complets et enregistrez le PDF de sortie graphique.


```java
public static void comparePdfWithCompareDocumentsToPdfMethod(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        GraphicalPdfComparer pdfComparer = new GraphicalPdfComparer();
        pdfComparer.setThreshold(3.0);
        pdfComparer.setColor(Color.getBlue());
        pdfComparer.setResolution(new Resolution(300));
        pdfComparer.compareDocumentsToPdf(document1, document2, outputFile.toString());
    }
    System.out.println("Graphical comparison saved to " + outputFile);
}
```

## 
Comparez des documents entiers côte à côte



Utilisez cet exemple lorsque les documents entiers doivent être comparés page par page dans une sortie PDF côte à côte.


1. 
Ouvrez les deux objets PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Configurez [SideBySideComparisonOptions] (https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) pour le comportement de comparaison souhaité.

1. 
Comparez les documents complets et enregistrez le résultat au format PDF.

```java
public static void comparingEntireDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        SideBySideComparisonOptions options = new SideBySideComparisonOptions();
        options.setAdditionalChangeMarks(true);
        options.setComparisonMode(ComparisonMode.IgnoreSpaces);

        SideBySidePdfComparer.compare(document1, document2, outputFile.toString(), options);
    }
    System.out.println("Entire document comparison saved to " + outputFile);
}
```
