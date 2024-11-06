---
title: Crear o Añadir Tabla en PDF
linktitle: Crear o Añadir Tabla
type: docs
weight: 10
url: es/java/add-table-in-existing-pdf-document/
description: Aprenda cómo crear o añadir una tabla a un documento PDF, aplicando estilo a las celdas, dividiendo la tabla en páginas y personalizando las filas y columnas, etc.
lastmod: "2021-12-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Creando Tabla

El espacio de nombres Aspose.PDF contiene clases llamadas [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table), [Cell](https://reference.aspose.com/pdf/java/com.aspose.pdf/cell), y [Row](https://reference.aspose.com/pdf/java/com.aspose.pdf/row) que proporcionan funcionalidad para crear tablas al generar documentos PDF desde cero.

La tabla se puede crear creando un objeto de la clase Table.

```java
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
```

### Añadiendo Tabla en Documento PDF Existente

Para añadir una tabla a un archivo PDF existente con Aspose.PDF para Java, siga los siguientes pasos:

1. Cargue el archivo fuente.

1. Inicializar una tabla y configurar sus columnas y filas.  
1. Configurar las opciones de la tabla (hemos configurado los bordes).  
1. Llenar la tabla.  
1. Añadir la tabla a una página.  
1. Guardar el archivo.  

Los siguientes fragmentos de código muestran cómo añadir texto en un archivo PDF existente.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddTable {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void CreateTable() {
        Document doc = new Document(_dataDir + "input.pdf");
        // Inicializa una nueva instancia de la tabla
        Table table = new Table();
        // Establecer el color del borde de la tabla como LightGray
        table.setBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // establecer el borde para las celdas de la tabla
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // crear un bucle para añadir 10 filas
        for (int row_count = 1; row_count < 10; row_count++) {
            // añadir fila a la tabla
            Row row = table.getRows().add();
            // añadir celdas de la tabla
            row.getCells().add("Columna (" + row_count + ", 1)");
            row.getCells().add("Columna (" + row_count + ", 2)");
            row.getCells().add("Columna (" + row_count + ", 3)");
        }
        // Añadir objeto de tabla a la primera página del documento de entrada
        doc.getPages().get_Item(1).getParagraphs().add(table);
        // Guardar documento actualizado que contiene el objeto de tabla
        doc.save(_dataDir + "document_with_table.pdf");
    }
```


### ColSpan y RowSpan en Tablas de Aspose.PDF usando Java

Aspose.PDF para Java proporciona el método [setColSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setColSpan-int-) para fusionar las columnas en una tabla y el método [setRowSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setRowSpan-int-) para fusionar las filas.

Usamos los métodos [setColSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setColSpan-int-) o [setRowSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setRowSpan-int-) en el objeto [Cell](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell) que crea la celda de la tabla. Después de aplicar las propiedades requeridas, la celda creada puede ser añadida a la tabla.

```java
public static void AddTable_RowColSpan() {
        // Cargar documento PDF fuente
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        // Inicializa una nueva instancia de la Tabla
        Table table = new Table();
        // Establecer el color del borde de la tabla como LightGray
        table.setBorder(new BorderInfo(BorderSide.All, .5f, Color.getBlack()));
        // Establecer el borde para las celdas de la tabla
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, .5f, Color.getBlack()));
        // Añadir la 1ª fila a la tabla
        Row row1 = table.getRows().add();
        for (int cellCount = 1; cellCount < 5; cellCount++) {
            // Añadir celdas a la tabla
            row1.getCells().add("Prueba 1 " + cellCount);
        }

        // Añadir la 2ª fila a la tabla
        Row row2 = table.getRows().add();
        row2.getCells().add("Prueba 2 1");
        Cell cell = row2.getCells().add("Prueba 2 2");
        cell.setColSpan(2);
        row2.getCells().add("Prueba 2 4");

        // Añadir la 3ª fila a la tabla
        Row row3 = table.getRows().add();
        row3.getCells().add("Prueba 3 1");
        row3.getCells().add("Prueba 3 2");
        row3.getCells().add("Prueba 3 3");
        row3.getCells().add("Prueba 3 4");

        // Añadir la 4ª fila a la tabla
        Row row4 = table.getRows().add();
        row3.getCells().add("Prueba 4 1");
        cell = row3.getCells().add("Prueba 4 2");
        cell.setRowSpan(2);
        row3.getCells().add("Prueba 4 3");
        row3.getCells().add("Prueba 4 4");

        // Añadir la 5ª fila a la tabla
        row4 = table.getRows().add();
        row4.getCells().add("Prueba 5 1");
        row4.getCells().add("Prueba 5 3");
        row4.getCells().add("Prueba 5 4");

        // Añadir el objeto tabla a la primera página del documento de entrada
        page.getParagraphs().add(table);

        // Guardar documento actualizado que contiene el objeto tabla
        pdfDocument.save(_dataDir + "document_with_table_out.pdf");
    }
