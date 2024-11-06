---
title: Créer ou Ajouter un Tableau dans un PDF 
linktitle: Créer ou Ajouter un Tableau
type: docs
weight: 10
url: fr/java/add-table-in-existing-pdf-document/
description: Apprenez à créer ou ajouter un tableau dans un document PDF, appliquer un style aux cellules, diviser le tableau sur des pages et personnaliser les lignes et colonnes, etc.
lastmod: "2021-12-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Création de Table

Le namespace Aspose.PDF contient des classes nommées [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table), [Cell](https://reference.aspose.com/pdf/java/com.aspose.pdf/cell), et [Row](https://reference.aspose.com/pdf/java/com.aspose.pdf/row) qui fournissent des fonctionnalités pour créer des tables lors de la génération de documents PDF à partir de zéro.

Un tableau peut être créé en créant un objet de la classe Table.

```java
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
```

### Ajout de Table dans un Document PDF Existant

Pour ajouter un tableau à un fichier PDF existant avec Aspose.PDF pour Java, suivez les étapes suivantes :

1. Chargez le fichier source.

1. Initialiser une table et définir ses colonnes et lignes.
1. Définir le paramétrage de la table (nous avons défini les bordures).
1. Remplir la table.
1. Ajouter la table à une page.
1. Enregistrer le fichier.

Les extraits de code suivants montrent comment ajouter du texte dans un fichier PDF existant.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddTable {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void CreateTable() {
        Document doc = new Document(_dataDir + "input.pdf");
        // Initialise une nouvelle instance de Table
        Table table = new Table();
        // Définir la couleur de bordure de la table comme LightGray
        table.setBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // définir la bordure pour les cellules de la table
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // créer une boucle pour ajouter 10 lignes
        for (int row_count = 1; row_count < 10; row_count++) {
            // ajouter une ligne à la table
            Row row = table.getRows().add();
            // ajouter des cellules de table
            row.getCells().add("Colonne (" + row_count + ", 1)");
            row.getCells().add("Colonne (" + row_count + ", 2)");
            row.getCells().add("Colonne (" + row_count + ", 3)");
        }
        // Ajouter l'objet table à la première page du document d'entrée
        doc.getPages().get_Item(1).getParagraphs().add(table);
        // Enregistrer le document mis à jour contenant l'objet table
        doc.save(_dataDir + "document_with_table.pdf");
    }
```


### ColSpan et RowSpan dans les tableaux Aspose.PDF en Java

Aspose.PDF pour Java fournit la méthode [setColSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setColSpan-int-) pour fusionner les colonnes dans un tableau et la méthode [setRowSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setRowSpan-int-) pour fusionner les lignes.

Nous utilisons les méthodes [setColSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setColSpan-int-) ou [setRowSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setRowSpan-int-) sur l'objet [Cell](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell) qui crée la cellule du tableau. Après avoir appliqué les propriétés requises, la cellule créée peut être ajoutée au tableau.

```java
public static void AddTable_RowColSpan() {
        // Charger le document PDF source
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        // Initialise une nouvelle instance de Table
        Table table = new Table();
        // Définir la couleur de la bordure du tableau comme LightGray
        table.setBorder(new BorderInfo(BorderSide.All, .5f, Color.getBlack()));
        // Définir la bordure pour les cellules du tableau
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, .5f, Color.getBlack()));
        // Ajouter la 1ère ligne au tableau
        Row row1 = table.getRows().add();
        for (int cellCount = 1; cellCount < 5; cellCount++) {
            // Ajouter des cellules au tableau
            row1.getCells().add("Test 1 " + cellCount);
        }

        // Ajouter la 2ème ligne au tableau
        Row row2 = table.getRows().add();
        row2.getCells().add("Test 2 1");
        Cell cell = row2.getCells().add("Test 2 2");
        cell.setColSpan(2);
        row2.getCells().add("Test 2 4");

        // Ajouter la 3ème ligne au tableau
        Row row3 = table.getRows().add();
        row3.getCells().add("Test 3 1");
        row3.getCells().add("Test 3 2");
        row3.getCells().add("Test 3 3");
        row3.getCells().add("Test 3 4");

        // Ajouter la 4ème ligne au tableau
        Row row4 = table.getRows().add();
        row3.getCells().add("Test 4 1");
        cell = row3.getCells().add("Test 4 2");
        cell.setRowSpan(2);
        row3.getCells().add("Test 4 3");
        row3.getCells().add("Test 4 4");

        // Ajouter la 5ème ligne au tableau
        row4 = table.getRows().add();
        row4.getCells().add("Test 5 1");
        row4.getCells().add("Test 5 3");
        row4.getCells().add("Test 5 4");

        // Ajouter l'objet table à la première page du document d'entrée
        page.getParagraphs().add(table);

        // Enregistrer le document mis à jour contenant l'objet table
        pdfDocument.save(_dataDir + "document_with_table_out.pdf");
    }
