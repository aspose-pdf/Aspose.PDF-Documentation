---
title: Trabajar con tablas en archivos PDF etiquetados en Java
linktitle: Trabajar con tablas en archivos PDF etiquetados
type: docs
weight: 40
url: /java/working-with-table-in-tagged-pdfs/
description: Aprenda a trabajar con tablas accesibles en archivos PDF etiquetados en Java con Aspose.PDF, incluida la estructura de la tabla, la extensión de las celdas, el estilo, la configuración de las filas y el posicionamiento.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Las API de tablas etiquetadas le permiten crear estructuras de tablas accesibles con encabezados explícitos, filas de cuerpo, pies de página y semántica por celda.


## 
Crear una tabla etiquetada

Utilice este ejemplo cuando necesite una tabla básica accesible con metadatos de encabezado, cuerpo, pie de página y resumen de tabla.


1. 
Cree un nuevo [Documento] PDF etiquetado(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agregue un [Elemento de tabla](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/tableelement/).

1. 
Configure el borde de la tabla y complete el contenido con el método auxiliar compartido.

1. 
Establezca el atributo de resumen de la tabla y guarde el documento.


```java
public static void createTable(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Example table");
        taggedContent.setLanguage("en-US");

        TableElement tableElement = taggedContent.createTableElement();
        taggedContent.getRootElement().appendChild(tableElement, true);
        tableElement.setBorder(new BorderInfo(BorderSide.All, 1.2f, Color.getDarkBlue()));

        fillTable(tableElement, 50, 4, true);

        StructureAttributes tableAttributes = tableElement.getAttributes().getAttributes(AttributeOwnerStandard.Table);
        StructureAttribute summaryAttribute = new StructureAttribute(AttributeKey.Summary);
        summaryAttribute.setStringValue("The summary text for table");
        tableAttributes.setAttribute(summaryAttribute);

        document.save(outputFile.toString());
    }
}
```

## 
Aplicar estilo a una tabla etiquetada

Este ejemplo aplica formato a nivel de tabla, como colores, bordes, tamaño de columna, filas repetidas y alineación.


1. 
Cree un nuevo [Documento] PDF etiquetado(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agregue un elemento de tabla.

1. 
Configure los ajustes visuales y de diseño a nivel de tabla.

1. 
Complete la tabla y guarde el documento.


```java
public static void styleTable(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Example table style");
        taggedContent.setLanguage("en-US");

        TableElement tableElement = taggedContent.createTableElement();
        taggedContent.getRootElement().appendChild(tableElement, true);

        tableElement.setBackgroundColor(Color.getBeige());
        tableElement.setBorder(new BorderInfo(BorderSide.All, 0.80f, Color.getGray()));
        tableElement.setAlignment(HorizontalAlignment.Center);
        tableElement.setBroken(TableBroken.Vertical);
        tableElement.setColumnAdjustment(ColumnAdjustment.AutoFitToWindow);
        tableElement.setColumnWidths("80 80 80 80 80");
        tableElement.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.50f, Color.getDarkBlue()));
        tableElement.setDefaultCellPadding(new MarginInfo(16.0, 2.0, 8.0, 2.0));
        tableElement.getDefaultCellTextState().setForegroundColor(Color.getDarkCyan());
        tableElement.getDefaultCellTextState().setFontSize(8.0f);
        tableElement.setDefaultColumnWidth("70");
        tableElement.setBordersIncluded(true);
        tableElement.setLeft(0.0f);
        tableElement.setTop(40.0f);
        tableElement.setRepeatingColumnsCount(2);
        tableElement.setRepeatingRowsCount(3);

        TextState rowStyle = new TextState();
        rowStyle.setBackgroundColor(Color.getLightCoral());
        tableElement.setRepeatingRowsStyle(rowStyle);

        fillTable(tableElement, 10, 5, false);
        document.save(outputFile.toString());
    }
}
```

## 
Estilo de filas de tabla etiquetadas

Utilice este ejemplo cuando cada fila deba tener sus propios metadatos, bordes, configuraciones de altura y valores predeterminados de celda.


1. 
Cree un nuevo [Documento] PDF etiquetado(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agregue secciones de tabla para la cabeza, el cuerpo y los pies.

1. 
Cree filas y configure sus ajustes a nivel de fila, como borde, relleno, altura y comportamiento de la página.

1. 
Complete las filas con celdas y guarde el documento.


```java
public static void styleTableRow(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Example table style");
        taggedContent.setLanguage("en-US");

        TableElement tableElement = taggedContent.createTableElement();
        taggedContent.getRootElement().appendChild(tableElement, true);
        TableTHeadElement tableTHeadElement = tableElement.createTHead();
        TableTBodyElement tableTBodyElement = tableElement.createTBody();
        TableTFootElement tableTFootElement = tableElement.createTFoot();

        TableTRElement headTrElement = tableTHeadElement.createTR();
        headTrElement.setAlternativeText("Head Row");
        for (int colIndex = 0; colIndex < 3; colIndex++) {
            headTrElement.createTH().setText("Head " + colIndex);
        }

        for (int rowIndex = 0; rowIndex < 7; rowIndex++) {
            TableTRElement trElement = tableTBodyElement.createTR();
            trElement.setAlternativeText("Row " + rowIndex);
            trElement.setBackgroundColor(Color.getLightGoldenrodYellow());
            trElement.setBorder(new BorderInfo(BorderSide.All, 0.75f, Color.getDarkGray()));
            trElement.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.50f, Color.getBlue()));
            trElement.setMinRowHeight(100.0);
            trElement.setFixedRowHeight(120.0);
            trElement.setInNewPage(rowIndex % 3 == 1);
            trElement.setRowBroken(true);

            TextState cellTextState = new TextState();
            cellTextState.setForegroundColor(Color.getRed());
            trElement.setDefaultCellTextState(cellTextState);
            trElement.setDefaultCellPadding(new MarginInfo(16.0, 2.0, 8.0, 2.0));
            trElement.setVerticalAlignment(VerticalAlignment.Bottom);

            for (int colIndex = 0; colIndex < 3; colIndex++) {
                trElement.createTD().setText("Cell [" + rowIndex + ", " + colIndex + "]");
            }
        }

        TableTRElement footTrElement = tableTFootElement.createTR();
        footTrElement.setAlternativeText("Foot Row");
        for (int colIndex = 0; colIndex < 3; colIndex++) {
            footTrElement.createTD().setText("Foot " + colIndex);
        }

        document.save(outputFile.toString());
    }
}
```

## 
Estilo de celdas de tabla etiquetadas

Este ejemplo utiliza el método auxiliar compartido para crear una tabla con formato a nivel de celda y celdas combinadas.


1. 
Cree un nuevo [Documento] PDF etiquetado(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Agregue un elemento de tabla y rellénelo mediante el método auxiliar con el estilo de celda habilitado.

1. 
Guarde el documento.


```java
public static void styleTableCell(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Example table cell style");
        taggedContent.setLanguage("en-US");

        TableElement tableElement = taggedContent.createTableElement();
        taggedContent.getRootElement().appendChild(tableElement, true);
        fillTable(tableElement, 4, 4, true);

        document.save(outputFile.toString());
    }
}
```

## 
Ajustar la posición de la mesa etiquetada

Utilice este ejemplo cuando una tabla etiquetada deba colocarse explícitamente en la página.


1. 
Cree un nuevo [Documento] PDF etiquetado(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agregue un elemento de tabla.

1. 
Configure [PositionSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure/positionsettings/) para la tabla.

1. 
Aplique la configuración de posición, complete la tabla y guarde el documento.


```java
public static void adjustTablePosition(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Example table position");
        taggedContent.setLanguage("en-US");

        TableElement tableElement = taggedContent.createTableElement();
        taggedContent.getRootElement().appendChild(tableElement, true);

        PositionSettings positionSettings = new PositionSettings();
        positionSettings.setHorizontalAlignment(HorizontalAlignment.None);
        positionSettings.setMargin(new MarginInfo(20, 0, 0, 0));
        positionSettings.setVerticalAlignment(VerticalAlignment.None);
        positionSettings.setFirstParagraphInColumn(false);
        positionSettings.setKeptWithNext(false);
        positionSettings.setInNewPage(false);
        positionSettings.setInLineParagraph(false);
        tableElement.adjustPosition(positionSettings);

        fillTable(tableElement, 4, 4, true);
        document.save(outputFile.toString());
    }
}
```

## 
Llene una tabla etiquetada con contenido estructurado

Este método auxiliar crea las filas de encabezado, cuerpo y pie de página de una tabla y, opcionalmente, aplica estilos y extensiones de celda.


1. 
Cree las secciones de cabecera, cuerpo y pies de la mesa.

1. 
Complete las filas de encabezado, cuerpo y pie de página con elementos de celda accesibles.

1. 
Opcionalmente, configure celdas con estilo, celdas combinadas y valores de estado de texto.

```java
private static void fillTable(TableElement tableElement, int rowCount, int colCount, boolean styleCells) {
    TableTHeadElement tableTHeadElement = tableElement.createTHead();
    TableTBodyElement tableTBodyElement = tableElement.createTBody();
    TableTFootElement tableTFootElement = tableElement.createTFoot();

    TableTRElement headTrElement = tableTHeadElement.createTR();
    headTrElement.setAlternativeText("Head Row");
    headTrElement.setBackgroundColor(Color.getLightGray());

    for (int columnIndex = 0; columnIndex < colCount; columnIndex++) {
        TableTHElement thElement = headTrElement.createTH();
        thElement.setText("Head " + columnIndex);
        thElement.setBackgroundColor(Color.getGreenYellow());
        thElement.setBorder(new BorderInfo(BorderSide.All, 4.0f, Color.getGray()));
        thElement.setNoBorder(true);
        thElement.setMargin(new MarginInfo(16.0, 2.0, 8.0, 2.0));
        thElement.setAlignment(HorizontalAlignment.Right);
    }

    for (int rowIndex = 0; rowIndex < rowCount; rowIndex++) {
        TableTRElement trElement = tableTBodyElement.createTR();
        trElement.setAlternativeText("Row " + rowIndex);

        for (int columnIndex = 0; columnIndex < colCount; columnIndex++) {
            int colSpan = 1;
            int rowSpan = 1;

            if (styleCells && columnIndex == 1 && rowIndex == 1) {
                colSpan = 2;
                rowSpan = 2;
            } else if (styleCells && ((rowIndex == 1 && columnIndex == 2)
                    || (rowIndex == 2 && (columnIndex == 1 || columnIndex == 2)))) {
                continue;
            }

            TableTDElement tdElement = trElement.createTD();
            tdElement.setText("Cell [" + rowIndex + ", " + columnIndex + "]");
            tdElement.setBackgroundColor(Color.getYellow());
            tdElement.setBorder(new BorderInfo(BorderSide.All, 4.0f, Color.getGray()));
            tdElement.setNoBorder(false);
            tdElement.setMargin(new MarginInfo(8.0, 2.0, 8.0, 2.0));
            tdElement.setAlignment(HorizontalAlignment.Center);

            TextState cellTextState = new TextState();
            cellTextState.setForegroundColor(Color.getDarkBlue());
            cellTextState.setFontSize(7.5f);
            cellTextState.setFontStyle(FontStyles.Bold);
            cellTextState.setFont(FontRepository.findFont("Arial"));
            tdElement.setDefaultCellTextState(cellTextState);

            tdElement.setWordWrapped(true);
            tdElement.setVerticalAlignment(VerticalAlignment.Center);
            tdElement.setColSpan(colSpan);
            tdElement.setRowSpan(rowSpan);
        }
    }

    TableTRElement footTrElement = tableTFootElement.createTR();
    footTrElement.setAlternativeText("Foot Row");
    footTrElement.setBackgroundColor(Color.getLightSeaGreen());

    for (int columnIndex = 0; columnIndex < colCount; columnIndex++) {
        TableTDElement tdElement = footTrElement.createTD();
        tdElement.setText("Foot " + columnIndex);
        tdElement.setAlignment(HorizontalAlignment.Center);
        tdElement.getStructureTextState().setFontSize(com.aspose.pdf.Nullable.of(7.0f));
        tdElement.getStructureTextState().setFontStyle(com.aspose.pdf.Nullable.of(FontStyles.Bold));
    }
}
```
