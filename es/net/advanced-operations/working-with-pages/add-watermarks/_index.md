---
title: Agregar marca de agua a PDF usando C#
linktitle: Agregar marca de agua
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /es/net/add-watermarks/
description: Este artículo explica las características de trabajar con artefactos y obtener marcas de agua en PDFs utilizando programáticamente C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add watermark to PDF using C#",
    "alternativeHeadline": "Add Custom Watermarks to PDF with C#",
    "abstract": "La nueva función en Aspose.PDF for .NET permite a los desarrolladores agregar programáticamente marcas de agua personalizables a documentos PDF utilizando la funcionalidad de Artefacto. Esta función mejora la gestión de documentos al soportar varias propiedades de artefactos, incluyendo tipo, opacidad, rotación y personalización de texto, permitiendo a los usuarios crear archivos PDF profesionales e identificables fácilmente.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "462",
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
    "url": "/net/add-watermarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-watermarks/"
    },
    "dateModified": "2024-11-26",
    "description": "Este artículo explica las características de trabajar con artefactos y obtener marcas de agua en PDFs utilizando programáticamente C#."
}
</script>

**Aspose.PDF for .NET** permite agregar marcas de agua a su documento PDF utilizando Artefactos. Por favor, consulte este artículo para resolver su tarea.

El siguiente fragmento de código también trabaja con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

Una marca de agua creada con Adobe Acrobat se llama un artefacto (como se describe en 14.8.2.2 Contenido Real y Artefactos de la especificación PDF). Para trabajar con artefactos, Aspose.PDF tiene dos clases: [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) y [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection).

Para obtener todos los artefactos en una página particular, la clase [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) tiene la propiedad Artifacts. Este tema explica cómo trabajar con artefactos en archivos PDF.

## Trabajando con Artefactos

La clase [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) contiene las siguientes propiedades:

- **Artifact.Type**: obtiene el tipo de artefacto (soporta valores de la enumeración Artifact.ArtifactType donde los valores incluyen Fondo, Diseño, Página, Paginación y No Definido).
- **Artifact.Subtype**: obtiene el subtipo de artefacto (soporta los valores de la enumeración Artifact.ArtifactSubtype donde los valores incluyen Fondo, Pie de página, Encabezado, No Definido, Marca de agua).

{{% alert color="primary" %}}

Tenga en cuenta que las marcas de agua creadas con Adobe Acrobat tienen el tipo Paginación y subtipo Marca de agua.

{{% /alert %}}

- **Artifact.Contents**: Obtiene una colección de operadores internos del artefacto. Su tipo soportado es System.Collections.ICollection.
- **Artifact.Form**: Obtiene un XForm del artefacto (si se utiliza XForm). Las marcas de agua, encabezados y pies de página contienen XForm que muestra todos los contenidos del artefacto.
- **Artifact.Image**: Obtiene la imagen de un artefacto (si hay una imagen presente, de lo contrario, null).
- **Artifact.Text**: Obtiene el texto de un artefacto.
- **Artifact.Rectangle**: Obtiene la posición de un artefacto en la página.
- **Artifact.Rotation**: Obtiene la rotación de un artefacto (en grados, un valor positivo indica rotación en sentido contrario a las agujas del reloj).
- **Artifact.Opacity**: Obtiene la opacidad de un artefacto. Los valores posibles están en el rango de 0…1, donde 1 es completamente opaco.

## Cómo Agregar Marca de Agua en Archivos PDF

El siguiente fragmento de código muestra cómo obtener cada marca de agua en la primera página de un archivo PDF con C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddWatermarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddWatermarksInput.pdf"))
    {
        // Create a new watermark artifact
        var artifact = new Aspose.Pdf.WatermarkArtifact();
        artifact.SetTextAndState(
            "WATERMARK",
            new Aspose.Pdf.Text.TextState()
            {
                FontSize = 72,
                ForegroundColor = Aspose.Pdf.Color.Blue,
                Font = Aspose.Pdf.Text.FontRepository.FindFont("Courier")
            });
        // Set watermark properties
        artifact.ArtifactHorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        artifact.ArtifactVerticalAlignment = Aspose.Pdf.VerticalAlignment.Center;
        artifact.Rotation = 45;
        artifact.Opacity = 0.5;
        artifact.IsBackground = true;
        // Add watermark artifact to the first page
        document.Pages[1].Artifacts.Add(artifact);
        // Save PDF document
        document.Save(dataDir + "AddWatermarks_out.pdf");
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