```


Le résultat de l'exécution du code ci-dessous est le tableau représenté sur l'image suivante :

![Démonstration de ColSpan et RowSpan](colspan_rowspan.png)

## Travailler avec les Bordures, Marges et Espacements

Aspose.PDF pour Java permet aux développeurs de créer des tableaux dans des documents PDF. Selon le modèle d'objet de document d'Aspose.PDF, un tableau est un élément de niveau paragraphe.

Veuillez noter qu'il prend également en charge la fonctionnalité de définir le style de bordure, les marges et l'espacement des cellules pour les tableaux. Avant d'entrer dans des détails plus techniques, il est important de comprendre les concepts de bordure, marges et espacement qui sont présentés ci-dessous dans un diagramme :

![Bordures, marges et espacements](set-border-style-margins-and-padding-of-table_1.png)

Dans la figure ci-dessus, vous pouvez voir que les bordures de la table, de la ligne et de la cellule se chevauchent. En utilisant Aspose.PDF, une table peut avoir des marges et les cellules peuvent avoir des espacements. Pour définir les marges des cellules, nous devons définir l'espacement des cellules.

## Bordures

Pour définir les bordures des objets [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table), [Row](https://reference.aspose.com/pdf/java/com.aspose.pdf/row) et [Cell](https://reference.aspose.com/pdf/java/com.aspose.pdf/cell), utilisez les méthodes [Table.setBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table#setBorder-com.aspose.pdf.BorderInfo-), [Row.setBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Row#setBorder-com.aspose.pdf.BorderInfo-) et [Cell.setBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setBorder-com.aspose.pdf.BorderInfo-).
 Les bordures des cellules peuvent également être définies en utilisant la méthode [DefaultCellBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Row#setDefaultCellBorder-com.aspose.pdf.BorderInfo-) de la classe [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table) ou [Row](https://reference.aspose.com/pdf/java/com.aspose.pdf/row). Toutes les propriétés liées aux bordures discutées ci-dessus sont assignées à une instance de la classe Row, qui est créée en appelant son constructeur. La classe Row a de nombreuses surcharges qui prennent presque tous les paramètres nécessaires pour personnaliser la bordure.

## Marges ou Rembourrage

Le rembourrage des cellules peut être géré en utilisant la méthode [DefaultCellPadding](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table#setDefaultCellPadding-com.aspose.pdf.MarginInfo-) de la classe Table. Toutes les propriétés liées au padding sont assignées à une instance de la classe [MarginInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/MarginInfo) qui prend des informations sur les paramètres `Left`, `Right`, `Top` et `Bottom` pour créer des marges personnalisées.

Dans l'exemple suivant, la largeur de la bordure de la cellule est fixée à 0,1 point, la largeur de la bordure du tableau est fixée à 1 point et le padding des cellules est fixé à 5 points.

![Marge et Bordure dans un Tableau PDF](margin-border.png)

```java
public static void MargingPadding() {
        // Instancier l'objet Document en appelant son constructeur vide
        Document doc = new Document();
        Page page = doc.getPages().add();
        // Instancier un objet table
        Table tab1 = new Table();
        // Ajouter le tableau dans la collection de paragraphes de la section souhaitée
        page.getParagraphs().add(tab1);
        // Définir les largeurs de colonne du tableau
        tab1.setColumnWidths ("50 50 50");
        // Définir la bordure par défaut des cellules en utilisant l'objet BorderInfo
        tab1.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1F));
        // Définir la bordure du tableau en utilisant un autre objet BorderInfo personnalisé
        tab1.setBorder (new BorderInfo(BorderSide.All, 1F));

        // Créer un objet MarginInfo et définir ses marges gauche, bas, droite et haut
        MarginInfo margin = new MarginInfo();
        margin.setTop (5f);
        margin.setLeft (5f);
        margin.setRight (5f);
        margin.setBottom (5f);

        // Définir le padding par défaut des cellules sur l'objet MarginInfo
        tab1.setDefaultCellPadding(margin);

        // Créer des lignes dans le tableau puis des cellules dans les lignes
        Row row1 = tab1.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add();

        TextFragment mytext = new TextFragment("col3 avec une longue chaîne de texte");

        row1.getCells().get_Item(2).getParagraphs().add(mytext);
        row1.getCells().get_Item(2).setWordWrapped(false);

        Row row2 = tab1.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");

        // Enregistrer le PDF
        doc.save(_dataDir + "MarginsOrPadding_out.pdf");
    }
}
```

Pour créer une table avec des coins arrondis, utilisez la valeur `RoundedBorderRadius` de la classe [BorderInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/BorderInfo) et définissez le style des coins de la table sur arrondi.

```java
    public static void RoundedBorderRadius() {
        Document doc = new Document();
        Page page = doc.getPages().add();

        // Instancier un objet table
        Table tab1 = new Table();

        // Ajouter la table dans la collection de paragraphes de la section souhaitée
        page.getParagraphs().add(tab1);

        GraphInfo graph = new GraphInfo();
        graph.setColor(Color.getRed());
        // Créer un objet BorderInfo vide
        BorderInfo bInfo = new BorderInfo(BorderSide.All, graph);
        // Définir la bordure comme une bordure arrondie avec un rayon de 15
        bInfo.setRoundedBorderRadius(15);
        // Définir le style des coins de la table comme arrondi.
        tab1.setCornerStyle(BorderCornerStyle.Round);
        // Définir les informations de bordure de la table
        tab1.setBorder(bInfo);
        // Créer des lignes dans la table, puis des cellules dans les lignes
        Row row1 = tab1.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add();

        TextFragment mytext = new TextFragment("col3 avec une longue chaîne de texte");

        row1.getCells().get_Item(2).getParagraphs().add(mytext);
        row1.getCells().get_Item(2).setWordWrapped(false);

        Row row2 = tab1.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");

        // Enregistrer le PDF
        doc.save(_dataDir + "BorderRadius_out.pdf");
    }
