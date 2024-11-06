---
title: Obter e Pesquisar Imagens em PDF
linktitle: Pesquisar e Obter Imagens
type: docs
weight: 60
url: pt/net/search-and-get-images-from-pdf-document/
description: Esta seção explica como pesquisar e obter imagens de um documento PDF com a biblioteca Aspose.PDF.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Obter e Pesquisar Imagens em PDF",
    "alternativeHeadline": "Como Obter e Pesquisar Imagens em um arquivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, .net, obter imagem, pesquisar imagem",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe de Documentação Aspose.PDF",
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
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/search-and-get-images-from-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/search-and-get-images-from-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta seção explica como pesquisar e obter imagens de um documento PDF com a biblioteca Aspose.PDF."
}
</script>
O ImagePlacementAbsorber permite que você procure por imagens em todas as páginas de um documento PDF.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

Para procurar um documento inteiro por imagens:

1. Chame o método Accept da coleção Pages. O método Accept recebe um objeto ImagePlacementAbsorber como parâmetro. Isso retorna uma coleção de objetos ImagePlacement.
1. Percorra os objetos ImagePlacements e obtenha suas propriedades (Imagem, dimensões, resolução e assim por diante).

O seguinte trecho de código mostra como procurar um documento por todas as suas imagens.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Abrir documento
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "SearchAndGetImages.pdf");

// Criar objeto ImagePlacementAbsorber para realizar a busca de colocação de imagem
ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

// Aceitar o absorvedor para todas as páginas
doc.Pages.Accept(abs);

// Percorrer todas as colocações de imagens, obter imagem e propriedades de ImagePlacement
foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
{
    // Obter a imagem usando o objeto ImagePlacement
    XImage image = imagePlacement.Image;

    // Exibir propriedades de colocação de imagem para todas as colocações
    Console.Out.WriteLine("largura da imagem:" + imagePlacement.Rectangle.Width);
    Console.Out.WriteLine("altura da imagem:" + imagePlacement.Rectangle.Height);
    Console.Out.WriteLine("LLX da imagem:" + imagePlacement.Rectangle.LLX);
    Console.Out.WriteLine("LLY da imagem:" + imagePlacement.Rectangle.LLY);
    Console.Out.WriteLine("resolução horizontal da imagem:" + imagePlacement.Resolution.X);
    Console.Out.WriteLine("resolução vertical da imagem:" + imagePlacement.Resolution.Y);
}
```
Para obter uma imagem de uma página individual, use o seguinte código:

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
doc.Pages[1].Accept(abs);
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
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
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
    "applicationCategory": "Biblioteca de manipulação de PDF para .NET",
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


