---
title: Manipular Documento PDF en C#
linktitle: Manipular Documento PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /es/net/manipulate-pdf-document/
description: Este artículo contiene información sobre cómo validar un Documento PDF para el estándar PDF A, cómo trabajar con el TOC, cómo establecer la fecha de caducidad del PDF, etc.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipulate PDF Document in C#",
    "alternativeHeadline": "Enhanced PDF Manipulation Features in C# Library",
    "abstract": "Descubre las poderosas capacidades de manipulación de documentos PDF en C#, incluyendo la validación para estándares PDF/A, la capacidad de crear y personalizar tablas de contenido, y establecer fechas de caducidad para documentos. Esta característica no solo mejora la gestión de documentos, sino que también asegura el cumplimiento de los estándares de la industria, haciéndola esencial para los desarrolladores que buscan soluciones robustas para el manejo de PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "manipulate PDF, C#, validate PDF/A, TOC, set PDF expiry date, flatten fillable PDF, Aspose.PDF, PDF generation progress, customize page numbers, PDF encryption",
    "wordcount": "2651",
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
    "url": "/net/manipulate-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-pdf-document/"
    },
    "dateModified": "2025-04-04",
    "description": "Este artículo contiene información sobre cómo validar un Documento PDF para el estándar PDF A, cómo trabajar con el TOC, cómo establecer la fecha de caducidad del PDF, etc."
}
</script>

## **Manipular Documento PDF en C#**

## Validar Documento PDF para el Estándar PDF A (A 1A y A 1B)

Para validar un documento PDF para la compatibilidad con PDF/A-1a o PDF/A-1b, utiliza el método Validate de la clase [Document](https://reference.aspose.com/pdf/es/net/aspose.pdf/document). Este método te permite especificar el nombre del archivo en el que se guardará el resultado y el tipo de validación requerida de la enumeración [PdfFormat](https://reference.aspose.com/pdf/es/net/aspose.pdf/pdfformat): PDF_A_1A o PDF_A_1B.

{{% alert color="primary" %}}

El formato XML de salida es un formato personalizado de Aspose. El XML contiene una colección de etiquetas con el nombre Problem; cada etiqueta contiene los detalles de un problema particular. El atributo ObjectID de la etiqueta Problem representa el ID del objeto particular al que se relaciona este problema. El atributo Clause representa una regla correspondiente en la especificación PDF.

{{% /alert %}}

El siguiente fragmento de código también trabaja con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

El siguiente fragmento de código te muestra cómo validar un documento PDF para PDF/A-1A.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ValidateToPdfA1aStandard()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ValidatePDFAStandard.pdf"))
    {
        // Validate PDF for PDF/A-1a
        document.Validate(dataDir + "validation-result-A1A.xml", Aspose.Pdf.PdfFormat.PDF_A_1A);
    }
}
```

El siguiente fragmento de código te muestra cómo validar un documento PDF para PDF/A-1b.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ValidateToPdfA1bStandard()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ValidatePDFAStandard.pdf"))
    {
        // Validate PDF for PDF/A-1b
        document.Validate(dataDir + "validation-result-A1B.xml", Aspose.Pdf.PdfFormat.PDF_A_1B);
    }
}
```

{{% alert color="primary" %}}

