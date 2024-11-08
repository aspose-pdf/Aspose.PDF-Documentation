---
title: Insertar una Imagen en una Celda de Tabla en PDF
type: docs
weight: 20
url: /es/java/insert-an-image-into-a-table-cell-in-pdf/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Las tablas son elementos importantes para mostrar datos. Proporcionan un formato presentable para la representación de datos. Las tablas se utilizan a menudo para mostrar información numérica. La API de Aspose.PDF proporciona una clase, Table, que le ofrece la capacidad de crear tablas en un archivo PDF.

En lugar de crear una tabla simple, puede establecer diferentes opciones de formato, por ejemplo, el estilo del borde de la tabla, información de margen, alineación, color de fondo, ancho de columna, información del título, el valor de las filas que se repetirán en cada página y muchas más.

{{% /alert %}}

## Enfoque de Aspose.PDF

Según nuestro DOM (Modelo de Objeto de Documento), un documento está compuesto por Páginas.
 Una página contiene uno o más párrafos, y un párrafo puede ser una imagen, texto, un campo de formulario, un encabezado, un cuadro flotante, un gráfico, un adjunto o una tabla. Una tabla, a su vez, tiene una colección de filas y cada fila tiene una colección de celdas. Una celda es una colección de párrafos.

Así que, de acuerdo con nuestro DOM, una celda de tabla puede contener cualquiera de los elementos de párrafo especificados anteriormente, incluidas las imágenes.

## Comprendiendo el Ancho de la Celda

Uno debe tener una comprensión clara del ancho de la celda, especialmente al mostrar una imagen en una celda de tabla, para que el ancho de la imagen se fije al ancho de una celda y se muestre correctamente. El ancho de una imagen se puede establecer utilizando el método setFixedWidth() de la clase Image.

## Ejemplo de Código

```java

 String dataDir = "C:\\temp\\";

//Instanciar un objeto Document llamando a su constructor vacío

Document pdfDocument = new Document();

//Crear una página en el objeto Document

com.aspose.pdf.Page page = pdfDocument.getPages().add();



//Instanciar un objeto tabla

Table table = new Table();

//Agregar la tabla en la colección de párrafos de la página deseada

page.getParagraphs().add(table);

//Establecer anchos de columna de la tabla

table.setColumnWidths("100 100 120");



//Establecer el borde de la tabla usando otro objeto BorderInfo personalizado

table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 1F));



//Crear un objeto de imagen en la página

com.aspose.pdf.Image img1 = new com.aspose.pdf.Image();

//Establecer la ruta del archivo de imagen

img1.setFile(dataDir + "logo.jpg");



img1.setFixWidth(100);

img1.setFixHeight(100);

//Crear filas en la tabla y luego celdas en las filas

Row row1 = table.getRows().add();

row1.getCells().add("Texto de muestra en la celda");

// Agregar la celda que contiene la imagen

Cell cell2 = row1.getCells().add();

//Agregar la imagen a la celda de la tabla

cell2.getParagraphs().add(img1);



row1.getCells().add("Celda anterior con imagen");

row1.getCells().get_Item(2).setVerticalAlignment(VerticalAlignment.Center);



//Guardar el documento

pdfDocument.save(dataDir + "Image_in_Cell.pdf");    

```