```


### Propriété AutoFitToWindow dans l'énumération ColumnAdjustmentType

```java
 public static void AutoFitToWindowProperty() {
        // Instancier l'objet Pdf en appelant son constructeur vide
        Document doc = new Document();
        // Créer la section dans l'objet Pdf
        Page sec1 = doc.getPages().add();

        // Instancier un objet table
        Table tab1 = new Table();
        // Ajouter la table dans la collection de paragraphes de la section souhaitée
        sec1.getParagraphs().add(tab1);

        // Définir les largeurs de colonnes du tableau
        tab1.setColumnWidths("50 50 50");
        tab1.setColumnAdjustment(ColumnAdjustment.AutoFitToWindow);

        // Définir la bordure de cellule par défaut en utilisant l'objet BorderInfo
        tab1.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1F));

        // Définir la bordure du tableau en utilisant un autre objet BorderInfo personnalisé
        tab1.setBorder(new BorderInfo(BorderSide.All, 1F));

        // Créer un objet MarginInfo et définir ses marges gauche, bas, droite et haut
        MarginInfo margin = new MarginInfo();
        margin.setTop(5f);
        margin.setLeft(5f);
        margin.setRight(5f);
        margin.setBottom(5f);

        // Définir le remplissage de cellule par défaut sur l'objet MarginInfo
        tab1.setDefaultCellPadding(margin);

        // Créer des lignes dans le tableau puis des cellules dans les lignes
        Row row1 = tab1.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add("col3");
        Row row2 = tab1.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");

        // Enregistrer le document mis à jour contenant l'objet table
        doc.save(_dataDir + "AutoFitToWindow_out.pdf");
    }
