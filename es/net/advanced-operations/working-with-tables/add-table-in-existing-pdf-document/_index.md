---
title: Crear o Añadir Tabla en PDF usando C#
linktitle: Crear o Añadir Tabla
type: docs
weight: 10
url: es/net/add-table-in-existing-pdf-document/
description: Aspose.PDF para .NET es una biblioteca utilizada para crear, leer y editar Tablas en PDF. Consulte otras funciones avanzadas en este tema.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/add-and-extract-a-table/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Crear o Añadir Tabla en PDF usando C#",
    "alternativeHeadline": "Cómo añadir Tabla en PDF con .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, crear tabla en pdf, añadir tabla",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentación de Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/add-table-in-existing-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-table-in-existing-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF para .NET es una biblioteca utilizada para crear, leer y editar Tablas en PDF. Consulte otras funciones avanzadas en este tema."
}
</script>
## Creando Tabla usando C\#

Las tablas son importantes cuando se trabaja con documentos PDF. Proporcionan excelentes características para mostrar información de manera sistemática. El espacio de nombres Aspose.PDF contiene clases denominadas [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table), [Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell), y [Row](https://reference.aspose.com/pdf/net/aspose.pdf/row) que proporcionan funcionalidad para crear tablas al generar documentos PDF desde cero.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

Se puede crear una tabla creando un objeto de la clase Table.

```csharp
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
```

### Agregando Tabla en un Documento PDF Existente

Para agregar una tabla a un archivo PDF existente con Aspose.PDF para .NET, siga los siguientes pasos:

1. Cargar el archivo fuente.
1. Inicializar una tabla y configurar sus columnas y filas.
1. Configurar la tabla (hemos configurado los bordes).
1. Llenar la tabla.
1. Agregar la tabla a una página.
1.
Los siguientes fragmentos de código muestran cómo agregar texto en un archivo PDF existente.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Cargar el documento PDF fuente
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "AddTable.pdf");
// Inicializa una nueva instancia de la Tabla
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// Establece el color del borde de la tabla como GrisClaro
table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// Establece el borde para las celdas de la tabla
table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// Crea un bucle para agregar 10 filas
for (int row_count = 1; row_count < 10; row_count++)
{
    // Añade fila a la tabla
    Aspose.Pdf.Row row = table.Rows.Add();
    // Añade celdas a la tabla
    row.Cells.Add("Columna (" + row_count + ", 1)");
    row.Cells.Add("Columna (" + row_count + ", 2)");
    row.Cells.Add("Columna (" + row_count + ", 3)");
}
// Añade el objeto tabla a la primera página del documento de entrada
doc.Pages[1].Paragraphs.Add(table);
dataDir = dataDir + "documento_con_tabla_salida.pdf";
// Guarda el documento actualizado que contiene el objeto tabla
doc.Save(dataDir);
```
### ColSpan y RowSpan en Tablas

Aspose.PDF para .NET proporciona la propiedad [ColSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/colspan) para fusionar las columnas en una tabla y la propiedad [RowSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/rowspan) para fusionar las filas.

Utilizamos la propiedad `ColSpan` o `RowSpan` en el objeto `Cell` que crea la celda de la tabla. Después de aplicar las propiedades requeridas, la celda creada se puede agregar a la tabla.

```csharp
public static void AddTable_RowColSpan()
{
    // Cargar el documento PDF fuente
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document();
    pdfDocument.Pages.Add();

    // Inicializa una nueva instancia de la Tabla
    Aspose.Pdf.Table table = new Aspose.Pdf.Table
    {
        // Establecer el color del borde de la tabla como GrisClaro
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Color.Black),
        // Establecer el borde para las celdas de la tabla
        DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Color.Black)
    };

    // Agregar la primera fila a la tabla
    Aspose.Pdf.Row row1 = table.Rows.Add();
    for (int cellCount = 1; cellCount <5; cellCount++)
    {
        // Agregar celdas a la tabla
        row1.Cells.Add($"Prueba 1 {cellCount}");
    }

    // Agregar la segunda fila a la tabla
    Aspose.Pdf.Row row2 = table.Rows.Add();
    row2.Cells.Add($"Prueba 2 1");
    var cell = row2.Cells.Add($"Prueba 2 2");
    cell.ColSpan = 2;
    row2.Cells.Add($"Prueba 2 4");

    // Agregar la tercera fila a la tabla
    Aspose.Pdf.Row row3 = table.Rows.Add();
    row3.Cells.Add("Prueba 3 1");
    row3.Cells.Add("Prueba 3 2");
    row3.Cells.Add("Prueba 3 3");
    row3.Cells.Add("Prueba 3 4");

    // Agregar la cuarta fila a la tabla
    Aspose.Pdf.Row row4 = table.Rows.Add();
    row4.Cells.Add("Prueba 4 1");
    cell = row4.Cells.Add("Prueba 4 2");
    cell.RowSpan = 2;
    row4.Cells.Add("Prueba 4 3");
    row4.Cells.Add("Prueba 4 4");

    // Agregar la quinta fila a la tabla
    row4 = table.Rows.Add();
    row4.Cells.Add("Prueba 5 1");
    row4.Cells.Add("Prueba 5 3");
    row4.Cells.Add("Prueba 5 4");

    // Agregar el objeto de tabla a la primera página del documento de entrada
    pdfDocument.Pages[1].Paragraphs.Add(table);

    // Guardar el documento actualizado que contiene el objeto de tabla
    doc.Save(Path.Combine(_dataDir, "documento_con_tabla_out.pdf"));
}
```
El resultado de la ejecución del código a continuación es la tabla que se muestra en la siguiente imagen:

![ColSpan and RowSpan demo](colspan_rowspan.png)

## Trabajando con Bordes, Márgenes y Relleno

Tenga en cuenta que también admite la función de configurar el estilo de borde, los márgenes y el relleno de celda para las tablas. Antes de entrar en detalles técnicos más profundos, es importante entender los conceptos de borde, márgenes y relleno que se presentan a continuación en un diagrama:

![Borders, margins and padding](set-border-style-margins-and-padding-of-table_1.png)

En la figura anterior, puede ver que los bordes de la tabla, fila y celda se superponen. Usando Aspose.PDF, una tabla puede tener márgenes y las celdas pueden tener rellenos. Para establecer los márgenes de las celdas, tenemos que configurar el relleno de la celda.

### Bordes

Para configurar los bordes de los objetos [Tabla](https://reference.aspose.com/pdf/net/aspose.pdf/table), [Fila](https://reference.aspose.com/pdf/net/aspose.pdf/row) y [Celda](https://reference.aspose.com/pdf/net/aspose.pdf/cell), use las propiedades Table.Border, Row.Border y Cell.Border.
Para configurar los bordes de la Tabla, [Fila](https://reference.aspose.com/pdf/net/aspose.pdf/row) y [Celda](https://reference.aspose.com/pdf/net/aspose.pdf/cell), use las propiedades Table.Border, Row.Border y Cell.Border.

### Márgenes o Relleno

El relleno de la celda se puede gestionar utilizando la propiedad [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) de la clase Table. Todas las propiedades relacionadas con el relleno se asignan a una instancia de la clase [MarginInfo](https://reference.aspose.com/pdf/net/aspose.pdf/margininfo) que toma información sobre los parámetros `Left`, `Right`, `Top` y `Bottom` para crear márgenes personalizados.

En el siguiente ejemplo, el ancho del borde de la celda se establece en 0.1 punto, el ancho del borde de la tabla se establece en 1 punto y el relleno de la celda se establece en 5 puntos.

![Margen y Borde en la Tabla PDF](margin-border.png)

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Instancia el objeto Document llamando a su constructor vacío
Document doc = new Document();
Page page = doc.Pages.Add();
// Instancia un objeto de tabla
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
// Añade la tabla a la colección de párrafos de la sección deseada
page.Paragraphs.Add(tab1);
// Establece los anchos de columna de la tabla
tab1.ColumnWidths = "50 50 50";
// Establece el borde de la celda predeterminado usando el objeto BorderInfo
tab1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
// Establece el borde de la tabla usando otro objeto BorderInfo personalizado
tab1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// Crea el objeto MarginInfo y establece sus márgenes izquierdo, inferior, derecho y superior
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;
// Establece el relleno de celda predeterminado al objeto MarginInfo
tab1.DefaultCellPadding = margin;
// Crea filas en la tabla y luego celdas en las filas
Aspose.Pdf.Row row1 = tab1.Rows.Add();
row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add();
TextFragment mytext = new TextFragment("col3 con texto largo");
// Fila1.Celdas.Add("col3 con cadena de texto largo para colocar dentro de la celda");
row1.Cells[2].Paragraphs.Add(mytext);
row1.Cells[2].IsWordWrapped = false;
// Fila1.Celdas[2].Párrafos[0].AnchoFijo= 80;
Aspose.Pdf.Row row2 = tab1.Rows.Add();
row2.Cells.Add("item1");
row2.Cells.Add("item2");
row2.Cells.Add("item3");
dataDir = dataDir + "MarginsOrPadding_out.pdf";
// Guarda el Pdf
doc.Save(dataDir);
```
Para crear una tabla con esquinas redondeadas, utilice el valor `RoundedBorderRadius` de la clase BorderInfo y configure el estilo de esquina de la tabla a redondo.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();

