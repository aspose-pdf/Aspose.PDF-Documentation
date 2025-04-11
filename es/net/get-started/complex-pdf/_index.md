---
title: Creando un PDF complejo
linktitle: Creando un PDF complejo
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /es/net/complex-pdf-example/
description: Aspose.PDF para NET te permite crear documentos más complejos que contienen imágenes, fragmentos de texto y tablas en un solo documento.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Creating a complex PDF",
    "alternativeHeadline": "Create Complex PDFs with Images, Text, and Tables in C#",
    "abstract": "Aspose.PDF for .NET introduce una poderosa característica para crear PDFs complejos, permitiendo a los desarrolladores integrar sin problemas imágenes, fragmentos de texto y tablas en un solo documento. Esta funcionalidad aprovecha un enfoque basado en DOM, permitiendo una personalización detallada y control de diseño en la generación de PDF, lo que lo hace ideal para crear documentos de calidad profesional de manera eficiente.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "632",
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
    "url": "/net/complex-pdf-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/complex-pdf-example/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

El [Hola, Mundo](/pdf/es/net/hello-world-example/) mostró pasos simples para crear un documento PDF usando C# y Aspose.PDF. En este artículo, echaremos un vistazo a la creación de un documento más complejo con C# y Aspose.PDF for .NET. Como ejemplo, tomaremos un documento de una empresa ficticia que opera servicios de ferry de pasajeros. 
Nuestro documento contendrá una imagen, dos fragmentos de texto (encabezado y párrafo) y una tabla. Para construir tal documento, utilizaremos un enfoque basado en DOM. Puedes leer más en la sección [Fundamentos de la API DOM](/pdf/es/net/basics-of-dom-api/).

Si creamos un documento desde cero, necesitamos seguir ciertos pasos:

1. Instanciar un objeto [Document](https://reference.aspose.com/pdf/es/net/aspose.pdf/document). En este paso crearemos un documento PDF vacío con algunos metadatos pero sin páginas.
1. Agregar una [Page](https://reference.aspose.com/pdf/es/net/aspose.pdf/page) al objeto documento. Así, ahora nuestro documento tendrá una página.
1. Agregar una [Image](https://reference.aspose.com/pdf/es/net/aspose.pdf/image/methods/index) a la página.
1. Crear un [TextFragment](https://reference.aspose.com/pdf/es/net/aspose.pdf.text/textfragment) para el encabezado. Para el encabezado utilizaremos la fuente Arial con un tamaño de fuente de 24pt y alineación centrada.
1. Agregar el encabezado a los [Paragraphs](https://reference.aspose.com/pdf/es/net/aspose.pdf/page/properties/paragraphs) de la página.
1. Crear un [TextFragment](https://reference.aspose.com/pdf/es/net/aspose.pdf.text/textfragment) para la descripción. Para la descripción utilizaremos la fuente Arial con un tamaño de fuente de 24pt y alineación centrada.
1. Agregar (descripción) a los párrafos de la página.
1. Crear una tabla, agregar propiedades a la tabla.
1. Agregar (tabla) a los [Paragraphs](https://reference.aspose.com/pdf/es/net/aspose.pdf/page/properties/paragraphs) de la página.
1. Guardar el documento como "Complex.pdf".

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/). 

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreatingComplexPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Add image
        page.AddImage(dataDir + "logo.png", new Aspose.Pdf.Rectangle(20, 730, 120, 830));

        // Add Header
        var header = new Aspose.Pdf.Text.TextFragment("New ferry routes in Fall 2020");
        header.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        header.TextState.FontSize = 24;
        header.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        header.Position = new Aspose.Pdf.Text.Position(130, 720);
        page.Paragraphs.Add(header);

        // Add description
        var descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. Ferry service is operating at half capacity and on a reduced schedule. Expect lineups.";
        var description = new Aspose.Pdf.Text.TextFragment(descriptionText);
        description.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Times New Roman");
        description.TextState.FontSize = 14;
        description.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Left;
        page.Paragraphs.Add(description);

        // Add table
        var table = new Aspose.Pdf.Table
        {
            ColumnWidths = "200",
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1f, Aspose.Pdf.Color.DarkSlateGray),
            DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 0.5f, Aspose.Pdf.Color.Black),
            DefaultCellPadding = new Aspose.Pdf.MarginInfo(4.5, 4.5, 4.5, 4.5),
            Margin =
            {
                Bottom = 10
            },
            DefaultCellTextState =
            {
                Font =  Aspose.Pdf.Text.FontRepository.FindFont("Helvetica")
            }
        };

        var headerRow = table.Rows.Add();
        headerRow.Cells.Add("Departs City");
        headerRow.Cells.Add("Departs Island");
        foreach (Aspose.Pdf.Cell headerRowCell in headerRow.Cells)
        {
            headerRowCell.BackgroundColor = Aspose.Pdf.Color.Gray;
            headerRowCell.DefaultCellTextState.ForegroundColor = Aspose.Pdf.Color.WhiteSmoke;
        }

        var time = new TimeSpan(6, 0, 0);
        var incTime = new TimeSpan(0, 30, 0);
        for (int i = 0; i < 10; i++)
        {
            var dataRow = table.Rows.Add();
            dataRow.Cells.Add(time.ToString(@"hh\:mm"));
            time = time.Add(incTime);
            dataRow.Cells.Add(time.ToString(@"hh\:mm"));
        }

        page.Paragraphs.Add(table);
        // Save PDF document
        document.Save(dataDir + "Complex_out.pdf");
    }
}
```