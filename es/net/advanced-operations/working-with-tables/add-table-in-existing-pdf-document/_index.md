---
title: Crear o Agregar Tabla en PDF usando C#
linktitle: Crear o Agregar Tabla
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/add-table-in-existing-pdf-document/
description: Aspose.PDF for .NET es una biblioteca utilizada para crear, leer y editar Tablas PDF. Consulta otras funciones avanzadas en este tema.
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
    "headline": "Create or Add Table In PDF using C#",
    "alternativeHeadline": "Add Tables to PDFs Effortlessly with C#",
    "abstract": "La nueva función en Aspose.PDF for .NET permite a los desarrolladores crear y agregar tablas a documentos PDF existentes usando C#. Esta funcionalidad incluye características avanzadas como bordes personalizables, relleno de celdas y soporte para fusionar celdas con ColSpan y RowSpan, mejorando la presentación de datos en archivos PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "3283",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
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
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NET es una biblioteca utilizada para crear, leer y editar Tablas PDF. Consulta otras funciones avanzadas en este tema."
}
</script>

## Creando Tabla usando C\#

Las tablas son importantes al trabajar con documentos PDF. Proporcionan grandes características para mostrar información de manera sistemática. El espacio de nombres Aspose.PDF contiene clases llamadas [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table), [Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell) y [Row](https://reference.aspose.com/pdf/net/aspose.pdf/row) que proporcionan funcionalidad para crear tablas al generar documentos PDF desde cero.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

La tabla se puede crear creando un objeto de la clase Table.

```csharp
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
```

### Agregando Tabla en Documento PDF Existente

Para agregar una tabla a un archivo PDF existente con Aspose.PDF for .NET, sigue los siguientes pasos:

1. Carga el archivo fuente.
1. Inicializa una tabla y establece sus columnas y filas.
1. Establece la configuración de la tabla (hemos establecido los bordes).
1. Población de la tabla.
1. Agrega la tabla a una página.
1. Guarda el archivo.

Los siguientes fragmentos de código muestran cómo agregar texto en un archivo PDF existente.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddTable.pdf"))
    {
        // Initializes a new instance of the Table
        Aspose.Pdf.Table table = new Aspose.Pdf.Table();
        // Set the table border color as LightGray
        table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
        // Set the border for table cells
        table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
        // Create a loop to add 10 rows
        for (int row_count = 1; row_count < 10; row_count++)
        {
            // Add row to table
            Aspose.Pdf.Row row = table.Rows.Add();
            // Add table cells
            row.Cells.Add("Column (" + row_count + ", 1)");
            row.Cells.Add("Column (" + row_count + ", 2)");
            row.Cells.Add("Column (" + row_count + ", 3)");
        }
        // Add table object to first page of input document
        document.Pages[1].Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "AddTable_out.pdf");
    }
}
```

### ColSpan y RowSpan en Tablas

Aspose.PDF for .NET proporciona la propiedad [ColSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/colspan) para fusionar las columnas en una tabla y la propiedad [RowSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/rowspan) para fusionar las filas.

Usamos la propiedad `ColSpan` o `RowSpan` en el objeto `Cell` que crea la celda de la tabla. Después de aplicar las propiedades requeridas, la celda creada se puede agregar a la tabla.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTableRowColSpan()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Initializes a new instance of the Table
        Aspose.Pdf.Table table = new Aspose.Pdf.Table
        {
            // Set the table border color as LightGray
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Color.Black),
            // Set the border for table cells
            DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Color.Black)
        };

        // Add 1st row to table
        Aspose.Pdf.Row row1 = table.Rows.Add();
        for (int cellCount = 1; cellCount <5; cellCount++)
        {
            // Add table cells
            row1.Cells.Add($"Test 1 {cellCount}");
        }

        // Add 2nd row to table
        Aspose.Pdf.Row row2 = table.Rows.Add();
        row2.Cells.Add($"Test 2 1");
        var cell = row2.Cells.Add($"Test 2 2");
        cell.ColSpan = 2;
        row2.Cells.Add($"Test 2 4");

        // Add 3rd row to table
        Aspose.Pdf.Row row3 = table.Rows.Add();
        row4.Cells.Add("Test 3 1");
        row4.Cells.Add("Test 3 2");
        row4.Cells.Add("Test 3 3");
        row4.Cells.Add("Test 3 4");

        // Add 4th row to table
        Aspose.Pdf.Row row4 = table.Rows.Add();
        row3.Cells.Add("Test 4 1");
        cell = row3.Cells.Add("Test 4 2");
        cell.RowSpan = 2;
        row3.Cells.Add("Test 4 3");
        row3.Cells.Add("Test 4 4");

        // Add 5th row to table
        row4 = table.Rows.Add();
        row4.Cells.Add("Test 5 1");
        row4.Cells.Add("Test 5 3");
        row4.Cells.Add("Test 5 4");

        // Add table object to first page of input document
        page.Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "AddTableRowColSpan_out.pdf");
    }
}
```

