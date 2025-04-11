---
title: Actualizar enlaces en PDF
linktitle: Actualizar enlaces
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /es/net/update-links/
description: Actualizar enlaces en PDF programáticamente. Esta guía trata sobre cómo actualizar enlaces en PDF en el lenguaje C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Update Links in PDF",
    "alternativeHeadline": "Programmatically Modify PDF Links Using C#",
    "abstract": "La nueva función de Actualizar enlaces en PDF permite a los usuarios modificar programáticamente hiperenlaces dentro de documentos PDF utilizando C#. Esta funcionalidad permite a los usuarios dirigir enlaces a páginas específicas, direcciones web externas o incluso otros archivos PDF, mejorando la interactividad y usabilidad de los documentos digitales. Al simplificar el proceso de gestión de enlaces, esta función es ideal para desarrolladores que buscan optimizar sus aplicaciones PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Update links in PDF, C#, LinkAnnotation, GoToAction, XYZExplicitDestination, GoToURIAction, update hyperlink, PDF manipulation",
    "wordcount": "797",
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
    "url": "/net/update-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/update-links/"
    },
    "dateModified": "2024-11-25",
    "description": "Actualizar enlaces en PDF programáticamente. Esta guía trata sobre cómo actualizar enlaces en PDF en el lenguaje C#."
}
</script>

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

## Actualizar enlaces en archivo PDF

