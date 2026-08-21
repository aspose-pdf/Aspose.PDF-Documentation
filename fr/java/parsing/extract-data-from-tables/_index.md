---
title: Extraire les données d'un tableau au format PDF avec Java
linktitle: Extraire les données du tableau
type: docs
weight: 40
url: /java/extract-data-from-table-in-pdf/
description: Découvrez comment extraire les données de tableaux de fichiers PDF avec Aspose.PDF pour Java et exporter les tableaux détectés pour un traitement ultérieur.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment extraire des données d'un tableau en PDF via Java
Abstract: Cet article explique comment extraire et traiter les données de tableaux à partir de documents PDF avec Aspose.PDF pour Java. Il montre comment numériser des pages avec `TableAbsorber`, lire les lignes et les cellules des tableaux détectés, limiter l'extraction à une région annotée spécifique et exporter le résultat vers Excel.
---
## Extraire des tableaux d'un PDF



Utilisez `TableAbsorber` pour rechercher des tableaux sur chaque page et parcourir les lignes, les cellules, les fragments de texte et les segments de texte.


1. 
Ouvrez le PDF source dans une instance [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez les objets du document [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) car les tableaux sont détectés page par page.

1. 
Créez un [TableAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) pour chaque page et appelez `visit(page)` pour remplir la liste des tables détectées.
1. Parcourez les objets [AbsorbedTable] (https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/), [AbsorbedRow] (https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/), [AbsorbedCell] (https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/), [TextFragment] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) et `TextSegment` détectés.

1. 
Créez le texte de la ligne extrait à partir du contenu du fragment et imprimez les données du tableau.


```java
public static void extractTablesFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            TableAbsorber absorber = new TableAbsorber();
            absorber.visit(page);

            for (AbsorbedTable table : absorber.getTableList()) {
                System.out.println("Table");
                for (AbsorbedRow row : table.getRowList()) {
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        if (rowText.length() > 0) {
                            rowText.append("|");
                        }
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            StringBuilder fragmentText = new StringBuilder();
                            for (TextSegment segment : fragment.getSegments()) {
                                fragmentText.append(segment.getText());
                            }
                            if (cellText.length() > 0) {
                                cellText.append("|");
                            }
                            cellText.append(fragmentText);
                        }
                        rowText.append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```

## 
Extraire un tableau d'une zone marquée spécifique



Cet exemple recherche une annotation carrée, compare son rectangle à chaque table détectée et génère uniquement les tables situées à l'intérieur de la région marquée.


1. 
Ouvrez le PDF source dans une instance [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Obtenez la cible [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) et localisez le carré [Annotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) qui marque la région d'extraction.

1. 
Créez un [TableAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) et appelez `visit(page)` pour détecter les tables sur cette page.

1. 
Comparez chaque [AbsorbedTable] (https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/) [Rectangle] (https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) détecté avec les limites du rectangle d'annotation.

1. 
Parcourez les objets [AbsorbedRow] (https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/) et [AbsorbedCell] (https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/) correspondants et reconstruisez le texte de la ligne.

1. 
Imprimez les données du tableau pour la région marquée uniquement.

```java
public static void extractTableFromSpecificArea(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        Annotation squareAnnotation = null;
        for (Annotation annotation : page.getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Square) {
                squareAnnotation = annotation;
                break;
            }
        }

        if (squareAnnotation == null) {
            System.out.println("No square annotation found.");
            return;
        }

        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(page);

        for (AbsorbedTable table : absorber.getTableList()) {
            Rectangle tableRect = table.getRectangle();
            Rectangle annotationRect = squareAnnotation.getRect();

            boolean isInRegion = annotationRect.getLLX() < tableRect.getLLX()
                    && annotationRect.getLLY() < tableRect.getLLY()
                    && annotationRect.getURX() > tableRect.getURX()
                    && annotationRect.getURY() > tableRect.getURY();

            if (isInRegion) {
                for (AbsorbedRow row : table.getRowList()) {
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        if (rowText.length() > 0) {
                            rowText.append("|");
                        }
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            StringBuilder fragmentText = new StringBuilder();
                            for (TextSegment segment : fragment.getSegments()) {
                                fragmentText.append(segment.getText());
                            }
                            if (cellText.length() > 0) {
                                cellText.append("|");
                            }
                            cellText.append(fragmentText);
                        }
                        rowText.append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```

## Exporter des tableaux vers Excel


1. 
Ouvrez le PDF source dans une instance [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez [ExcelSaveOptions] (https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) pour l'exportation.

1. 
Définissez le format de sortie Excel sur `XLSX` afin que la disposition du tableau détectée soit écrite sous forme de classeur Excel.

1. 
Appelez `document.save(outputFile.toString(), excelSave)` pour exporter le document au format Excel.

```java
public static void exportTablesToExcel(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), excelSave);
    }
}
```