El resultado de la ejecución del código a continuación es la tabla representada en la siguiente imagen:

![Demostración de ColSpan y RowSpan](colspan_rowspan.png)

## Trabajando con Bordes, Márgenes y Relleno

Ten en cuenta que también admite la función para establecer el estilo del borde, márgenes y relleno de celdas para tablas. Antes de entrar en más detalles técnicos, es importante entender los conceptos de borde, márgenes y relleno que se presentan a continuación en un diagrama:

![Bordes, márgenes y relleno](set-border-style-margins-and-padding-of-table_1.png)

En la figura anterior, puedes ver que los bordes de la tabla, la fila y la celda se superponen. Usando Aspose.PDF, una tabla puede tener márgenes y las celdas pueden tener rellenos. Para establecer los márgenes de la celda, debemos establecer el relleno de la celda.

### Bordes

Para establecer los bordes de los objetos Table, [Row](https://reference.aspose.com/pdf/net/aspose.pdf/row) y [Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell), utiliza las propiedades Table.Border, Row.Border y Cell.Border. Los bordes de las celdas también se pueden establecer utilizando la propiedad DefaultCellBorder de la clase [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) o Row. Todas las propiedades relacionadas con los bordes discutidas anteriormente se asignan a una instancia de la clase Row, que se crea llamando a su constructor. La clase Row tiene muchas sobrecargas que toman casi todos los parámetros necesarios para personalizar el borde.

### Márgenes o Relleno

El relleno de la celda se puede gestionar utilizando la propiedad [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) de la clase Table. Todas las propiedades relacionadas con el relleno se asignan a una instancia de la clase [MarginInfo](https://reference.aspose.com/pdf/net/aspose.pdf/margininfo) que toma información sobre los parámetros `Izquierda`, `Derecha`, `Arriba` y `Abajo` para crear márgenes personalizados.

En el siguiente ejemplo, el ancho del borde de la celda se establece en 0.1 puntos, el ancho del borde de la tabla se establece en 1 punto y el relleno de la celda se establece en 5 puntos.

![Margen y Borde en Tabla PDF](margin-border.png)

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddMarginsOrPadding()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        Aspose.Pdf.Page page = document.Pages.Add();
        // Instantiate a table object
        Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
        // Add the table in paragraphs collection of the desired section
        page.Paragraphs.Add(tab1);
        // Set with column widths of the table
        tab1.ColumnWidths = "50 50 50";
        // Set default cell border using BorderInfo object
        tab1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
        // Set table border using another customized BorderInfo object
        tab1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
        // Create MarginInfo object and set its left, bottom, right and top margins
        Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
        margin.Top = 5f;
        margin.Left = 5f;
        margin.Right = 5f;
        margin.Bottom = 5f;
        // Set the default cell padding to the MarginInfo object
        tab1.DefaultCellPadding = margin;
        // Create rows in the table and then cells in the rows
        Aspose.Pdf.Row row1 = tab1.Rows.Add();
        row1.Cells.Add("col1");
        row1.Cells.Add("col2");
        row1.Cells.Add();
        Aspose.Pdf.Text.TextFragment mytext = new Aspose.Pdf.Text.TextFragment("col3 with large text string");
        // Row1.Cells.Add("col3 with large text string to be placed inside cell");
        row1.Cells[2].Paragraphs.Add(mytext);
        row1.Cells[2].IsWordWrapped = false;
        // Row1.Cells[2].Paragraphs[0].FixedWidth= 80;
        Aspose.Pdf.Row row2 = tab1.Rows.Add();
        row2.Cells.Add("item1");
        row2.Cells.Add("item2");
        row2.Cells.Add("item3");
        // Save PDF document
        document.Save(dataDir + "MarginsOrPadding_out.pdf");
    }
}
```

Para crear una tabla con esquinas redondeadas, utiliza el valor `RoundedBorderRadius` de la clase BorderInfo y establece el estilo de la esquina de la tabla en redondeado.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateTableWithRoundCorner()
{
    Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();

    Aspose.Pdf.GraphInfo graph = new Aspose.Pdf.GraphInfo();
    graph.Color = Aspose.Pdf.Color.Red;
    // Create a blank BorderInfo object
    Aspose.Pdf.BorderInfo bInfo = new Aspose.Pdf.BorderInfo(BorderSide.All, graph);
    // Set the border a rounder border where radius of round is 15
    bInfo.RoundedBorderRadius = 15;
    // Set the table Corner style as Round.
    tab1.CornerStyle = Aspose.Pdf.BorderCornerStyle.Round;
    // Set the table border information
    tab1.Border = bInfo;
}
```