```


### Obtenir la largeur de la table

Parfois, il est nécessaire d'obtenir la largeur de la table de manière dynamique. La classe Aspose.PDF.Table dispose d'une méthode [GetWidth](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table#getWidth--) à cet effet. Par exemple, vous n'avez pas défini explicitement la largeur des colonnes de la table et avez défini [ColumnAdjustment](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColumnAdjustment) sur AutoFitToContent. Dans ce cas, vous pouvez obtenir la largeur de la table comme suit.

```java
public static void GetTableWidth() {
        // Créer un nouveau document
        Document doc = new Document();
        // Ajouter une page dans le document
        Page page = doc.getPages().add();

        // Initialiser une nouvelle table
        Table table = new Table();

        // Ajouter la table dans la collection de paragraphes de la section souhaitée
        page.getParagraphs().add(table);
        table.setColumnAdjustment(ColumnAdjustment.AutoFitToContent);

        // Ajouter une ligne dans la table
        Row row = table.getRows().add();
        // Ajouter une cellule dans la table
        row.getCells().add("Texte de la cellule 1");
        row.getCells().add("Texte de la cellule 2");
        // Obtenir la largeur de la table
        System.out.println(table.getWidth());
    }
```


## Ajouter un objet SVG à une cellule de tableau

Aspose.PDF pour Java prend en charge la fonctionnalité d'ajout d'une cellule de tableau dans un fichier PDF. Lors de la création d'un tableau, il est possible d'ajouter du texte ou des images dans les cellules. De plus, l'API offre également la fonctionnalité de conversion des fichiers SVG au format PDF. En utilisant une combinaison de ces fonctionnalités, il est possible de charger une image SVG et de l'ajouter dans une cellule de tableau.

Le code suivant montre les étapes pour créer une instance de tableau et ajouter une image SVG à l'intérieur d'une cellule de tableau.

```java
 public static void AddSVGObjectToTableCell() {
        // Instancier l'objet Document
        Document doc = new Document();
        // Créer une instance d'image
        com.aspose.pdf.Image img = new com.aspose.pdf.Image();
        // Définir le type d'image comme SVG
        img.setFileType (com.aspose.pdf.ImageFileType.Svg);
        // Chemin pour le fichier source
        img.setFile (_dataDir + "SVGToPDF.svg");
        // Définir la largeur de l'instance d'image
        img.setFixWidth (50);
        // Définir la hauteur de l'instance d'image
        img.setFixHeight (50);
        // Créer une instance de tableau
        com.aspose.pdf.Table table = new com.aspose.pdf.Table();
        // Définir la largeur des cellules du tableau
        table.setColumnWidths ("100 100");
        // Créer un objet de ligne et l'ajouter à l'instance de tableau
        com.aspose.pdf.Row row = table.getRows().add();
        // Créer un objet de cellule et l'ajouter à l'instance de ligne
        com.aspose.pdf.Cell cell = row.getCells().add();
        // Ajouter un fragment de texte à la collection de paragraphes de l'objet cellule
        cell.getParagraphs().add(new TextFragment("First cell"));
        // Ajouter une autre cellule à l'objet ligne
        cell = row.getCells().add();
        // Ajouter une image SVG à la collection de paragraphes de l'instance de cellule récemment ajoutée
        cell.getParagraphs().add(img);
        // Créer un objet page et l'ajouter à la collection de pages de l'instance de document
        Page page = doc.getPages().add();
        // Ajouter le tableau à la collection de paragraphes de l'objet page
        page.getParagraphs().add(table);
        // Enregistrer le fichier PDF
        doc.save(_dataDir + "AddSVGObject_out.pdf");
    }
