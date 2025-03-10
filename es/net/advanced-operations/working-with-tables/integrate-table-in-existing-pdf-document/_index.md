---
title: Integrar Tabla con Fuentes de Datos PDF
linktitle: Integrar Tabla
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /es/net/integrate-table/
description: Este artículo muestra cómo integrar tablas PDF. Integra Tabla con Base de Datos y determina si la tabla se dividirá en la página actual.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Integrate Table with Data Sources PDF",
    "alternativeHeadline": "Integrate PDF Tables with Data Sources Seamlessly",
    "abstract": "La función de integrar Tabla con Fuentes de Datos PDF permite a los desarrolladores importar datos de diversas fuentes, incluidas bases de datos y el Entity Framework, directamente en tablas PDF usando Aspose.PDF for .NET. Con funcionalidades para determinar la paginación y soporte para columnas repetidas, esta función mejora la presentación de datos mientras mantiene la integridad del documento al prevenir rupturas de tabla a través de páginas.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2201",
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
    "url": "/net/integrate-table/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/integrate-table/"
    },
    "dateModified": "2024-11-26",
    "description": "Este artículo muestra cómo integrar tablas PDF. Integra Tabla con Base de Datos y determina si la tabla se dividirá en la página actual."
}
</script>

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Integrar Tabla con Base de Datos

Las bases de datos están diseñadas para almacenar y gestionar datos. Es una práctica común para los programadores poblar diferentes objetos con datos de bases de datos. Este artículo discute cómo agregar datos de una base de datos a una tabla. Es posible poblar un objeto [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) con datos de cualquier fuente de datos usando Aspose.PDF for .NET. Y no solo es posible, sino que es muy fácil.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) permite a los desarrolladores importar datos de:

- Array de Objetos
- DataTable
- DataView

Este tema proporciona información sobre cómo obtener datos de un DataTable o DataView.

Todos los desarrolladores que trabajan en la plataforma .NET deben estar familiarizados con los conceptos básicos de ADO.NET introducidos por el .NET Framework. Es posible conectarse a casi todos los tipos de fuentes de datos usando ADO.NET. Podemos recuperar datos de bases de datos y guardarlos en un DataSet, DataTable o DataView. Aspose.PDF for .NET también proporciona soporte para importar datos de estos. Esto brinda más libertad a los desarrolladores para poblar tablas en documentos PDF desde cualquier fuente de datos.

Los métodos ImportDataTable(..) e ImportDataView(..) de la clase Table se utilizan para importar datos de bases de datos.

