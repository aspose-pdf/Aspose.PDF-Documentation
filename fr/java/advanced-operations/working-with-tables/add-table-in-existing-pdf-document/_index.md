---
title: Ajouter des tableaux au PDF en Java
linktitle: Ajout de tableaux
type: docs
weight: 10
url: /java/adding-tables/
description: Découvrez comment ajouter et configurer des tableaux dans des documents PDF existants en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter et formater des tableaux dans des documents PDF avec Java
Abstract: Cet article explique comment ajouter et configurer des tableaux dans des documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre la création de tableaux, les bordures, les marges, le remplissage, les étendues de lignes et de colonnes, le comportement d'ajustement automatique, l'insertion d'images dans les cellules, la répétition de lignes et de colonnes, les fragments HTML et LaTeX et le contrôle du rendu sur plusieurs pages.
---
Aspose.PDF pour Java fournit une riche API `Table` pour créer des tableaux avec une mise en page et une personnalisation du contenu.


## 
Créer un tableau de base



Utilisez cet exemple lorsque vous devez ajouter un tableau simple avec des bordures et des cellules de texte uniformes.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page.

1. 
Créez une [Table] (https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) et configurez ses bordures.
1. Ajoutez des lignes et des cellules, attachez le tableau à la page et enregistrez le document.


```java
public static void createTable(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 5, Color.getLightGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 5, Color.getLightGray()));
        for (int rowCount = 0; rowCount < 10; rowCount++) {
            Row row = table.getRows().add();
            row.getCells().add("Column (" + rowCount + ", 1)");
            row.getCells().add("Column (" + rowCount + ", 2)");
            row.getCells().add("Column (" + rowCount + ", 3)");
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter des cellules avec une étendue de lignes et une étendue de colonnes



Utilisez cet exemple lorsque le tableau nécessite des cellules fusionnées sur des lignes ou des colonnes.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page.

1. 
Créez un [Table] (https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) et ajoutez des lignes.
1. Configurez `ColSpan` et `RowSpan` sur les cellules cibles, puis enregistrez le PDF.


```java
public static void addRowspanOrColspan(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getBlack()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getBlack()));

        Row row1 = table.getRows().add();
        for (int cellCount = 1; cellCount < 5; cellCount++) {
            row1.getCells().add("Test 1" + cellCount);
        }

        Row row2 = table.getRows().add();
        row2.getCells().add("Test 2 1");
        Cell cell = row2.getCells().add("Test 2 2");
        cell.setColSpan(2);
        row2.getCells().add("Test 2 4");

        Row row3 = table.getRows().add();
        row3.getCells().add("Test 3 1");
        row3.getCells().add("Test 3 2");
        row3.getCells().add("Test 3 3");
        row3.getCells().add("Test 3 4");

        Row row4 = table.getRows().add();
        row4.getCells().add("Test 4 1");
        cell = row4.getCells().add("Test 4 2");
        cell.setRowSpan(2);
        row4.getCells().add("Test 4 3");
        row4.getCells().add("Test 4 4");

        Row row5 = table.getRows().add();
        row5.getCells().add("Test 5 1");
        row5.getCells().add("Test 5 3");
        row5.getCells().add("Test 5 4");

        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter des bordures de tableau et un remplissage de cellules



Utilisez cet exemple lorsque vous devez configurer les bordures, le remplissage et le comportement de retour à la ligne des cellules.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page.

1. 
Créez un [Table] (https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) et configurez les largeurs, les bordures et le remplissage.
1. Ajoutez des lignes et enregistrez le document résultant.


```java
public static void addBorders(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        page.getParagraphs().add(table);
        table.setColumnWidths("50 50 50");
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1f));
        table.setBorder(new BorderInfo(BorderSide.All, 1));
        table.setDefaultCellPadding(new MarginInfo(5, 5, 5, 5));

        Row row1 = table.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add();
        row1.getCells().get_Item(2).getParagraphs().add(new TextFragment("col3 with large text string"));
        row1.getCells().get_Item(2).setWordWrapped(false);

        Row row2 = table.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");
        document.save(outputFile.toString());
    }
}
```

## 
Activer la disposition du tableau à ajustement automatique



Utilisez cet exemple lorsque le tableau doit s'ajuster automatiquement à la largeur de page disponible.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page.

1. 
Créez une [Table] (https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) et définissez `ColumnAdjustment.AutoFitToWindow`.
1. Ajoutez des exemples de lignes et enregistrez le PDF.


