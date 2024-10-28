---
title: Trabajando con Artefactos en .NET
linktitle: Trabajando con Artefactos
type: docs
weight: 110
url: /net/artifacts/
description: Aspose.PDF para .NET te permite agregar una imagen de fondo a las páginas de PDF y obtener cada marca de agua usando la clase Artifact.
lastmod: "2024-01-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabajando con Artefactos en .NET",
    "alternativeHeadline": "Artefactos en documento PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, artefactos en pdf",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentación de Aspose.PDF",
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
    "url": "/net/artifacts/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/artifacts/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF para .NET te permite agregar una imagen de fondo a las páginas de PDF y obtener cada marca de agua usando la clase Artifact."
}
</script>

Los artefactos en PDF son objetos gráficos u otros elementos que no son parte del contenido actual del documento. Generalmente se utilizan para decoración, diseño o propósitos de fondo. Ejemplos de artefactos incluyen encabezados de página, pies de página, separadores o imágenes que no transmiten ningún significado.

El propósito de los artefactos en PDF es permitir la distinción entre elementos de contenido y no contenido. Esto es importante para la accesibilidad, ya que los lectores de pantalla y otras tecnologías de asistencia pueden ignorar los artefactos y centrarse en el contenido relevante. Los artefactos también pueden mejorar el rendimiento y la calidad de los documentos PDF, ya que se pueden omitir al imprimir, buscar o copiar.

Para crear un elemento como un artefacto en PDF, necesitas usar la clase [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact).
Contiene las siguientes propiedades útiles:

- **Artifact.Type** – obtiene el tipo de artefacto (soporta valores de la enumeración Artifact.ArtifactType donde los valores incluyen Background, Layout, Page, Pagination y Undefined).
- **Artifact.Type** – obtiene el tipo de artefacto (admite valores de la enumeración Artifact.ArtifactType donde los valores incluyen Fondo, Diseño, Página, Paginación e Indefinido).
- **Artifact.Subtype** – obtiene el subtipo de artefacto (admite los valores de la enumeración Artifact.ArtifactSubtype donde los valores incluyen Fondo, Pie de página, Encabezado, Indefinido, Marca de agua).
- **Artifact.Image** – Obtiene la imagen de un artefacto (si hay una imagen presente, de lo contrario nulo).
- **Artifact.Text** – Obtiene el texto de un artefacto.
- **Artifact.Contents** – Obtiene una colección de operadores internos del artefacto. Su tipo compatible es System.Collections.ICollection.
- **Artifact.Form** – Obtiene el XForm de un artefacto (si se utiliza XForm). Los artefactos de marcas de agua, encabezado y pie de página contienen XForm que muestra todos los contenidos del artefacto.
- **Artifact.Rectangle** – Obtiene la posición de un artefacto en la página.
- **Artifact.Rotation** – Obtiene la rotación de un artefacto (en grados, un valor positivo indica una rotación en sentido antihorario).
- **Artifact.Opacity** – Obtiene la opacidad de un artefacto.
- **Artifact.Opacity** – Obtiene la opacidad de un artefacto.

Las siguientes clases también pueden ser útiles para trabajar con artefactos:

- [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection)
- [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/watermarkartifact/)

## Trabajando con marcas de agua existentes

Una marca de agua creada con Adobe Acrobat se llama un artefacto (como se describe en 14.8.2.2 Contenido Real y Artefactos de la especificación PDF).

Para obtener todas las marcas de agua en una página en particular, la clase [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) tiene la propiedad Artifacts.

El siguiente fragmento de código muestra cómo obtener todas las marcas de agua en la primera página de un archivo PDF.

_Nota:_ Este código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).
_Nota:_ Este código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample-w.pdf"));
var watermarks = document.Pages[1].Artifacts
    .Where(artifact =>
    artifact.Type == Artifact.ArtifactType.Pagination
    && artifact.Subtype == Artifact.ArtifactSubtype.Watermark);
foreach (WatermarkArtifact item in watermarks.Cast<WatermarkArtifact>())
{
    Console.WriteLine($"{item.Text} {item.Rectangle}");
}
```

## Trabajando con Fondos como Artefactos

Las imágenes de fondo se pueden utilizar para añadir una marca de agua u otro diseño sutil a los documentos. En Aspose.PDF para .NET, cada documento PDF es una colección de páginas y cada página contiene una colección de artefactos. La clase [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact) se puede utilizar para agregar una imagen de fondo a un objeto de página.

El siguiente fragmento de código muestra cómo agregar una imagen de fondo a las páginas PDF utilizando el objeto BackgroundArtifact.

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var background = new BackgroundArtifact()
{
    BackgroundImage = System.IO.File.OpenRead(System.IO.Path.Combine(_dataDir, "background.jpg"))
};
document.Pages[1].Artifacts.Add(background);
document.Save(System.IO.Path.Combine(_dataDir, "sample_artifacts_background.pdf"));
```
Si deseas, por alguna razón, utilizar un fondo de color sólido, cambia el código anterior de la siguiente manera:

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var background = new BackgroundArtifact()
{
    BackgroundColor = Color.DarkKhaki,
};
document.Pages[1].Artifacts.Add(background);
document.Save(System.IO.Path.Combine(_dataDir, "sample_artifacts_background.pdf"));
```

## Contando Artefactos de un Tipo Particular

Para calcular el total de artefactos de un tipo particular (por ejemplo, el número total de marcas de agua), utiliza el siguiente código:

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var paginationArtifacts = document.Pages[1].Artifacts.Where(artifact => artifact.Type == Artifact.ArtifactType.Pagination);
Console.WriteLine("Watermarks: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Watermark));
Console.WriteLine("Backgrounds: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Background));
Console.WriteLine("Headers: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Header));
Console.WriteLine("Footers: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Footer));
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
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/destacado",
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
```