El siguiente ejemplo demuestra el uso del método ImportDataTable. En este ejemplo, el objeto DataTable se crea desde cero y los registros se agregan programáticamente en lugar de llenar el DataTable con datos de bases de datos. Los desarrolladores también pueden poblar DataTable desde la base de datos según su deseo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFromDataTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    DataTable dt = new DataTable("Employee");
    dt.Columns.Add("Employee_ID", typeof(Int32));
    dt.Columns.Add("Employee_Name", typeof(string));
    dt.Columns.Add("Gender", typeof(string));
    // Add 2 rows into the DataTable object programmatically
    DataRow dr = dt.NewRow();
    dr[0] = 1;
    dr[1] = "John Smith";
    dr[2] = "Male";
    dt.Rows.Add(dr);
    dr = dt.NewRow();
    dr[0] = 2;
    dr[1] = "Mary Miller";
    dr[2] = "Female";
    dt.Rows.Add(dr);
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Initializes a new instance of the Table
        Aspose.Pdf.Table table = new Aspose.Pdf.Table();
        // Set column widths of the table
        table.ColumnWidths = "40 100 100 100";
        // Set the table border color as LightGray
        table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
        // Set the border for table cells
        table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
        table.ImportDataTable(dt, true, 0, 1, 3, 3);

        // Add table object to first page of input document
        page.Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "ImportFromDataTable_out.pdf");
    }
}
```

## Cómo determinar si la tabla se romperá en la página actual

Las tablas se agregan por defecto desde la posición superior izquierda y si la tabla alcanza el final de la página, se rompe automáticamente. Puedes obtener programáticamente la información de si la Tabla se acomodará en la página actual o se romperá en la parte inferior de la página. Por esa razón, primero necesitas obtener la información del tamaño del documento, luego necesitas obtener la información del margen superior e inferior de la página, la información del margen superior de la tabla y la altura de la tabla. Si sumas el Margen Superior de la Página + Margen Inferior de la Página + Margen Superior de la Tabla + Altura de la Tabla y lo deduces de la altura del documento, puedes obtener la cantidad de espacio restante sobre el documento. Dependiendo de la altura particular de la fila (que has especificado), puedes calcular si todas las filas de una tabla pueden acomodarse dentro del espacio restante sobre una página o no. Por favor, echa un vistazo al siguiente fragmento de código. En el siguiente código, la altura promedio de la fila es de 23.002 Puntos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DetermineTableBreak()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = pdf.Pages.Add();
        // Instantiate a table object
        Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
        table1.Margin.Top = 300;
        // Add the table in paragraphs collection of the desired section
        page.Paragraphs.Add(table1);
        // Set with column widths of the table
        table1.ColumnWidths = "100 100 100";
        // Set default cell border using BorderInfo object
        table1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
        // Set table border using another customized BorderInfo object
        table1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
        // Create MarginInfo object and set its left, bottom, right and top margins
        Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
        margin.Top = 5f;
        margin.Left = 5f;
        margin.Right = 5f;
        margin.Bottom = 5f;
        // Set the default cell padding to the MarginInfo object
        table1.DefaultCellPadding = margin;
        // If you increase the counter to 17, table will break
        // Because it cannot be accommodated any more over this page
        for (int RowCounter = 0; RowCounter <= 16; RowCounter++)
        {
            // Create rows in the table and then cells in the rows
            Aspose.Pdf.Row row1 = table1.Rows.Add();
            row1.Cells.Add("col " + RowCounter.ToString() + ", 1");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 2");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 3");
        }
        // Get the Page Height information
        float PageHeight = (float)pdf.PageInfo.Height;
        // Get the total height information of Page Top & Bottom margin,
        // Table Top margin and table height.
        float TotalObjectsHeight = (float)page.PageInfo.Margin.Top + (float)page.PageInfo.Margin.Bottom + (float)table1.Margin.Top + (float)table1.GetHeight();

        // Display Page Height, Table Height, table Top margin and Page Top
        // And Bottom margin information
        Console.WriteLine("PDF document Height = " + pdf.PageInfo.Height.ToString() + "\nTop Margin Info = " + page.PageInfo.Margin.Top.ToString() + "\nBottom Margin Info = " + page.PageInfo.Margin.Bottom.ToString() + "\n\nTable-Top Margin Info = " + table1.Margin.Top.ToString() + "\nAverage Row Height = " + table1.Rows[0].MinRowHeight.ToString() + " \nTable height " + table1.GetHeight().ToString() + "\n ----------------------------------------" + "\nTotal Page Height =" + PageHeight.ToString() + "\nCummulative height including Table =" + TotalObjectsHeight.ToString());

        // Check if we deduct the sume of Page top margin + Page Bottom margin
        // + Table Top margin and table height from Page height and its less
        // Than 10 (an average row can be greater than 10)
        if ((PageHeight - TotalObjectsHeight) <= 10)
        {
            // If the value is less than 10, then display the message.
            // Which shows that another row can not be placed and if we add new
            // Row, table will break. It depends upon the row height value.
            Console.WriteLine("Page Height - Objects Height < 10, so table will break");
        }

        // Save PDF document
        document.Save(dataDir + "DetermineTableBreak_out.pdf");
    }
}
```

## Agregar Columna Repetida en la Tabla

