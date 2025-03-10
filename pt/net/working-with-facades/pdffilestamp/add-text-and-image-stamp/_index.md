---
title: Adicionar Carimbo de Texto e Imagem
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /pt/net/add-text-and-image-stamp/
description: Esta seção explica como adicionar Carimbo de Texto e Imagem com Aspose.PDF Facades usando a Classe PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Text and Image Stamp",
    "alternativeHeadline": "Add Custom Text and Image Stamps in PDFs",
    "abstract": "Os recursos de Adicionar Carimbo de Texto e Imagem em Aspose.PDF for .NET permitem que os usuários apliquem facilmente carimbos de texto e imagem personalizados em todas ou em páginas específicas de documentos PDF. Essa funcionalidade melhora a personalização do documento, permitindo um controle detalhado sobre atributos do carimbo, como posição, rotação e qualidade, melhorando, em última análise, a apresentação e a marcação de seus arquivos PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1435",
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
    "url": "/net/add-text-and-image-stamp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-text-and-image-stamp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Adicionar Carimbo de Texto em Todas as Páginas de um Arquivo PDF

A classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) permite que você adicione um carimbo de texto em todas as páginas de um arquivo PDF. Para adicionar um carimbo de texto, você primeiro precisa criar objetos das classes [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) e [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Você também precisa criar o carimbo de texto usando o método [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) da classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Você pode definir outros atributos como origem, rotação, fundo, etc., usando o objeto [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) também. Em seguida, você pode adicionar o carimbo no arquivo PDF usando o método [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Por fim, salve o arquivo PDF de saída usando o método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). O seguinte trecho de código mostra como adicionar um carimbo de texto em todas as páginas de um arquivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampOnAllPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Hello World!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Helvetica,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            true,
            14));

        stamp.SetOrigin(10, 400);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddTextStampOnAllPages_out.pdf");
    }
}
```

## Adicionar Carimbo de Texto em Páginas Específicas de um Arquivo PDF

A classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) permite que você adicione um carimbo de texto em páginas específicas de um arquivo PDF. Para adicionar um carimbo de texto, você primeiro precisa criar objetos das classes [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) e [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Você também precisa criar o carimbo de texto usando o método [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) da classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Você pode definir outros atributos como origem, rotação, fundo, etc., usando o objeto [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) também. Como você deseja adicionar um carimbo de texto em páginas específicas do arquivo PDF, você também precisa definir a propriedade [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) da classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Esta propriedade requer um array de inteiros contendo os números das páginas nas quais você deseja adicionar o carimbo. Em seguida, você pode adicionar o carimbo no arquivo PDF usando o método [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Por fim, salve o arquivo PDF de saída usando o método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). O seguinte trecho de código mostra como adicionar um carimbo de texto em páginas específicas de um arquivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampOnParticularPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Hello World!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Helvetica,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            true,
            14));
        stamp.SetOrigin(10, 400);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Set particular pages (page 2)
        stamp.Pages = new[] { 2 };

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddTextStampOnParticularPages_out.pdf");
    }
}
```

## Adicionar Carimbo de Imagem em Todas as Páginas de um Arquivo PDF

A classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) permite que você adicione um carimbo de imagem em todas as páginas de um arquivo PDF. Para adicionar um carimbo de imagem, você primeiro precisa criar objetos das classes [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) e [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Você também precisa criar o carimbo de imagem usando o método [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) da classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Você pode definir outros atributos como origem, rotação, fundo, etc., usando o objeto [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) também. Em seguida, você pode adicionar o carimbo no arquivo PDF usando o método [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Por fim, salve o arquivo PDF de saída usando o método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). O seguinte trecho de código mostra como adicionar um carimbo de imagem em todas as páginas de um arquivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageStampOnAllPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindImage(dataDir + "StampImage.png");
        stamp.SetOrigin(10, 200);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Set particular pages (page 2)
        stamp.Pages = new[] { 2 };

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddImageStampOnAllPages_out.pdf");
    }
}
```

### Controlar a qualidade da imagem ao adicionar como carimbo

Ao adicionar uma imagem como objeto de carimbo, você também pode controlar a qualidade da imagem. Para atender a esse requisito, a propriedade Quality foi adicionada à classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Ela indica a qualidade da imagem em porcentagens (valores válidos são 0..100).

## Adicionar Carimbo de Imagem em Páginas Específicas de um Arquivo PDF

A classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) permite que você adicione um carimbo de imagem em páginas específicas de um arquivo PDF. Para adicionar um carimbo de imagem, você primeiro precisa criar objetos das classes [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) e [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Você também precisa criar o carimbo de imagem usando o método [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) da classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Você pode definir outros atributos como origem, rotação, fundo, etc., usando o objeto [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) também. Como você deseja adicionar um carimbo de imagem em páginas específicas do arquivo PDF, você também precisa definir a propriedade [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) da classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Esta propriedade requer um array de inteiros contendo os números das páginas nas quais você deseja adicionar o carimbo. Em seguida, você pode adicionar o carimbo no arquivo PDF usando o método [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Por fim, salve o arquivo PDF de saída usando o método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). O seguinte trecho de código mostra como adicionar um carimbo de imagem em páginas específicas de um arquivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageStampOnParticularPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindImage(dataDir + "StampImage.png");
        stamp.SetOrigin(10, 200);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddImageStampOnParticularPages_out.pdf");
    }
}
```