GraphInfo graph = new GraphInfo();
graph.Color = Aspose.Pdf.Color.Red;
// Crear un objeto BorderInfo en blanco
BorderInfo bInfo = new BorderInfo(BorderSide.All, graph);
// Establecer el borde con un borde redondeado donde el radio de la redondez es 15
bInfo.RoundedBorderRadius = 15;
// Establecer el estilo de esquina de la tabla como Redondo.
tab1.CornerStyle = Aspose.Pdf.BorderCornerStyle.Round;
// Establecer la información del borde de la tabla
tab1.Border = bInfo;
```

## Aplicando Diferentes Configuraciones de AutoAjuste a una Tabla

Al crear una tabla utilizando un agente visual como Microsoft Word, a menudo se encontrará utilizando una de las opciones de AutoAjuste para dimensionar automáticamente la tabla al ancho deseado.
Cuando se crea una tabla usando un agente visual como Microsoft Word, a menudo te encontrarás utilizando una de las opciones de AutoAjuste para ajustar automáticamente la tabla al ancho deseado.

Por defecto Aspose.Pdf inserta una nueva tabla usando `ColumnAdjustment` con el valor `Customized`. La tabla se ajustará al ancho disponible en la página. Para cambiar el comportamiento de dimensionamiento en tal tabla o una tabla existente, puedes llamar al método Table.autoFit(int). Este método acepta una enumeración AutoFitBehavior que define qué tipo de ajuste automático se aplica a la tabla.

Como en Microsoft Word, un método de autofit es en realidad un atajo que aplica diferentes propiedades a la tabla de una sola vez. Estas propiedades son realmente lo que le da a la tabla el comportamiento observado. Discutiremos estas propiedades para cada opción de autofit. Usaremos la siguiente tabla y aplicaremos los diferentes ajustes de autofit como demostración:

```csharp
// Para ejemplos completos y archivos de datos, por favor ve a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Instancia el objeto Pdf llamando a su constructor vacío
Document doc = new Document();
// Crea la sección en el objeto Pdf
Page sec1 = doc.Pages.Add();

