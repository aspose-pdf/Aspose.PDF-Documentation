---
title: Travailler avec des tableaux dans les PDF balisés
linktitle: Travailler avec des tableaux dans les PDF balisés
type: docs
weight: 40
url: /java/working-with-table-in-tagged-pdfs/
description: Cet article explique comment travailler avec des tableaux dans un document PDF balisé avec Aspose.PDF pour Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Cette fonctionnalité est supportée par la version 19.6 ou supérieure.

{{% /alert %}}

## Créer un tableau dans un PDF balisé

Aspose.PDF pour Java permet de créer un tableau dans des documents PDF balisés.
 For working with tables, the API provides [TableElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement) class.

Pour travailler avec des tableaux, l'API fournit la classe [TableElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement). In order to create a table, you can use [createTableElement()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#createTableElement--) method of [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) interface. 

Afin de créer un tableau, vous pouvez utiliser la méthode [createTableElement()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#createTableElement--) de l'interface [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). De plus, vous pouvez utiliser les méthodes [createTHead()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement#createTHead--), [createTBody()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement#createTBody--) et [createTFoot()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement#createTFoot--) de la classe TableElement pour créer respectivement l'en-tête de table, le corps de table et le pied de table. Pour créer une ligne de table, vous pouvez utiliser la méthode [createTR()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableRowCollectionElement#createTR--) de la classe [TableRowCollectionElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableRowCollectionElement). Le code suivant montre comment créer une table dans le document PDF balisé :

```java
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Le chemin vers le répertoire des documents.
String path = Utils.getDataDir() + "TaggedPDFs\\";

// Créer un document
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Exemple de tableau");
taggedContent.setLanguage("en-US");

// Obtenir l'élément de structure racine
StructureElement rootElement = taggedContent.getRootElement();


TableElement tableElement = taggedContent.createTableElement();
rootElement.appendChild(tableElement);

tableElement.setBorder(new BorderInfo(BorderSide.All, 1.2F, Color.getDarkBlue()));

TableTHeadElement tableTHeadElement = tableElement.createTHead();
TableTBodyElement tableTBodyElement = tableElement.createTBody();
TableTFootElement tableTFootElement = tableElement.createTFoot();
int rowCount = 50;
int colCount = 4;
int rowIndex;
int colIndex;

TableTRElement headTrElement = tableTHeadElement.createTR();
headTrElement.setAlternativeText("Ligne d'en-tête");

headTrElement.setBackgroundColor(Color.getLightGray());

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.createTH();
    thElement.setText(String.format("En-tête %s", colIndex));

    thElement.setBackgroundColor(Color.getGreenYellow());
    thElement.setBorder(new BorderInfo(BorderSide.All, 4.0F, Color.getLightGray()));

    thElement.setMargin(new MarginInfo(16.0, 2.0, 8.0, 2.0));

    thElement.setAlignment(HorizontalAlignment.Right);
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.createTR();
    trElement.setAlternativeText(String.format("Ligne %s", rowIndex));

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        int colSpan = 1;
        int rowSpan = 1;

        if (colIndex == 1 && rowIndex == 1)
        {
            colSpan = 2;
            rowSpan = 2;
        }
        else if (colIndex == 2 && (rowIndex == 1 || rowIndex == 2))
        {
            continue;
        }
        else if (rowIndex == 2 && (colIndex == 1 || colIndex == 2))
        {
            continue;
        }

        TableTDElement tdElement = trElement.createTD();
        tdElement.setText(String.format("Cellule [%s, %s]", rowIndex, colIndex));


        tdElement.setBackgroundColor(Color.getYellow());
        tdElement.setBorder(new BorderInfo(BorderSide.All, 4.0F, Color.getGray()));


        tdElement.setMargin(new MarginInfo(8.0, 2.0, 8.0, 2.0));

        tdElement.setAlignment(HorizontalAlignment.Center);

        TextState cellTextState = new TextState();
        cellTextState.setForegroundColor(Color.getDarkBlue());
        cellTextState.setFontSize(7.5F);
        cellTextState.setFontStyle(FontStyles.Bold);
        cellTextState.setFont(FontRepository.findFont("Arial"));
        tdElement.setDefaultCellTextState(cellTextState);

        tdElement.isWordWrapped();
        tdElement.setVerticalAlignment(VerticalAlignment.Center);

        tdElement.setColSpan(colSpan);
        tdElement.setRowSpan(rowSpan);
    }
}

TableTRElement footTrElement = tableTFootElement.createTR();
footTrElement.setAlternativeText("Ligne de pied");

footTrElement.setBackgroundColor(Color.getLightSeaGreen());

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.createTD();
    tdElement.setText(String.format("Pied %s", colIndex));

    tdElement.setAlignment(HorizontalAlignment.Center);
    tdElement.getStructureTextState().setFontSize(7F);
    tdElement.getStructureTextState().setFontStyle(FontStyles.Bold);
}


StructureAttributes tableAttributes = tableElement.getAttributes().getAttributes(AttributeOwnerStandard.Table);
StructureAttribute summaryAttribute = new StructureAttribute(AttributeKey.Summary);
summaryAttribute.setStringValue("Le texte de résumé pour la table");
tableAttributes.setAttribute(summaryAttribute);


// Enregistrer le document PDF balisé
document.save(path + "CreateTableElement.pdf");
```

## Élément de Style de Table

Aspose.PDF pour Java permet de styliser une table dans un document PDF tagué. Afin de styliser une table, vous pouvez créer une table en utilisant la méthode [createTableElement()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#createTableElement--) de l'interface [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) et définir le style de la table en utilisant les propriétés de la classe [TableElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement). Voici la liste des propriétés que vous pouvez utiliser pour styliser une table :

- BackgroundColor
- Border
- Alignment
- CornerStyle
- Broken
- ColumnAdjustment
- ColumnWidths
- DefaultCellBorder
- DefaultCellPadding
- DefaultCellTextState
- DefaultColumnWidth
- IsBroken
- IsBordersIncluded
- Left
- Top

Le code suivant montre comment styliser une table dans un document PDF tagué :

```java
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Le chemin vers le répertoire des documents.
String path = Utils.getDataDir() + "TaggedPDFs\\";

// Créer un document
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Exemple de style de table");
taggedContent.setLanguage("en-US");

// Obtenir l'élément de structure racine
StructureElement rootElement = taggedContent.getRootElement();


// Créer un élément de structure de table
TableElement tableElement = taggedContent.createTableElement();
rootElement.appendChild(tableElement);


tableElement.setBackgroundColor(Color.getBeige());
tableElement.setBorder(new BorderInfo(BorderSide.All, 0.80F, Color.getGray()));
tableElement.setAlignment(HorizontalAlignment.Center);
tableElement.setBroken(TableBroken.Vertical);
tableElement.setColumnAdjustment(ColumnAdjustment.AutoFitToWindow);
tableElement.setColumnWidths("80 80 80 80 80");
tableElement.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.50F, Color.getDarkBlue()));
tableElement.setDefaultCellPadding(new MarginInfo(16.0, 2.0, 8.0, 2.0));
tableElement.getDefaultCellTextState().setForegroundColor(Color.getDarkCyan());
tableElement.getDefaultCellTextState().setFontSize(8F);
tableElement.setDefaultColumnWidth("70");

tableElement.setBroken(false);
tableElement.setBordersIncluded(true);

tableElement.setLeft(0F);
tableElement.setTop(40F);

tableElement.setRepeatingColumnsCount(2);
tableElement.setRepeatingRowsCount(3);
TextState rowStyle = new TextState();
rowStyle.setBackgroundColor(Color.getLightCoral());
tableElement.setRepeatingRowsStyle(rowStyle);




TableTHeadElement tableTHeadElement = tableElement.createTHead();
TableTBodyElement tableTBodyElement = tableElement.createTBody();
TableTFootElement tableTFootElement = tableElement.createTFoot();
int rowCount = 10;
int colCount = 5;
int rowIndex;
int colIndex;

TableTRElement headTrElement = tableTHeadElement.createTR();
headTrElement.setAlternativeText("Ligne de Tête");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.createTH();
    thElement.setText(String.format("Tête %s", colIndex));
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.createTR();
    trElement.setAlternativeText(String.format("Ligne %s", rowIndex));

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        TableTDElement tdElement = trElement.createTD();
        tdElement.setText(String.format("Cellule [%s, %s]", rowIndex, colIndex));
    }
}

TableTRElement footTrElement = tableTFootElement.createTR();
footTrElement.setAlternativeText("Ligne de Pied");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.createTD();
    tdElement.setText(String.format("Pied %s", colIndex));
}

// Sauvegarder le document PDF tagué
document.save(path + "StyleTableElement.pdf");
```


## Style Table Row

Aspose.PDF pour Java permet de styliser une ligne de tableau dans un document PDF étiqueté. Afin de styliser une ligne de tableau, vous pouvez utiliser les propriétés de la classe [TableTRElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableTRElement). Voici la liste des propriétés que vous pouvez utiliser pour styliser une ligne de tableau :

- BackgroundColor
- Border
- DefaultCellBorder
- MinRowHeight
- FixedRowHeight
- IsInNewPage
- IsRowBroken
- DefaultCellTextState
- DefaultCellPadding
- VerticalAlignment

Le code suivant montre comment styliser une ligne de tableau dans un document PDF étiqueté :

```java
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Le chemin vers le répertoire des documents.
String path = Utils.getDataDir() + "TaggedPDFs\\";

// Créer un document
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Exemple de style de ligne de tableau");
taggedContent.setLanguage("en-US");

// Obtenez l'élément de structure racine
StructureElement rootElement = taggedContent.getRootElement();


// Créer un élément de structure de tableau
TableElement tableElement = taggedContent.createTableElement();
rootElement.appendChild(tableElement);


TableTHeadElement tableTHeadElement = tableElement.createTHead();
TableTBodyElement tableTBodyElement = tableElement.createTBody();
TableTFootElement tableTFootElement = tableElement.createTFoot();
int rowCount = 7;
int colCount = 3;
int rowIndex;
int colIndex;

TableTRElement headTrElement = tableTHeadElement.createTR();
headTrElement.setAlternativeText("Ligne d'en-tête");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.createTH();
    thElement.setText(String.format("En-tête %s", colIndex));
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.createTR();
    trElement.setAlternativeText(String.format("Ligne %s", rowIndex));

    trElement.setBackgroundColor(Color.getLightSeaGreen());
    trElement.setBorder(new BorderInfo(BorderSide.All, 0.75F, Color.getDarkGray()));

    trElement.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.50F, Color.getBlue()));
    trElement.setMinRowHeight(100.0);
    trElement.setFixedRowHeight(120.0);
    trElement.setRowBroken(true);

    TextState cellTextState = new TextState();
    cellTextState.setForegroundColor(Color.getRed());
    trElement.setDefaultCellTextState(cellTextState);

    trElement.setDefaultCellPadding(new MarginInfo(16.0, 2.0, 8.0, 2.0));
    trElement.setVerticalAlignment(VerticalAlignment.Bottom);

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        TableTDElement tdElement = trElement.createTD();
        tdElement.setText(String.format("Cellule [{0}, {1}]", rowIndex, colIndex));
    }
}

TableTRElement footTrElement = tableTFootElement.createTR();
footTrElement.setAlternativeText("Ligne de pied");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.createTD();
    tdElement.setText(String.format("Pied %s", colIndex));
}



// Enregistrer le document PDF étiqueté
document.save(path + "StyleTableRow.pdf");
```


## Style Table Cell

Aspose.PDF pour Java permet de styliser une cellule de tableau dans un document PDF balisé. Afin de styliser une cellule de tableau, vous pouvez utiliser les propriétés de la classe [TableCellElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableCellElement). Voici la liste des propriétés que vous pouvez utiliser pour styliser une cellule de tableau :

- BackgroundColor
- Border
- IsNoBorder
- Margin
- Alignment
- DefaultCellTextState
- IsWordWrapped
- VerticalAlignment
- ColSpan
- RowSpan

Le code suivant montre comment styliser une cellule de tableau dans le document PDF balisé. Vous pouvez également vérifier la conformité **PDF/UA** du document créé. Le code ci-dessous montre comment utiliser cette fonctionnalité.

```java
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Le chemin vers le répertoire des documents.
String path = Utils.getDataDir() + "TaggedPDFs\\";

// Créer un document
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Exemple de style de cellule de tableau");
taggedContent.setLanguage("en-US");

// Obtenir l'élément de structure racine
StructureElement rootElement = taggedContent.getRootElement();


// Créer un élément de structure de tableau
TableElement tableElement = taggedContent.createTableElement();
rootElement.appendChild(tableElement);


TableTHeadElement tableTHeadElement = tableElement.createTHead();
TableTBodyElement tableTBodyElement = tableElement.createTBody();
TableTFootElement tableTFootElement = tableElement.createTFoot();
int rowCount = 4;
int colCount = 4;
int rowIndex;
int colIndex;

TableTRElement headTrElement = tableTHeadElement.createTR();
headTrElement.setAlternativeText("Ligne d'en-tête");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.createTH();
    thElement.setText(String.format("En-tête %s", colIndex));

    thElement.setBackgroundColor(Color.getGreenYellow());
    thElement.setBorder(new BorderInfo(BorderSide.All, 4.0F, Color.getGray()));

    thElement.setNoBorder(false);
    thElement.setMargin(new MarginInfo(16.0, 2.0, 8.0, 2.0));

    thElement.setAlignment(HorizontalAlignment.Right);
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.createTR();
    trElement.setAlternativeText(String.format("Ligne %s", rowIndex));

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        int colSpan = 1;
        int rowSpan = 1;

        if (colIndex == 1 && rowIndex == 1)
        {
            colSpan = 2;
            rowSpan = 2;
        }
        else if (colIndex == 2 && (rowIndex == 1 || rowIndex == 2))
        {
            continue;
        }
        else if (rowIndex == 2 && (colIndex == 1 || colIndex == 2))
        {
            continue;
        }

        TableTDElement tdElement = trElement.createTD();
        tdElement.setText(String.format("Cellule [%s, %s]", rowIndex, colIndex));


        tdElement.setBackgroundColor(Color.getYellow());
        tdElement.setBorder(new BorderInfo(BorderSide.All, 4.0F, Color.getGray()));

        tdElement.setNoBorder(false);
        tdElement.setMargin(new MarginInfo(8.0, 2.0, 8.0, 2.0));

        tdElement.setAlignment(HorizontalAlignment.Center);

        TextState cellTextState = new TextState();
        cellTextState.setForegroundColor(Color.getDarkBlue());
        cellTextState.setFontSize(7.5F);
        cellTextState.setFontStyle(FontStyles.Bold);
        cellTextState.setFont(FontRepository.findFont("Arial"));
        tdElement.setDefaultCellTextState(cellTextState);

        tdElement.setWordWrapped(false);
        tdElement.setVerticalAlignment(VerticalAlignment.Center);

        tdElement.setColSpan(colSpan);
        tdElement.setRowSpan(rowSpan);
    }
}

TableTRElement footTrElement = tableTFootElement.createTR();
footTrElement.setAlternativeText("Ligne de pied");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.createTD();
    tdElement.setText(String.format("Pied %s", colIndex));
}


// Enregistrer le document PDF balisé
document.save(path + "StyleTableCell.pdf");
```