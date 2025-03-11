---
title: Postando Dados do AcroForm
linktitle: Postando AcroForm
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /pt/net/posting-acroform-data/
description: Você pode importar e exportar dados de formulário para um arquivo XML com o namespace Aspose.Pdf.Facades em Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Posting AcroForm Data",
    "alternativeHeadline": "Post AcroForm Data",
    "abstract": "Apresentando um novo recurso poderoso em Aspose.PDF for .NET, a capacidade de postar dados do AcroForm. Essa funcionalidade permite que os desenvolvedores não apenas criem e editem AcroForms, mas também importem e exportem dados de formulário para arquivos XML, aprimorando as capacidades de processamento e armazenamento de dados dentro das aplicações.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Posting AcroForm Data, Import and Export Form Data, Aspose.PDF for .NET, AcroForm Fields, Submit Button, External Web Page Integration, Form Data Posting, XML File Handling, FieldType.Text, Database Saving",
    "wordcount": "400",
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
    "url": "/net/posting-acroform-data/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/posting-acroform-data/"
    },
    "dateModified": "2024-11-25",
    "description": "Você pode importar e exportar dados de formulário para um arquivo XML com o namespace Aspose.Pdf.Facades em Aspose.PDF for .NET."
}
</script>

{{% alert color="primary" %}}

AcroForm é um tipo importante do documento PDF. Você pode não apenas criar e editar um AcroForm usando o [namespace Aspose.Pdf.Facades](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace), mas também importar e exportar dados de formulário para um arquivo XML. O namespace Aspose.Pdf.Facades em Aspose.PDF for .NET permite que você implemente outro recurso do AcroForm, que ajuda você a postar dados do AcroForm em uma página da web externa. Esta página da web então lê as variáveis postadas e usa esses dados para processamento adicional. Este recurso é útil nos casos em que você não deseja apenas manter os dados no arquivo PDF, mas sim enviá-los para o seu servidor e, em seguida, salvá-los em um banco de dados, etc.

{{% /alert %}}

## Detalhes da implementação

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

Neste artigo, tentamos criar um AcroForm usando o [namespace Aspose.Pdf.Facades](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace). Também adicionamos um botão de envio e definimos sua URL de destino. Os seguintes trechos de código mostram como criar o formulário e, em seguida, receber os dados postados na página da web.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateAcroFormWithFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create an instance of FormEditor class and bind input and output pdf files
    using (var editor = new Aspose.Pdf.Facades.FormEditor(dataDir + "input.pdf", dataDir + "output.pdf"))
    {
        // Create AcroForm fields - I have created only two fields for simplicity
        editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "firstname", 1, 100, 600, 200, 625);
        editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "lastname", 1, 100, 550, 200, 575);

        // Add a submit button and set target URL
        editor.AddSubmitBtn("submitbutton", 1, "Submit", "http://localhost/csharptesting/show.aspx", 100, 450, 150, 475);

        // Save PDF document
        editor.Save();
    }
}
```

{{% alert color="primary" %}}

O seguinte trecho de código mostra como receber os valores postados na página da web de destino. Neste exemplo, usei uma página chamada Show.aspx e adicionei um código simples de uma linha no método de carregamento da página.

{{% /alert %}}

```csharp
// Show the posted values on the target web page
Response.Write("Hello " + Request.Form.Get("firstname") + " " + Request.Form.Get("lastname"));
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