// Instancia un objeto de tabla
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
// Añade la tabla en la colección de párrafos de la sección deseada
sec1.Paragraphs.Add(tab1);

// Establece los anchos de columna de la tabla
tab1.ColumnWidths = "50 50 50";
tab1.ColumnAdjustment = ColumnAdjustment.AutoFitToWindow;

// Establece el borde de celda predeterminado usando el objeto BorderInfo
tab1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);

// Establece el borde de la tabla usando otro objeto BorderInfo personalizado
tab1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// Crea un objeto MarginInfo y establece sus márgenes izquierdo, inferior, derecho y superior
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;

// Establece el relleno de celda predeterminado al objeto MarginInfo
tab1.DefaultCellPadding = margin;

// Crea filas en la tabla y luego celdas en las filas
Aspose.Pdf.Row row1 = tab1.Rows.Add();
row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add("col3");
Aspose.Pdf.Row row2 = tab1.Rows.Add();
row2.Cells.Add("item1");
row2.Cells.Add("item2");
row2.Cells.Add("item3");

dataDir = dataDir + "AutoFitToWindow_out.pdf";
// Guarda el documento actualizado que contiene el objeto de tabla
doc.Save(dataDir);
```
### Obtener el Ancho de la Tabla

A veces, es necesario obtener el ancho de la tabla dinámicamente. La clase Aspose.PDF.Table tiene un método [GetWidth](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/getwidth) para este propósito. Por ejemplo, no has establecido explícitamente el ancho de las columnas de la tabla y has configurado [ColumnAdjustment](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnadjustment) en AutoFitToContent. En este caso, puedes obtener el ancho de la tabla de la siguiente manera.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Crear un nuevo documento
Document doc = new Document();
// Agregar página al documento
Page page = doc.Pages.Add();
// Inicializar una nueva tabla
Table table = new Table
{
    ColumnAdjustment = ColumnAdjustment.AutoFitToContent
};
// Agregar fila a la tabla
Row row = table.Rows.Add();
// Agregar celda a la tabla
Cell cell = row.Cells.Add("Texto de celda 1");
cell = row.Cells.Add("Texto de celda 2");
// Obtener el ancho de la tabla
Console.WriteLine(table.GetWidth());
```

