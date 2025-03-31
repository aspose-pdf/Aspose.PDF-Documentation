---
title: Agregar Encabezado y Pie de Página a PDF
linktitle: Agregar Encabezado y Pie de Página a PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /es/net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for .NET te permite agregar encabezados y pies de página a tu archivo PDF utilizando la clase TextStamp.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Header and Footer to PDF",
    "alternativeHeadline": "Add Custom Headers and Footers to PDF Files",
    "abstract": "Aspose.PDF for .NET presenta una poderosa característica que permite a los usuarios enriquecer sus documentos PDF al agregar encabezados y pies de página personalizables. Usando las clases TextStamp e ImageStamp, los desarrolladores pueden integrar fácilmente tanto texto como imágenes, adaptando su colocación y apariencia para ajustarse a varios formatos y estilos de documentos. Esto mejora la profesionalidad y legibilidad del documento, haciéndolo ideal para informes, facturas y otras comunicaciones formales.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1549",
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
    "url": "/net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NET te permite agregar encabezados y pies de página a tu archivo PDF utilizando la clase TextStamp."
}
</script>

**Aspose.PDF for .NET** te permite agregar encabezados y pies de página en tu archivo PDF existente. Puedes agregar imágenes o texto a un documento PDF. Además, intenta agregar diferentes encabezados en un archivo PDF con C#.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

## Agregar Texto en el Encabezado del Archivo PDF

Puedes usar la clase [TextStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/textstamp) para agregar texto en el encabezado de un archivo PDF. La clase TextStamp proporciona propiedades necesarias para crear un sello basado en texto como tamaño de fuente, estilo de fuente y color de fuente, etc. Para agregar texto en el encabezado, necesitas crear un objeto Document y un objeto TextStamp utilizando las propiedades requeridas. Después de eso, puedes llamar al método AddStamp de la Página para agregar el texto en el encabezado del PDF.

Necesitas establecer la propiedad TopMargin de tal manera que ajuste el texto en el área del encabezado de tu PDF. También necesitas establecer HorizontalAlignment en Center y VerticalAlignment en Top.

El siguiente fragmento de código te muestra cómo agregar texto en el encabezado de un archivo PDF con C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHeaderText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextinHeader.pdf"))
    {
        // Create header as a TextStamp
        var textStamp = new Aspose.Pdf.TextStamp("Header Text")
        {
            TopMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top
        };

        // Add header on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(textStamp);
        }

        // Save PDF document
        document.Save(dataDir + "TextinHeader_out.pdf");
    }
}
```

## Agregar Texto en el Pie de Página del Archivo PDF

Puedes usar la clase TextStamp para agregar texto en el pie de página de un archivo PDF. La clase TextStamp proporciona propiedades necesarias para crear un sello basado en texto como tamaño de fuente, estilo de fuente y color de fuente, etc. Para agregar texto en el pie de página, necesitas crear un objeto Document y un objeto TextStamp utilizando las propiedades requeridas. Después de eso, puedes llamar al método AddStamp de la Página para agregar el texto en el pie de página del PDF.

{{% alert color="primary" %}}

Necesitas establecer la propiedad Bottom Margin de tal manera que ajuste el texto en el área del pie de página de tu PDF. También necesitas establecer HorizontalAlignment en Center y VerticalAlignment en Bottom.

{{% /alert %}}

El siguiente fragmento de código te muestra cómo agregar texto en el pie de página de un archivo PDF con C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFooterText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextinFooter.pdf"))
    {
        // Create footer as a TextStamp
        var textStamp = new Aspose.Pdf.TextStamp("Footer Text")
        {
            BottomMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Bottom
        };

        // Add footer on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(textStamp);
        }

        // Save PDF document
        document.Save(dataDir + "TextinFooter_out.pdf");
    }
}
```

## Agregar Imagen en el Encabezado del Archivo PDF

Puedes usar la clase [ImageStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/ImageStamp) para agregar una imagen en el encabezado de un archivo PDF. La clase Image Stamp proporciona propiedades necesarias para crear un sello basado en imagen como tamaño de fuente, estilo de fuente y color de fuente, etc. Para agregar una imagen en el encabezado, necesitas crear un objeto Document y un objeto Image Stamp utilizando las propiedades requeridas. Después de eso, puedes llamar al método [AddStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/page/methods/addstamp) de la Página para agregar la imagen en el encabezado del PDF.