En la clase Aspose.Pdf.Table, puedes establecer un RepeatingRowsCount que repetirá filas si la tabla es demasiado larga verticalmente y se desborda a la siguiente página. Sin embargo, en algunos casos, las tablas son demasiado anchas para caber en una sola página y necesitan continuar en la siguiente página. Para servir a este propósito, hemos implementado la propiedad RepeatingColumnsCount en la clase Aspose.Pdf.Table. Establecer esta propiedad hará que la tabla se rompa a la siguiente página columna por columna y repita el número de columnas dado al inicio de la siguiente página. El siguiente fragmento de código muestra el uso de la propiedad RepeatingColumnsCount:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRepeatingColumn()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Instantiate an outer table that takes up the entire page
        Aspose.Pdf.Table outerTable = new Aspose.Pdf.Table();
        outerTable.ColumnWidths = "100%";
        outerTable.HorizontalAlignment = HorizontalAlignment.Left;

        // Instantiate a table object that will be nested inside outerTable that will break inside the same page
        Aspose.Pdf.Table mytable = new Aspose.Pdf.Table();
        mytable.Broken = TableBroken.VerticalInSamePage;
        mytable.ColumnAdjustment = ColumnAdjustment.AutoFitToContent;

        // Add the outerTable to the page paragraphs
        // Add mytable to outerTable
        page.Paragraphs.Add(outerTable);
        var bodyRow = outerTable.Rows.Add();
        var bodyCell = bodyRow.Cells.Add();
        bodyCell.Paragraphs.Add(mytable);
        mytable.RepeatingColumnsCount = 5;
        page.Paragraphs.Add(mytable);

        // Add header Row
        Aspose.Pdf.Row row = mytable.Rows.Add();
        row.Cells.Add("header 1");
        row.Cells.Add("header 2");
        row.Cells.Add("header 3");
        row.Cells.Add("header 4");
        row.Cells.Add("header 5");
        row.Cells.Add("header 6");
        row.Cells.Add("header 7");
        row.Cells.Add("header 11");
        row.Cells.Add("header 12");
        row.Cells.Add("header 13");
        row.Cells.Add("header 14");
        row.Cells.Add("header 15");
        row.Cells.Add("header 16");
        row.Cells.Add("header 17");

        for (int RowCounter = 0; RowCounter <= 5; RowCounter++)
        {
            // Create rows in the table and then cells in the rows
            Aspose.Pdf.Row row1 = mytable.Rows.Add();
            row1.Cells.Add("col " + RowCounter.ToString() + ", 1");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 2");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 3");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 4");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 5");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 6");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 7");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 11");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 12");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 13");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 14");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 15");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 16");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 17");
        }

        // Save PDF document
        document.Save(dataDir + "AddRepeatingColumn_out.pdf");
    }
}
```

## Integrar Tabla con la fuente de Entity Framework

Más relevante para .NET moderno es la importación de datos de marcos ORM. En este caso, es una buena idea extender la clase Table con métodos de extensión para importar datos de una lista simple o de los datos agrupados. Demos un ejemplo para uno de los ORM más populares: Entity Framework.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
public static class PdfHelper
{
    private static void ImportEntityList<TSource>(this Pdf.Table table, IList<TSource> data)
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
    
    private static void ImportGroupedData<TKey,TValue>(this Pdf.Table table, IEnumerable<Models.GroupViewModel<TKey, TValue>> groupedData)
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
            cell.BackgroundColor = Pdf.Color.DarkGray;
            cell.DefaultCellTextState.ForegroundColor = Pdf.Color.White;

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

Los atributos de Anotaciones de Datos se utilizan a menudo para describir modelos y ayudarnos a crear la tabla. Por lo tanto, se eligió el siguiente algoritmo de generación de tablas para ImportEntityList:

- líneas 12-18: construir una fila de encabezado y agregar celdas de encabezado de acuerdo con la regla "Si el DisplayAttribute está presente, entonces toma su valor, de lo contrario toma el nombre de la propiedad"
- líneas 50-53: construir las filas de datos y agregar celdas de fila de acuerdo con la regla "Si el atributo DataTypeAttribute está definido, entonces verificamos si necesitamos hacer configuraciones de diseño adicionales para él, y de lo contrario simplemente convertimos los datos a cadena y los agregamos a la celda;"

En este ejemplo, se realizaron personalizaciones adicionales para DataType.Currency (líneas 32-34) y DataType.Date (líneas 35-43), pero puedes agregar otras si es necesario. El algoritmo del método ImportGroupedData es casi el mismo que el anterior. Se utiliza una clase adicional GroupViewModel para almacenar los datos agrupados.

```csharp
using System.Collections.Generic;
public class GroupViewModel<K,T>
{
    public K Key;
    public IEnumerable<T> Values;
}
```

Dado que procesamos grupos, primero generamos una línea para el valor clave (líneas 66-71), y después las líneas de este grupo.

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