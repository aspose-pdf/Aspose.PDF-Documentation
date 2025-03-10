---
title: Adicionar Cabeçalho e Rodapé ao PDF
linktitle: Adicionar Cabeçalho e Rodapé ao PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /pt/net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for .NET permite adicionar cabeçalhos e rodapés ao seu arquivo PDF usando a classe TextStamp.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/manage-header-and-footer-of-pdf-file/
    - /net/manage-header-and-footer/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Header and Footer to PDF",
    "alternativeHeadline": "Add Custom Headers and Footers to PDF Files",
    "abstract": "Aspose.PDF for .NET apresenta um recurso poderoso que permite aos usuários enriquecer seus documentos PDF adicionando cabeçalhos e rodapés personalizáveis. Usando as classes TextStamp e ImageStamp, os desenvolvedores podem facilmente integrar texto e imagens, ajustando sua colocação e aparência para se adequar a vários formatos e estilos de documentos. Isso aumenta o profissionalismo e a legibilidade do documento, tornando-o ideal para relatórios, faturas e outras comunicações formais.",
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
    "description": "Aspose.PDF for .NET permite adicionar cabeçalhos e rodapés ao seu arquivo PDF usando a classe TextStamp."
}
</script>

**Aspose.PDF for .NET** permite adicionar cabeçalho e rodapé ao seu arquivo PDF existente. Você pode adicionar imagens ou texto a um documento PDF. Além disso, tente adicionar diferentes cabeçalhos em um arquivo PDF com C#.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Adicionando Texto no Cabeçalho do Arquivo PDF

Você pode usar a classe [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp) para adicionar texto no cabeçalho de um arquivo PDF. A classe TextStamp fornece propriedades necessárias para criar um carimbo baseado em texto, como tamanho da fonte, estilo da fonte e cor da fonte, etc. Para adicionar texto no cabeçalho, você precisa criar um objeto Document e um objeto TextStamp usando as propriedades necessárias. Depois disso, você pode chamar o método AddStamp da Página para adicionar o texto no cabeçalho do PDF.

Você precisa definir a propriedade TopMargin de tal forma que ajuste o texto na área do cabeçalho do seu PDF. Você também precisa definir HorizontalAlignment como Center e VerticalAlignment como Top.

O seguinte trecho de código mostra como adicionar texto no cabeçalho de um arquivo PDF com C#.

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

## Adicionando Texto no Rodapé do Arquivo PDF

Você pode usar a classe TextStamp para adicionar texto no rodapé de um arquivo PDF. A classe TextStamp fornece propriedades necessárias para criar um carimbo baseado em texto, como tamanho da fonte, estilo da fonte e cor da fonte, etc. Para adicionar texto no rodapé, você precisa criar um objeto Document e um objeto TextStamp usando as propriedades necessárias. Depois disso, você pode chamar o método AddStamp da Página para adicionar o texto no rodapé do PDF.

{{% alert color="primary" %}}

Você precisa definir a propriedade Bottom Margin de tal forma que ajuste o texto na área do rodapé do seu PDF. Você também precisa definir HorizontalAlignment como Center e VerticalAlignment como Bottom.

{{% /alert %}}

O seguinte trecho de código mostra como adicionar texto no rodapé de um arquivo PDF com C#.

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

## Adicionando Imagem no Cabeçalho do Arquivo PDF

Você pode usar a classe [ImageStamp](https://reference.aspose.com/pdf/net/aspose.pdf/ImageStamp) para adicionar uma imagem no cabeçalho de um arquivo PDF. A classe Image Stamp fornece propriedades necessárias para criar um carimbo baseado em imagem, como tamanho da fonte, estilo da fonte e cor da fonte, etc. Para adicionar uma imagem no cabeçalho, você precisa criar um objeto Document e um objeto Image Stamp usando as propriedades necessárias. Depois disso, você pode chamar o método [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) da Página para adicionar a imagem no cabeçalho do PDF.

{{% alert color="primary" %}}

Você precisa definir a propriedade TopMargin de tal forma que ajuste a imagem na área do cabeçalho do seu PDF. Você também precisa definir HorizontalAlignment como Center e VerticalAlignment como Top.

{{% /alert %}}

O seguinte trecho de código mostra como adicionar uma imagem no cabeçalho de um arquivo PDF com C#.

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

## Adicionando Imagem no Rodapé do Arquivo PDF

Você pode usar a classe Image Stamp para adicionar uma imagem no rodapé de um arquivo PDF. A classe Image Stamp fornece propriedades necessárias para criar um carimbo baseado em imagem, como tamanho da fonte, estilo da fonte e cor da fonte, etc. Para adicionar uma imagem no rodapé, você precisa criar um objeto Document e um objeto Image Stamp usando as propriedades necessárias. Depois disso, você pode chamar o método AddStamp da Página para adicionar a imagem no rodapé do PDF.

{{% alert color="primary" %}}

Você precisa definir a propriedade [BottomMargin](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/bottommargin) de tal forma que ajuste a imagem na área do rodapé do seu PDF. Você também precisa definir [HorizontalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/horizontalalignment) como `Center` e [VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/verticalalignment) como `Bottom`.

{{% /alert %}}

O seguinte trecho de código mostra como adicionar uma imagem no rodapé de um arquivo PDF com C#.

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

## Adicionando Diferentes Cabeçalhos em um Arquivo PDF

Sabemos que podemos adicionar TextStamp na seção de Cabeçalho/Rodapé do documento usando as propriedades TopMargin ou Bottom Margin, mas às vezes podemos ter a necessidade de adicionar múltiplos cabeçalhos/rodapés em um único documento PDF. **Aspose.PDF for .NET** explica como fazer isso.

Para atender a essa necessidade, criaremos objetos TextStamp individuais (o número de objetos depende do número de Cabeçalhos/Rodapés necessários) e os adicionaremos ao documento PDF. Também podemos especificar diferentes informações de formatação para cada objeto de carimbo. No exemplo a seguir, criamos um objeto Document e três objetos TextStamp e, em seguida, usamos o método [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) da Página para adicionar o texto na seção do cabeçalho do PDF. O seguinte trecho de código mostra como adicionar uma imagem no rodapé de um arquivo PDF com Aspose.PDF for .NET.

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