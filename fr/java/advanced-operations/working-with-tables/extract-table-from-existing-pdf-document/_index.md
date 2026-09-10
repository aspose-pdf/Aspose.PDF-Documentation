---
title: Extraire des tableaux d'un PDF en Java
linktitle: Extraire le tableau
type: docs
weight: 20
url: /java/extracting-table/
description: Découvrez comment extraire des données de tableau à partir de documents PDF existants en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraire les données d'un tableau à partir de fichiers PDF avec Java
Abstract: Cet article explique comment extraire des tableaux de documents PDF à l'aide d'Aspose.PDF pour Java. Il montre comment utiliser TableAbsorber pour détecter les tableaux par page, itérer les lignes et les cellules et collecter le texte des cellules pour le traitement en aval.
---
Utilisez `TableAbsorber` lorsque vous devez détecter les structures de tableaux dans un PDF existant et lire leur contenu.


## 
Extraire le texte des tables détectées



Utilisez cet exemple lorsque vous devez localiser des tableaux sur chaque page et collecter le texte de leur cellule.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Visitez chaque page avec [TableAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
1. Parcourez les tableaux, les lignes et les cellules absorbés, puis affichez le texte extrait.

```java
public static void extract(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            TableAbsorber absorber = new TableAbsorber();
            absorber.visit(page);
            for (AbsorbedTable table : absorber.getTableList()) {
                System.out.println("Table ----");
                for (AbsorbedRow row : table.getRowList()) {
                    System.out.println("Row:");
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            for (TextSegment segment : fragment.getSegments()) {
                                cellText.append(segment.getText());
                            }
                        }
                        rowText.append(" | ").append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```
