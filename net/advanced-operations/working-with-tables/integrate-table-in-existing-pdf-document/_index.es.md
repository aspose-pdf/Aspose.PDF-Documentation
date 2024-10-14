---
title: Integrar Tabla con Fuentes de Datos PDF
linktitle: Integrar Tabla
type: docs
weight: 30
url: /net/integrate-table/
description: Este artículo muestra cómo integrar tablas PDF. Integrar Tabla con Base de Datos y determinar si la tabla se dividirá en la página actual.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Integrar Tabla con Fuentes de Datos PDF",
    "alternativeHeadline": "Cómo integrar Tabla con Fuentes de Datos PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, integrar tabla",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/integrate-table/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/integrate-table/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artículo muestra cómo integrar tablas PDF. Integrar Tabla con Base de Datos y determinar si la tabla se dividirá en la página actual."
}
</script>

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Integrar Tabla con Base de Datos

Las bases de datos están construidas para almacenar y gestionar datos. Es una práctica común para los programadores poblar diferentes objetos con datos provenientes de bases de datos. Este artículo discute cómo agregar datos de una base de datos a una tabla. Es posible poblar un objeto [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) con datos de cualquier fuente de datos usando Aspose.PDF para .NET. Y no solo es posible, sino que es muy fácil.

[Aspose.PDF para .NET](https://docs.aspose.com/pdf/net/) permite a los desarrolladores importar datos desde:

- Array de Objetos
- DataTable
- DataView

Este tema proporciona información sobre cómo obtener datos de un DataTable o DataView.

Todos los desarrolladores que trabajan bajo la plataforma .NET deben estar familiarizados con los conceptos básicos de ADO.NET introducidos por el .NET Framework.
Todos los desarrolladores que trabajan bajo la plataforma .NET deben estar familiarizados con los conceptos básicos de ADO.NET introducidos por .NET Framework.

Los métodos ImportDataTable(..) y ImportDataView(..) de la clase Table se utilizan para importar datos desde bases de datos.

El ejemplo a continuación demuestra el uso del método ImportDataTable. En este ejemplo, el objeto DataTable se crea desde cero y los registros se añaden programáticamente en lugar de llenar el DataTable con datos de bases de datos. Los desarrolladores también pueden poblar DataTable desde la base de datos según su deseo.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

DataTable dt = new DataTable("Empleado");
dt.Columns.Add("ID_Empleado", typeof(Int32));
dt.Columns.Add("Nombre_Empleado", typeof(string));
dt.Columns.Add("Género", typeof(string));
// Añadir 2 filas en el objeto DataTable programáticamente
DataRow dr = dt.NewRow();
dr[0] = 1;
dr[1] = "John Smith";
dr[2] = "Masculino";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = 2;
dr[1] = "Mary Miller";
dr[2] = "Femenino";
dt.Rows.Add(dr);
// Crear instancia de Documento
Document doc = new Document();
doc.Pages.Add();
// Inicializa una nueva instancia de la Table
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// Establecer anchos de columnas de la tabla
table.ColumnWidths = "40 100 100 100";
// Establecer el color del borde de la tabla como GrisClaro
table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// Establecer el borde para las celdas de la tabla
table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
table.ImportDataTable(dt, true, 0, 1, 3, 3);

// Agregar objeto de tabla a la primera página del documento de entrada
doc.Pages[1].Paragraphs.Add(table);
dataDir = dataDir + "DataIntegrated_out.pdf";
// Guardar documento actualizado que contiene objeto de tabla
doc.Save(dataDir);
```
## Cómo determinar si la tabla se romperá en la página actual

Las tablas se añaden por defecto desde la posición superior izquierda y si la tabla llega al final de la página, se rompe automáticamente. Puedes obtener programáticamente la información de si la Tabla se acomodará en la página actual o se romperá en la parte inferior de la página. Para ello, primero, necesitas obtener la información del tamaño del documento, luego necesitas obtener la información del margen superior e inferior de la página, la información del margen superior de la tabla y la altura de la tabla. Si sumas el Margen Superior de la página + el Margen Inferior de la página + el Margen Superior de la tabla + la Altura de la tabla y lo restas de la altura del documento, puedes obtener la cantidad de espacio restante sobre el documento. Dependiendo de la altura particular de la fila (que has especificado), puedes calcular si todas las filas de una tabla pueden ser acomodadas dentro del espacio restante en una página o no. Por favor, echa un vistazo al siguiente fragmento de código. En el siguiente código, la altura promedio de la fila es de 23.002 puntos.

```csharp
// Para ejemplos completos y archivos de datos, por favor ve a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Instancia un objeto de clase PDF
Document pdf = new Document();
// Añade la sección a la colección de secciones del documento PDF
Aspose.Pdf.Page page = pdf.Pages.Add();
// Instancia un objeto de tabla
Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
table1.Margin.Top = 300;
// Añade la tabla en la colección de párrafos de la sección deseada
page.Paragraphs.Add(table1);
// Establece los anchos de columna de la tabla
table1.ColumnWidths = "100 100 100";
// Establece el borde de celda predeterminado usando el objeto BorderInfo
table1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
// Establece el borde de la tabla usando otro objeto BorderInfo personalizado
table1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// Crea un objeto MarginInfo y establece sus márgenes izquierdo, inferior, derecho y superior
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;
// Establece el relleno de celda predeterminado al objeto MarginInfo
table1.DefaultCellPadding = margin;
// Si aumentas el contador a 17, la tabla se romperá
// Porque no puede ser acomodada más en esta página
for (int RowCounter = 0; RowCounter <= 16; RowCounter++)
{
    // Crea filas en la tabla y luego celdas en las filas
    Aspose.Pdf.Row row1 = table1.Rows.Add();
    row1.Cells.Add("col " + RowCounter.ToString() + ", 1");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 2");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 3");
}
// Obtén la información de altura de la página
float PageHeight = (float)pdf.PageInfo.Height;
// Obtén la información de altura total del margen superior e inferior de la página,
// El margen superior de la tabla y la altura de la tabla.
float TotalObjectsHeight = (float)page.PageInfo.Margin.Top + (float)page.PageInfo.Margin.Bottom + (float)table1.Margin.Top + (float)table1.GetHeight();