Aspose.PDF for .NET se puede utilizar para determinar si el documento cargado es un PDF válido y también [si está cifrado o no](https://docs.aspose.com/pdf/net/set-privileges-encrypt-and-decrypt-pdf-file/). Para ampliar aún más las capacidades de la clase Document, se ha añadido la propiedad *IsPdfaCompliant* para determinar si el archivo de entrada es compatible con PDF/A y se ha introducido una propiedad llamada *PdfaFormat* para identificar el formato PDF/A.

{{% /alert %}}

## Trabajando con TOC

### Agregar TOC a un PDF Existente

La API de Aspose.PDF te permite agregar una tabla de contenido ya sea al crear un PDF o a un archivo existente. La clase ListSection en el espacio de nombres Aspose.Pdf.Generator te permite crear una tabla de contenido al crear un PDF desde cero. Para agregar encabezados, que son elementos del TOC, utiliza la clase Aspose.Pdf.Generator.Heading.

Para agregar un TOC a un archivo PDF existente, utiliza la clase Heading en el espacio de nombres Aspose.PDF. El espacio de nombres Aspose.Pdf puede tanto crear nuevos archivos PDF como manipular archivos PDF existentes. El siguiente fragmento de código muestra cómo crear una tabla de contenido dentro de un archivo PDF existente.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTOCToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddTOC.pdf"))
    {
        // Get access to the first page of PDF file
        var tocPage = document.Pages.Insert(1);

        // Create an object to represent TOC information
        var tocInfo = new Aspose.Pdf.TocInfo();
        var title = new Aspose.Pdf.Text.TextFragment("Table Of Contents");
        title.TextState.FontSize = 20;
        title.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Set the title for TOC
        tocInfo.Title = title;
        tocPage.TocInfo = tocInfo;

        // Create string objects which will be used as TOC elements
        string[] titles = { "First page", "Second page", "Third page", "Fourth page" };

        for (int i = 0; i < 2; i++)
        {
            // Create Heading object
            var heading = new Aspose.Pdf.Heading(1);
            var segment = new Aspose.Pdf.Text.TextSegment();
            heading.TocPage = tocPage;
            heading.Segments.Add(segment);

            // Specify the destination page for the heading object
            heading.DestinationPage = document.Pages[i + 2];

            // Destination page
            heading.Top = document.Pages[i + 2].Rect.Height;

            // Destination coordinate
            segment.Text = titles[i];

            // Add heading to the page containing TOC
            tocPage.Paragraphs.Add(heading);
        }

        // Save PDF document
        document.Save(dataDir + "TOC_out.pdf");
    }
}
```

### Establecer diferentes TabLeaderType para diferentes Niveles de TOC

Aspose.PDF también permite establecer diferentes TabLeaderType para diferentes niveles de TOC. Necesitas establecer la propiedad LineDash de FormatArray con el valor apropiado de la enumeración TabLeaderType como sigue.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateTocWithCustomFormatting()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add a TOC page
        var tocPage = document.Pages.Add();

        // Create TOC information
        var tocInfo = new Aspose.Pdf.TocInfo();

        // Set LeaderType
        tocInfo.LineDash = Aspose.Pdf.Text.TabLeaderType.Solid;

        // Set the title for TOC
        var title = new Aspose.Pdf.Text.TextFragment("Table Of Contents");
        title.TextState.FontSize = 30;
        tocInfo.Title = title;

        // Add the TOC section to the document
        tocPage.TocInfo = tocInfo;

        // Define the format of the four levels list by setting the left margins
        // and text format settings of each level
        tocInfo.FormatArrayLength = 4;

        // Level 1
        tocInfo.FormatArray[0].Margin.Left = 0;
        tocInfo.FormatArray[0].Margin.Right = 30;
        tocInfo.FormatArray[0].LineDash = Aspose.Pdf.Text.TabLeaderType.Dot;
        tocInfo.FormatArray[0].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold | Aspose.Pdf.Text.FontStyles.Italic;

        // Level 2
        tocInfo.FormatArray[1].Margin.Left = 10;
        tocInfo.FormatArray[1].Margin.Right = 30;
        tocInfo.FormatArray[1].LineDash = Aspose.Pdf.Text.TabLeaderType.None;
        tocInfo.FormatArray[1].TextState.FontSize = 10;

        // Level 3
        tocInfo.FormatArray[2].Margin.Left = 20;
        tocInfo.FormatArray[2].Margin.Right = 30;
        tocInfo.FormatArray[2].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Level 4
        tocInfo.FormatArray[3].LineDash = Aspose.Pdf.Text.TabLeaderType.Solid;
        tocInfo.FormatArray[3].Margin.Left = 30;
        tocInfo.FormatArray[3].Margin.Right = 30;
        tocInfo.FormatArray[3].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Create a section in the Pdf document
        var page = document.Pages.Add();

        // Add four headings in the section
        for (int level = 1; level <= 4; level++)
        {
            var heading = new Aspose.Pdf.Heading(level);
            var segment = new Aspose.Pdf.Text.TextSegment();
            heading.Segments.Add(segment);
            heading.IsAutoSequence = true;
            heading.TocPage = tocPage;
            segment.Text = "Sample Heading " + level;
            heading.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial Unicode MS");

            // Add the heading into Table Of Contents.
            heading.IsInList = true;
            page.Paragraphs.Add(heading);
        }

        // Save PDF document
        document.Save(dataDir + "TOC_out.pdf");
    }
}
```

### Ocultar Números de Página en el TOC