```java
public static void autoFit(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        page.getParagraphs().add(table);
        table.setColumnWidths("50 50 50");
        table.setColumnAdjustment(ColumnAdjustment.AutoFitToWindow);
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1f));
        table.setBorder(new BorderInfo(BorderSide.All, 1));
        table.setDefaultCellPadding(new MarginInfo(5, 5, 5, 5));

        Row row1 = table.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add("col3");
        Row row2 = table.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter une image dans une cellule du tableau



Utilisez cet exemple lorsque le tableau doit afficher le contenu d’une image raster dans l’une de ses cellules.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page.

1. 
Créez un [Table] (https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) et ajoutez une ligne avec des cellules de texte et d'image.
1. Configurez la taille de [Image] (https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) et enregistrez le document.


```java
public static void addImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setColumnWidths("200 100");

        Row row = table.getRows().add();
        row.getCells().add().getParagraphs().add(new TextFragment(imageFile.toString()));
        Image image = new Image();
        image.setFile(imageFile.toString());
        image.setFixWidth(50);
        image.setFixHeight(50);
        row.getCells().add().getParagraphs().add(image);

        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter des images SVG dans les cellules du tableau



Utilisez cet exemple lorsque la table doit restituer les fichiers SVG ligne par ligne.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page.

1. 
Créez une [Table] (https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) et parcourez les fichiers SVG.
1. Ajoutez une ligne par image, configurez le SVG [Image] (https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) et enregistrez le PDF.


