---
title: Manipuler les tableaux dans un PDF existant
linktitle: Manipuler les tableaux
type: docs
weight: 30
url: /fr/java/manipulate-tables-in-existing-pdf/
description: Manipulez les tableaux dans un fichier PDF existant et remplacez l'ancien tableau par un nouveau dans un document PDF avec Aspose.PDF pour Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Manipuler les tableaux dans un PDF existant

L'une des premières fonctionnalités prises en charge par Aspose.PDF pour Java est ses capacités de travail avec les tableaux et il offre un excellent support pour l'ajout de tableaux dans des fichiers PDF générés à partir de zéro ou dans tout fichier PDF existant.
 Vous obtenez également la capacité d'intégrer Table avec Database (DOM) pour créer des tables dynamiques basées sur le contenu de la base de données. Dans cette nouvelle version, nous avons implémenté une nouvelle fonctionnalité de recherche et d'analyse de tables simples qui existent déjà sur la page d'un document PDF. Une nouvelle classe nommée **Aspose.PDF.Text.TableAbsorber** fournit ces capacités. L'utilisation de TableAbsorber est très similaire à l'utilisation de la classe existante TextFragmentAbsorber.

Le code suivant montre les étapes pour mettre à jour le contenu d'une cellule de tableau particulière.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleManipulate {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ManipulateTables() {

        // Charger le fichier PDF existant
        Document pdfDocument = new Document(_dataDir + "input.pdf");
        // Créer un objet TableAbsorber pour trouver les tables
        TableAbsorber absorber = new TableAbsorber();

        // Visiter la première page avec l'absorbeur
        absorber.visit(pdfDocument.getPages().get_Item(1));

        // Accéder à la première table de la page, à leur première cellule et aux fragments de texte qu'elle contient
        TextFragment fragment = absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0)
                .getTextFragments().get_Item(1);

        // Changer le texte du premier fragment de texte dans la cellule
        fragment.setText("salut monde");

        pdfDocument.save(_dataDir + "ManipulateTable_out.pdf");
    }
```

## Remplacer l'ancienne table par une nouvelle dans le document PDF

Dans le cas où vous avez besoin de trouver une table particulière et de la remplacer par celle souhaitée, vous pouvez utiliser la méthode Replace() de la classe [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) pour cela.

L'exemple suivant démontre la fonctionnalité pour remplacer la table à l'intérieur d'un document PDF :

```java
public static void ReplaceOldTableWithNew() {

        // Charger le document PDF existant
        Document pdfDocument = new Document(_dataDir + "Table_input2.pdf");

        // Créer un objet TableAbsorber pour trouver des tables
        TableAbsorber absorber = new TableAbsorber();

        Page page = pdfDocument.getPages().get_Item(1);

        // Visiter la première page avec l'absorbeur
        absorber.visit(page);

        // Obtenir la première table sur la page
        AbsorbedTable table = absorber.getTableList().get(0);

        // Créer une nouvelle table
        Table newTable = new Table();
        newTable.setColumnWidths("100 100 100");
        newTable.setDefaultCellBorder (new BorderInfo(BorderSide.All, 1F));

        Row row = newTable.getRows().add();
        row.getCells().add("Col 1");
        row.getCells().add("Col 2");
        row.getCells().add("Col 3");

        // Remplacer la table par la nouvelle
        absorber.replace(page, table, newTable);

        // Sauvegarder le document
        pdfDocument.save(_dataDir + "TableReplaced_out.pdf");
        
    }

}
```