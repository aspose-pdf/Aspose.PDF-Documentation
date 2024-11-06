---
title: Trabajando con Tablas en PDFs Etiquetados
linktitle: Trabajando con Tablas en PDFs Etiquetados
type: docs
weight: 40
url: es/java/working-with-table-in-tagged-pdfs/
description: Este artículo explica cómo trabajar con tablas en documentos PDF etiquetados con Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Esta función es compatible con la versión 19.6 o superior.

{{% /alert %}}

## Crear Tabla en PDF Etiquetado

Aspose.PDF para Java permite crear una tabla en documentos PDF etiquetados.
 Para trabajar con tablas, la API proporciona la clase [TableElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement). Para crear una tabla, puedes usar el método [createTableElement()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#createTableElement--) de la interfaz [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). Además, puede utilizar los métodos [createTHead()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement#createTHead--), [createTBody()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement#createTBody--) y [createTFoot()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement#createTFoot--) de la clase TableElement para crear el encabezado de la tabla, el cuerpo de la tabla y el pie de la tabla respectivamente. Para crear una fila de tabla, puede utilizar el método [createTR()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableRowCollectionElement#createTR--) de la clase [TableRowCollectionElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableRowCollectionElement). El siguiente fragmento de código muestra cómo crear una tabla en el documento PDF etiquetado:

```java
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-Java
// La ruta al directorio de documentos.
String path = Utils.getDataDir() + "TaggedPDFs\\";

// Crear documento
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Ejemplo de tabla");
taggedContent.setLanguage("en-US");

// Obtener elemento raíz de la estructura
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
headTrElement.setAlternativeText("Fila de Encabezado");

headTrElement.setBackgroundColor(Color.getLightGray());

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.createTH();
    thElement.setText(String.format("Encabezado %s", colIndex));

    thElement.setBackgroundColor(Color.getGreenYellow());
    thElement.setBorder(new BorderInfo(BorderSide.All, 4.0F, Color.getLightGray()));

    thElement.setMargin(new MarginInfo(16.0, 2.0, 8.0, 2.0));

    thElement.setAlignment(HorizontalAlignment.Right);
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.createTR();
    trElement.setAlternativeText(String.format("Fila %s", rowIndex));

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
        tdElement.setText(String.format("Celda [%s, %s]", rowIndex, colIndex));

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
footTrElement.setAlternativeText("Fila de Pie");

footTrElement.setBackgroundColor(Color.getLightSeaGreen());

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.createTD();
    tdElement.setText(String.format("Pie %s", colIndex));

    tdElement.setAlignment(HorizontalAlignment.Center);
    tdElement.getStructureTextState().setFontSize(7F);
    tdElement.getStructureTextState().setFontStyle(FontStyles.Bold);
}

StructureAttributes tableAttributes = tableElement.getAttributes().getAttributes(AttributeOwnerStandard.Table);
StructureAttribute summaryAttribute = new StructureAttribute(AttributeKey.Summary);
summaryAttribute.setStringValue("El texto resumen para la tabla");
tableAttributes.setAttribute(summaryAttribute);

// Guardar documento PDF etiquetado
document.save(path + "CreateTableElement.pdf");
```

## Estilo del Elemento de Tabla

Aspose.PDF para Java permite estilizar una tabla en un documento PDF etiquetado. Para estilizar una tabla, puedes crear una tabla usando el método [createTableElement()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#createTableElement--) de la interfaz [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) y establecer el estilo de la tabla usando las propiedades de la clase [TableElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement). La siguiente es la lista de propiedades que puedes usar para estilizar una tabla:

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

El siguiente fragmento de código muestra cómo estilizar una tabla en un documento PDF etiquetado:

```java
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-Java
// La ruta al directorio de documentos.
String path = Utils.getDataDir() + "TaggedPDFs\\";

// Crear documento
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Ejemplo de estilo de tabla");
taggedContent.setLanguage("en-US");

// Obtener elemento raíz de la estructura
StructureElement rootElement = taggedContent.getRootElement();


// Crear elemento de estructura de tabla
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
headTrElement.setAlternativeText("Fila de Encabezado");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.createTH();
    thElement.setText(String.format("Encabezado %s", colIndex));
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.createTR();
    trElement.setAlternativeText(String.format("Fila %s", rowIndex));

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        TableTDElement tdElement = trElement.createTD();
        tdElement.setText(String.format("Celda [%s, %s]", rowIndex, colIndex));
    }
}

TableTRElement footTrElement = tableTFootElement.createTR();
footTrElement.setAlternativeText("Fila de Pie");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.createTD();
    tdElement.setText(String.format("Pie %s", colIndex));
}

// Guardar Documento PDF Etiquetado
document.save(path + "StyleTableElement.pdf");
```


## Estilo de Fila de Tabla

Aspose.PDF para Java permite estilizar una fila de tabla en un documento PDF etiquetado. Para estilizar una fila de tabla, puedes usar las propiedades de la clase [TableTRElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableTRElement). La siguiente es la lista de propiedades que puedes usar para estilizar una fila de tabla:

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

El siguiente fragmento de código muestra cómo estilizar una fila de tabla en el documento PDF etiquetado:

```java
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-Java
// La ruta al directorio de documentos.
String path = Utils.getDataDir() + "TaggedPDFs\\";

// Crear documento
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Ejemplo de estilo de fila de tabla");
taggedContent.setLanguage("en-US");

// Obtener elemento de estructura raíz
StructureElement rootElement = taggedContent.getRootElement();

// Crear elemento de estructura de tabla
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
headTrElement.setAlternativeText("Fila de Cabecera");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.createTH();
    thElement.setText(String.format("Cabecera %s", colIndex));
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.createTR();
    trElement.setAlternativeText(String.format("Fila %s", rowIndex));

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
        tdElement.setText(String.format("Celda [{0}, {1}]", rowIndex, colIndex));
    }
}

TableTRElement footTrElement = tableTFootElement.createTR();
footTrElement.setAlternativeText("Fila de Pie");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.createTD();
    tdElement.setText(String.format("Pie %s", colIndex));
}

// Guardar Documento PDF Etiquetado
document.save(path + "StyleTableRow.pdf");
```


## Estilo de Celda de Tabla

Aspose.PDF para Java permite estilizar una celda de tabla en un documento PDF etiquetado. Para estilizar una celda de tabla, puedes usar las propiedades de la clase [TableCellElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableCellElement). La siguiente es la lista de propiedades que puedes usar para estilizar una celda de tabla:

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

El siguiente fragmento de código muestra cómo estilizar una celda de tabla en el documento PDF etiquetado. También puedes verificar el cumplimiento de **PDF/UA** del documento creado. El fragmento de código a continuación muestra cómo usar esta funcionalidad.

```java
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-Java
// La ruta al directorio de documentos.
String path = Utils.getDataDir() + "TaggedPDFs\\";

// Crear documento
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Ejemplo de estilo de celda de tabla");
taggedContent.setLanguage("en-US");

// Obtener elemento de estructura raíz
StructureElement rootElement = taggedContent.getRootElement();


// Crear elemento de estructura de tabla
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
headTrElement.setAlternativeText("Fila de Cabecera");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.createTH();
    thElement.setText(String.format("Cabecera %s", colIndex));

    thElement.setBackgroundColor(Color.getGreenYellow());
    thElement.setBorder(new BorderInfo(BorderSide.All, 4.0F, Color.getGray()));

    thElement.setNoBorder(false);
    thElement.setMargin(new MarginInfo(16.0, 2.0, 8.0, 2.0));

    thElement.setAlignment(HorizontalAlignment.Right);
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.createTR();
    trElement.setAlternativeText(String.format("Fila %s", rowIndex));

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
        tdElement.setText(String.format("Celda [%s, %s]", rowIndex, colIndex));


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
footTrElement.setAlternativeText("Fila de Pie");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.createTD();
    tdElement.setText(String.format("Pie %s", colIndex));
}


// Guardar documento PDF etiquetado
document.save(path + "StyleTableCell.pdf");
```