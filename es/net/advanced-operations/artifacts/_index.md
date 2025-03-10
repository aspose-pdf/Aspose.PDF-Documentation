---
title: Trabajando con Artefactos en .NET
linktitle: Trabajando con Artefactos
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 170
url: /es/net/artifacts/
description: Aspose.PDF for .NET te permite agregar una imagen de fondo a las páginas PDF y obtener cada marca de agua utilizando la clase Artifact.
lastmod: "2024-01-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Artifacts in .NET",
    "alternativeHeadline": "Add and Manage Artifacts in PDF Documents",
    "abstract": "Aspose.PDF for .NET introduce la clase Artifact, permitiendo a los desarrolladores gestionar eficientemente elementos no relacionados con el contenido, como imágenes de fondo y marcas de agua dentro de documentos PDF. Esta funcionalidad mejora la estructura del documento mientras mejora la accesibilidad y el rendimiento, ya que los artefactos pueden ser ignorados por tecnologías asistivas. Con opciones personalizables para tipos y propiedades, los usuarios pueden manipular fácilmente estos elementos para crear PDFs visualmente atractivos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Artifacts, PDF document generation, Aspose.PDF for .NET, BackgroundArtifact, WatermarkArtifact, Artifact class, PDF artifacts, Artifact types, Accessibility in PDF, PDF watermark handling",
    "wordcount": "779",
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
    "url": "/net/artifacts/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/artifacts/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NET te permite agregar una imagen de fondo a las páginas PDF y obtener cada marca de agua utilizando la clase Artifact."
}
</script>

Los artefactos en PDF son objetos gráficos u otros elementos que no son parte del contenido real del documento. Se utilizan generalmente para decoración, diseño o propósitos de fondo. Ejemplos de artefactos incluyen encabezados de página, pies de página, separadores o imágenes que no transmiten ningún significado.

El propósito de los artefactos en PDF es permitir la distinción entre elementos de contenido y no contenido. Esto es importante para la accesibilidad, ya que los lectores de pantalla y otras tecnologías asistivas pueden ignorar los artefactos y centrarse en el contenido relevante. Los artefactos también pueden mejorar el rendimiento y la calidad de los documentos PDF, ya que pueden ser omitidos en la impresión, búsqueda o copia.

Para crear un elemento como un artefacto en PDF, necesitas usar la clase [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact).
Contiene las siguientes propiedades útiles:

- **Artifact.Type** – obtiene el tipo de artefacto (soporta valores de la enumeración Artifact.ArtifactType donde los valores incluyen Background, Layout, Page, Pagination y Undefined).
- **Artifact.Subtype** – obtiene el subtipo de artefacto (soporta los valores de la enumeración Artifact.ArtifactSubtype donde los valores incluyen Background, Footer, Header, Undefined, Watermark).
- **Artifact.Image** – Obtiene la imagen de un artefacto (si hay una imagen presente, de lo contrario null).
- **Artifact.Text** – Obtiene el texto de un artefacto.
- **Artifact.Contents** – Obtiene una colección de operadores internos del artefacto. Su tipo soportado es System.Collections.ICollection.
- **Artifact.Form** – Obtiene el XForm de un artefacto (si se usa XForm). Las marcas de agua, encabezados y pies de página contienen XForm que muestra todos los contenidos del artefacto.
- **Artifact.Rectangle** – Obtiene la posición de un artefacto en la página.
- **Artifact.Rotation** – Obtiene la rotación de un artefacto (en grados, un valor positivo indica rotación en sentido contrario a las agujas del reloj).
- **Artifact.Opacity** – Obtiene la opacidad de un artefacto. Los valores posibles están en el rango 0...1, donde 1 es completamente opaco.

Las siguientes clases también pueden ser útiles para trabajar con artefactos:

- [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection)
- [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/watermarkartifact/)

## Trabajando con Marcas de Agua Existentes

Una marca de agua creada con Adobe Acrobat se llama un artefacto (como se describe en 14.8.2.2 Contenido Real y Artefactos de la especificación PDF).

Para obtener todas las marcas de agua en una página particular, la clase [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) tiene la propiedad Artifacts.

El siguiente fragmento de código muestra cómo obtener todas las marcas de agua en la primera página de un archivo PDF.

_Nota:_ Este código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractWatermarkFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample-w.pdf"))
    {
        // Get the watermarks from the first page artifacts
        var watermarks = document.Pages[1].Artifacts
            .Where(artifact =>
                artifact.Type == Aspose.Pdf.Artifact.ArtifactType.Pagination
                && artifact.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Watermark);

        // Iterate through the found watermark artifacts and print details
        foreach (Aspose.Pdf.WatermarkArtifact item in watermarks.Cast<Aspose.Pdf.WatermarkArtifact>())
        {
            Console.WriteLine($"{item.Text} {item.Rectangle}");
        }
    }
}
```

## Trabajando con Fondos como Artefactos

Las imágenes de fondo se pueden usar para agregar una marca de agua u otro diseño sutil a los documentos. En Aspose.PDF for .NET, cada documento PDF es una colección de páginas y cada página contiene una colección de artefactos. La clase [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact) se puede usar para agregar una imagen de fondo a un objeto de página.

El siguiente fragmento de código muestra cómo agregar una imagen de fondo a las páginas PDF utilizando el objeto BackgroundArtifact.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBackgroundImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Create a new BackgroundArtifact and set the background image
        var background = new Aspose.Pdf.BackgroundArtifact()
        {
            BackgroundImage = File.OpenRead(dataDir + "background.jpg")
        };

        // Add the background image to the first page's artifacts
        document.Pages[1].Artifacts.Add(background);

        // Save PDF document with the added background
        document.Save(dataDir + "SampleArtifactsBackground_out.pdf");
    }
}
```

Si deseas, por alguna razón, usar un fondo de color sólido, por favor cambia el código anterior de la siguiente manera:

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

 private static void AddBackgroundColorToPDF()
 {
    // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
     {
         // Create a new BackgroundArtifact and set the background color
         var background = new Aspose.Pdf.BackgroundArtifact()
         {
             BackgroundColor = Aspose.Pdf.Color.DarkKhaki
         };

         // Add the background color to the first page's artifacts
         document.Pages[1].Artifacts.Add(background);

         // Save PDF document
         document.Save(dataDir + "SampleArtifactsBackground_out.pdf");
     }
 }
```

## Contando Artefactos de un Tipo Particular

Para calcular el conteo total de artefactos de un tipo particular (por ejemplo, el número total de marcas de agua), usa el siguiente código:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CountPDFArtifacts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Get pagination artifacts from the first page
        var paginationArtifacts = document.Pages[1].Artifacts
            .Where(artifact => artifact.Type == Aspose.Pdf.Artifact.ArtifactType.Pagination);

        // Count and display the number of each artifact type
        Console.WriteLine("Watermarks: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Watermark));
        Console.WriteLine("Backgrounds: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Background));
        Console.WriteLine("Headers: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Header));
        Console.WriteLine("Footers: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Footer));
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