## Aplicando Diferentes Configuraciones de AutoFit a una Tabla

Al crear una tabla utilizando un agente visual como Microsoft Word, a menudo te encontrarás utilizando una de las opciones de AutoFit para ajustar automáticamente el tamaño de la tabla al ancho deseado. Por ejemplo, puedes usar la opción AutoFit to Window para ajustar la tabla al ancho de la página y la opción AutoFit to Contents para permitir que cada celda crezca o se reduzca para acomodar su contenido.

Por defecto, Aspose.PDF inserta una nueva tabla utilizando `ColumnAdjustment` con el valor `Customized`. La tabla se ajustará al ancho disponible en la página. Para cambiar el comportamiento de ajuste en tal tabla o en una tabla existente, puedes llamar al método Table.autoFit(int). Este método acepta una enumeración AutoFitBehavior que define qué tipo de ajuste automático se aplica a la tabla.

Al igual que en Microsoft Word, un método de autofit es en realidad un atajo que aplica diferentes propiedades a la tabla de una vez. Estas propiedades son en realidad las que le dan a la tabla el comportamiento observado. Discutiremos estas propiedades para cada opción de autofit. Usaremos la siguiente tabla y aplicaremos las diferentes configuraciones de ajuste automático como demostración:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAutoFitToWindow()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        Aspose.Pdf.Page sec1 = document.Pages.Add();

        // Instantiate a table object
        Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
        // Add the table in paragraphs collection of the desired section
        sec1.Paragraphs.Add(tab1);

        // Set with column widths of the table
        tab1.ColumnWidths = "50 50 50";
        tab1.ColumnAdjustment = ColumnAdjustment.AutoFitToWindow;

        // Set default cell border using BorderInfo object
        tab1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);

        // Set table border using another customized BorderInfo object
        tab1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
        // Create MarginInfo object and set its left, bottom, right and top margins
        Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
        margin.Top = 5f;
        margin.Left = 5f;
        margin.Right = 5f;
        margin.Bottom = 5f;

        // Set the default cell padding to the MarginInfo object
        tab1.DefaultCellPadding = margin;

        // Create rows in the table and then cells in the rows
        Aspose.Pdf.Row row1 = tab1.Rows.Add();
        row1.Cells.Add("col1");
        row1.Cells.Add("col2");
        row1.Cells.Add("col3");
        Aspose.Pdf.Row row2 = tab1.Rows.Add();
        row2.Cells.Add("item1");
        row2.Cells.Add("item2");
        row2.Cells.Add("item3");

        // Save PDF document
        document.Save(dataDir + "AutoFitToWindow_out.pdf");
    }
}
```

### Obtener Ancho de la Tabla

A veces, es necesario obtener el ancho de la tabla dinámicamente. La clase Aspose.PDF.Table tiene un método [GetWidth](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/getwidth) para este propósito. Por ejemplo, no has establecido el ancho de las columnas de la tabla explícitamente y has establecido [ColumnAdjustment](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnadjustment) en AutoFitToContent. En este caso, puedes obtener el ancho de la tabla de la siguiente manera.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetTableWidth()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        Aspose.Pdf.Page page = document.Pages.Add();
        // Initialize new table
        Aspose.Pdf.Table table = new Aspose.Pdf.Table
        {
            ColumnAdjustment = ColumnAdjustment.AutoFitToContent
        };
        // Add row in table
        Aspose.Pdf.Row row = table.Rows.Add();
        // Add cell in table
        Aspose.Pdf.Cell cell = row.Cells.Add("Cell 1 text");
        cell = row.Cells.Add("Cell 2 text");
        // Get table width
        Console.WriteLine(table.GetWidth());
    }
}
```