En caso de que no desees mostrar números de página, junto con los encabezados en el TOC, puedes utilizar la propiedad [IsShowPageNumbers](https://reference.aspose.com/pdf/es/net/aspose.pdf/tocinfo/properties/isshowpagenumbers) de la clase [TOCInfo](https://reference.aspose.com/pdf/es/net/aspose.pdf/tocinfo) como falsa. Por favor, revisa el siguiente fragmento de código para ocultar números de página en la tabla de contenido:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateTocWithHiddenPageNumbers()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add a TOC page
        var tocPage = document.Pages.Add();

        // Create TOC information
        var tocInfo = new Aspose.Pdf.TocInfo();

        // Set the title for TOC
        var title = new Aspose.Pdf.Text.TextFragment("Table Of Contents");
        title.TextState.FontSize = 20;
        title.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
        tocInfo.Title = title;

        // Add the TOC section to the document
        tocPage.TocInfo = tocInfo;

        // Hide page numbers in TOC
        tocInfo.IsShowPageNumbers = false;

        // Define the format of the four levels list by setting the left margins and
        // text format settings of each level
        tocInfo.FormatArrayLength = 4;

        // Level 1
        tocInfo.FormatArray[0].Margin.Right = 0;
        tocInfo.FormatArray[0].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold | Aspose.Pdf.Text.FontStyles.Italic;

        // Level 2
        tocInfo.FormatArray[1].Margin.Left = 30;
        tocInfo.FormatArray[1].TextState.Underline = true;
        tocInfo.FormatArray[1].TextState.FontSize = 10;

        // Level 3
        tocInfo.FormatArray[2].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Level 4
        tocInfo.FormatArray[3].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Create a section in the Pdf document
        var page = document.Pages.Add();

        // Add four headings in the section
        for (int level = 1; level <= 4; level++)
        {
            var heading = new Aspose.Pdf.Heading(level);
            var segment = new Aspose.Pdf.Text.TextSegment();
            heading.TocPage = tocPage;
            heading.Segments.Add(segment);
            heading.IsAutoSequence = true;
            segment.Text = "this is heading of level " + level;
            heading.IsInList = true;
            page.Paragraphs.Add(heading);
        }

        // Save PDF document
        document.Save(dataDir + "TOC_out.pdf");
    }
}
```

### Personalizar Números de Página al agregar TOC

Es común personalizar la numeración de páginas en el TOC al agregar TOC en un documento PDF. Por ejemplo, puede que necesitemos agregar algún prefijo antes del número de página como P1, P2, P3, etc. En tal caso, Aspose.PDF for .NET proporciona la propiedad PageNumbersPrefix de la clase TocInfo que se puede utilizar para personalizar los números de página como se muestra en el siguiente ejemplo de código.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomizePageNumbersAddingToC()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CustomizePageNumbersAddingToC.pdf"))
    {
        // Get access to first page of PDF file
        Page tocPage = document.Pages.Insert(1);

        // Create object to represent TOC information
        var tocInfo = new Aspose.Pdf.TocInfo();
        var title = new Aspose.Pdf.Text.TextFragment("Table Of Contents");
        title.TextState.FontSize = 20;
        title.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Set the title for TOC
        tocInfo.Title = title;
        tocInfo.PageNumbersPrefix = "P";
        tocPage.TocInfo = tocInfo;

        // Loop through the pages to create TOC entries
        for (int i = 1; i < document.Pages.Count; i++)
        {
            // Create Heading object
            var heading2 = new Aspose.Pdf.Heading(1);
            var segment2 = new Aspose.Pdf.Text.TextSegment();
            heading2.TocPage = tocPage;
            heading2.Segments.Add(segment2);

            // Specify the destination page for heading object
            heading2.DestinationPage = document.Pages[i + 1];

            // Destination page
            heading2.Top = document.Pages[i + 1].Rect.Height;

            // Destination coordinate
            segment2.Text = "Page " + i.ToString();

            // Add heading to page containing TOC
            tocPage.Paragraphs.Add(heading2);
        }

        // Save PDF document
        document.Save(dataDir + "CustomizePageNumbersAddingToC_out.pdf");
    }
}
```

## Cómo establecer la fecha de caducidad del PDF

Aplicamos privilegios de acceso en archivos PDF para que un cierto grupo de usuarios pueda acceder a características/objetos particulares de los documentos PDF. Para restringir el acceso al archivo PDF, generalmente aplicamos cifrado y podemos tener la necesidad de establecer la caducidad del archivo PDF, de modo que el usuario que accede/visualiza el documento reciba un aviso válido sobre la caducidad del archivo PDF.