{{% alert color="primary" %}}

Necesitas establecer la propiedad TopMargin de tal manera que ajuste la imagen en el área del encabezado de tu PDF. También necesitas establecer HorizontalAlignment en Center y VerticalAlignment en Top.

{{% /alert %}}

El siguiente fragmento de código te muestra cómo agregar una imagen en el encabezado de un archivo PDF con C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageHeader()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageinHeader.pdf"))
    {
        // Create header as an ImageStamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg")
        {
            TopMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top
        };

        // Add image header on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(imageStamp);
        }

        // Save PDF document
        document.Save(dataDir + "ImageinHeader_out.pdf");
    }
}
```

## Agregar Imagen en el Pie de Página del Archivo PDF

Puedes usar la clase Image Stamp para agregar una imagen en el pie de página de un archivo PDF. La clase Image Stamp proporciona propiedades necesarias para crear un sello basado en imagen como tamaño de fuente, estilo de fuente y color de fuente, etc. Para agregar una imagen en el pie de página, necesitas crear un objeto Document y un objeto Image Stamp utilizando las propiedades requeridas. Después de eso, puedes llamar al método AddStamp de la Página para agregar la imagen en el pie de página del PDF.

{{% alert color="primary" %}}

Necesitas establecer la propiedad [BottomMargin](https://reference.aspose.com/pdf/es/net/aspose.pdf/stamp/properties/bottommargin) de tal manera que ajuste la imagen en el área del pie de página de tu PDF. También necesitas establecer [HorizontalAlignment](https://reference.aspose.com/pdf/es/net/aspose.pdf/stamp/properties/horizontalalignment) en `Center` y [VerticalAlignment](https://reference.aspose.com/pdf/es/net/aspose.pdf/stamp/properties/verticalalignment) en `Bottom`.

{{% /alert %}}

El siguiente fragmento de código te muestra cómo agregar una imagen en el pie de página de un archivo PDF con C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageFooter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageInFooter.pdf"))
    {
        // Create footer as an ImageStamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg")
        {
            BottomMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Bottom
        };

        // Add image footer on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(imageStamp);
        }

        // Save PDF document
        document.Save(dataDir + "ImageInFooter_out.pdf");
    }
}
```

## Agregar diferentes Encabezados en un Archivo PDF

Sabemos que podemos agregar TextStamp en la sección de Encabezado/Pie de Página del documento utilizando las propiedades TopMargin o Bottom Margin, pero a veces podemos tener la necesidad de agregar múltiples encabezados/pies de página en un solo documento PDF. **Aspose.PDF for .NET** explica cómo hacer esto.

Para cumplir con este requisito, crearemos objetos TextStamp individuales (el número de objetos depende del número de encabezados/pies de página requeridos) y los agregaremos al documento PDF. También podemos especificar diferentes información de formato para cada objeto de sello. En el siguiente ejemplo, hemos creado un objeto Document y tres objetos TextStamp y luego hemos utilizado el método [AddStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/page/methods/addstamp) de la Página para agregar el texto en la sección del encabezado del PDF. El siguiente fragmento de código te muestra cómo agregar una imagen en el pie de página de un archivo PDF con Aspose.PDF for .NET.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddDifferentHeaders()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddingDifferentHeaders.pdf"))
    {
        // Create three stamps
        var stamp1 = new Aspose.Pdf.TextStamp("Header 1");
        var stamp2 = new Aspose.Pdf.TextStamp("Header 2");
        var stamp3 = new Aspose.Pdf.TextStamp("Header 3");

        // Set stamp1 properties (Header 1)
        stamp1.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        stamp1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        stamp1.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
        stamp1.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
        stamp1.TextState.FontSize = 14;

        // Set stamp2 properties (Header 2)
        stamp2.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        stamp2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        stamp2.Zoom = 10;

        // Set stamp3 properties (Header 3)
        stamp3.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        stamp3.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        stamp3.RotateAngle = 35;
        stamp3.TextState.BackgroundColor = Aspose.Pdf.Color.Pink;
        stamp3.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Verdana");

        // Add the stamps to specific pages
        document.Pages[1].AddStamp(stamp1);
        document.Pages[2].AddStamp(stamp2);
        document.Pages[3].AddStamp(stamp3);

        // Save PDF document
        document.Save(dataDir + "MultiHeader_out.pdf");
    }
}
```

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