## Agregar Imagen SVG a Celda de Tabla

Aspose.PDF for .NET admite la función de agregar una celda de tabla en un archivo PDF. Al crear una tabla, es posible agregar texto o imágenes dentro de las celdas. Además, la API también ofrece la función de convertir archivos SVG a formato PDF. Usando una combinación de estas características, es posible cargar una imagen SVG y agregarla dentro de una celda de tabla.

El siguiente fragmento de código muestra los pasos para crear una instancia de tabla y agregar una imagen SVG dentro de una celda de tabla.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddSvgObjectToTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Create an image instance
        Aspose.Pdf.Image img = new Aspose.Pdf.Image();
        // Set image type as SVG
        img.FileType = Aspose.Pdf.ImageFileType.Svg;
        // Path for source file
        img.File = dataDir + "SVGToPDF.svg";
        // Set width for image instance
        img.FixWidth = 50;
        // Set height for image instance
        img.FixHeight = 50;
        // Create table instance
        Aspose.Pdf.Table table = new Aspose.Pdf.Table();
        // Set width for table cells
        table.ColumnWidths = "100 100";
        // Create row object and add it to table instance
        Aspose.Pdf.Row row = table.Rows.Add();
        // Create cell object and add it to row instance
        Aspose.Pdf.Cell cell = row.Cells.Add();
        // Add textfragment to paragraphs collection of cell object
        cell.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("First cell"));
        // Add another cell to row object
        cell = row.Cells.Add();
        // Add SVG image to paragraphs collection of recently added cell instance
        cell.Paragraphs.Add(img);
        // Create page object and add it to pages collection of document instance
        Aspose.Pdf.Page page = document.Pages.Add();
        // Add table to paragraphs collection of page object
        page.Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "AddSVGObjectToTable_out.pdf");
    }
}
```

## Usando Etiquetas HTML dentro de la Tabla

A veces puedes encontrarte con la necesidad de importar contenidos de base de datos que tienen algunas etiquetas HTML y luego importar el contenido al objeto Tabla. Al importar el contenido, las etiquetas HTML deben renderizarse adecuadamente dentro del documento PDF. Hemos mejorado el método ImprotDataTable() para lograr tal requisito de la siguiente manera:

{{% alert color="primary" %}}

Ten en cuenta que el uso de etiquetas HTML dentro del elemento de tabla aumenta el tiempo de generación del documento, ya que la API necesita procesar las etiquetas HTML adecuadamente y renderizarlas en el documento PDF de salida.

{{% /alert %}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHtmlInsideTableCell()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    DataTable dt = new DataTable("Employee");
    dt.Columns.Add("data", System.Type.GetType("System.String"));

    DataRow dr = dt.NewRow();
    dr[0] = "<li>Department of Emergency Medicine: 3400 Spruce Street Ground Silverstein Bldg Philadelphia PA 19104-4206</li>";
    dt.Rows.Add(dr);
    dr = dt.NewRow();
    dr[0] = "<li>Penn Observation Medicine Service: 3400 Spruce Street Ground Floor Donner Philadelphia PA 19104-4206</li>";
    dt.Rows.Add(dr);
    dr = dt.NewRow();
    dr[0] = "<li>UPHS/Presbyterian - Dept. of Emergency Medicine: 51 N. 39th Street . Philadelphia PA 19104-2640</li>";
    dt.Rows.Add(dr);

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Initializes a new instance of the Table
        Aspose.Pdf.Table tableProvider = new Aspose.Pdf.Table();
        //Set column widths of the table
        tableProvider.ColumnWidths = "400 50 ";
        // Set the table border color as LightGray
        tableProvider.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
        // Set the border for table cells
        tableProvider.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
        Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
        margin.Top = 2.5F;
        margin.Left = 2.5F;
        margin.Bottom = 1.0F;
        tableProvider.DefaultCellPadding = margin;

        tableProvider.ImportDataTable(dt, false, 0, 0, 3, 1, true);

        page.Paragraphs.Add(tableProvider);

        // Save PDF document
        document.Save(dataDir + "HTMLInsideTableCell_out.pdf");
    }
}
```

