---
title: Adicionar carimbos de imagem em PDF usando C#
linktitle: Carimbos de imagem em arquivo PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/image-stamps-in-pdf-page/
description: Adicione o carimbo de imagem no seu documento PDF usando a classe ImageStamp com a biblioteca Aspose.PDF.
lastmod: "2024-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Image stamps in PDF using C#",
    "alternativeHeadline": "Add Custom Image Stamps to PDF Documents",
    "abstract": "O novo recurso na biblioteca Aspose.PDF permite que os usuários adicionem carimbos de imagem a documentos PDF usando C#. Com a classe ImageStamp, os desenvolvedores podem personalizar atributos como tamanho, opacidade e qualidade, melhorando significativamente a apresentação e acessibilidade do documento. Essa funcionalidade também inclui a capacidade de adicionar texto alternativo, promovendo melhor usabilidade para leitores de tela.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "646",
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
    "url": "/net/image-stamps-in-pdf-page/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/image-stamps-in-pdf-page/"
    },
    "dateModified": "2024-11-26",
    "description": "Adicione o carimbo de imagem no seu documento PDF usando a classe ImageStamp com a biblioteca Aspose.PDF."
}
</script>

## Adicionar carimbo de imagem em arquivo PDF

Você pode usar a classe ImageStamp para adicionar um carimbo de imagem a um arquivo PDF. A classe ImageStamp fornece as propriedades necessárias para criar um carimbo baseado em imagem, como altura, largura, opacidade e assim por diante.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

Para adicionar um carimbo de imagem:

1. Crie um objeto Document e um objeto ImageStamp usando as propriedades necessárias.
1. Chame o método AddStamp da classe Page para adicionar o carimbo ao PDF.

O seguinte trecho de código mostra como adicionar um carimbo de imagem no arquivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageStampInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageStampInput.pdf"))
    {
        // Create image stamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg");
        imageStamp.Background = true;
        imageStamp.XIndent = 100;
        imageStamp.YIndent = 100;
        imageStamp.Height = 300;
        imageStamp.Width = 300;
        imageStamp.Rotate = Rotation.on270;
        imageStamp.Opacity = 0.5;
        // Add stamp to particular page
        document.Pages[1].AddStamp(imageStamp);
        // Save PDF document
        document.Save(dataDir + "AddImageStamp_out.pdf");
    }
}
```

## Controlar a qualidade da imagem ao adicionar o carimbo

Ao adicionar uma imagem como um objeto de carimbo, você pode controlar a qualidade da imagem. A propriedade Quality da classe ImageStamp é usada para esse propósito. Ela indica a qualidade da imagem em porcentagens (valores válidos são 0..100).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ControlImageQualityWhenAddingStamp()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageStampInput.pdf"))
    {
        // Create image stamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg");
        imageStamp.Quality = 10;
        document.Pages[1].AddStamp(imageStamp);
        // Save PDF document
        document.Save(dataDir + "ControlImageQuality_out.pdf");
    }
}
```

## Carimbo de imagem como fundo em caixa flutuante

A API Aspose.PDF permite que você adicione um carimbo de imagem como fundo em uma caixa flutuante. A propriedade BackgroundImage da classe FloatingBox pode ser usada para definir o carimbo de imagem de fundo para uma caixa flutuante, conforme mostrado no seguinte exemplo de código.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImageStampAsBackgroundInFloatingBox()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to PDF document
        Page page = document.Pages.Add();
        // Create FloatingBox object
        var aBox = new Aspose.Pdf.FloatingBox(200, 100);
        // Set left position for FloatingBox
        aBox.Left = 40;
        // Set Top position for FloatingBox
        aBox.Top = 80;
        // Set the Horizontal alignment for FloatingBox
        aBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        // Add text fragment to paragraphs collection of FloatingBox
        aBox.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("main text"));
        // Set border for FloatingBox
        aBox.Border = new Aspose.Pdf.BorderInfo(BorderSide.All, Aspose.Pdf.Color.Red);
        // Add background image
        aBox.BackgroundImage = new Aspose.Pdf.Image
        {
            File = dataDir + "aspose-logo.jpg"
        };
        // Set background color for FloatingBox
        aBox.BackgroundColor = Aspose.Pdf.Color.Yellow;
        // Add FloatingBox to paragraphs collection of page object
        page.Paragraphs.Add(aBox);
        // Save PDF document
        document.Save(dataDir + "AddImageStampAsBackgroundInFloatingBox_out.pdf");
    }
}
```

## Adicionar texto alternativo ao carimbo de imagem

Desde a versão 24.6, é possível adicionar texto alternativo ao carimbo de imagem.

Este código abre um arquivo PDF, adiciona uma imagem como um carimbo em uma posição específica e inclui texto alternativo para acessibilidade. O PDF atualizado é então salvo com um novo nome de arquivo.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAlternativeTextToTheImageStamp()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageStampInput.pdf"))
    {
        // Create image stamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg")
        {
            XIndent = 100,
            YIndent = 700,
            Quality = 100,
            AlternativeText = "Your alt text"  // This property added.
        };
        // Add stamp
        document.Pages[1].AddStamp(imageStamp);
        // Save PDF document
        document.Save(dataDir + "DocWithImageStamp_out.pdf");
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