```


## Ajouter des Balises HTML dans un Tableau

Aspose.PDF pour Java permet d'ajouter un nouveau fragment HTML dans un paragraphe de votre fichier PDF.

{{% alert color="primary" %}}

Veuillez noter que l'utilisation de balises HTML à l'intérieur d'un élément de tableau augmente le temps de génération du document, car l'API doit traiter les balises HTML en conséquence et les rendre dans le document PDF de sortie.

{{% /alert %}}

```java
  public static void AddHTMLFragmentToTableCell() {
        Document doc = new Document(_dataDir + "input.pdf");
        // Initialise une nouvelle instance de Table
        Table table = new Table();
        // Définir la couleur de la bordure de la table en gris clair
        table.setBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // définir la bordure pour les cellules du tableau
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // créer une boucle pour ajouter 10 lignes
        for (int row_count = 1; row_count < 10; row_count++) {
            Cell cell;
            // ajouter une ligne au tableau
            Row row = table.getRows().add();
            // ajouter des cellules au tableau
            cell = row.getCells().add();
            cell.getParagraphs().add(new HtmlFragment("Colonne <strong>(" + row_count + ", 1)</strong>"));

            cell = row.getCells().add();
            cell.getParagraphs().add(new HtmlFragment("Colonne <span style='color:red'>(" + row_count + ", 2)</span>"));

            cell = row.getCells().add();
            cell.getParagraphs().add(new HtmlFragment("Colonne <span style='text-decoration: underline'>(" + row_count + ", 3)</span>"));
        }
        // Ajouter l'objet tableau à la première page du document d'entrée
        doc.getPages().get_Item(1).getParagraphs().add(table);
        // Enregistrer le document mis à jour contenant l'objet tableau
        doc.save(_dataDir + "AddHTMLObject_out.pdf");
    }

}
```


## Insérer un saut de page entre les lignes du tableau

Par défaut, lors de la création d'un tableau dans un fichier PDF, le tableau s'étend sur les pages suivantes lorsqu'il atteint la marge inférieure du tableau. Cependant, nous pouvons avoir besoin d'insérer un saut de page de force lorsqu'un certain nombre de lignes sont ajoutées au tableau. Le code suivant montre les étapes pour insérer un saut de page lorsque 10 lignes sont ajoutées au tableau.

```java
    public static void InsertPageBreak() {
        // Instancier l'instance Document
        Document doc = new Document();
        // Ajouter une page à la collection de pages du fichier PDF
        Page page = doc.getPages().add();
        // Créer une instance de table
        Table tab = new Table();
        // Définir le style de bordure pour le tableau
        tab.setBorder (new BorderInfo(BorderSide.All, Color.getRed()));
        // Définir le style de bordure par défaut pour le tableau avec la couleur de la bordure en rouge
        tab.setDefaultCellBorder (new BorderInfo(BorderSide.All, Color.getRed()));
        // Spécifier la largeur des colonnes du tableau
        tab.setColumnWidths ("100 100");
        // Créer une boucle pour ajouter 200 lignes au tableau
        for (int counter = 0; counter <= 200; counter++) {
            Row row = new Row();
            tab.getRows().add(row);
            Cell cell1 = new Cell();
            cell1.getParagraphs().add(new TextFragment("Cellule " + counter + ", 0"));
            row.getCells().add(cell1);
            Cell cell2 = new Cell();
            cell2.getParagraphs().add(new TextFragment("Cellule " + counter + ", 1"));
            row.getCells().add(cell2);
            // Lorsque 10 lignes sont ajoutées, rendre la nouvelle ligne sur une nouvelle page
            if (counter % 10 == 0 && counter != 0)
                row.setInNewPage(true);
        }
        // Ajouter le tableau à la collection de paragraphes du fichier PDF
        page.getParagraphs().add(tab);

        // Enregistrer le document PDF
        doc.save(_dataDir + "InsertPageBreak_out.pdf");
    }