```


El resultado del código de ejecución a continuación es la tabla representada en la siguiente imagen:

![Demostración de ColSpan y RowSpan](colspan_rowspan.png)

## Trabajando con Bordes, Márgenes y Relleno

Aspose.PDF para Java permite a los desarrolladores crear tablas en documentos PDF. Según el Modelo de Objeto de Documento de Aspose.PDF, una tabla es un elemento a nivel de párrafo.

Tenga en cuenta que también admite la función para establecer el estilo de borde, márgenes y relleno de celda para tablas. Antes de entrar en detalles más técnicos, es importante entender los conceptos de borde, márgenes y relleno que se presentan a continuación en un diagrama:

![Bordes, márgenes y relleno](set-border-style-margins-and-padding-of-table_1.png)

En la figura anterior, puede ver que los bordes de la tabla, fila y celda se superponen. Usando Aspose.PDF, una tabla puede tener márgenes y las celdas pueden tener rellenos. Para establecer márgenes de celda, debemos establecer el relleno de celda.

## Bordes

Para establecer los bordes de los objetos [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table), [Row](https://reference.aspose.com/pdf/java/com.aspose.pdf/row) y [Cell](https://reference.aspose.com/pdf/java/com.aspose.pdf/cell), use los métodos [Table.setBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table#setBorder-com.aspose.pdf.BorderInfo-), [Row.setBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Row#setBorder-com.aspose.pdf.BorderInfo-) y [Cell.setBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setBorder-com.aspose.pdf.BorderInfo-).
 Los bordes de las celdas también se pueden establecer utilizando la clase [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table) o la clase [Row](https://reference.aspose.com/pdf/java/com.aspose.pdf/row) con el método [DefaultCellBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Row#setDefaultCellBorder-com.aspose.pdf.BorderInfo-). Todas las propiedades relacionadas con los bordes discutidas anteriormente se asignan a una instancia de la clase Row, que se crea llamando a su constructor. La clase Row tiene muchas sobrecargas que toman casi todos los parámetros necesarios para personalizar el borde.

## Márgenes o Relleno

El relleno de las celdas se puede gestionar utilizando la clase Table con el método [DefaultCellPadding](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table#setDefaultCellPadding-com.aspose.pdf.MarginInfo-). Todas las propiedades relacionadas con el relleno se asignan a una instancia de la clase [MarginInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/MarginInfo) que toma información sobre los parámetros `Left`, `Right`, `Top` y `Bottom` para crear márgenes personalizados.

En el siguiente ejemplo, el ancho del borde de la celda se establece en 0.1 punto, el ancho del borde de la tabla se establece en 1 punto y el relleno de la celda se establece en 5 puntos.

![Márgen y Borde en Tabla PDF](margin-border.png)

```java
public static void MargingPadding() {
        // Instanciar el objeto Document llamando a su constructor vacío
        Document doc = new Document();
        Page page = doc.getPages().add();
        // Instanciar un objeto tabla
        Table tab1 = new Table();
        // Añadir la tabla en la colección de párrafos de la sección deseada
        page.getParagraphs().add(tab1);
        // Establecer con anchos de columna de la tabla
        tab1.setColumnWidths ("50 50 50");
        // Establecer el borde de celda predeterminado usando el objeto BorderInfo
        tab1.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1F));
        // Establecer el borde de la tabla usando otro objeto BorderInfo personalizado
        tab1.setBorder (new BorderInfo(BorderSide.All, 1F));

        // Crear objeto MarginInfo y establecer sus márgenes izquierdo, inferior, derecho y superior
        MarginInfo margin = new MarginInfo();
        margin.setTop (5f);
        margin.setLeft (5f);
        margin.setRight (5f);
        margin.setBottom (5f);

        // Establecer el relleno de celda predeterminado al objeto MarginInfo
        tab1.setDefaultCellPadding(margin);

        // Crear filas en la tabla y luego celdas en las filas
        Row row1 = tab1.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add();

        TextFragment mytext = new TextFragment("col3 con una cadena de texto grande");

        row1.getCells().get_Item(2).getParagraphs().add(mytext);
        row1.getCells().get_Item(2).setWordWrapped(false);

        Row row2 = tab1.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");

        // Guardar el PDF
        doc.save(_dataDir + "MarginsOrPadding_out.pdf");
    }
}
```

Para crear una tabla con esquinas redondeadas, use el valor `RoundedBorderRadius` de la clase [BorderInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/BorderInfo) y establezca el estilo de esquina de la tabla en redondo.

```java
    public static void RoundedBorderRadius() {
        Document doc = new Document();
        Page page = doc.getPages().add();

        // Instanciar un objeto de tabla
        Table tab1 = new Table();

        // Agregar la tabla en la colección de párrafos de la sección deseada
        page.getParagraphs().add(tab1);

        GraphInfo graph = new GraphInfo();
        graph.setColor(Color.getRed());
        // Crear un objeto BorderInfo en blanco
        BorderInfo bInfo = new BorderInfo(BorderSide.All, graph);
        // Establecer el borde como un borde redondeado donde el radio de la curva es 15
        bInfo.setRoundedBorderRadius(15);
        // Establecer el estilo de esquina de la tabla como Redondo.
        tab1.setCornerStyle(BorderCornerStyle.Round);
        // Establecer la información del borde de la tabla
        tab1.setBorder(bInfo);
        // Crear filas en la tabla y luego celdas en las filas
        Row row1 = tab1.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add();

        TextFragment mytext = new TextFragment("col3 con una cadena de texto larga");

        row1.getCells().get_Item(2).getParagraphs().add(mytext);
        row1.getCells().get_Item(2).setWordWrapped(false);

        Row row2 = tab1.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");

        // Guardar el PDF
        doc.save(_dataDir + "BorderRadius_out.pdf");
    }
