---
title: Trabalhando com Títulos em PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
url: /pt/net/working-with-headings/
weight: 70
description: Crie numeração nos títulos do seu documento PDF com C#. Aspose.PDF for .NET oferece diferentes tipos de estilos de numeração.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Headings in PDF",
    "alternativeHeadline": "Enhance PDF Headings with Custom Numbering Styles",
    "abstract": "Aprimore seus documentos PDF com numeração de títulos personalizável usando Aspose.PDF for .NET. Este novo recurso permite que você aplique vários estilos de numeração pré-definidos, como números romanos e listagens alfabéticas, para organizar seus títulos de forma eficaz, melhorando a legibilidade e a estrutura do documento. Agilize seu processo de criação de PDF integrando essa funcionalidade versátil em suas aplicações C#",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF, C#, headings in PDF, numbering style, Aspose.PDF for .NET, pre-defined numbering styles, NumberingStyle enumeration, document generation, Heading class, pdf document manipulation",
    "wordcount": "453",
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
    "url": "/net/working-with-headings/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-headings/"
    },
    "dateModified": "2024-11-25",
    "description": "Crie numeração nos títulos do seu documento PDF com C#. Aspose.PDF for .NET oferece diferentes tipos de estilos de numeração."
}
</script>

## Aplicar Estilo de Numeração em Títulos

Os títulos são partes importantes de qualquer documento. Os escritores sempre tentam tornar os títulos mais proeminentes e significativos para seus leitores. Se houver mais de um título em um documento, um escritor tem várias opções para organizar esses títulos. Uma das abordagens mais comuns para organizar títulos é escrever títulos em Estilo de Numeração.

[Aspose.PDF for .NET](/pdf/pt/net/) oferece muitos estilos de numeração pré-definidos. Esses estilos de numeração pré-definidos são armazenados em uma enumeração, NumberingStyle. Os valores pré-definidos da enumeração NumberingStyle e suas descrições são dados abaixo:

|**Tipos de Títulos**|**Descrição**|
| :- | :- |
|NumeraisÁrabes|Tipo árabe, por exemplo, 1,1.1,...|
|NumeraisRomanosMaiúsculos|Tipo romano maiúsculo, por exemplo, I,I.II, ...|
|NumeraisRomanosMinúsculos|Tipo romano minúsculo, por exemplo, i,i.ii, ...|
|LetrasMaiúsculas|Tipo inglês maiúsculo, por exemplo, A,A.B, ...|
|LetrasMinúsculas|Tipo inglês minúsculo, por exemplo, a,a.b, ...|
A propriedade **Style** da classe **Aspose.Pdf.Heading** é usada para definir os estilos de numeração dos títulos.

|**Figura: Estilos de numeração pré-definidos**|
| :- |
O código fonte, para obter a saída mostrada na figura acima, é dado abaixo no exemplo.

O próximo trecho de código também funciona com a biblioteca [Aspose.Drawing](/pdf/pt/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ApplyNumberStyleToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.PageInfo.Width = 612.0;
        document.PageInfo.Height = 792.0;
        document.PageInfo.Margin = new Aspose.Pdf.MarginInfo();
        document.PageInfo.Margin.Left = 72;
        document.PageInfo.Margin.Right = 72;
        document.PageInfo.Margin.Top = 72;
        document.PageInfo.Margin.Bottom = 72;

        // Add page
        var pdfPage = document.Pages.Add();
        pdfPage.PageInfo.Width = 612.0;
        pdfPage.PageInfo.Height = 792.0;
        pdfPage.PageInfo.Margin = new Aspose.Pdf.MarginInfo();
        pdfPage.PageInfo.Margin.Left = 72;
        pdfPage.PageInfo.Margin.Right = 72;
        pdfPage.PageInfo.Margin.Top = 72;
        pdfPage.PageInfo.Margin.Bottom = 72;

        // Create a floating box with the same margin as the page
        var floatBox = new Aspose.Pdf.FloatingBox();
        floatBox.Margin = pdfPage.PageInfo.Margin;

        // Add the floating box to the page
        pdfPage.Paragraphs.Add(floatBox);

        // Add headings with numbering styles
        var heading = new Aspose.Pdf.Heading(1);
        heading.IsInList = true;
        heading.StartNumber = 1;
        heading.Text = "List 1";
        heading.Style = Aspose.Pdf.NumberingStyle.NumeralsRomanLowercase;
        heading.IsAutoSequence = true;
        floatBox.Paragraphs.Add(heading);

        var heading2 = new Aspose.Pdf.Heading(1);
        heading2.IsInList = true;
        heading2.StartNumber = 13;
        heading2.Text = "List 2";
        heading2.Style = Aspose.Pdf.NumberingStyle.NumeralsRomanLowercase;
        heading2.IsAutoSequence = true;
        floatBox.Paragraphs.Add(heading2);

        var heading3 = new Aspose.Pdf.Heading(2);
        heading3.IsInList = true;
        heading3.StartNumber = 1;
        heading3.Text = "the value, as of the effective date of the plan, of property to be distributed under the plan on account of each allowed";
        heading3.Style = Aspose.Pdf.NumberingStyle.LettersLowercase;
        heading3.IsAutoSequence = true;
        floatBox.Paragraphs.Add(heading3);

        // Save PDF document
        document.Save(dataDir + "ApplyNumberStyle_out.pdf");
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