## Agregar Imagen SVG a la Celda de la Tabla

## Agregar Imagen SVG a Celda de Tabla

Aspose.PDF para .NET soporta la característica de agregar una celda de tabla en un archivo PDF. Al crear una tabla, es posible agregar texto o imágenes en las celdas. Además, la API también ofrece la característica de convertir archivos SVG a formato PDF. Usando una combinación de estas características, es posible cargar una imagen SVG y agregarla dentro de una celda de tabla.

El siguiente fragmento de código muestra los pasos para crear una instancia de tabla y agregar una imagen SVG dentro de una celda de tabla.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Instanciar objeto Documento
Document doc = new Document();
// Crear una instancia de imagen
Aspose.Pdf.Image img = new Aspose.Pdf.Image();
// Establecer tipo de imagen como SVG
img.FileType = Aspose.Pdf.ImageFileType.Svg;
// Ruta para el archivo fuente
img.File = dataDir + "SVGToPDF.svg";
// Establecer ancho para la instancia de imagen
img.FixWidth = 50;
// Establecer altura para la instancia de imagen
img.FixHeight = 50;
// Crear instancia de tabla
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// Establecer ancho para las celdas de la tabla
table.ColumnWidths = "100 100";
// Crear objeto de fila y añadirlo a la instancia de tabla
Aspose.Pdf.Row row = table.Rows.Add();
// Crear objeto de celda y añadirlo a la instancia de fila
Aspose.Pdf.Cell cell = row.Cells.Add();
// Añadir textfragment a la colección de párrafos del objeto de celda
cell.Paragraphs.Add(new TextFragment("Primera celda"));
// Añadir otra celda al objeto de fila
cell = row.Cells.Add();
// Añadir imagen SVG a la colección de párrafos de la instancia de celda recientemente añadida
cell.Paragraphs.Add(img);
// Crear objeto de página y añadirlo a la colección de páginas del objeto de documento
Page page = doc.Pages.Add();
// Añadir tabla a la colección de párrafos del objeto de página
page.Paragraphs.Add(table);

dataDir = dataDir + "AddSVGObject_out.pdf";
// Guardar archivo PDF
doc.Save(dataDir);
```
## Uso de Etiquetas HTML dentro de una Tabla

A veces, puedes encontrarte con el requisito de importar contenidos de una base de datos que tienen algunas etiquetas HTML y luego importar el contenido al objeto Tabla. Al importar el contenido, las etiquetas HTML deben renderizarse adecuadamente dentro del documento PDF. Hemos mejorado el método ImprotDataTable(), para lograr dicho requisito de la siguiente manera:

{{% alert color="primary" %}}

Ten en cuenta que el uso de etiquetas HTML dentro del elemento de tabla aumenta el tiempo de generación del documento, ya que la API necesita procesar las etiquetas HTML adecuadamente y renderizarlas en el documento PDF de salida.

{{% /alert %}}

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

DataTable dt = new DataTable("Empleado");
dt.Columns.Add("data", System.Type.GetType("System.String"));

DataRow dr = dt.NewRow();
dr[0] = "<li>Departamento de Medicina de Emergencia: 3400 Spruce Street Ground Silverstein Bldg Philadelphia PA 19104-4206</li>";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = "<li>Servicio de Medicina de Observación de Penn: 3400 Spruce Street Planta Baja Donner Philadelphia PA 19104-4206</li>";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = "<li>UPHS/Presbyterian - Dept. de Medicina de Emergencia: 51 N. 39th Street. Philadelphia PA 19104-2640</li>";
dt.Rows.Add(dr);

Document doc = new Document();
doc.Pages.Add();
// Inicializa una nueva instancia de la Tabla
Aspose.Pdf.Table tableProvider = new Aspose.Pdf.Table();
//Establece el ancho de las columnas de la tabla
tableProvider.ColumnWidths = "400 50 ";
// Establece el color del borde de la tabla como GrisClaro
tableProvider.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// Establece el borde para las celdas de la tabla
tableProvider.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 2.5F;
margin.Left = 2.5F;
margin.Bottom = 1.0F;
tableProvider.DefaultCellPadding = margin;

tableProvider.ImportDataTable(dt, false, 0, 0, 3, 1, true);

doc.Pages[1].Paragraphs.Add(tableProvider);
doc.Save(dataDir + "HTMLInsideTableCell_out.pdf");
```
## Insertar un salto de página entre filas de tabla

