---
title: Recortar páginas PDF programáticamente C#
linktitle: Recortar Páginas
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /es/net/crop-pages/
description: Puede obtener propiedades de página, como el ancho, la altura, el sangrado, el recorte y el trimbox utilizando Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Crop PDF Pages programmatically C#",
    "alternativeHeadline": "Crop PDF Pages Easily with Aspose.PDF for .NET",
    "abstract": "Aspose.PDF for .NET introduce una nueva característica poderosa que permite a los desarrolladores acceder y manipular programáticamente varias propiedades de página de un PDF, incluyendo el media box, bleed box, trim box, art box y crop box. Esta funcionalidad agiliza el proceso de personalización de diseños PDF, asegurando precisión en la presentación de documentos y mejorando la calidad de impresión mientras minimiza los bordes blancos. Con fragmentos de código fáciles de usar, los usuarios pueden integrar sin problemas estas capacidades en sus aplicaciones, mejorando la gestión y manipulación de PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "494",
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
    "url": "/net/crop-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/crop-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "Puede obtener propiedades de página, como el ancho, la altura, el sangrado, el recorte y el trimbox utilizando Aspose.PDF for .NET."
}
</script>

## Obtener propiedades de página

Cada página en un archivo PDF tiene una serie de propiedades, como el ancho, la altura, el sangrado, el recorte y el trimbox. Aspose.PDF le permite acceder a estas propiedades.

- **Media box**: El media box es la caja de página más grande. Corresponde al tamaño de la página (por ejemplo, A4, A5, US Letter, etc.) seleccionado cuando el documento fue impreso en PostScript o PDF. En otras palabras, el media box determina el tamaño físico del medio en el que se muestra o imprime el documento PDF.
- **Bleed box**: Si el documento tiene sangrado, el PDF también tendrá un bleed box. El sangrado es la cantidad de color (o arte) que se extiende más allá del borde de una página. Se utiliza para asegurarse de que cuando el documento se imprime y se corta a tamaño ("recortado"), la tinta llegue hasta el borde de la página. Incluso si la página está mal recortada - cortada ligeramente fuera de las marcas de recorte - no aparecerán bordes blancos en la página.
- **Trim box**: El trim box indica el tamaño final de un documento después de imprimir y recortar.
- **Art box**: El art box es la caja dibujada alrededor del contenido real de las páginas en sus documentos. Esta caja de página se utiliza al importar documentos PDF en otras aplicaciones.
- **Crop box**: El crop box es el tamaño de "página" en el que se muestra su documento PDF en Adobe Acrobat. En la vista normal, solo se muestran los contenidos del crop box en Adobe Acrobat. Para descripciones detalladas de estas propiedades, lea la especificación de Adobe.Pdf, particularmente 10.10.1 Límites de página.
- **Page.Rect**: la intersección (rectángulo comúnmente visible) del MediaBox y DropBox. La imagen a continuación ilustra estas propiedades.
Para más detalles, visite [esta página](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

El fragmento a continuación muestra cómo recortar la página:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CropPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CropPageInput.pdf"))
    {
        Console.WriteLine(document.Pages[1].CropBox);
        Console.WriteLine(document.Pages[1].TrimBox);
        Console.WriteLine(document.Pages[1].ArtBox);
        Console.WriteLine(document.Pages[1].BleedBox);
        Console.WriteLine(document.Pages[1].MediaBox);
        // Create new Box rectangle
        var newBox = new Rectangle(200, 220, 2170, 1520);
        document.Pages[1].CropBox = newBox;
        document.Pages[1].TrimBox = newBox;
        document.Pages[1].ArtBox = newBox;
        document.Pages[1].BleedBox = newBox;
        // Save PDF document
        document.Save(dataDir + "CropPage_out.pdf");  
    }
}
```

En este ejemplo utilizamos un archivo de muestra [aquí](crop_page.pdf). Inicialmente, nuestra página se ve como se muestra en la Figura 1.

Después del cambio, la página se verá como la Figura 2.

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