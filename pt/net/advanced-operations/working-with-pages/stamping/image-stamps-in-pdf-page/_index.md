---
title: Adicionar selos de imagem em PDF usando C#
linktitle: Selos de imagem em arquivo PDF
type: docs
weight: 10
url: /pt/net/image-stamps-in-pdf-page/
description: Adicionar o Selo de Imagem no seu documento PDF usando a classe ImageStamp com a biblioteca Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adicionar selos de imagem em PDF usando C#",
    "alternativeHeadline": "Adicionar selos de imagem em PDF usando C#",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, c#, geração de documento",
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
    "url": "/net/image-stamps-in-pdf-page/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/image-stamps-in-pdf-page/"
    },
    "dateModified": "2022-02-04",
    "description": "Adicionar o Selo de Imagem no seu documento PDF usando a classe ImageStamp com a biblioteca Aspose.PDF."
}
</script>
## Adicionar Carimbo de Imagem em Arquivo PDF

Você pode usar a classe ImageStamp para adicionar um carimbo de imagem a um arquivo PDF. A classe ImageStamp fornece as propriedades necessárias para criar um carimbo baseado em imagem, como altura, largura, opacidade e assim por diante.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

Para adicionar um carimbo de imagem:

1. Crie um objeto Document e um objeto ImageStamp usando as propriedades necessárias.
1. Chame o método AddStamp da classe Page para adicionar o carimbo ao PDF.

O seguinte trecho de código mostra como adicionar o carimbo de imagem no arquivo PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Abrir documento
Document pdfDocument = new Document(dataDir+ "AddImageStamp.pdf");

// Criar carimbo de imagem
ImageStamp imageStamp = new ImageStamp(dataDir + "aspose-logo.jpg");
imageStamp.Background = true;
imageStamp.XIndent = 100;
imageStamp.YIndent = 100;
imageStamp.Height = 300;
imageStamp.Width = 300;
imageStamp.Rotate = Rotation.on270;
imageStamp.Opacity = 0.5;
// Adicionar carimbo a uma página específica
pdfDocument.Pages[1].AddStamp(imageStamp);

dataDir = dataDir + "AddImageStamp_out.pdf";
// Salvar documento de saída
pdfDocument.Save(dataDir);
```
## Controle a Qualidade da Imagem ao Adicionar Carimbo

Ao adicionar uma imagem como um objeto de carimbo, você pode controlar a qualidade da imagem. A propriedade Quality da classe ImageStamp é usada para esse propósito. Ela indica a qualidade da imagem em porcentagens (valores válidos são de 0 a 100).

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Abrir documento
Document pdfDocument = new Document(dataDir+ "AddImageStamp.pdf");

// Criar carimbo de imagem
ImageStamp imageStamp = new ImageStamp(dataDir + "aspose-logo.jpg");

imageStamp.Quality = 10;
pdfDocument.Pages[1].AddStamp(imageStamp);
pdfDocument.Save(dataDir + "ControlImageQuality_out.pdf");
```

## Carimbo de Imagem como Fundo em Caixa Flutuante

A API Aspose.PDF permite adicionar carimbo de imagem como fundo em uma caixa flutuante.
A API Aspose.PDF permite adicionar um selo de imagem como fundo em uma caixa flutuante.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Instanciar objeto Document
Document doc = new Document();
// Adicionar página ao documento PDF
Page page = doc.Pages.Add();
// Criar objeto FloatingBox
FloatingBox aBox = new FloatingBox(200, 100);
// Definir posição esquerda para FloatingBox
aBox.Left = 40;
// Definir posição superior para FloatingBox
aBox.Top = 80;
// Definir o alinhamento horizontal para FloatingBox
aBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Adicionar fragmento de texto à coleção de parágrafos de FloatingBox
aBox.Paragraphs.Add(new TextFragment("texto principal"));
// Definir borda para FloatingBox
aBox.Border = new BorderInfo(BorderSide.All, Aspose.Pdf.Color.Red);
// Adicionar imagem de fundo
aBox.BackgroundImage = new Image
{
    File = dataDir + "aspose-logo.jpg"
};
// Definir cor de fundo para FloatingBox
aBox.BackgroundColor = Aspose.Pdf.Color.Yellow;
// Adicionar FloatingBox à coleção de parágrafos do objeto de página
page.Paragraphs.Add(aBox);
// Salvar o documento PDF
doc.Save(dataDir + "AddImageStampAsBackgroundInFloatingBox_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para Biblioteca .NET",
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
```

