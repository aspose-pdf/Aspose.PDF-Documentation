---
title: Convertir PDF a Excel en .NET
linktitle: Convertir PDF a Excel
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /es/net/convert-pdf-to-excel/
lastmod: "2021-11-01"
description: La biblioteca Aspose.PDF for .NET permite convertir PDF a formato Excel utilizando C#. Estos formatos incluyen XLS, XLSX, XML 2003 Spreadsheet, CSV, ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to Excel in .NET",
    "alternativeHeadline": "Convert PDF Files to Excel Formats with C#",
    "abstract": "Descubre la poderosa capacidad de Aspose.PDF for .NET para convertir documentos PDF en varios formatos de Excel, incluyendo XLS, XLSX, CSV y ODS, utilizando C#. Esta función no solo permite la transformación de páginas individuales de PDF en hojas de Excel separadas, sino que también ofrece opciones para hojas combinadas, proporcionando flexibilidad a los usuarios para gestionar sus datos PDF de manera eficiente.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1780",
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
    "url": "/net/convert-pdf-to-excel/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-excel/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también hacer frente a objetivos más complejos. Consulta la siguiente sección para usuarios avanzados y desarrolladores."
}
</script>

## Resumen

Este artículo explica cómo **convertir PDF a formatos Excel utilizando C#**. Cubre los siguientes temas.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

_Formato_: **XLS**