```


### Propiedad AutoFitToWindow en la enumeración ColumnAdjustmentType

```java
 public static void AutoFitToWindowProperty() {
        // Instanciar el objeto Pdf llamando a su constructor vacío
        Document doc = new Document();
        // Crear la sección en el objeto Pdf
        Page sec1 = doc.getPages().add();

        // Instanciar un objeto de tabla
        Table tab1 = new Table();
        // Añadir la tabla en la colección de párrafos de la sección deseada
        sec1.getParagraphs().add(tab1);

        // Establecer los anchos de columna de la tabla
        tab1.setColumnWidths("50 50 50");
        tab1.setColumnAdjustment(ColumnAdjustment.AutoFitToWindow);

        // Establecer el borde de celda predeterminado usando el objeto BorderInfo
        tab1.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1F));

        // Establecer el borde de la tabla usando otro objeto BorderInfo personalizado
        tab1.setBorder(new BorderInfo(BorderSide.All, 1F));

        // Crear objeto MarginInfo y establecer sus márgenes izquierdo, inferior, derecho y superior
        MarginInfo margin = new MarginInfo();
        margin.setTop(5f);
        margin.setLeft(5f);
        margin.setRight(5f);
        margin.setBottom(5f);

        // Establecer el relleno de celda predeterminado al objeto MarginInfo
        tab1.setDefaultCellPadding(margin);

        // Crear filas en la tabla y luego celdas en las filas
        Row row1 = tab1.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add("col3");
        Row row2 = tab1.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");

        // Guardar el documento actualizado que contiene el objeto tabla
        doc.save(_dataDir + "AutoFitToWindow_out.pdf");
    }
