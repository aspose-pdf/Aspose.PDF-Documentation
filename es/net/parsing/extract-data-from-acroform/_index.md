---
title: Extraer datos de AcroForm usando C#
linktitle: Extraer datos de AcroForm
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /es/net/extract-data-from-acroform/
description: Aspose.PDF facilita la extracción de datos de campos de formulario de archivos PDF. Aprenda cómo extraer datos de AcroForms y guardarlos en formato JSON, XML o FDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Data from AcroForm using C#",
    "alternativeHeadline": "Effortlessly Extract Acrobat Form Data with C#",
    "abstract": "Descubra la nueva funcionalidad en Aspose.PDF for .NET que simplifica la extracción de datos de campos de formulario de AcroForms en documentos PDF. Con la capacidad de exportar datos a formatos JSON, XML, FDF y XFDF, los usuarios pueden gestionar eficientemente los datos del formulario mientras aprovechan ejemplos de código concisos para una integración sin problemas en aplicaciones",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "826",
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
    "url": "/net/extract-data-from-acroform/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-data-from-acroform/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulte la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Extraer campos de formulario de un documento PDF

Además de permitirle generar campos de formulario y completar campos de formulario, Aspose.PDF for .NET facilita la extracción de datos de campos de formulario o información sobre campos de formulario de archivos PDF.

En el código de muestra a continuación, demostramos cómo iterar a través de cada página en un PDF para extraer información sobre todo el AcroForm en el PDF, así como los valores de los campos de formulario. Este código de muestra presume que no conoce el nombre de los campos de formulario de antemano.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractFormFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "StudentInfoFormElectronic.pdf"))
    {
        // Get values from all fields
        foreach (Aspose.Pdf.Forms.Field formField in document.Form)
        {
            Console.WriteLine("Field Name : {0} ", formField.PartialName);
            Console.WriteLine("Value : {0} ", formField.Value);
        }
    }
}
```

Si conoce el nombre de los campos de formulario de los que desea extraer valores, puede usar el indexador en la colección Documents.Form para recuperar rápidamente estos datos. Mire al final de este artículo para un código de muestra sobre cómo usar esa función.

## Recuperar el valor del campo de formulario por título

La propiedad Value del campo de formulario le permite obtener el valor de un campo particular. Para obtener el valor, obtenga el campo de formulario de la colección Form del objeto Document. Este ejemplo selecciona un TextBoxField y recupera su valor utilizando la propiedad Value.

## Extraer campos de formulario de un documento PDF a JSON

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractFormFieldsToJson()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "StudentInfoFormElectronic.pdf"))
    {
        // Extract form fields and convert to JSON
        var formData = document.Form.Cast<Aspose.Pdf.Forms.Field>().Select(f => new { Name = f.PartialName, f.Value });
        string jsonString = System.Text.Json.JsonSerializer.Serialize(formData);

        // Output the JSON string
        Console.WriteLine(jsonString);
    }
}
```

## Extraer datos a XML desde un archivo PDF

La clase Form le permite exportar datos a un archivo XML desde el archivo PDF utilizando el método ExportXml. Para exportar datos a XML, necesita crear un objeto de la clase Form y luego llamar al método ExportXml utilizando el objeto FileStream. Finalmente, puede cerrar el objeto FileStream y liberar el objeto Form. El siguiente fragmento de código le muestra cómo exportar datos a un archivo XML.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportFormDataToXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Create form
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Create XML file
        using (var xmlOutputStream = new FileStream(dataDir + "input.xml", FileMode.Create))
        {
            // Export data
            form.ExportXml(xmlOutputStream);
        }
    }
}
```

## Exportar datos a FDF desde un archivo PDF

La clase Form le permite exportar datos a un archivo FDF desde el archivo PDF utilizando el método ExportFdf. Para exportar datos a FDF, necesita crear un objeto de la clase Form y luego llamar al método ExportFdf utilizando el objeto FileStream. Finalmente, puede guardar el archivo PDF utilizando el método Save de la clase Form. El siguiente fragmento de código le muestra cómo exportar datos a un archivo FDF.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Create form
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Create fdf file
        using (var fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create))
        {
            // Export data
            form.ExportFdf(fdfOutputStream);
        }

        // Save PDF document
        form.Save(dataDir + "ExportDataToPdf_out.pdf");
    }
}
```

## Exportar datos a XFDF desde un archivo PDF

La clase Form le permite exportar datos a un archivo XFDF desde el archivo PDF utilizando el método ExportXfdf. Para exportar datos a XFDF, necesita crear un objeto de la clase Form y luego llamar al método ExportXfdf utilizando el objeto FileStream. Finalmente, puede guardar el archivo PDF utilizando el método Save de la clase Form. El siguiente fragmento de código le muestra cómo exportar datos a un archivo XFDF.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToXFDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Create form
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Create xfdf file
        using (var xfdfOutputStream = new FileStream(dataDir + "student1.xfdf", FileMode.Create))
        {
            // Export data
            form.ExportXfdf(xfdfOutputStream);
        }

        // Save PDF document
        form.Save(dataDir + "ExportDataToXFDF_out.pdf");
    }
}
```