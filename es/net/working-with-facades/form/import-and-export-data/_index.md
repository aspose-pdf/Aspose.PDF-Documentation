---
title: Importar y Exportar Datos
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /es/net/import-and-export-data/
description: Esta sección explica cómo importar y exportar datos con Aspose.PDF Facades utilizando la clase Form.
lastmod: "2024-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Data",
    "alternativeHeadline": "Effortless Data Import and Export for PDF Forms",
    "abstract": "La función de Importar y Exportar Datos en Aspose.PDF for .NET permite la integración fluida de la gestión de datos de documentos al habilitar a los usuarios para importar y exportar datos de formularios PDF utilizando formatos XML, FDF, XFDF y JSON. Esta funcionalidad mejora las capacidades de manejo de datos, facilitando la automatización de flujos de trabajo y el mantenimiento de registros precisos directamente desde documentos PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1085",
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
    "url": "/net/import-and-export-data/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-and-export-data/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios avanzados y desarrolladores."
}
</script>

La clase [Form](https://reference.aspose.com/pdf/es/net/aspose.pdf.forms/form) permite importar datos de un archivo XML al archivo PDF utilizando el método [ImportXml](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.form/importxml/methods/1). Para importar datos de XML, necesitas crear un objeto de la clase [Form](https://reference.aspose.com/pdf/es/net/aspose.pdf.forms/form) y luego llamar al método [ImportXml](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form/methods/importxml/index) utilizando el objeto FileStream. Finalmente, puedes guardar el archivo PDF utilizando el método [Save](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor/methods/save) de la clase [Form](https://reference.aspose.com/pdf/es/net/aspose.pdf.forms/form). El siguiente fragmento de código te muestra cómo importar datos de un archivo XML.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportDataFromXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Open xml file
        using (var xmlInputStream = new FileStream(dataDir + "input.xml", FileMode.Open))
        {
            // Import data
            pdfForm.ImportXml(xmlInputStream);           

            // Save PDF document
            pdfForm.Save(dataDir + "ImportDataFromXML_out.pdf");
        }
    }
}
```

## Exportar Datos a XML desde un Archivo PDF

La clase [Form](https://reference.aspose.com/pdf/es/net/aspose.pdf.forms/form) permite exportar datos a un archivo XML desde el archivo PDF utilizando el método [ExportXml](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form/methods/exportxml). Para exportar datos a XML, necesitas crear un objeto de la clase [Form](https://reference.aspose.com/pdf/es/net/aspose.pdf.forms/form) y luego llamar al método [ExportXml](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form/methods/exportxml) utilizando el objeto FileStream. Finalmente, puedes cerrar el objeto FileStream y liberar el objeto Form. El siguiente fragmento de código te muestra cómo exportar datos a un archivo XML.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Create XML file
        using (var xmlOutputStream = new FileStream(dataDir + "input.xml", FileMode.Create))
        {
            // Export data
            pdfForm.ExportXml(xmlOutputStream);
        }
    }
}
```

## Importar Datos de FDF a un Archivo PDF

La clase [Form](https://reference.aspose.com/pdf/es/net/aspose.pdf.forms/form) permite importar datos de un archivo FDF al archivo PDF utilizando el método [ImportFdf](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form/methods/importfdf). Para importar datos de FDF, necesitas crear un objeto de la clase [Form](https://reference.aspose.com/pdf/es/net/aspose.pdf.forms/form) y luego llamar al método [ImportFdf](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form/methods/importfdf) utilizando el objeto FileStream. Finalmente, puedes guardar el archivo PDF utilizando el método [Save](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor/methods/save) de la clase [Form](https://reference.aspose.com/pdf/es/net/aspose.pdf.forms/form). El siguiente fragmento de código te muestra cómo importar datos de un archivo FDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportDataFromPdfIntoPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");
        
        // Open FDF file
        using (var fdfInputStream = new FileStream(dataDir + "student.fdf", FileMode.Open))
        {
            // Import data
            pdfForm.ImportFdf(fdfInputStream);         

            // Save PDF document
            pdfForm.Save(dataDir + "ImportDataFromPdf_out.pdf");
        }
    }
}
```

## Exportar Datos a FDF desde un Archivo PDF

La clase [Form](https://reference.aspose.com/pdf/es/net/aspose.pdf.forms/form) permite exportar datos a un archivo FDF desde el archivo PDF utilizando el método [ExportFdf](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form/methods/exportfdf). Para exportar datos a FDF, necesitas crear un objeto de la clase [Form](https://reference.aspose.com/pdf/es/net/aspose.pdf.forms/form) y luego llamar al método [ExportFdf](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form/methods/exportfdf) utilizando el objeto FileStream. Finalmente, puedes guardar el archivo PDF utilizando el método [Save](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor/methods/save) de la clase [Form](https://reference.aspose.com/pdf/es/net/aspose.pdf.forms/form). El siguiente fragmento de código te muestra cómo exportar datos a un archivo FDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToPdfFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Create FDF file
        using (var fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create))
        {
            // Export data
            pdfForm.ExportFdf(fdfOutputStream);           

            // Save PDF document
            pdfForm.Save(dataDir + "ExportDataToPdf_out.pdf"); 
        }
    }
}
```

