---
title: Renderizar tabla con Entity Framework
linktitle: Renderizar tabla con Entity Framework
type: docs
weight: 40
url: es/net/render-table-using-entity-framework-model-as-data-source/
description: Este artículo te mostrará cómo renderizar una tabla utilizando el modelo de Entity Framework como fuente de datos usando Aspose.PDF para .NET.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Hay varias tareas cuando por alguna razón es más conveniente exportar datos de bases de datos a un documento PDF sin usar el esquema de conversión de HTML a PDF recientemente popular.

Este artículo te mostrará cómo generar un documento PDF usando Aspose.PDF para .NET.

## Fundamentos de la generación de PDF con Aspose.PDF

Una de las clases más importantes en Aspose.PDF es la [clase Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Esta clase es un motor de renderizado de PDF. Para presentar una estructura PDF, la biblioteca Aspose.PDF utiliza el modelo Documento-Página, donde:

* Documento - contiene las propiedades del documento PDF incluyendo la colección de páginas;
* Documento: contiene las propiedades del documento PDF incluyendo la colección de páginas;
* Página: contiene las propiedades de una página específica y varias colecciones de elementos asociados con esta página.

Por lo tanto, para crear un documento PDF con Aspose.PDF, debe seguir estos pasos:

1. Crear el objeto Documento;
1. Añadir la página (el objeto Página) al objeto Documento;
1. Crear objetos que se colocan en la página (p. ej., fragmento de texto, tabla, etc.)
1. Añadir los elementos creados a la colección correspondiente en la página (en nuestro caso será una colección de párrafos);
1. Guardar el documento como archivo PDF.

```csharp
// Paso 1
var document = new Document
{
    PageInfo = new PageInfo { Margin = new MarginInfo(28, 28, 28, 42) }
};

// Paso 2
var pdfPage = document.Pages.Add();

// Paso 3
var textFragment = new TextFragment(reportTitle);
// ..........................................

var table = new Table
{
    // .................................
};

// Paso 4
pdfPage.Paragraphs.Add(textFragment);
pdfPage.Paragraphs.Add(table);

// Paso 5
using (var streamOut = new MemoryStream())
{
    document.Save(streamOut);
    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        FileDownloadName = "tenants.pdf"
    };
}
```
El problema más común es la salida de datos en formato de tabla. Se utiliza la [clase Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) para procesar tablas. Esta clase nos da la capacidad de crear tablas y colocarlas en el documento, utilizando [Rows](https://reference.aspose.com/pdf/net/aspose.pdf/rows) y [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cell). Por lo tanto, para crear la tabla, necesitas agregar el número requerido de filas y llenarlas con el número apropiado de celdas.

El siguiente ejemplo crea una tabla de 4x10.

```csharp
var table = new Table
    {
        // Establece el ancho automático de las columnas de la tabla
        ColumnWidths = "25% 25% 25% 25%",
        // Establece el relleno de las celdas
        DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // Izquierda Inferior Derecha Superior
        // Establece el color del borde de la tabla como Verde
        Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
        // Establece el borde de las celdas de la tabla como Negro
        DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
    };
    for (var rowCount = 0; rowCount < 10; rowCount++)
    {
        // Añade fila a la tabla
        var row = table.Rows.Add();
        // Añade celdas a la tabla
        for (int i = 0; i < 4; i++)
        {
            row.Cells.Add($"Celda ({i+1}, {rowCount +1})");
        }
    }
    // Añade el objeto de tabla a la primera página del documento de entrada
    document.Pages[1].Paragraphs.Add(table);
```
Al inicializar el objeto Table, se utilizaron los ajustes mínimos de apariencia:

* [ColumnWidths](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnwidths) - ancho de las columnas (por defecto);
* [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) - los campos predeterminados para la celda de la tabla;
* [Border](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/border) - atributos del marco de la tabla (estilo, grosor, color);
* [DefaultCellBorder](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellborder) - atributos del marco de la celda (estilo, grosor, color).

Como resultado, obtenemos una tabla de 4x10 con columnas de igual anchura.

![Tabla 4x10](http://aspose-html-doc.azurewebsites.net/docs/images/img001.jpg)

## Exportación de Datos desde Objetos ADO.NET

La clase Table proporciona métodos para interactuar con fuentes de datos ADO.NET - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) y [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview).
La clase Table proporciona métodos para interactuar con fuentes de datos ADO.NET - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) y [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview).
Aunque estos objetos no son muy convenientes para trabajar en la plantilla MVC, nos limitaremos a un breve ejemplo. En este ejemplo (línea 50), se llama al método ImportDataTable y recibe como parámetros una instancia de DataTable y configuraciones adicionales como la bandera de encabezado y la posición inicial (filas/columnas) para la salida de datos.

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
    // Establecer el relleno de celda
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

// Agregar el objeto tabla a la primera página del documento de entrada
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
## Exportando Datos desde Entity Framework

Más relevante para modernos .NET es la importación de datos desde frameworks ORM. En este caso, es una buena idea extender la clase Table con métodos de extensión para importar datos desde una lista simple o desde datos agrupados. Vamos a dar un ejemplo para uno de los ORMs más populares - Entity Framework.

```csharp
public static class PdfHelper
    {
        public static void ImportEntityList<TSource>(this Pdf.Table table, IList<TSource> data)
        {
            var headRow = table.Rows.Add();

            var props = typeof(TSource).GetProperties(BindingFlags.Public | BindingFlags.Instance);
            foreach (var prop in props)
            {
                headRow.Cells.Add(prop.GetCustomAttribute(typeof(DisplayAttribute)) is DisplayAttribute dd ? dd.Name : prop.Name);
            }

            foreach (var item in data)
            {
                // Agregar fila a la tabla
                var row = table.Rows.Add();
                // Agregar celdas a la tabla
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
        public static void ImportGroupedData<TKey,TValue>(this Pdf.Table table, IEnumerable<Models.GroupViewModel<TKey, TValue>> groupedData)
        {
            var headRow = table.Rows.Add();           
            var props = typeof(TValue).GetProperties(BindingFlags.Public | BindingFlags.Instance);
            foreach (var prop in props)
            {
               headRow.Cells.Add(prop.GetCustomAttribute(typeof(DisplayAttribute)) is DisplayAttribute dd ? dd.Name : prop.Name);               
            }

            foreach (var group in groupedData)
            {
                // Agregar fila de grupo a la tabla
                var row = table.Rows.Add();
                var cell = row.Cells.Add(group.Key.ToString());
                cell.ColSpan = props.Length;
                cell.BackgroundColor = Pdf.Color.DarkGray;
                cell.DefaultCellTextState.ForegroundColor = Pdf.Color.White;

                foreach (var item in group.Values)
                {
                    // Agregar fila de datos a la tabla
                    var dataRow = table.Rows.Add();
                    // Agregar celdas
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
Los atributos de Data Annotations se utilizan a menudo para describir modelos y ayudarnos a crear la tabla. Por lo tanto, se eligió el siguiente algoritmo de generación de tablas para ImportEntityList:

* líneas 12-18: construir una fila de encabezado y agregar celdas de encabezado según la regla "Si el DisplayAttribute está presente, entonces tomar su valor, de lo contrario tomar el nombre de la propiedad"
* líneas 50-53: construir las filas de datos y agregar celdas de fila según la regla "Si el atributo DataTypeAttribute está definido, entonces verificamos si necesitamos hacer configuraciones de diseño adicionales para él, y de lo contrario simplemente convertir los datos a cadena y agregar a la celda;"

En este ejemplo, se realizaron personalizaciones adicionales para DataType.Currency (líneas 32-34) y DataType.Date (líneas 35-43), pero puedes agregar otras si es necesario.
El algoritmo del método ImportGroupedData es casi el mismo que el anterior. Se utiliza una clase adicional GroupViewModel, para almacenar los datos agrupados.

```csharp
.using System.Collections.Generic;
    public class GroupViewModel<K,T>
    {
        public K Key;
        public IEnumerable<T> Values;
    }
```
Dado que procesamos grupos, primero generamos una línea para el valor clave (líneas 66-71), y después de eso - las líneas de este grupo.
