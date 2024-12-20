---
title: Añadir número de página a PDF con C#
linktitle: Añadir número de página
type: docs
weight: 100
url: /es/net/add-page-number/
description: Aspose.PDF para .NET te permite añadir un sello de número de página a tu archivo PDF utilizando la clase PageNumber Stamp.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Añadir número de página a PDF con C#",
    "alternativeHeadline": "Cómo añadir un sello de número de página a PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, sello de número de página",
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
    "url": "/net/add-page-number/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-page-number/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF para .NET te permite añadir un sello de número de página a tu archivo PDF utilizando la clase PageNumber Stamp."
}
</script>
Todos los documentos deben tener números de página. El número de página facilita al lector la localización de diferentes partes del documento.
**Aspose.PDF for .NET** le permite agregar números de página con PageNumberStamp.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

Puede usar la clase [PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) para agregar un sello de número de página en un archivo PDF.
Puedes usar la clase [PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) para añadir un sello de número de página en un archivo PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Abrir documento
Document pdfDocument = new Document(dataDir+ "PageNumberStamp.pdf");

// Crear sello de número de página
PageNumberStamp pageNumberStamp = new PageNumberStamp();
// Si el sello es de fondo
pageNumberStamp.Background = false;
pageNumberStamp.Format = "Página # de " + pdfDocument.Pages.Count;
pageNumberStamp.BottomMargin = 10;
pageNumberStamp.HorizontalAlignment = HorizontalAlignment.Center;
pageNumberStamp.StartingNumber = 1;
// Establecer propiedades del texto
pageNumberStamp.TextState.Font = FontRepository.FindFont("Arial");
pageNumberStamp.TextState.FontSize = 14.0F;
pageNumberStamp.TextState.FontStyle = FontStyles.Bold;
pageNumberStamp.TextState.FontStyle = FontStyles.Italic;
pageNumberStamp.TextState.ForegroundColor = Color.Aqua;

// Añadir sello a una página específica
pdfDocument.Pages[1].AddStamp(pageNumberStamp);

dataDir = dataDir + "PageNumberStamp_out.pdf";
// Guardar documento de salida
pdfDocument.Save(dataDir);
```
## Ejemplo en Vivo

[Agregar números de página en PDF](https://products.aspose.app/pdf/page-number) es una aplicación web gratuita en línea que te permite investigar cómo funciona la funcionalidad de agregar números de página.

[![Cómo agregar número de página en pdf usando C#](page_number.png)](https://products.aspose.app/pdf/page-number)

## Agregar/Remover numeración Bates

**La numeración Bates** (también conocida como estampado Bates) se utiliza en los campos legal, médico y empresarial para colocar números identificativos y/o marcas de fecha/hora en imágenes y documentos a medida que se escanean o procesan, por ejemplo, durante la etapa de descubrimiento de preparativos para un juicio o identificando recibos empresariales. Este proceso proporciona identificación, protección y numeración consecutiva automática de las imágenes o documentos.

Aspose.PDF tiene soporte limitado para la Numeración Bates por ahora. Esta funcionalidad se actualizará según las solicitudes de los clientes.

### Cómo remover la numeración Bates

```csharp
static void Demo03()
{
    Document doc = new Document(@"C:\Samples\Sample-Document03.pdf");
    foreach (var page in doc.Pages)
    {
        var batesNum = page.Artifacts.First(ar => ar.CustomSubtype == "BatesN");
        page.Artifacts.Delete(batesNum);
    }
    doc.Save(@"C:\Samples\Sample-Document04.pdf");
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para la biblioteca .NET",
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