```


## Masquer les Bordures de Cellules Fusionnées

Lors de l'ajout de cellules à un tableau, les bordures de cellules fusionnées peuvent apparaître lorsqu'elles se cassent sur une autre ligne. Ces bordures fusionnées peuvent être masquées comme indiqué dans l'exemple de code suivant.

```java
Document doc = new Document();
com.aspose.pdf.Page page = doc.getPages().add();

//Instancier un objet table qui sera imbriqué à l'intérieur d'outerTable qui se cassera
//à l'intérieur de la même page
com.aspose.pdf.Table mytable = new com.aspose.pdf.Table();
mytable.setBroken(TableBroken.Vertical);
mytable.setDefaultCellBorder(new BorderInfo(BorderSide.All));
mytable.setRepeatingColumnsCount(2);
page.getParagraphs().add(mytable);

//Ajouter une ligne d'en-tête
com.aspose.pdf.Row row = mytable.getRows().add();
Cell cell = row.getCells().add("en-tête 1");
cell.setColSpan(2);
cell.setBackgroundColor(Color.getLightGray());
Cell header3 = row.getCells().add("en-tête 3");
Cell cell2 = row.getCells().add("en-tête 4");
cell2.setColSpan(2);
cell2.setBackgroundColor(Color.getLightBlue());
row.getCells().add("en-tête 6");
Cell cell3 = row.getCells().add("en-tête 7");
cell3.setColSpan(2);
cell3.setBackgroundColor(Color.getLightGreen());
Cell cell4 = row.getCells().add("en-tête 9");
cell4.setColSpan(3);
cell4.setBackgroundColor(Color.getLightCoral());
row.getCells().add("en-tête 12");
row.getCells().add("en-tête 13");
row.getCells().add("en-tête 14");
row.getCells().add("en-tête 15");
row.getCells().add("en-tête 16");
row.getCells().add("en-tête 17");

for (int rowCounter = 0; rowCounter < 1; rowCounter++)
{
  //Créer des lignes dans le tableau puis des cellules dans les lignes
  com.aspose.pdf.Row row1 = mytable.getRows().add();
  row1.getCells().add("col "+rowCounter+", 1");
  row1.getCells().add("col "+rowCounter+", 2");
  row1.getCells().add("col "+rowCounter+", 3");
  row1.getCells().add("col "+rowCounter+", 4");
  row1.getCells().add("col "+rowCounter+", 5");
  row1.getCells().add("col "+rowCounter+", 6");
  row1.getCells().add("col "+rowCounter+", 7");
  row1.getCells().add("col "+rowCounter+", 8");
  row1.getCells().add("col "+rowCounter+", 9");
  row1.getCells().add("col "+rowCounter+", 10");
  row1.getCells().add("col "+rowCounter+", 11");
  row1.getCells().add("col "+rowCounter+", 12");
  row1.getCells().add("col "+rowCounter+", 13");
  row1.getCells().add("col "+rowCounter+", 14");
  row1.getCells().add("col "+rowCounter+", 15");
  row1.getCells().add("col "+rowCounter+", 16");
  row1.getCells().add("col "+rowCounter+", 17");
}
doc.save(dataDir + "3_out.pdf");
```