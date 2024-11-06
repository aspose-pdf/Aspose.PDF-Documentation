---
title: Crear enlaces en archivos PDF con C#
linktitle: Crear enlaces
type: docs
weight: 10
url: es/net/create-links/
description: Esta sección explica cómo crear enlaces en su documento PDF con C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Crear enlaces en archivos PDF con C#",
    "alternativeHeadline": "Cómo crear enlaces en PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, crear enlace en pdf",
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
    "url": "/net/create-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-links/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta sección explica cómo crear enlaces en su documento PDF con C#."
}
</script>

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Crear enlaces

Al agregar un enlace a una aplicación en un documento, es posible enlazar aplicaciones desde un documento. Esto es útil cuando deseas que los lectores realicen una acción determinada en un punto específico de un tutorial, por ejemplo, o para crear un documento con muchas funciones. Para crear un enlace de aplicación:

1. [Crea un objeto Documento](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Obtén la [Página](https://reference.aspose.com/pdf/net/aspose.pdf/page) a la que deseas agregar el enlace.
1. Crea un objeto [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) usando los objetos Página y [Rectángulo](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle).
1. Establece los atributos del enlace utilizando el objeto [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation).
1. Al crear el objeto [LaunchAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/launchaction), especifica la aplicación que deseas lanzar.
1. Agrega el enlace a la propiedad [Annotations](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/annotations) del objeto Page.
1. Finalmente, guarda el PDF actualizado usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) del objeto Document.

El siguiente fragmento de código muestra cómo crear un enlace a una aplicación en un archivo PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// Abrir documento
Document document = new Document(dataDir + "CreateApplicationLink.pdf");

// Crear enlace
Page page = document.Pages[1];
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
link.Action = new LaunchAction(document, dataDir + "CreateApplicationLink.pdf");
page.Annotations.Add(link);

dataDir = dataDir + "CreateApplicationLink_out.pdf";
// Guardar el documento actualizado
document.Save(dataDir);
```
### Crear un enlace de documento PDF en un archivo PDF

Aspose.PDF para .NET te permite agregar un enlace a un archivo PDF externo para que puedas vincular varios documentos entre sí. Para crear un enlace de documento PDF:

1. Primero, crea un objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Luego, obtén la [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) específica a la que deseas agregar el enlace.
1. Crea un objeto [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) utilizando los objetos Page y [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle).
1. Establece los atributos del enlace utilizando el objeto [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation).
1. Establece la propiedad Action al objeto [GoToRemoteAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoremoteaction).
1. Añade el enlace a la colección de Anotaciones del objeto Página.
1. Guarda el PDF actualizado usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) del objeto Documento.

El siguiente fragmento de código muestra cómo crear un enlace de documento PDF en un archivo PDF.

 ```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Abrir documento
Document document = new Document(dataDir+ "CreateDocumentLink.pdf");
// Crear enlace
Page page = document.Pages[1];
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
link.Action = new GoToRemoteAction(dataDir + "RemoveOpenAction.pdf", 1);
page.Annotations.Add(link);
dataDir = dataDir + "CreateDocumentLink_out.pdf";
// Guardar documento actualizado
document.Save(dataDir);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Biblioteca Aspose.PDF para .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organización",
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
                "@type": "Punto de Contacto",
                "telephone": "+1 903 306 1676",
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "Punto de Contacto",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "Punto de Contacto",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Oferta",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Biblioteca de manipulación de PDF para .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "Puntuación Agregada",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