Como comportamiento predeterminado, al crear una tabla dentro de un archivo PDF, la tabla fluye hacia las páginas siguientes cuando alcanza el margen inferior de la tabla. Sin embargo, podemos tener el requisito de insertar forzosamente un salto de página cuando se añade un cierto número de filas a la tabla. El siguiente fragmento de código muestra los pasos para insertar un salto de página cuando se añaden 10 filas a la tabla.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Instanciar la instancia de Documento
Document doc = new Document();
// Añadir página a la colección de páginas del archivo PDF
doc.Pages.Add();
// Crear instancia de tabla
Aspose.Pdf.Table tab = new Aspose.Pdf.Table();
// Establecer estilo de borde para la tabla
tab.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
// Establecer estilo de borde predeterminado para la tabla con color de borde Rojo
tab.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
// Especificar el ancho de columnas de la tabla
tab.ColumnWidths = "100 100";
// Crear un bucle para añadir 200 filas a la tabla
for (int counter = 0; counter <= 200; counter++)
{
    Aspose.Pdf.Row row = new Aspose.Pdf.Row();
    tab.Rows.Add(row);
    Aspose.Pdf.Cell cell1 = new Aspose.Pdf.Cell();
    cell1.Paragraphs.Add(new TextFragment("Celda " + counter + ", 0"));
    row.Cells.Add(cell1); Aspose.Pdf.Cell cell2 = new Aspose.Pdf.Cell();
    cell2.Paragraphs.Add(new TextFragment("Celda " + counter + ", 1"));
    row.Cells.Add(cell2);
    // Cuando se añaden 10 filas, renderizar nueva fila en nueva página
    if (counter % 10 == 0 && counter != 0) row.IsInNewPage = true;
}
// Añadir tabla a la colección de párrafos del archivo PDF
doc.Pages[1].Paragraphs.Add(tab);

dataDir = dataDir + "InsertPageBreak_out.pdf";
// Guardar el documento PDF
doc.Save(dataDir);
```
## Render una Tabla en una Nueva Página

Por defecto, los párrafos se añaden a la colección de Párrafos de un objeto Página. Sin embargo, es posible renderizar una tabla en una nueva página en lugar de inmediatamente después del objeto de nivel de párrafo previamente añadido en la página.

### Ejemplo: Cómo Renderizar una Tabla en una Nueva Página usando C#

Para renderizar una tabla en una nueva página, utiliza la propiedad [IsInNewPage](https://reference.aspose.com/pdf/net/aspose.pdf/baseparagraph/properties/isinnewpage) en la clase BaseParagraph. El siguiente fragmento de código muestra cómo hacerlo.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

Document doc = new Document();
PageInfo pageInfo = doc.PageInfo;
Aspose.Pdf.MarginInfo marginInfo = pageInfo.Margin;

marginInfo.Left = 37;
marginInfo.Right = 37;
marginInfo.Top = 37;
marginInfo.Bottom = 37;

pageInfo.IsLandscape = true;

Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.ColumnWidths = "50 100";
// Página añadida.
Page curPage = doc.Pages.Add();
for (int i = 1; i <= 120; i++)
{
    Aspose.Pdf.Row row = table.Rows.Add();
    row.FixedRowHeight = 15;
    Aspose.Pdf.Cell cell1 = row.Cells.Add();
    cell1.Paragraphs.Add(new TextFragment("Contenido 1"));
    Aspose.Pdf.Cell cell2 = row.Cells.Add();
    cell2.Paragraphs.Add(new TextFragment("HHHHH"));
}
Aspose.Pdf.Paragraphs paragraphs = curPage.Paragraphs;
paragraphs.Add(table);
/********************************************/
Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
table.ColumnWidths = "100 100";
for (int i = 1; i hasta 10; i++)
{
    Aspose.Pdf.Row row = table1.Rows.Add();
    Aspose.Pdf.Cell cell1 = row.Cells.Add();
    cell1.Paragraphs.Add(new TextFragment("LAAAAAAA"));
    Aspose.Pdf.Cell cell2 = row.Cells.Add();
    cell2.Paragraphs.Add(new TextFragment("LAAGGGGGG"));
}
table1.IsInNewPage = true;
// Quiero mantener la tabla 1 en la próxima página por favor...
paragraphs.Add(table1);
dataDir = dataDir + "IsNewPageProperty_Test_out.pdf";
doc.Save(dataDir);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para la biblioteca .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Biblioteca de manipulación de PDF para .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

