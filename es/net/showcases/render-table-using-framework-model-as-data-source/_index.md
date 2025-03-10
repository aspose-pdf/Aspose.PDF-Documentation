---
title: Renderizar tabla con Entity Framework
linktitle: Renderizar tabla con Entity Framework
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /es/net/render-table-using-entity-framework-model-as-data-source/
description: Este artículo te mostrará cómo renderizar una tabla utilizando el modelo de Entity Framework como fuente de datos usando el Aspose.PDF for .NET.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Render table with Entity Framework",
    "alternativeHeadline": "Render PDF from Entity Framework Data Easily",
    "abstract": "Presentando una nueva función que permite la renderización sin problemas de tablas directamente desde modelos de Entity Framework en documentos PDF usando Aspose.PDF for .NET. Esta funcionalidad simplifica la visualización de datos al permitir a los usuarios importar datos de marcos ORM de manera eficiente, creando tablas bien estructuradas con atributos personalizables y opciones de formato. Mejora tus capacidades de informes con esta poderosa integración, proporcionando salidas PDF limpias y profesionales sin necesidad de conversiones basadas en HTML.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1540",
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
    "url": "/net/render-table-using-entity-framework-model-as-data-source/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/render-table-using-entity-framework-model-as-data-source/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también hacer frente a objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

Hay una serie de tareas cuando, por alguna razón, es más conveniente exportar datos de bases de datos a un documento PDF sin utilizar el esquema de conversión de HTML a PDF que ha ganado popularidad recientemente.

Este artículo te mostrará cómo generar un documento PDF utilizando el Aspose.PDF for .NET.

## Conceptos básicos de generación de PDF con Aspose.PDF