```


### Obtener Ancho de la Tabla

A veces, es necesario obtener el ancho de la tabla dinámicamente. La clase Aspose.PDF.Table tiene un método [GetWidth](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table#getWidth--) para este propósito. Por ejemplo, no has establecido el ancho de las columnas de la tabla explícitamente y has configurado [ColumnAdjustment](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColumnAdjustment) en AutoFitToContent. En este caso, puedes obtener el ancho de la tabla de la siguiente manera.

```java
public static void GetTableWidth() {
        // Crear un nuevo documento
        Document doc = new Document();
        // Agregar página en el documento
        Page page = doc.getPages().add();

        // Inicializar nueva tabla
        Table table = new Table();

        // Agregar la tabla en la colección de párrafos de la sección deseada
        page.getParagraphs().add(table);
        table.setColumnAdjustment(ColumnAdjustment.AutoFitToContent);

        // Agregar fila en la tabla
        Row row = table.getRows().add();
        // Agregar celda en la tabla
        row.getCells().add("Texto de la Celda 1");
        row.getCells().add("Texto de la Celda 2");
        // Obtener ancho de la tabla
        System.out.println(table.getWidth());
    }
```


## Agregar objeto SVG a la celda de la tabla

Aspose.PDF para Java admite la función de agregar una celda de tabla en un archivo PDF. Al crear una tabla, es posible agregar texto o imágenes en las celdas. Además, la API también ofrece la función de convertir archivos SVG al formato PDF. Usando una combinación de estas funciones, es posible cargar una imagen SVG y agregarla en una celda de tabla.

El siguiente fragmento de código muestra los pasos para crear una instancia de tabla y agregar una imagen SVG dentro de una celda de tabla.

```java
 public static void AddSVGObjectToTableCell() {
        // Instanciar objeto Documento
        Document doc = new Document();
        // Crear una instancia de imagen
        com.aspose.pdf.Image img = new com.aspose.pdf.Image();
        // Establecer tipo de imagen como SVG
        img.setFileType (com.aspose.pdf.ImageFileType.Svg);
        // Ruta para el archivo fuente
        img.setFile (_dataDir + "SVGToPDF.svg");
        // Establecer ancho para la instancia de imagen
        img.setFixWidth (50);
        // Establecer altura para la instancia de imagen
        img.setFixHeight (50);
        // Crear instancia de tabla
        com.aspose.pdf.Table table = new com.aspose.pdf.Table();
        // Establecer ancho para las celdas de la tabla
        table.setColumnWidths ("100 100");
        // Crear objeto fila y añadirlo a la instancia de tabla
        com.aspose.pdf.Row row = table.getRows().add();
        // Crear objeto celda y añadirlo a la instancia de fila
        com.aspose.pdf.Cell cell = row.getCells().add();
        // Añadir fragmento de texto a la colección de párrafos del objeto celda
        cell.getParagraphs().add(new TextFragment("Primera celda"));
        // Añadir otra celda al objeto fila
        cell = row.getCells().add();
        // Añadir imagen SVG a la colección de párrafos de la instancia de celda recién añadida
        cell.getParagraphs().add(img);
        // Crear objeto página y añadirlo a la colección de páginas de la instancia de documento
        Page page = doc.getPages().add();
        // Añadir tabla a la colección de párrafos del objeto página
        page.getParagraphs().add(table);
        // Guardar archivo PDF
        doc.save(_dataDir + "AddSVGObject_out.pdf");
    }