## Importar Datos de XFDF a un Archivo PDF

La clase [Form](https://reference.aspose.com/pdf/es/net/aspose.pdf.forms/form) permite importar datos de un archivo XFDF al archivo PDF utilizando el método [ImportXfdf](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form/methods/importxfdf). Para importar datos de XFDF, necesitas crear un objeto de la clase [Form](https://reference.aspose.com/pdf/es/net/aspose.pdf.forms/form) y luego llamar al método [ImportXfdf](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form/methods/importxfdf) utilizando el objeto FileStream. Finalmente, puedes guardar el archivo PDF utilizando el método [Save](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor/methods/save) de la clase [Form](https://reference.aspose.com/pdf/es/net/aspose.pdf.forms/form). El siguiente fragmento de código te muestra cómo importar datos de un archivo XFDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportDataFromXFDIntoPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Open XFDF file
        using (var xfdfInputStream = new FileStream(dataDir + "test2.xfdf", FileMode.Open))
        {
            // Import data
            pdfForm.ImportXfdf(xfdfInputStream);           

            // Save PDF document
            pdfForm.Save(dataDir + "ImportDataFromXFDF_out.pdf");
        }
    }
}
```

## Exportar Datos a XFDF desde un Archivo PDF

La clase [Form](https://reference.aspose.com/pdf/es/net/aspose.pdf.forms/form) permite exportar datos a un archivo XFDF desde el archivo PDF utilizando el método [ExportXfdf](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form/methods/exportxfdf). Para exportar datos a XFDF, necesitas crear un objeto de la clase [Form](https://reference.aspose.com/pdf/es/net/aspose.pdf.forms/form) y luego llamar al método [ExportXfdf](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form/methods/exportxfdf) utilizando el objeto FileStream. Finalmente, puedes guardar el archivo PDF utilizando el método [Save](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor/methods/save) de la clase [Form](https://reference.aspose.com/pdf/es/net/aspose.pdf.forms/form). El siguiente fragmento de código te muestra cómo exportar datos a un archivo XFDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToXFDFFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Create XFDF file
        using (var xfdfOutputStream = new FileStream(dataDir + "out.xfdf", FileMode.Create))
        {
            // Export data
            pdfForm.ExportXfdf(xfdfOutputStream);

            // Save PDF document
            pdfForm.Save(dataDir + "ExportDataToXFDF_out.pdf");
        }
    }
}
```

## Exportar valores de campos a un archivo JSON

Aspose.Pdf.Facades proporciona una API alternativa para trabajar con campos de formularios. Este fragmento demuestra cómo exportar e importar valores de campos utilizando esta API.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportValuesFromFieldsToJSON()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();
    
    using (var form = new Aspose.Pdf.Facades.Form())
    {       
        // Bind PDF document
        form.BindPdf(dataDir + "Test2.pdf");

        // Create JSON file
        using (FileStream jsonStream = new FileStream(dataDir + "Test2.json", FileMode.Create))
        {
            // Export data
            form.ExportJson(jsonStream);
        }
    }
}
```

## Importar valores a campos desde el archivo JSON

Este fragmento de código demuestra cómo importar valores en los campos de un documento PDF desde un archivo JSON utilizando la API Aspose.Pdf.Facades. Se utiliza FileStream para manejar el archivo JSON.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportValuesFromJsonToForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form())
    {        
        // Bind PDF document
        form.BindPdf(dataDir + "Test2.pdf");

        // Import from JSON file
        using (FileStream jsonStream = new FileStream(dataDir + "Test2.json", FileMode.Open))
        {
            // Export data
            form.ImportJson(jsonStream);
        }
    }
}
```