Una de las clases más importantes en Aspose.PDF es la [clase Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Esta clase es un motor de renderización de PDF. Para presentar una estructura PDF, la biblioteca Aspose.PDF utiliza el modelo Documento-Página, donde:

* Documento - contiene las propiedades del documento PDF, incluida la colección de páginas.
* Página - contiene las propiedades de una página específica y varias colecciones de elementos asociados con esta página.

Por lo tanto, para crear un documento PDF con Aspose.PDF, debes seguir estos pasos:

1. Crear el objeto Document.
1. Agregar la página (el objeto Page) al objeto Document.
1. Crear objetos que se colocarán en la página (por ejemplo, fragmento de texto, tabla, etc.).
1. Agregar los elementos creados a la colección correspondiente en la página (en nuestro caso, será una colección de párrafos).
1. Guardar el documento como archivo PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTable()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document
           {
               PageInfo = new Aspose.Pdf.PageInfo { Margin = new Aspose.Pdf.MarginInfo(28, 28, 28, 42) }
           })
    {
        // Add page
        var page = document.Pages.Add();

        var textFragment = new Aspose.Pdf.Text.TextFragment(reportTitle);

        var table = new Aspose.Pdf.Table
        {
            // .................................
        };

        page.Paragraphs.Add(textFragment);
        page.Paragraphs.Add(table);

        using (var streamOut = new MemoryStream())
        {
            // Save PDF document
            document.Save(streamOut);

            return new FileContentResult(streamOut.ToArray(), "application/pdf")
            {
                FileDownloadName = "tenants.pdf"
            };
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTable()
{
    // Create PDF document
    using var document = new Aspose.Pdf.Document
    {
        PageInfo = new Aspose.Pdf.PageInfo { Margin = new Aspose.Pdf.MarginInfo(28, 28, 28, 42) }
    };

    // Add page
    var page = document.Pages.Add();

    var textFragment = new Aspose.Pdf.Text.TextFragment(reportTitle);

    var table = new Aspose.Pdf.Table
    {
        // .................................
    };

    page.Paragraphs.Add(textFragment);
    page.Paragraphs.Add(table);

    using var streamOut = new MemoryStream();

    // Save PDF document
    document.Save(streamOut);

    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        FileDownloadName = "tenants.pdf"
    };
}
```
{{< /tab >}}
{{< /tabs >}}

El problema más común es la salida de datos en formato de tabla. La [clase Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) se utiliza para procesar tablas. Esta clase nos da la capacidad de crear tablas y colocarlas en el documento, utilizando [Rows](https://reference.aspose.com/pdf/net/aspose.pdf/rows) y [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cell). Así que, para crear la tabla, necesitas agregar el número requerido de filas y llenarlas con el número apropiado de celdas.

El siguiente ejemplo crea la tabla 4x10.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        var table = new Aspose.Pdf.Table
        {
            // Set column auto widths of the table
            ColumnWidths = "25% 25% 25% 25%",

            // Set cell padding
            DefaultCellPadding = new Aspose.Pdf.MarginInfo(10, 5, 10, 5), // Left Bottom Right Top

            // Set the table border color as Green
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.Green),

            // Set the border for table cells as Black
            DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .2f, Aspose.Pdf.Color.Green),
        };

        for (var rowCount = 0; rowCount < 10; rowCount++)
        {
            // Add row to table
            var row = table.Rows.Add();

            // Add table cells
            for (int i = 0; i < 4; i++)
            {
                row.Cells.Add($"Cell ({i + 1}, {rowCount + 1})");
            }
        }

        // Add table object to first page of input document
        page.Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "AddTable_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();

    // Add page
    var page = document.Pages.Add();

    var table = new Aspose.Pdf.Table
    {
        // Set column auto widths of the table
        ColumnWidths = "25% 25% 25% 25%",

        // Set cell padding
        DefaultCellPadding = new Aspose.Pdf.MarginInfo(10, 5, 10, 5), // Left Bottom Right Top

        // Set the table border color as Green
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.Green),

        // Set the border for table cells as Black
        DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .2f, Aspose.Pdf.Color.Green),
    };

    for (var rowCount = 0; rowCount < 10; rowCount++)
    {
        // Add row to table
        var row = table.Rows.Add();

        // Add table cells
        for (int i = 0; i < 4; i++)
        {
            row.Cells.Add($"Cell ({i + 1}, {rowCount + 1})");
        }
    }

    // Add table object to first page of input document
    page.Paragraphs.Add(table);

    // Save PDF document
    document.Save(dataDir + "AddTable_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

Al inicializar el objeto Table, se utilizaron las configuraciones mínimas de apariencia:

* [ColumnWidths](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnwidths) - ancho de las columnas (por defecto).
* [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) - los campos predeterminados para la celda de la tabla.
* [Border](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/border) - atributos del marco de la tabla (estilo, grosor, color).
* [DefaultCellBorder](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellborder) - atributos del marco de la celda (estilo, grosor, color).

Como resultado, obtenemos la tabla 4x10 con columnas de igual ancho.

![Tabla 4x10](http://aspose-html-doc.azurewebsites.net/docs/images/img001.jpg)

## Exportando datos desde objetos ADO.NET

La clase Table proporciona métodos para interactuar con fuentes de datos ADO.NET - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) y [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview). El primer método importa datos desde el DataTable, el segundo desde el DataView.
Premitiendo que estos objetos no son muy convenientes para trabajar en la plantilla MVC, nos limitaremos a un breve ejemplo. En este ejemplo (línea 50), se llama al método ImportDataTable y recibe como parámetros una instancia de DataTable y configuraciones adicionales como la bandera de encabezado y la posición inicial (filas/columnas) para la salida de datos.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTable()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document
    {
        PageInfo = new Aspose.Pdf.PageInfo { Margin = new Aspose.Pdf.MarginInfo(28, 28, 28, 42) }
    })
    {
        var table = new Aspose.Pdf.Table
        {
            // Set column widths of the table
            ColumnWidths = "25% 25% 25% 25%",
            // Set cell padding
            DefaultCellPadding = new Aspose.Pdf.MarginInfo(10, 5, 10, 5), // Left Bottom Right Top
            // Set the table border color as Green
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.Green),
            // Set the border for table cells as Black
            DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .2f, Aspose.Pdf.Color.Green),
        };

        var configuration = new ConfigurationBuilder()
            .SetBasePath(Directory.GetCurrentDirectory())
            .AddJsonFile("config.json", false)
            .Build();

        var connectionString = configuration.GetSection("connectionString").Value;

        if (string.IsNullOrEmpty(connectionString))
        {
            throw new ArgumentException("No connection string in config.json");
        }

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

        table.ImportDataTable(resultTable, true, 1, 1);

        // Add table object to first page of input document
        document.Pages[1].Paragraphs.Add(table);

        using (var streamOut = new MemoryStream())
        {
            // Save PDF document
            document.Save(streamOut);

            return new FileContentResult(streamOut.ToArray(), "application/pdf")
            {
                FileDownloadName = "demotable2.pdf"
            };
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTable()
{
    // Create PDF document
    using var document = new Aspose.Pdf.Document
    {
        PageInfo = new Aspose.Pdf.PageInfo { Margin = new Aspose.Pdf.MarginInfo(28, 28, 28, 42) }
    };

    var table = new Aspose.Pdf.Table
    {
        // Set column widths of the table
        ColumnWidths = "25% 25% 25% 25%",
        // Set cell padding
        DefaultCellPadding = new Aspose.Pdf.MarginInfo(10, 5, 10, 5), // Left Bottom Right Top
        // Set the table border color as Green
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.Green),
        // Set the border for table cells as Black
        DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .2f, Aspose.Pdf.Color.Green),
    };

    var configuration = new ConfigurationBuilder()
        .SetBasePath(Directory.GetCurrentDirectory())
        .AddJsonFile("config.json", false)
        .Build();

    var connectionString = configuration.GetSection("connectionString").Value;

    if (string.IsNullOrEmpty(connectionString))
    {
        throw new ArgumentException("No connection string in config.json");
    }

    var resultTable = new DataTable();

    using var conn = new SqlConnection(connectionString);

    const string sql = "SELECT * FROM Tennats";

    using var cmd = new SqlCommand(sql, conn);

    using var adapter = new SqlDataAdapter(cmd);
    
    adapter.Fill(resultTable);

    table.ImportDataTable(resultTable, true, 1, 1);

    // Add table object to first page of input document
    document.Pages[1].Paragraphs.Add(table);

    using var streamOut = new MemoryStream();
    
    // Save PDF document
    document.Save(streamOut);

    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        PageInfo = new Aspose.Pdf.PageInfo { Margin = new Aspose.Pdf.MarginInfo(28, 28, 28, 42) }
    };
}
```
{{< /tab >}}
{{< /tabs >}}

## Exportando datos desde Entity Framework

Más relevante para .NET moderno es la importación de datos desde marcos ORM. En este caso, es una buena idea extender la clase Table con métodos de extensión para importar datos desde una lista simple o desde los datos agrupados. Demos un ejemplo para uno de los ORM más populares - Entity Framework.

```csharp
public static class PdfHelper
{
    private static void ImportEntityList<TSource>(this Aspose.Pdf.Table table, IList<TSource> data)
    {
        var headRow = table.Rows.Add();

        var props = typeof(TSource).GetProperties(BindingFlags.Public | BindingFlags.Instance);
        foreach (var prop in props)
        {
            headRow.Cells.Add(prop.GetCustomAttribute(typeof(DisplayAttribute)) is DisplayAttribute dd ? dd.Name : prop.Name);
        }

        foreach (var item in data)
        {
            // Add row to table
            var row = table.Rows.Add();
            // Add table cells
            foreach (var t in props)
            {
                var dataItem = t.GetValue(item, null);
                if (t.GetCustomAttribute(typeof(DataTypeAttribute)) is DataTypeAttribute dataType)
                    switch (dataType.DataType)
                    {

                        case DataType.Currency:
                            row.Cells.Add(string.Format("{0:C}", dataItem));
                            break;
                        case DataType.Date:
                            var dateTime = (DateTime)dataItem;
                            if (t.GetCustomAttribute(typeof(DisplayFormatAttribute)) is DisplayFormatAttribute df)
                            {
                                row.Cells.Add(string.IsNullOrEmpty(df.DataFormatString)
                                    ? dateTime.ToShortDateString()
                                    : string.Format(df.DataFormatString, dateTime));
                            }
                            break;
                        default:
                            row.Cells.Add(dataItem.ToString());
                            break;
                    }
                else
                {
                    row.Cells.Add(dataItem.ToString());
                }
            }
        }
    }

    private static void ImportGroupedData<TKey, TValue>(this Aspose.Pdf.Table table, IEnumerable<Models.GroupViewModel<TKey, TValue>> groupedData)
    {
        var headRow = table.Rows.Add();
        var props = typeof(TValue).GetProperties(BindingFlags.Public | BindingFlags.Instance);
        foreach (var prop in props)
        {
            headRow.Cells.Add(prop.GetCustomAttribute(typeof(DisplayAttribute)) is DisplayAttribute dd ? dd.Name : prop.Name);
        }

        foreach (var group in groupedData)
        {
            // Add group row to table
            var row = table.Rows.Add();
            var cell = row.Cells.Add(group.Key.ToString());
            cell.ColSpan = props.Length;
            cell.BackgroundColor = Aspose.Pdf.Color.DarkGray;
            cell.DefaultCellTextState.ForegroundColor = Aspose.Pdf.Color.White;

            foreach (var item in group.Values)
            {
                // Add data row to table
                var dataRow = table.Rows.Add();
                // Add cells
                foreach (var t in props)
                {
                    var dataItem = t.GetValue(item, null);

                    if (t.GetCustomAttribute(typeof(DataTypeAttribute)) is DataTypeAttribute dataType)
                        switch (dataType.DataType)
                        {
                            case DataType.Currency:
                                dataRow.Cells.Add(string.Format("{0:C}", dataItem));
                                break;
                            case DataType.Date:
                                var dateTime = (DateTime)dataItem;
                                if (t.GetCustomAttribute(typeof(DisplayFormatAttribute)) is DisplayFormatAttribute df)
                                {
                                    dataRow.Cells.Add(string.IsNullOrEmpty(df.DataFormatString)
                                        ? dateTime.ToShortDateString()
                                        : string.Format(df.DataFormatString, dateTime));
                                }
                                break;
                            default:
                                dataRow.Cells.Add(dataItem.ToString());
                                break;
                        }
                    else
                    {
                        dataRow.Cells.Add(dataItem.ToString());
                    }
                }
            }
        }
    }
}
```

Los atributos de Data Annotations se utilizan a menudo para describir modelos y nos ayudan a crear la tabla. Por lo tanto, se eligió el siguiente algoritmo de generación de tabla para ImportEntityList:

* líneas 12-18: construir una fila de encabezado y agregar celdas de encabezado de acuerdo con la regla "Si el DisplayAttribute está presente, entonces toma su valor, de lo contrario toma el nombre de la propiedad".
* líneas 50-53: construir las filas de datos y agregar celdas de fila de acuerdo con la regla "Si el atributo DataTypeAttribute está definido, entonces verificamos si necesitamos hacer configuraciones de diseño adicionales para él, y de lo contrario simplemente convertimos los datos a cadena y los agregamos a la celda;".

En este ejemplo, se realizaron personalizaciones adicionales para DataType.Currency (líneas 32-34) y DataType.Date (líneas 35-43), pero puedes agregar otras si es necesario.
El algoritmo del método ImportGroupedData es casi el mismo que el anterior. Se utiliza una clase adicional GroupViewModel, para almacenar los datos agrupados.

```csharp
using System.Collections.Generic;
public class GroupViewModel<K,T>
{
    public K Key;
    public IEnumerable<T> Values;
}
```

Dado que procesamos grupos, primero generamos una línea para el valor clave (líneas 66-71), y después las líneas de este grupo.