// Muestra la altura del documento PDF, altura de la tabla, margen superior de la tabla y la información del margen superior e inferior de la página
Console.WriteLine("Altura del documento PDF = " + pdf.PageInfo.Height.ToString() + "\nInformación del margen superior = " + page.PageInfo.Margin.Top.ToString() + "\nInformación del margen inferior = " + page.PageInfo.Margin.Bottom.ToString() + "\n\nInformación del margen superior de la tabla = " + table1.Margin.Top.ToString() + "\nAltura promedio de la fila = " + table1.Rows[0].MinRowHeight.ToString() + " \nAltura de la tabla " + table1.GetHeight().ToString() + "\n ----------------------------------------" + "\nAltura total de la página =" + PageHeight.ToString() + "\nAltura acumulativa incluyendo la tabla =" + TotalObjectsHeight.ToString());

// Verifica si restamos la suma del margen superior de la página + el margen inferior de la página
// + El margen superior de la tabla y la altura de la tabla de la altura de la página y es menos
// Que 10 (una fila promedio puede ser mayor que 10)
if ((PageHeight - TotalObjectsHeight) <= 10)
    // Si el valor es menor que 10, entonces muestra el mensaje.
    // Lo que muestra que no se puede colocar otra fila y si añadimos nueva
    // Fila, la tabla se romperá. Depende del valor de altura de la fila.
    Console.WriteLine("Altura de la página - Altura de objetos < 10, así que la tabla se romperá");