- [C# PDF a XLS](#csharp-pdf-to-xls)
- [C# Convertir PDF a XLS](#csharp-pdf-to-xls)
- [C# Cómo convertir archivo PDF a XLS](#csharp-pdf-to-xls)

_Formato_: **XLSX**

- [C# PDF a XLSX](#csharp-pdf-to-xlsx)
- [C# Convertir PDF a XLSX](#csharp-pdf-to-xlsx)
- [C# Cómo convertir archivo PDF a XLSX](#csharp-pdf-to-xlsx)

_Formato_: **Excel**

- [C# PDF a Excel](#csharp-pdf-to-xlsx)
- [C# PDF a Excel XLS](#csharp-pdf-to-xls)
- [C# PDF a Excel XLSX](#csharp-pdf-to-xlsx)

_Formato_: **Hoja de Excel única**

- [C# Convertir PDF a XLS teniendo una sola hoja](#csharp-pdf-to-excel-single)
- [C# Convertir PDF a XLSX teniendo una sola hoja](#csharp-pdf-to-excel-single)

_Formato_: **Formato de hoja de cálculo XML 2003**

- [C# PDF a XML Excel](#csharp-pdf-to-excel-xml-2003)
- [C# Convertir PDF a hoja de cálculo XML Excel](#csharp-pdf-to-excel-xml-2003)

_Formato_: **CSV**

- [C# PDF a CSV](#csharp-pdf-to-csv)
- [C# Convertir PDF a CSV](#csharp-pdf-to-csv)
- [C# Cómo convertir archivo PDF a CSV](#csharp-pdf-to-csv)

_Formato_: **ODS**

- [C# PDF a ODS](#csharp-pdf-to-ods)
- [C# Convertir PDF a ODS](#csharp-pdf-to-ods)
- [C# Cómo convertir archivo PDF a ODS](#csharp-pdf-to-ods)

## Conversiones de C# PDF a Excel

**Aspose.PDF for .NET** admite la función de convertir archivos PDF a formatos Excel 2007, CSV y SpeadsheetML.

Aspose.PDF for .NET es un componente de manipulación de PDF, hemos introducido una función que renderiza el archivo PDF a un libro de Excel (archivos XLSX). Durante esta conversión, las páginas individuales del archivo PDF se convierten en hojas de Excel.

{{% alert color="success" %}}
**Intenta convertir PDF a Excel en línea**

Aspose.PDF for .NET te presenta una aplicación gratuita en línea ["PDF a XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), donde puedes investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión PDF a Excel con aplicación gratuita](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Para convertir archivos PDF a formato <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr>, Aspose.PDF tiene una clase llamada [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions). Un objeto de la clase ExcelSaveOptions se pasa como segundo argumento al constructor Document.Save(..).

El siguiente fragmento de código muestra el proceso para convertir un archivo PDF en formato XLS o XLSX con Aspose.PDF for .NET.

<a name="csharp-pdf-to-xls"><strong>Pasos: Convertir PDF a XLS en C#</strong></a>

1. Crea una instancia del objeto **Document** con el documento PDF de origen.
2. Crea una instancia de **ExcelSaveOptions**.
3. Guárdalo en formato **XLS** especificando la **extensión .xls** llamando al método **Document.Save()** y pasándole **ExcelSaveOptions**.

<a name="csharp-pdf-to-xlsx"><strong>Pasos: Convertir PDF a XLSX en C#</strong></a>

1. Crea una instancia del objeto **Document** con el documento PDF de origen.
2. Crea una instancia de **ExcelSaveOptions**.
3. Guárdalo en formato **XLSX** especificando la **extensión .xlsx** llamando al método **Document.Save()** y pasándole **ExcelSaveOptions**.

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertPDFtoExcel()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
     {
         // Instantiate ExcelSaveOptions object
         var saveOptions = new Aspose.Pdf.ExcelSaveOptions();

         // Save the file in XLSX format
         document.Save(dataDir + "PDFToXLS_out.xlsx", saveOptions);
     }
 }
```

## Convertir PDF a XLS con Control de Columna

Al convertir un PDF a formato XLS, se agrega una columna en blanco al archivo de salida como primera columna. La opción InsertBlankColumnAtFirst de la clase ExcelSaveOptions se utiliza para controlar esta columna. El valor predeterminado es `false`, lo que significa que no se insertarán columnas en blanco.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            InsertBlankColumnAtFirst = false
        };

        // Save the file in XLSX format
        document.Save(dataDir + "PDFToXLS_out.xlsx", saveOptions);
    }
}
```

## Convertir PDF a Hoja de Excel Única

Al exportar un archivo PDF con muchas páginas a XLS, cada página se exporta a una hoja diferente en el archivo de Excel. Esto se debe a que la propiedad MinimizeTheNumberOfWorksheets está configurada en false de forma predeterminada. Para asegurarte de que todas las páginas se exporten a una sola hoja en el archivo Excel de salida, establece la propiedad MinimizeTheNumberOfWorksheets en true.

<a name="csharp-pdf-to-excel-single"><strong>Pasos: Convertir PDF a XLS o XLSX Hoja Única en C#</strong></a>

1. Crea una instancia del objeto **Document** con el documento PDF de origen.
2. Crea una instancia de **ExcelSaveOptions** con **MinimizeTheNumberOfWorksheets = true**.
3. Guárdalo en formato **XLS** o **XLSX** teniendo una sola hoja llamando al método **Document.Save()** y pasándole **ExcelSaveOptions**.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            MinimizeTheNumberOfWorksheets = true
        };

        // Save the file in XLSX format
        document.Save(dataDir + "PDFToXLS_out.xlsx", saveOptions);
    }
}
```

## Convertir a otros formatos de hoja de cálculo

### Convertir a formato XML Spreadsheet 2003

Desde la versión 20.8, Aspose.PDF utiliza el formato de archivo Microsoft Excel Open XML Spreadsheet 2007 como predeterminado para almacenar datos. Para convertir archivos PDF a formato XML Spreadsheet 2003, Aspose.PDF tiene una clase llamada [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) con [Format](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions/properties/format). Un objeto de la clase [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) se pasa como segundo argumento al método [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index).

El siguiente fragmento de código muestra el proceso para convertir un archivo PDF en formato XLS Excel 2003 XML.

<a name="csharp-pdf-to-excel-xml-2003"><strong>Pasos: Convertir PDF a Excel 2003 XML Formato en C#</strong></a>

1. Crea una instancia del objeto **Document** con el documento PDF de origen.
2. Crea una instancia de **ExcelSaveOptions** con **Format = ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003**.
3. Guárdalo en formato **XLS - Formato XML Excel 2003** llamando al método **Document.Save()** y pasándole **ExcelSaveOptions**.

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertPDFtoExcelAdvanced_SaveXLS2003()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
     {
         // Instantiate ExcelSaveOptions object
         var saveOptions = new Aspose.Pdf.ExcelSaveOptions
         {
             Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
         };

         // Save the file in XLS format
         document.Save(dataDir + "PDFToXLS_out.xls", saveOptions);
     }
 }
```

### Convertir a CSV

La conversión a formato CSV se realiza de la misma manera que la anterior. Todo lo que necesitas es establecer el formato apropiado.

<a name="csharp-pdf-to-csv"><strong>Pasos: Convertir PDF a CSV en C#</strong></a>

1. Crea una instancia del objeto **Document** con el documento PDF de origen.
2. Crea una instancia de **ExcelSaveOptions** con **Format = ExcelSaveOptions.ExcelFormat.CSV**.
3. Guárdalo en formato **CSV** llamando al método **Document.Save()** y pasándole **ExcelSaveOptions**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToCSV()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.CSV
        };
        
        // Save the file in CSV format
        document.Save(dataDir + "PDFToXLS_out.csv", saveOptions);
    }
}
```

### Convertir a ODS

<a name="csharp-pdf-to-ods"><strong>Pasos: Convertir PDF a ODS en C#</strong></a>

1. Crea una instancia del objeto **Document** con el documento PDF de origen.
2. Crea una instancia de **ExcelSaveOptions** con **Format = ExcelSaveOptions.ExcelFormat.ODS**.
3. Guárdalo en formato **ODS** llamando al método **Document.Save()** y pasándole **ExcelSaveOptions**.

La conversión a formato ODS se realiza de la misma manera que todos los otros formatos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToODS()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.ODS
        };

        // Save the file in ODS format
        document.Save(dataDir + "PDFToODS_out.ods", saveOptions);
    }
}
```

## Ver También 

Este artículo también cubre estos temas. Los códigos son los mismos que los anteriores.

_Formato_: **Excel**
- [C# PDF a Código Excel](#csharp-pdf-to-xlsx)
- [C# PDF a API Excel](#csharp-pdf-to-xlsx)
- [C# PDF a Excel Programáticamente](#csharp-pdf-to-xlsx)
- [C# PDF a Biblioteca Excel](#csharp-pdf-to-xlsx)
- [C# Guardar PDF como Excel](#csharp-pdf-to-xlsx)
- [C# Generar Excel desde PDF](#csharp-pdf-to-xlsx)
- [C# Crear Excel desde PDF](#csharp-pdf-to-xlsx)
- [C# PDF a Convertidor Excel](#csharp-pdf-to-xlsx)

_Formato_: **XLS**
- [C# PDF a Código XLS](#csharp-pdf-to-xls)
- [C# PDF a API XLS](#csharp-pdf-to-xls)
- [C# PDF a XLS Programáticamente](#csharp-pdf-to-xls)
- [C# PDF a Biblioteca XLS](#csharp-pdf-to-xls)
- [C# Guardar PDF como XLS](#csharp-pdf-to-xls)
- [C# Generar XLS desde PDF](#csharp-pdf-to-xls)
- [C# Crear XLS desde PDF](#csharp-pdf-to-xls)
- [C# PDF a Convertidor XLS](#csharp-pdf-to-xls)

_Formato_: **XLSX**
- [C# PDF a Código XLSX](#csharp-pdf-to-xlsx)
- [C# PDF a API XLSX](#csharp-pdf-to-xlsx)
- [C# PDF a XLSX Programáticamente](#csharp-pdf-to-xlsx)
- [C# PDF a Biblioteca XLSX](#csharp-pdf-to-xlsx)
- [C# Guardar PDF como XLSX](#csharp-pdf-to-xlsx)
- [C# Generar XLSX desde PDF](#csharp-pdf-to-xlsx)
- [C# Crear XLSX desde PDF](#csharp-pdf-to-xlsx)
- [C# PDF a Convertidor XLSX](#csharp-pdf-to-xlsx)

_Formato_: **CSV**
- [C# PDF a Código CSV](#csharp-pdf-to-csv)
- [C# PDF a API CSV](#csharp-pdf-to-csv)
- [C# PDF a CSV Programáticamente](#csharp-pdf-to-csv)
- [C# PDF a Biblioteca CSV](#csharp-pdf-to-csv)
- [C# Guardar PDF como CSV](#csharp-pdf-to-csv)
- [C# Generar CSV desde PDF](#csharp-pdf-to-csv)
- [C# Crear CSV desde PDF](#csharp-pdf-to-csv)
- [C# PDF a Convertidor CSV](#csharp-pdf-to-csv)

_Formato_: **ODS**
- [C# PDF a Código ODS](#csharp-pdf-to-ods)
- [C# PDF a API ODS](#csharp-pdf-to-ods)
- [C# PDF a ODS Programáticamente](#csharp-pdf-to-ods)
- [C# PDF a Biblioteca ODS](#csharp-pdf-to-ods)
- [C# Guardar PDF como ODS](#csharp-pdf-to-ods)
- [C# Generar ODS desde PDF](#csharp-pdf-to-ods)
- [C# Crear ODS desde PDF](#csharp-pdf-to-ods)
- [C# PDF a Convertidor ODS](#csharp-pdf-to-ods)