Para lograr el requisito mencionado anteriormente, podemos utilizar el objeto *JavascriptAction*. Por favor, echa un vistazo al siguiente fragmento de código.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetExpiryDate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Add text fragment to paragraphs collection of page object
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World..."));

        // Create JavaScript object to set PDF expiry date
        var javaScript = new Aspose.Pdf.Annotations.JavascriptAction(
            "var year=2017;" +
            "var month=5;" +
            "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());" +
            "expiry = new Date(year, month);" +
            "if (today.getTime() > expiry.getTime())" +
            "app.alert('The file is expired. You need a new one.');"
        );

        // Set JavaScript as PDF open action
        document.OpenAction = javaScript;

        // Save PDF Document
        document.Save(dataDir + "SetExpiryDate_out.pdf");
    }
}
```

## Determinar el Progreso de la Generación del Archivo PDF

Un cliente nos pidió que agregáramos una función que permita a los desarrolladores determinar el progreso de la generación del archivo PDF. Aquí está la respuesta a esa solicitud.

El campo [CustomerProgressHandler](https://reference.aspose.com/pdf/es/net/aspose.pdf/docsaveoptions/fields/customprogresshandler) de la clase [DocSaveOptions](https://reference.aspose.com/pdf/es/net/aspose.pdf/docsaveoptions) permite determinar cómo va la generación del PDF. El controlador tiene los siguientes tipos:

- DocSaveOptions.ConversionProgessEventHandler.
- DocSaveOptions.ProgressEventHandlerInfo.
- DocSaveOptions.ProgressEventType.

Los fragmentos de código a continuación muestran cómo usar CustomerProgressHandler.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DetermineProgress()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddTOC.pdf"))
    {
        // Create DocSaveOptions instance and set custom progress handler
        var saveOptions = new Aspose.Pdf.DocSaveOptions();
        saveOptions.CustomProgressHandler = new Aspose.Pdf.UnifiedSaveOptions.ConversionProgressEventHandler(ShowProgressOnConsole);

        // Save PDF Document
        document.Save(dataDir + "DetermineProgress_out.pdf", saveOptions);
    }
}

// Method to handle progress and display it on the console
private static void ShowProgressOnConsole(Aspose.Pdf.UnifiedSaveOptions.ProgressEventHandlerInfo eventInfo)
{
    switch (eventInfo.EventType)
    {
        case Aspose.Pdf.ProgressEventType.TotalProgress:
            Console.WriteLine(String.Format("{0}  - Conversion progress : {1}% .", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString()));
            break;
        case Aspose.Pdf.ProgressEventType.SourcePageAnalysed:
            Console.WriteLine(String.Format("{0}  - Source page {1} of {2} analyzed.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case Aspose.Pdf.ProgressEventType.ResultPageCreated:
            Console.WriteLine(String.Format("{0}  - Result page's {1} of {2} layout created.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case Aspose.Pdf.ProgressEventType.ResultPageSaved:
            Console.WriteLine(String.Format("{0}  - Result page {1} of {2} exported.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        default:
            break;
    }
}
```

## Aplanar PDF Rellenable

Los documentos PDF a menudo incluyen formularios con widgets interactivos rellenables como botones de opción, casillas de verificación, cuadros de texto, listas, etc. Para hacer que no se pueda editar para varios propósitos de aplicación, necesitamos aplanar el archivo PDF. Aspose.PDF proporciona la función para aplanar tu PDF en C# con solo unas pocas líneas de código:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenForms()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Flatten Fillable PDF
        if (document.Form.Fields.Count() > 0)
        {
            foreach (var item in document.Form.Fields)
            {
                item.Flatten();
            }
        }

        // Save PDF document
        document.Save(dataDir + "FlattenForms_out.pdf");
    }
}
```

## Analizando el documento PDF para Actualizaciones Incrementales
Para verificar si un documento ha sido actualizado de manera incremental, utiliza el método `HasIncrementalUpdate` de la clase [Document](https://reference.aspose.com/pdf/es/net/aspose.pdf/document). Este método analiza el archivo PDF y devuelve un valor booleano que indica si se detectaron actualizaciones incrementales. Ten en cuenta que cuando un documento se guarda utilizando el método [Save](https://reference.aspose.com/pdf/es/net/aspose.pdf/document/save/#save) sin parámetros, se guarda de manera incremental.

El siguiente código C# demuestra cómo usar el método `HasIncrementalUpdate`:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IncrementalUpdatesCheck()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Check for incremental updates
        bool updatedIncrementally = document.HasIncrementalUpdate();

        // Output the result
        if (updatedIncrementally)
        {
            Console.WriteLine("This document has been incrementally updated.");
        }
        else
        {
            Console.WriteLine("This document has no incremental updates.");
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IncrementalUpdatesCheck()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Check for incremental updates
    bool updatedIncrementally = document.HasIncrementalUpdate();

    // Output the result
    if (updatedIncrementally)
    {
        Console.WriteLine("This document has been incrementally updated.");
    }
    else
    {
        Console.WriteLine("This document has no incremental updates.");
    }
}
```
{{< /tab >}}
{{< /tabs >}}

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