Como se discutió en Agregar hiperenlace en un archivo PDF, la clase [LinkAnnotation](https://reference.aspose.com/pdf/es/net/aspose.pdf.annotations/linkannotation) hace posible agregar enlaces en un archivo PDF. También hay una clase similar utilizada para obtener enlaces existentes dentro de archivos PDF. Utiliza esto si necesitas actualizar un enlace existente. Para actualizar un enlace existente:

1. Carga un archivo PDF.
1. Ve a una página específica en el archivo PDF.
1. Especifica el destino del enlace utilizando la propiedad Destination del objeto [GoToAction](https://reference.aspose.com/pdf/es/net/aspose.pdf.annotations/gotoaction).
1. La página de destino se especifica utilizando el constructor [XYZExplicitDestination](https://reference.aspose.com/pdf/es/net/aspose.pdf.annotations/xyzexplicitdestination).

### Establecer el destino del enlace a una página en el mismo documento

El siguiente fragmento de código te muestra cómo actualizar un enlace en un archivo PDF y establecer su destino en la segunda página del documento.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf"))
    {
        // Get the first link annotation from first page of document
        var linkAnnot = (Aspose.Pdf.Annotations.LinkAnnotation)document.Pages[1].Annotations[1];

        // Modification link: change link destination
        var goToAction = (Aspose.Pdf.Annotations.GoToAction)linkAnnot.Action;

        // Specify the destination for link object
        // The first parameter is document object, second is destination page number.
        // The 5ht argument is zoom factor when displaying the respective page. When using 2, the page will be displayed in 200% zoom
        goToAction.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(1, 1, 2, 2);

        // Save PDF document
        document.Save(dataDir + "UpdateLinks_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf");

    // Get the first link annotation from first page of document
    var linkAnnot = (Aspose.Pdf.Annotations.LinkAnnotation)document.Pages[1].Annotations[1];

    // Modification link: change link destination
    var goToAction = (Aspose.Pdf.Annotations.GoToAction)linkAnnot.Action;

    // Specify the destination for link object
    // The first parameter is document object, second is destination page number.
    // The 5ht argument is zoom factor when displaying the respective page. When using 2, the page will be displayed in 200% zoom
    goToAction.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(1, 1, 2, 2);

    // Save PDF document
    document.Save(dataDir + "UpdateLinks_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### Establecer el destino del enlace a una dirección web

Para actualizar el hiperenlace de modo que apunte a una dirección web, instancia el objeto [GoToURIAction](https://reference.aspose.com/pdf/es/net/aspose.pdf.annotations/gotouriaction) y pásalo a la propiedad Action de LinkAnnotation. El siguiente fragmento de código muestra cómo actualizar un enlace en un archivo PDF y establecer su destino en una dirección web.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf"))
    {
        // Get the first link annotation from first page of document
        var linkAnnot = (Aspose.Pdf.Annotations.LinkAnnotation)document.Pages[1].Annotations[1];

        // Modification link: change link action and set target as web address
        linkAnnot.Action = new Aspose.Pdf.Annotations.GoToURIAction("www.aspose.com");

        // Save PDF document
        document.Save(dataDir + "SetDestinationLink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf");

    // Get the first link annotation from first page of document
    var linkAnnot = (Aspose.Pdf.Annotations.LinkAnnotation)document.Pages[1].Annotations[1];

    // Modification link: change link action and set target as web address
    linkAnnot.Action = new Aspose.Pdf.Annotations.GoToURIAction("www.aspose.com");

    // Save PDF document
    document.Save(dataDir + "SetDestinationLink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### Establecer el destino del enlace a otro archivo PDF

El siguiente fragmento de código muestra cómo actualizar un enlace en un archivo PDF y establecer su destino en otro archivo PDF.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf"))
    {
        var linkAnnot = (Aspose.Pdf.Annotations.LinkAnnotation)document.Pages[1].Annotations[1];
        var goToR = (Aspose.Pdf.Annotations.GoToRemoteAction)linkAnnot.Action;

        // Next line update destination, do not update file
        goToR.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(2, 0, 0, 1.5);

        // Next line update file
        goToR.File = new Aspose.Pdf.FileSpecification(dataDir + "input.pdf");

        // Save PDF document
        document.Save(dataDir + "SetTargetLink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf");

    var linkAnnot = (Aspose.Pdf.Annotations.LinkAnnotation)document.Pages[1].Annotations[1];
    var goToR = (Aspose.Pdf.Annotations.GoToRemoteAction)linkAnnot.Action;

    // Next line update destination, do not update file
    goToR.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(2, 0, 0, 1.5);

    // Next line update file
    goToR.File = new Aspose.Pdf.FileSpecification(dataDir + "input.pdf");

    // Save PDF document
    document.Save(dataDir + "SetTargetLink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### Actualizar el color del texto de LinkAnnotation

La anotación de enlace no contiene texto. En cambio, el texto se coloca en los contenidos de la página bajo la anotación. Por lo tanto, para cambiar el color del texto, reemplaza el color del texto de la página en lugar de intentar cambiar el color de la anotación. El siguiente fragmento de código muestra cómo actualizar el color de la anotación de enlace en un archivo PDF.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf"))
    {
        foreach (var annotation in document.Pages[1].Annotations)
        {
            if (annotation is Aspose.Pdf.Annotations.LinkAnnotation)
            {
                // Search the text under the annotation
                var ta = new Aspose.Pdf.Text.TextFragmentAbsorber();
                var rect = annotation.Rect;
                rect.LLX -= 10;
                rect.LLY -= 10;
                rect.URX += 10;
                rect.URY += 10;
                ta.TextSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(rect);
                ta.Visit(document.Pages[1]);

                // Change color of the text.
                foreach (var textFragment in ta.TextFragments)
                {
                    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "UpdateLinkTextColor_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf");

    foreach (var annotation in document.Pages[1].Annotations)
    {
        if (annotation is Aspose.Pdf.Annotations.LinkAnnotation)
        {
            // Search the text under the annotation
            var ta = new Aspose.Pdf.Text.TextFragmentAbsorber();
            var rect = annotation.Rect;
            rect.LLX -= 10;
            rect.LLY -= 10;
            rect.URX += 10;
            rect.URY += 10;
            ta.TextSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(rect);
            ta.Visit(document.Pages[1]);

            // Change color of the text.
            foreach (var textFragment in ta.TextFragments)
            {
                textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
            }
        }
    }

    // Save PDF document
    document.Save(dataDir + "UpdateLinkTextColor_out.pdf");
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