dataDir = dataDir + "DetermineTableBreak_out.pdf";
// Guarda el documento pdf
pdf.Save(dataDir);
```
## Añadir columna repetida en tabla

En la clase Aspose.Pdf.Table, puedes configurar un RepeatingRowsCount que repetirá filas si la tabla es demasiado larga verticalmente y se desborda a la siguiente página. Sin embargo, en algunos casos, las tablas son demasiado anchas para caber en una sola página y necesitan continuar en la siguiente página. Para cumplir con este propósito, hemos implementado la propiedad RepeatingColumnsCount en la clase Aspose.Pdf.Table. Configurar esta propiedad hará que la tabla se divida hacia la siguiente página por columnas y repita la cantidad de columnas dada al inicio de la siguiente página. El siguiente fragmento de código muestra el uso de la propiedad RepeatingColumnsCount:

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

string outFile = dataDir + "AddRepeatingColumn_out.pdf";
// Crear un nuevo documento
Document doc = new Document();
Aspose.Pdf.Page page = doc.Pages.Add();

// Instanciar una tabla exterior que ocupe toda la página
Aspose.Pdf.Table outerTable = new Aspose.Pdf.Table();
outerTable.ColumnWidths = "100%";
outerTable.HorizontalAlignment = HorizontalAlignment.Left;

// Instanciar un objeto de tabla que se anidará dentro de outerTable que se romperá dentro de la misma página
Aspose.Pdf.Table mytable = new Aspose.Pdf.Table();
mytable.Broken = TableBroken.VerticalInSamePage;
mytable.ColumnAdjustment = ColumnAdjustment.AutoFitToContent;

// Añadir la outerTable a los párrafos de la página
// Añadir mytable a outerTable
page.Paragraphs.Add(outerTable);
var bodyRow = outerTable.Rows.Add();
var bodyCell = bodyRow.Cells.Add();
bodyCell.Paragraphs.Add(mytable);
mytable.RepeatingColumnsCount = 5;
page.Paragraphs.Add(mytable);

// Añadir fila de encabezado
Aspose.Pdf.Row row = mytable.Rows.Add();
row.Cells.Add("encabezado 1");
row.Cells.Add("encabezado 2");
row.Cells.Add("encabezado 3");
row.Cells.Add("encabezado 4");
row.Cells.Add("encabezado 5");
row.Cells.Add("encabezado 6");
row.Cells.Add("encabezado 7");
row.Cells.Add("encabezado 11");
row.Cells.Add("encabezado 12");
row.Cells.Add("encabezado 13");
row.Cells.Add("encabezado 14");
row.Cells.Add("encabezado 15");
row.Cells.Add("encabezado 16");
row.Cells.Add("encabezado 17");

for (int RowCounter = 0; RowCounter <= 5; RowCounter++)

{
    // Crear filas en la tabla y luego celdas en las filas
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
doc.Save(outFile);
```
## Integrar tabla con la fuente del Entity Framework

Más relevante para el .NET moderno es la importación de datos desde frameworks ORM. En este caso, es una buena idea extender la clase Table con métodos de extensión para importar datos desde una lista simple o desde datos agrupados. Vamos a dar un ejemplo para uno de los ORMs más populares - Entity Framework.

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
Los atributos de Anotaciones de Datos se utilizan a menudo para describir modelos y ayudarnos a crear la tabla. Por lo tanto, se eligió el siguiente algoritmo de generación de tablas para ImportEntityList:

- líneas 12-18: construir una fila de encabezado y agregar celdas de encabezado de acuerdo con la regla "Si el atributo DisplayAttribute está presente, entonces tomar su valor, de lo contrario tomar el nombre de la propiedad"
- líneas 50-53: construir las filas de datos y agregar celdas de fila de acuerdo con la regla "Si el atributo DataTypeAttribute está definido, entonces verificamos si necesitamos hacer configuraciones de diseño adicionales para él, y de lo contrario simplemente convertir los datos a cadena y agregar a la celda;"

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
Dado que procesamos grupos, primero generamos una línea para el valor clave (líneas 66-71), y después de eso, las líneas de este grupo.

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
Por supuesto, necesitaría ver el contenido específico del documento que mencionas para poder traducirlo adecuadamente al español, manteniendo el formato markdown original. Por favor, proporciona el texto o el documento que necesitas traducir.
