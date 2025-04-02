---
title: Gestionar Encabezado y Pie de Página
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /es/net/manage-header-and-footer/
description: Explora cómo manipular encabezados y pies de página en archivos PDF en .NET con Aspose.PDF para mejorar la estructuración de documentos.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manage Header and Footer",
    "alternativeHeadline": "Enhance PDFs with Custom Headers and Footers",
    "abstract": "Las funciones de Gestionar Encabezado y Pie de Página en Aspose.PDF for .NET permiten a los usuarios agregar, personalizar y formatear fácilmente tanto encabezados como pies de página en documentos PDF utilizando la clase PdfFileStamp. Esta funcionalidad admite la inclusión de texto e imágenes, proporcionando flexibilidad en la presentación del documento mientras asegura un formato profesional. Los usuarios pueden integrar sin problemas esta función en sus aplicaciones para mejorar el atractivo visual y la organización de los archivos PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1007",
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
    "url": "/net/manage-header-and-footer/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manage-header-and-footer/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Agregar Encabezado en un Archivo PDF

La clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp/constructors/main) te permite agregar un encabezado en un archivo PDF. Para agregar un encabezado, primero necesitas crear un objeto de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp/constructors/main). Puedes formatear el texto del encabezado utilizando la clase [FormattedText](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formattedtext). Una vez que estés listo para agregar el encabezado en el archivo, necesitas llamar al método [AddHeader](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp/constructors/main). También necesitas especificar al menos el margen superior en el método [AddHeader](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4). Finalmente, guarda el archivo PDF de salida utilizando el método [Close](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/facade/methods/close) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp/constructors/main). El siguiente fragmento de código te muestra cómo agregar un encabezado en un archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHeader()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create formatted text for the header
        var formattedText = new Aspose.Pdf.Facades.FormattedText(
            "Aspose - Your File Format Experts!",
            System.Drawing.Color.Yellow,
            System.Drawing.Color.Black,
            Aspose.Pdf.Facades.FontStyle.Courier,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false,
            14);

        // Add header
        fileStamp.AddHeader(formattedText, 10);

        // Save PDF document
        fileStamp.Save(dataDir + "AddHeader_out.pdf");
    }
}
```

## Agregar Pie de Página en un Archivo PDF

La clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp/constructors/main) te permite agregar un pie de página en un archivo PDF. Para agregar un pie de página, primero necesitas crear un objeto de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp/constructors/main). Puedes formatear el texto del pie de página utilizando la clase [FormattedText](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formattedtext). Una vez que estés listo para agregar el pie de página en el archivo, necesitas llamar al método [AddFooter](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp/constructors/main). También necesitas especificar al menos el margen inferior en el método [AddFooter](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index). Finalmente, guarda el archivo PDF de salida utilizando el método [Close](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/facade/methods/close) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp/constructors/main). El siguiente fragmento de código te muestra cómo agregar un pie de página en un archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFooter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create formatted text for the footer
        var formattedText = new Aspose.Pdf.Facades.FormattedText(
            "Aspose - Your File Format Experts!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Courier,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false,
            14);

        // Add footer
        fileStamp.AddFooter(formattedText, 10);

        // Save PDF document
        fileStamp.Save(dataDir + "AddFooter_out.pdf");
    }
}
```

## Agregar Imagen en el Encabezado de un Archivo PDF Existente

La clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp/constructors/main) te permite agregar una imagen en el encabezado de un archivo PDF. Para agregar una imagen en el encabezado, primero necesitas crear un objeto de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp/constructors/main). Después de eso, necesitas llamar al método [AddHeader](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp/constructors/main). Puedes pasar la imagen al método [AddHeader](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4). Finalmente, guarda el archivo PDF de salida utilizando el método [Close](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/facade/methods/close) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp/constructors/main). El siguiente fragmento de código te muestra cómo agregar una imagen en el encabezado de un archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageHeader()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Add Header
        using (var fs = new FileStream(dataDir + "ImageHeader.png", FileMode.Open))
        {
            fileStamp.AddHeader(fs, 10);  // Add image header with position offset

            // Save PDF document
            fileStamp.Save(dataDir + "AddImageHeader_out.pdf");
        }
    }
}
```

## Agregar Imagen en el Pie de Página de un Archivo PDF Existente

La clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp/constructors/main) te permite agregar una imagen en el pie de página de un archivo PDF. Para agregar una imagen en el pie de página, primero necesitas crear un objeto de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp/constructors/main). Después de eso, necesitas llamar al método [AddFooter](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp/constructors/main). Puedes pasar la imagen al método [AddFooter](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index). Finalmente, guarda el archivo PDF de salida utilizando el método [Close](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/facade/methods/close) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp/constructors/main). El siguiente fragmento de código te muestra cómo agregar una imagen en el pie de página de un archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageFooter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Add footer
        using (var fs = new FileStream(dataDir + "ImageFooter.png", FileMode.Open))
        {
            fileStamp.AddFooter(fs, 10);  // Add image footer with position offset

            // Save PDF document
            fileStamp.Save(dataDir + "AddImageFooter_out.pdf");
        }
    }
}
```