```java
public static void addSvgImage(List<Path> imageFiles, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setColumnWidths("200 100");
        for (Path imageFile : imageFiles) {
            Row row = table.getRows().add();
            row.getCells().add().getParagraphs().add(new TextFragment(imageFile.toString()));
            Image image = new Image();
            image.setFileType(ImageFileType.Svg);
            image.setFile(imageFile.toString());
            image.setFixWidth(50);
            image.setFixHeight(50);
            row.getCells().add().getParagraphs().add(image);
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter des fragments HTML aux cellules du tableau



Utilisez cet exemple lorsque le contenu du tableau doit inclure un formatage HTML en ligne.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page.

1. 
Créez une [Table] (https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) et configurez les bordures.
1. Ajoutez des objets [HtmlFragment] (https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlfragment/) aux cellules et enregistrez le document.


```java
public static void addHtmlFragments(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getLightGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getLightGray()));
        for (int rowCount = 1; rowCount < 10; rowCount++) {
            Row row = table.getRows().add();
            row.getCells().add().getParagraphs().add(new HtmlFragment("Column <strong>(" + rowCount + ", 1)</strong>"));
            row.getCells().add().getParagraphs().add(new HtmlFragment("Column <span style='color:red'>(" + rowCount + ", 2)</span>"));
            row.getCells().add().getParagraphs().add(new HtmlFragment("Column <span style='text-decoration: underline'>(" + rowCount + ", 3)</span>"));
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter des fragments LaTeX aux cellules du tableau



Utilisez cet exemple lorsque le contenu d'un tableau doit restituer des expressions TeX ou LaTeX.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page.

1. 
Créez un [Table] (https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) avec des bordures.
1. Ajoutez des objets [TeXFragment] (https://reference.aspose.com/pdf/java/com.aspose.pdf/texfragment/) aux cellules et enregistrez le fichier de sortie.


```java
public static void addLatexFragments(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getLightGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getLightGray()));
        for (int rowCount = 1; rowCount < 10; rowCount++) {
            Row row = table.getRows().add();
            row.getCells().add().getParagraphs().add(new TeXFragment("Column $\\mathbf{(" + rowCount + ", 1)}$"));
            row.getCells().add().getParagraphs().add(new TeXFragment("Column $\\textcolor{red}{(" + rowCount + ", 2)}$"));
            row.getCells().add().getParagraphs().add(new TeXFragment("Column $\\underline{(" + rowCount + ", 3)}$"));
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## 
Forcer un tableau sur une nouvelle page



Utilisez cet exemple lorsqu'un deuxième tableau doit commencer sur une page distincte après un grand tableau.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et configurez les paramètres de la page.

1. 
Créez la première grande [Table] (https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) et ajoutez-la à la page.
1. Créez un deuxième tableau, définissez `InNewPage` et enregistrez le document.


```java
public static void addTableOnNewPage(Path outputFile) {
    try (Document document = new Document()) {
        document.getPageInfo().getMargin().setLeft(37);
        document.getPageInfo().getMargin().setRight(37);
        document.getPageInfo().getMargin().setTop(37);
        document.getPageInfo().getMargin().setBottom(37);
        document.getPageInfo().setLandscape(true);

        Page page = document.getPages().add();
        Table table = new Table();
        table.setColumnWidths("50 100");
        for (int i = 1; i < 121; i++) {
            Row row = table.getRows().add();
            row.setFixedRowHeight(15);
            row.getCells().add().getParagraphs().add(new TextFragment("Content 1"));
            row.getCells().add().getParagraphs().add(new TextFragment("Content 2"));
        }
        page.getParagraphs().add(table);

        Table table1 = new Table();
        table1.setColumnWidths("100 100");
        for (int i = 1; i < 11; i++) {
            Row row = table1.getRows().add();
            row.getCells().add().getParagraphs().add(new TextFragment("Content 3"));
            row.getCells().add().getParagraphs().add(new TextFragment("Content 4"));
        }
        table1.setInNewPage(true);
        page.getParagraphs().add(table1);
        document.save(outputFile.toString());
    }
}
```

## 
Construisez un tableau divisé verticalement avec des colonnes répétitives



Utilisez cet exemple lorsqu'un tableau large doit continuer verticalement et répéter les colonnes clés.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page.

1. 
Créez un [Table] (https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) et configurez la rupture verticale avec des colonnes répétitives.
1. Ajoutez l'en-tête et les lignes de données, puis enregistrez le document.


```java
public static void addTableHideBorders(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBroken(TableBroken.Vertical);
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All));
        table.setRepeatingColumnsCount(2);
        page.getParagraphs().add(table);

        Row row = table.getRows().add();
        Cell cell = row.getCells().add("header 1");
        cell.setColSpan(2);
        cell.setBackgroundColor(Color.getLightGray());
        row.getCells().add("header 3");
        Cell cell2 = row.getCells().add("header 4");
        cell2.setColSpan(2);
        cell2.setBackgroundColor(Color.getLightBlue());
        row.getCells().add("header 6");
        Cell cell3 = row.getCells().add("header 7");
        cell3.setColSpan(2);
        cell3.setBackgroundColor(Color.getLightGreen());
        Cell cell4 = row.getCells().add("header 9");
        cell4.setColSpan(3);
        cell4.setBackgroundColor(Color.getLightCoral());
        for (int i = 12; i < 18; i++) {
            row.getCells().add("header " + i);
        }

        for (int rowCounter = 0; rowCounter < 3; rowCounter++) {
            Row row1 = table.getRows().add();
            for (int i = 1; i < 18; i++) {
                row1.getCells().add("col " + rowCounter + ", " + i);
            }
        }
        document.save(outputFile.toString());
    }
}
```

## 
Réutiliser les bordures et l'exemple de remplissage



Utilisez cette assistante lorsque le scénario de marges et de remplissage doit déléguer à l'exemple de bordure partagée.


1. 
Appelez la méthode de bordure et de remplissage de table existante.

1. 
Réutilisez la même logique de disposition de table sans dupliquer le code.

```java
public static void addMarginsOrPadding(Path outputFile) {
    addBorders(outputFile);
}
```

## Créer une table aux coins arrondis



Utilisez cet exemple lorsque le tableau doit utiliser un style de coins arrondis au lieu de bordures rectangulaires standard.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page.

1. 
Créez un [Table] (https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) et configurez les paramètres de bordure arrondie.

1. 
Ajoutez des lignes au tableau et enregistrez le PDF.

```java
public static void createTableWithRoundCorner(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        BorderInfo borderInfo = new BorderInfo(BorderSide.All);
        borderInfo.setRoundedBorderRadius(15);
        table.setCornerStyle(BorderCornerStyle.Round);
        table.setBorder(borderInfo);
        for (int rowCount = 0; rowCount < 10; rowCount++) {
            Row row = table.getRows().add();
            row.getCells().add("Column (" + rowCount + ", 1)");
            row.getCells().add("Column (" + rowCount + ", 2)");
            row.getCells().add("Column (" + rowCount + ", 3)");
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## Ajouter des lignes d'en-tête répétitives



Utilisez cet exemple lorsque les tableaux de plusieurs pages doivent répéter leurs lignes d'en-tête sur chaque page de suite.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page.

1. 
Créez un [Table] divisé verticalement (https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) et configurez le nombre et le style de lignes répétitives.

1. 
Ajoutez des lignes d'en-tête et des lignes de données, puis enregistrez le document.

```java
public static void addRepeatingRows(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBroken(TableBroken.Vertical);
        table.setRepeatingRowsCount(2);
        TextState textState = new TextState();
        textState.setFontSize(12);
        textState.setFont(FontRepository.findFont("TimesNewRoman"));
        textState.setForegroundColor(Color.getRed());
        table.setRepeatingRowsStyle(textState);
        table.setColumnWidths("100 100 100");
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getBlack()));
        table.setBorder(new BorderInfo(BorderSide.All, 1, Color.getBlack()));

        Row headerRow1 = table.getRows().add();
        headerRow1.getCells().add("Header 1-1");
        headerRow1.getCells().add("Header 1-2");
        headerRow1.getCells().add("Header 1-3");
        for (Cell cell : headerRow1.getCells()) {
            cell.setBackgroundColor(Color.getLightGray());
        }
        Row headerRow2 = table.getRows().add();
        headerRow2.getCells().add("Header 2-1");
        headerRow2.getCells().add("Header 2-2");
        headerRow2.getCells().add("Header 2-3");
        for (Cell cell : headerRow2.getCells()) {
            cell.setBackgroundColor(Color.getLightBlue());
        }
        for (int i = 1; i < 101; i++) {
            Row row = table.getRows().add();
            row.getCells().add("Data " + i + "-1");
            row.getCells().add("Data " + i + "-2");
            row.getCells().add("Data " + i + "-3");
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## Ajouter des colonnes répétitives dans un large tableau



Utilisez cet exemple lorsque les premières colonnes doivent se répéter alors que le tableau se divise verticalement sur la même page.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et configurez la taille de la page.

1. 
Créez un [Table] (https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) et définissez des colonnes répétitives ainsi qu'un comportement d'ajustement automatique.

1. 
Ajoutez des lignes d'en-tête et de données, puis enregistrez le PDF.

```java
public static void addRepeatingColumns(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.setPageSize(PageSize.getA5().getHeight(), PageSize.getA5().getWidth());
        BorderInfo border = new BorderInfo(BorderSide.All, 0.5f, Color.getLightGray());
        Table table = new Table();
        table.setBroken(TableBroken.VerticalInSamePage);
        table.setColumnAdjustment(ColumnAdjustment.AutoFitToContent);
        table.setRepeatingColumnsCount(5);
        table.setBorder(border);
        table.setDefaultCellBorder(border);
        page.getParagraphs().add(table);

        Row row = table.getRows().add();
        for (int i = 1; i < 6; i++) {
            Cell cell = row.getCells().add("header " + i);
            cell.setBackgroundColor(Color.getLightGray());
        }
        for (int i = 6; i < 18; i++) {
            row.getCells().add("header " + i);
        }

        for (int rowCounter = 1; rowCounter < 6; rowCounter++) {
            row = table.getRows().add();
            for (int i = 1; i < 6; i++) {
                Cell cell = row.getCells().add("cell " + rowCounter + "," + i);
                cell.setBackgroundColor(Color.getLightGray());
            }
            for (int i = 6; i < 18; i++) {
                row.getCells().add("cell " + rowCounter + "," + i);
            }
        }
        document.save(outputFile.toString());
    }
}
```

## Insérer des sauts de page entre les lignes du tableau



Utilisez cet exemple lorsque des lignes de tableau spécifiques doivent commencer sur une nouvelle page.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page.

1. 
Créez une [Table] (https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) et remplissez plusieurs lignes.

1. 
Marquez les lignes sélectionnées avec `InNewPage` et enregistrez le document.

```java
public static void insertPageBreak(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, Color.getRed()));
        table.setColumnWidths("100 100");
        for (int counter = 0; counter < 201; counter++) {
            Row row = new Row();
            table.getRows().add(row);
            row.getCells().add().getParagraphs().add(new TextFragment("Cell " + counter + ", 0"));
            row.getCells().add().getParagraphs().add(new TextFragment("Cell " + counter + ", 1"));
            if (counter % 10 == 0 && counter != 0) {
                row.setInNewPage(true);
            }
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## Faire pivoter le texte à l'intérieur des cellules du tableau



Utilisez cet exemple lorsque le texte d’une cellule doit être affiché sous différents angles de rotation.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page.

1. 
Créez un [Table] (https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) et ajoutez une ligne avec plusieurs cellules.

1. 
Créez des objets [TextFragment] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) pivotés, ajoutez-les aux cellules et enregistrez le PDF.

```java
public static void rotatedTextTable(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getBlack()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getBlack()));
        Row row = table.getRows().add();
        row.setMinRowHeight(200);
        for (int cellCount = 0; cellCount < 4; cellCount++) {
            Cell cell = row.getCells().add();
            TextFragment textFragment = new TextFragment("Cell 1 " + (cellCount - 1));
            textFragment.getTextState().setRotation(90 * cellCount);
            textFragment.setHorizontalAlignment(HorizontalAlignment.Center);
            cell.getParagraphs().add(textFragment);
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```
