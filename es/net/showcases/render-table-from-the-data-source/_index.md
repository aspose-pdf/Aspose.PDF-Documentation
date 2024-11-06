---
title: Renderizar tabla desde la fuente de datos
linktitle: Renderizar tabla desde la fuente de datos
type: docs
weight: 30
url: es/net/render-table-from-the-data-source/
description: Esta página explica cómo es posible renderizar una tabla desde la fuente de datos utilizando la biblioteca Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF permite crear una tabla con DataSource desde DataSet, DataTable, arreglos y objetos IEnumerable utilizando la clase PdfLightTable

La [clase Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) se utiliza para procesar tablas. Esta clase nos da la capacidad de crear tablas y colocarlas en el documento, utilizando [Rows](https://reference.aspose.com/pdf/net/aspose.pdf/rows) y [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cell). Por lo tanto, para crear la tabla, necesitas añadir el número requerido de filas y llenarlas con el número apropiado de celdas.

El siguiente ejemplo crea una tabla de 4x10.

```csharp
var table = new Table
    {
        // Establecer anchuras automáticas de columna de la tabla
        ColumnWidths = "25% 25% 25% 25%",
        // Establecer el relleno de la celda
        DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // Izquierda Abajo Derecha Arriba
        // Establecer el color del borde de la tabla como Verde
        Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
        // Establecer el borde para las celdas de la tabla como Negro
        DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
    };
    for (var rowCount = 0; rowCount < 10; rowCount++)
    {
        // Añadir fila a la tabla
        var row = table.Rows.Add();
        // Añadir celdas a la tabla
        for (int i = 0; i < 4; i++)
        {
            row.Cells.Add($"Celda ({i+1}, {rowCount +1})");
        }
    }
    // Añadir el objeto de tabla a la primera página del documento de entrada
    document.Pages[1].Paragraphs.Add(table);
```
Al inicializar el objeto Table, se utilizaron las configuraciones mínimas de apariencia:

* [ColumnWidths](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnwidths) - ancho de las columnas (por defecto);
* [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) - los campos predeterminados para la celda de la tabla;
* [Border](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/border) - atributos del marco de la tabla (estilo, grosor, color);
* [DefaultCellBorder](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellborder) - atributos del marco de la celda (estilo, grosor, color).

## Exportación de datos desde un arreglo de objetos

La clase Table proporciona métodos para interactuar con fuentes de datos ADO.NET - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) y [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview).

Dado que estos objetos no son muy convenientes para trabajar en la plantilla MVC, nos limitaremos a un breve ejemplo. En este ejemplo (línea 50), se llama al método ImportDataTable y recibe como parámetros una instancia de DataTable y configuraciones adicionales como la bandera de encabezado y la posición inicial (filas/columnas) para la salida de datos.

```csharp
// Crear un nuevo documento PDF
var document = new Document
{
    PageInfo = new PageInfo { Margin = new MarginInfo(28, 28, 28, 42) }
};

var pdfPage = document.Pages.Add();

// Inicializa una nueva instancia de TextFragment para el título del informe
var textFragment = new TextFragment(reportTitle1);
Table table = new Table
{
    // Establecer los anchos de columna de la tabla
    ColumnWidths = "25% 25% 25% 25%",
    // Establecer el relleno de las celdas
    DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // Izquierda Abajo Derecha Arriba
    // Establecer el color del borde de la tabla como Verde
    Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
    // Establecer el borde de las celdas de la tabla como Negro
    DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
};

var configuration = new ConfigurationBuilder()
    .SetBasePath(Directory.GetCurrentDirectory())
    .AddJsonFile("config.json", false)
    .Build();

var connectionString = configuration.GetSection("connectionString").Value;

if (string.IsNullOrEmpty(connectionString))
    throw new ArgumentException("No hay cadena de conexión en config.json");

var resultTable = new DataTable();

using (var conn = new SqlConnection(connectionString))
{
    const string sql = "SELECT * FROM Tennats";
    using (var cmd = new SqlCommand(sql, conn))
    {
        using (var adapter = new SqlDataAdapter(cmd))
        {
            adapter.Fill(resultTable);
        }
    }
}

table.ImportDataTable(resultTable,true,1,1);

// Agregar el objeto de tabla a la primera página del documento de entrada
document.Pages[1].Paragraphs.Add(table);
using (var streamOut = new MemoryStream())
{
    document.Save(streamOut);
    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        FileDownloadName = "demotable2.pdf"
    };
}
```

