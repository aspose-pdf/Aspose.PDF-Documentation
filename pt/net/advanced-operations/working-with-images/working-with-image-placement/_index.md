---
title: Trabalhando com Colocação de Imagens
linktitle: Trabalhando com Colocação de Imagens
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /pt/net/working-with-image-placement/
description: Esta seção descreve os recursos de trabalhar com arquivos PDF de colocação de imagens usando a biblioteca C#.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Image Placement",
    "alternativeHeadline": "Enhanced Image Placement in PDF",
    "abstract": "O novo recurso de colocação de imagens em Aspose.PDF for .NET permite que os desenvolvedores posicionem e manipulem imagens de forma eficiente dentro de documentos PDF. Essa funcionalidade inclui classes como ImagePlacement e ImagePlacementAbsorber, permitindo a recuperação precisa das dimensões e resolução da imagem, aprimorando as capacidades de geração de documentos PDF com maior controle sobre elementos visuais.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Image Placement, C# library, Aspose.PDF, ImagePlacement, ImagePlacementAbsorber, PDF document generation, image resolution, image properties, bitmap scaling, PDF manipulation",
    "wordcount": "306",
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
    "url": "/net/working-with-image-placement/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-image-placement/"
    },
    "dateModified": "2024-11-26",
    "description": "Esta seção descreve os recursos de trabalhar com arquivos PDF de colocação de imagens usando a biblioteca C#."
}
</script>

Com o lançamento de Aspose.PDF for .NET 7.0.0, introduzimos classes chamadas [ImagePlacement](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacement), [ImagePlacementAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacementabsorber) e [ImagePlacementCollection](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacementcollection) que fornecem capacidade semelhante às classes descritas acima para obter a resolução e a posição de uma imagem em um documento PDF.

- ImagePlacementAbsorber realiza a busca de uso de imagem como a coleção de objetos ImagePlacement.
- ImagePlacement fornece os membros Resolution e Rectangle que retornam os valores reais de colocação da imagem.

O próximo trecho de código também trabalha com a biblioteca [Aspose.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractAndScaleImagesFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImagePlacement.pdf"))
    {
        var abs = new Aspose.Pdf.ImagePlacementAbsorber();

        // Load the contents of the first page
        document.Pages[1].Accept(abs);

        // Iterate through each image placement on the first page
        foreach (var imagePlacement in abs.ImagePlacements)
        {
            // Get image properties
            Console.Out.WriteLine("image width: " + imagePlacement.Rectangle.Width);
            Console.Out.WriteLine("image height: " + imagePlacement.Rectangle.Height);
            Console.Out.WriteLine("image LLX: " + imagePlacement.Rectangle.LLX);
            Console.Out.WriteLine("image LLY: " + imagePlacement.Rectangle.LLY);
            Console.Out.WriteLine("image horizontal resolution: " + imagePlacement.Resolution.X);
            Console.Out.WriteLine("image vertical resolution: " + imagePlacement.Resolution.Y);
        }
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