```


## Añadir etiquetas HTML dentro de la tabla

Aspose.PDF para Java permite agregar un nuevo Fragmento HTML en un Párrafo de su archivo PDF.

{{% alert color="primary" %}}

Por favor, tenga en cuenta que el uso de etiquetas HTML dentro del elemento de tabla aumenta el tiempo de generación del documento, ya que la API necesita procesar las etiquetas HTML en consecuencia y renderizarlas en el documento PDF de salida.

{{% /alert %}}

```java
  public static void AddHTMLFragmentToTableCell() {
        Document doc = new Document(_dataDir + "input.pdf");
        // Inicializa una nueva instancia de la Tabla
        Table table = new Table();
        // Establece el color del borde de la tabla como LightGray
        table.setBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // establece el borde para las celdas de la tabla
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // crea un bucle para añadir 10 filas
        for (int row_count = 1; row_count < 10; row_count++) {
            Cell cell;
            // añade fila a la tabla
            Row row = table.getRows().add();
            // añade celdas a la tabla
            cell = row.getCells().add();
            cell.getParagraphs().add(new HtmlFragment("Columna <strong>(" + row_count + ", 1)</strong>"));

            cell = row.getCells().add();
            cell.getParagraphs().add(new HtmlFragment("Columna <span style='color:red'>(" + row_count + ", 2)</span>"));

            cell = row.getCells().add();
            cell.getParagraphs().add(new HtmlFragment("Columna <span style='text-decoration: underline'>(" + row_count + ", 3)</span>"));
        }
        // Agrega el objeto de tabla a la primera página del documento de entrada
        doc.getPages().get_Item(1).getParagraphs().add(table);
        // Guarda el documento actualizado que contiene el objeto de tabla
        doc.save(_dataDir + "AddHTMLObject_out.pdf");
    }

}
```


## Insertar un salto de página entre las filas de la tabla

Por defecto, al crear una tabla dentro de un archivo PDF, la tabla fluye a las páginas subsecuentes cuando alcanza el margen inferior de la tabla. Sin embargo, podemos tener un requerimiento de insertar forzadamente un salto de página cuando se agregan un cierto número de filas a la tabla. El siguiente fragmento de código muestra los pasos para insertar un salto de página cuando se agregan 10 filas a la tabla.

```java
    public static void InsertPageBreak() {
        // Crear una instancia de Document
        Document doc = new Document();
        // Agregar una página a la colección de páginas del archivo PDF
        Page page = doc.getPages().add();
        // Crear una instancia de tabla
        Table tab = new Table();
        // Establecer estilo de borde para la tabla
        tab.setBorder (new BorderInfo(BorderSide.All, Color.getRed()));
        // Establecer estilo de borde predeterminado para la tabla con color de borde rojo
        tab.setDefaultCellBorder (new BorderInfo(BorderSide.All, Color.getRed()));
        // Especificar el ancho de las columnas de la tabla
        tab.setColumnWidths ("100 100");
        // Crear un bucle para agregar 200 filas a la tabla
        for (int counter = 0; counter <= 200; counter++) {
            Row row = new Row();
            tab.getRows().add(row);
            Cell cell1 = new Cell();
            cell1.getParagraphs().add(new TextFragment("Cell " + counter + ", 0"));
            row.getCells().add(cell1);
            Cell cell2 = new Cell();
            cell2.getParagraphs().add(new TextFragment("Cell " + counter + ", 1"));
            row.getCells().add(cell2);
            // Cuando se agregan 10 filas, renderizar nueva fila en nueva página
            if (counter % 10 == 0 && counter != 0)
                row.setInNewPage(true);
        }
        // Agregar la tabla a la colección de párrafos del archivo PDF
        page.getParagraphs().add(tab);

        // Guardar el documento PDF
        doc.save(_dataDir + "InsertPageBreak_out.pdf");
    }
```


## Ocultar Bordes de Celdas Combinadas

Al agregar celdas a una tabla, los bordes de las celdas combinadas pueden aparecer cuando se rompen a otra fila. Tales bordes combinados pueden hacerse invisibles como se muestra en el siguiente ejemplo de código.

```java
Document doc = new Document();
com.aspose.pdf.Page page = doc.getPages().add();

//Instanciar un objeto de tabla que se anidará dentro de outerTable que se romperá
//dentro de la misma página
com.aspose.pdf.Table mytable = new com.aspose.pdf.Table();
mytable.setBroken(TableBroken.Vertical);
mytable.setDefaultCellBorder(new BorderInfo(BorderSide.All));
mytable.setRepeatingColumnsCount(2);
page.getParagraphs().add(mytable);

//Agregar fila de encabezado
com.aspose.pdf.Row row = mytable.getRows().add();
Cell cell = row.getCells().add("encabezado 1");
cell.setColSpan(2);
cell.setBackgroundColor(Color.getLightGray());
Cell header3 = row.getCells().add("encabezado 3");
Cell cell2 = row.getCells().add("encabezado 4");
cell2.setColSpan(2);
cell2.setBackgroundColor(Color.getLightBlue());
row.getCells().add("encabezado 6");
Cell cell3 = row.getCells().add("encabezado 7");
cell3.setColSpan(2);
cell3.setBackgroundColor(Color.getLightGreen());
Cell cell4 = row.getCells().add("encabezado 9");
cell4.setColSpan(3);
cell4.setBackgroundColor(Color.getLightCoral());
row.getCells().add("encabezado 12");
row.getCells().add("encabezado 13");
row.getCells().add("encabezado 14");
row.getCells().add("encabezado 15");
row.getCells().add("encabezado 16");
row.getCells().add("encabezado 17");

for (int rowCounter = 0; rowCounter < 1; rowCounter++)
{
  //Crear filas en la tabla y luego celdas en las filas
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