## Insertar un Salto de Página entre las filas de la tabla

Como comportamiento predeterminado, al crear una tabla dentro de un archivo PDF, la tabla fluye a las páginas subsiguientes cuando alcanza el margen inferior de la tabla. Sin embargo, podemos tener la necesidad de insertar forzosamente un salto de página cuando se agregan un cierto número de filas a la tabla. El siguiente fragmento de código muestra los pasos para insertar un salto de página cuando se agregan 10 filas a la tabla.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertPageBreak()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create table instance
        Aspose.Pdf.Table tab = new Aspose.Pdf.Table();
        // Set border style for table
        tab.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
        // Set default border style for table with border color as Red
        tab.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
        // Specify table columsn widht
        tab.ColumnWidths = "100 100";
        // Create a loop to add 200 rows for table
        for (int counter = 0; counter <= 200; counter++)
        {
            Aspose.Pdf.Row row = new Aspose.Pdf.Row();
            tab.Rows.Add(row);
            Aspose.Pdf.Cell cell1 = new Aspose.Pdf.Cell();
            cell1.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Cell " + counter + ", 0"));
            row.Cells.Add(cell1); Aspose.Pdf.Cell cell2 = new Aspose.Pdf.Cell();
            cell2.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Cell " + counter + ", 1"));
            row.Cells.Add(cell2);
            // When 10 rows are added, render new row in new page
            if (counter % 10 == 0 && counter != 0)
            {
                row.IsInNewPage = true;
            }
        }
        // Add table to paragraphs collection of PDF file
        page.Paragraphs.Add(tab);

        // Save PDF document
        document.Save(dataDir + "InsertPageBreak_out.pdf");
    }
}
```

## Renderizar una Tabla en Nueva Página

Por defecto, los párrafos se agregan a la colección de Párrafos de un objeto Página. Sin embargo, es posible renderizar una tabla en una nueva página en lugar de directamente después del objeto de nivel de párrafo previamente agregado en la página.

### Ejemplo: Cómo Renderizar una Tabla en Nueva Página usando C\#

Para renderizar la tabla en una nueva página, utiliza la propiedad [IsInNewPage](https://reference.aspose.com/pdf/net/aspose.pdf/baseparagraph/properties/isinnewpage) en la clase BaseParagraph. El siguiente fragmento de código muestra cómo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTableOnNewPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        Aspose.Pdf.PageInfo pageInfo = document.PageInfo;
        Aspose.Pdf.MarginInfo marginInfo = pageInfo.Margin;

        marginInfo.Left = 37;
        marginInfo.Right = 37;
        marginInfo.Top = 37;
        marginInfo.Bottom = 37;

        pageInfo.IsLandscape = true;

        Aspose.Pdf.Table table = new Aspose.Pdf.Table();
        table.ColumnWidths = "50 100";
        // Add page
        Page curPage = document.Pages.Add();
        for (int i = 1; i <= 120; i++)
        {
            Aspose.Pdf.Row row = table.Rows.Add();
            row.FixedRowHeight = 15;
            Aspose.Pdf.Cell cell1 = row.Cells.Add();
            cell1.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Content 1"));
            Aspose.Pdf.Cell cell2 = row.Cells.Add();
            cell2.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("HHHHH"));
        }
        Aspose.Pdf.Paragraphs paragraphs = curPage.Paragraphs;
        paragraphs.Add(table);

        Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
        table.ColumnWidths = "100 100";
        for (int i = 1; i <= 10; i++)
        {
            Aspose.Pdf.Row row = table1.Rows.Add();
            Aspose.Pdf.Cell cell1 = row.Cells.Add();
            cell1.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("LAAAAAAA"));
            Aspose.Pdf.Cell cell2 = row.Cells.Add();
            cell2.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("LAAGGGGGG"));
        }
        table1.IsInNewPage = true;
        // Keep table 1 to next page
        paragraphs.Add(table1);
        // Save PDF document
        document.Save(dataDir + "AddTableOnNewPage_out.pdf");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
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
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
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
    "applicationCategory": "PDF Manipulation Library for .NET",
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