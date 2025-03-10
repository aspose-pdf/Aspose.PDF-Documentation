---
title: Rotacionando carimbo em torno do ponto central
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /pt/net/rotating-stamp-about-the-center-point/
description: Esta seção explica como rotacionar um carimbo em torno do ponto central usando a classe Stamp.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Rotating stamp about the center point",
    "alternativeHeadline": "Rotate Stamps Precisely Around Their Center Point",
    "abstract": "O recurso em Aspose.PDF for .NET permite que os usuários girem carimbos dentro de arquivos PDF precisamente em torno de seu ponto central. Utilizando a classe Stamp, os desenvolvedores podem facilmente definir valores de rotação de 0 a 360 graus, aumentando a flexibilidade e personalização da colocação de marcas d'água em documentos. Essa funcionalidade é ideal para criar PDFs visualmente dinâmicos com orientações de carimbo personalizadas.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "339",
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
    "url": "/net/rotating-stamp-about-the-center-point/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/rotating-stamp-about-the-center-point/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

{{% alert color="primary" %}}

[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) em [Aspose.PDF for .NET](/pdf/net/) permite que você adicione um carimbo em um arquivo PDF existente. Às vezes, os usuários precisam rotacionar o carimbo. Neste artigo, veremos como rotacionar um carimbo em torno de seu ponto central.

{{% /alert %}}

## Detalhes da implementação

A classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) permite que você adicione uma marca d'água em um arquivo PDF. Você pode especificar a imagem a ser adicionada como um carimbo usando o método [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.stamp/bindimage/methods/1). O método [SetOrigin](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setorigin) permite que você defina a origem do carimbo adicionado; essa origem é as coordenadas do canto inferior esquerdo do carimbo. Você também pode definir o tamanho da imagem usando o método [SetImageSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setimagesize).

Agora, veremos como o carimbo pode ser rotacionado em torno do centro do carimbo. A classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) fornece uma propriedade chamada Rotation. Essa propriedade define ou obtém a rotação de 0 a 360 do conteúdo do carimbo. Podemos especificar qualquer valor de rotação de 0 a 360. Ao especificar o valor de rotação, podemos girar o carimbo em torno de seu ponto central. Se um Stamp for um objeto do tipo Stamp, então o valor de rotação pode ser especificado como aStamp.Rotation = 90. Nesse caso, o carimbo será rotacionado em 90 graus em torno do centro do conteúdo do carimbo. O seguinte trecho de código mostra como rotacionar o carimbo em torno do ponto central:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRotatingStampToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();  

    // Create PdfFileInfo object to get height and width of the pages
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "RotatingStamp.pdf"))
    {
        // Create Stamp object
        var aStamp = new Aspose.Pdf.Facades.Stamp();

        // Bind image file with the Stamp object
        aStamp.BindImage(dataDir + "RotatingStamp.jpg");

        // Specify whether the stamp will be added as a background or not
        aStamp.IsBackground = false;

        // Specifies at which pages to add the watermark
        aStamp.Pages = new int[] { 1 };

        // Specifies the watermark rotation - rotate at 90 degrees
        aStamp.Rotation = 90;

        // Specifies the position of stamp - lower left corner of the stamp
        aStamp.SetOrigin(fileInfo.GetPageWidth(1) / 2, fileInfo.GetPageHeight(1) / 2);

        // Set the size of the watermark
        aStamp.SetImageSize(100, 100);

        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "RotatingStamp_out.pdf"))
        {
            // Create PdfFileStamp class to bind input and output files
            using (var stamper = new Aspose.Pdf.Facades.PdfFileStamp(document))
            {
                // Add the stamp in the PDF file
                stamper.AddStamp(aStamp);
            }
        }
    }
}
```