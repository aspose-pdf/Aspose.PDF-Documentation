---
title: Agregar tablas a PDF en Java
linktitle: Agregar tablas
type: docs
weight: 10
url: /es/java/adding-tables/
description: Aprenda cómo agregar y configurar tablas en documentos PDF existentes en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregue y formatee tablas en documentos PDF con Java
Abstract: Este artículo explica cómo agregar y configurar tablas en documentos PDF utilizando Aspose.PDF for Java. Cubre la creación de tablas, bordes, márgenes, relleno, fusiones de filas y columnas, comportamiento AutoFit, inserción de imágenes en celdas, filas y columnas repetidas, fragmentos HTML y LaTeX, y control de renderizado de varias páginas.
---
Aspose.PDF for Java proporciona un rico `Table` API para crear tablas con personalización de diseño y contenido.

## Crear una tabla básica

Utilice este ejemplo cuando necesite agregar una tabla simple con bordes uniformes y celdas de texto.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega una página.
1. Crear un [Tabla](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) y configure sus bordes.
1. Agregar filas y celdas, adjuntar la tabla a la página y guardar el documento.

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

## Agregar celdas con fila de extensión y columna de extensión

Utilice este ejemplo cuando la tabla necesite celdas combinadas a través de filas o columnas.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega una página.
1. Crear un [Tabla](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) y agregar filas.
1. Configurar `ColSpan` y `RowSpan` en las celdas de destino, luego guarde el PDF.

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

## Agregar bordes de tabla y relleno de celdas

Utilice este ejemplo cuando necesite configurar los bordes, el relleno y el comportamiento de ajuste de celdas.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega una página.
1. Crear un [Tabla](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) y configure anchos, bordes y relleno.
1. Agregar filas y guardar el documento resultante.

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

## Habilitar ajuste automático del diseño de tabla

Utilice este ejemplo cuando la tabla debe ajustarse automáticamente al ancho disponible de la página.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega una página.
1. Crear un [Tabla](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) y establecer `ColumnAdjustment.AutoFitToWindow`.
1. Agregar filas de muestra y guardar el PDF.

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

## Agregar una imagen dentro de una celda de tabla

Utilice este ejemplo cuando la tabla necesite mostrar contenido de imagen raster dentro de una de sus celdas.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega una página.
1. Crear un [Tabla](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) y añade una fila con celdas de texto e imagen.
1. Configura el [Imagen](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) tamaño y guardar el documento.

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

## Agregar imágenes SVG dentro de celdas de tabla

Utilice este ejemplo cuando la tabla debe renderizar archivos SVG fila por fila.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega una página.
1. Crear un [Tabla](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) y iterar a través de los archivos SVG.
1. Agregar una fila por imagen, configurar el SVG [Imagen](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/), y guarde el PDF.

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

## Agregar fragmentos HTML a las celdas de la tabla

Utilice este ejemplo cuando el contenido de la tabla deba incluir formato HTML en línea.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega una página.
1. Crear un [Tabla](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) y configurar bordes.
1. Agregar [HtmlFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlfragment/) objetos a las celdas y guardar el documento.

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

## Agregar fragmentos LaTeX a celdas de tabla

Utiliza este ejemplo cuando el contenido de la tabla deba renderizar expresiones TeX o LaTeX.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega una página.
1. Crear un [Tabla](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) con bordes.
1. Agregar [FragmentoTeX](https://reference.aspose.com/pdf/java/com.aspose.pdf/texfragment/) objetos a las celdas y guarda el archivo de salida.

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

## Forzar una tabla a una nueva página

Utilice este ejemplo cuando una segunda tabla deba comenzar en una página separada después de una tabla grande.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y configure la configuración de página.
1. Construye el primer grande [Tabla](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) y añádelo a la página.
1. Crear una segunda tabla, establecer `InNewPage`, y guarde el documento.

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

## Construye una tabla rota verticalmente con columnas repetidas

Utilice este ejemplo cuando una tabla ancha debe continuar verticalmente y repetir columnas clave.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega una página.
1. Crear un [Tabla](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) y configure la ruptura vertical con columnas repetidas.
1. Añade el encabezado y las filas de datos, luego guarda el documento.

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

## Reutilizar el ejemplo de bordes y relleno

Utilice este ayudante cuando el escenario de márgenes y relleno deba delegar al ejemplo de borde compartido.

1. Llama al método existente de borde y relleno de la tabla.
1. Reutiliza la misma lógica de diseño de tabla sin duplicar el código.

```java
public static void addMarginsOrPadding(Path outputFile) {
    addBorders(outputFile);
}
```

## Crear una tabla con esquinas redondeadas

Utilice este ejemplo cuando la tabla deba usar un estilo de esquinas redondeadas en lugar de bordes rectangulares estándar.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega una página.
1. Crear un [Tabla](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) y configure los ajustes de borde redondeado.
1. Añade filas a la tabla y guarda el PDF.

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

## Agregar filas de encabezado repetidas

Utilice este ejemplo cuando las tablas de varias páginas deban repetir sus filas de encabezado en cada página de continuación.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega una página.
1. Crear un verticalmente roto [Tabla](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) y configure el recuento de filas repetidas y el estilo.
1. Agregar filas de encabezado y filas de datos, luego guardar el documento.

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

## Agregar columnas repetidas en una tabla ancha

Utilice este ejemplo cuando las primeras columnas deban repetirse mientras la tabla se divide verticalmente en la misma página.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y configure el tamaño de página.
1. Crear un [Tabla](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) y establecer columnas repetidas más comportamiento de ajuste automático.
1. Agregar encabezado y filas de datos, luego guardar el PDF.

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

## Insertar saltos de página entre filas de tabla

Utilice este ejemplo cuando filas de tabla específicas deben comenzar en una nueva página.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega una página.
1. Crear un [Tabla](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) y poblar muchas filas.
1. Marcar filas seleccionadas con `InNewPage` y guarda el documento.

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

## Rotar texto dentro de celdas de tabla

Utilice este ejemplo cuando el texto de la celda deba mostrarse en diferentes ángulos de rotación.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega una página.
1. Crear un [Tabla](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) y añada una fila con múltiples celdas.
1. Crear rotado [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) objetos, agréguelos a las celdas y guarde el PDF.

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
