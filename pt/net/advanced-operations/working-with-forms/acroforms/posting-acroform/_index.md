---
title: Posting AcroForm Data
linktitle: Posting AcroForm
type: docs
weight: 50
url: /pt/net/posting-acroform-data/
description: Você pode importar e exportar dados de formulário para um arquivo XML com o namespace Aspose.Pdf.Facades no Aspose.PDF para .NET.
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
    "alternativeHeadline": "Importar e Exportar dados de formulário para arquivo XML",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, posting acroform data",
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
    "url": "/net/posting-acroform-data/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/posting-acroform-data/"
    },
    "dateModified": "2022-02-04",
    "description": "Você pode importar e exportar dados de formulário para um arquivo XML com o namespace Aspose.Pdf.Facades no Aspose.PDF para .NET."
}
</script>

{{% alert color="primary" %}}

AcroForm é um tipo importante de documento PDF. Você pode não apenas criar e editar um AcroForm usando o [namespace Aspose.Pdf.Facades](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace), mas também importar e exportar dados de formulário para um arquivo XML. O namespace Aspose.Pdf.Facades no Aspose.PDF para .NET permite que você implemente outra funcionalidade do AcroForm, que ajuda você a enviar os dados de um AcroForm para uma página web externa. Esta página web então lê as variáveis postadas e usa esses dados para processamento adicional. Esta funcionalidade é útil nos casos em que você não quer apenas manter os dados no arquivo PDF, mas também enviá-los para o seu servidor e então salvá-los em um banco de dados, etc.

{{% /alert %}}

## Detalhes da Implementação

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

Neste artigo, tentamos criar um AcroForm usando o [namespace Aspose.Pdf.Facades](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace).
Neste artigo, tentamos criar um AcroForm usando [Aspose.Pdf.Facades namespace](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace).

```csharp
// Cria uma instância da classe FormEditor e vincula os arquivos pdf de entrada e saída
Aspose.Pdf.Facades.FormEditor editor = new Aspose.Pdf.Facades.FormEditor("input.pdf","output.pdf");

// Cria campos AcroForm - Criei apenas dois campos para simplificar
editor.AddField(Aspose.PDF.Facades.FieldType.Text, "firstname", 1, 100, 600, 200, 625);
editor.AddField(Aspose.PDF.Facades.FieldType.Text, "lastname", 1, 100, 550, 200, 575);

// Adiciona um botão de envio e define a URL de destino
editor.AddSubmitBtn("submitbutton", 1, "Submit", "http://localhost/csharptesting/show.aspx", 100, 450, 150, 475);

// Salva o arquivo pdf de saída
editor.Save();
```

{{% alert color="primary" %}}

O trecho de código a seguir mostra como receber os valores postados na página web de destino.
O seguinte trecho de código mostra como receber os valores postados na página web de destino.
{{% /alert %}}

```csharp
// Exibe os valores postados na página web de destino
Response.Write("Olá " + Request.Form.Get("firstname") + " " + Request.Form.Get("lastname"));
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
    "applicationCategory": "Biblioteca de Manipulação de PDF para .NET",
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

