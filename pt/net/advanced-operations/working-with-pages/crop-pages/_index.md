---
title: Recortar páginas PDF programaticamente C#
linktitle: Recortar Páginas
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /pt/net/crop-pages/
description: Você pode obter propriedades da página, como largura, altura, bleed-, crop- e trimbox usando Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Crop PDF Pages programmatically C#",
    "alternativeHeadline": "Crop PDF Pages Easily with Aspose.PDF for .NET",
    "abstract": "Aspose.PDF for .NET introduz um novo recurso poderoso que permite aos desenvolvedores acessar e manipular programaticamente várias propriedades de página de um PDF, incluindo a media box, bleed box, trim box, art box e crop box. Essa funcionalidade simplifica o processo de personalização de layouts PDF, garantindo precisão na apresentação do documento e melhorando a qualidade de impressão enquanto minimiza bordas brancas. Com trechos de código fáceis de usar, os usuários podem integrar essas capacidades em suas aplicações, melhorando o gerenciamento e a manipulação de PDFs.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "494",
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
    "url": "/net/crop-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/crop-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "Você pode obter propriedades da página, como largura, altura, bleed-, crop- e trimbox usando Aspose.PDF for .NET."
}
</script>

## Obter Propriedades da Página

Cada página em um arquivo PDF possui um número de propriedades, como largura, altura, bleed-, crop- e trimbox. Aspose.PDF permite que você acesse essas propriedades.

- **Media box**: A media box é a maior caixa de página. Ela corresponde ao tamanho da página (por exemplo, A4, A5, US Letter, etc.) selecionado quando o documento foi impresso em PostScript ou PDF. Em outras palavras, a media box determina o tamanho físico do meio no qual o documento PDF é exibido ou impresso.
- **Bleed box**: Se o documento tiver bleed, o PDF também terá uma bleed box. Bleed é a quantidade de cor (ou arte) que se estende além da borda de uma página. É usado para garantir que, quando o documento é impresso e cortado para o tamanho ("trimmed"), a tinta vá até a borda da página. Mesmo que a página seja mal cortada - cortada ligeiramente fora das marcas de corte - nenhuma borda branca aparecerá na página.
- **Trim box**: A trim box indica o tamanho final de um documento após impressão e corte.
- **Art box**: A art box é a caixa desenhada ao redor do conteúdo real das páginas em seus documentos. Esta caixa de página é usada ao importar documentos PDF em outras aplicações.
- **Crop box**: A crop box é o tamanho da "página" em que seu documento PDF é exibido no Adobe Acrobat. Na visualização normal, apenas o conteúdo da crop box é exibido no Adobe Acrobat. Para descrições detalhadas dessas propriedades, leia a especificação Adobe.Pdf, particularmente 10.10.1 Limites da Página.
- **Page.Rect**: a interseção (comumente retângulo visível) da MediaBox e DropBox. A imagem abaixo ilustra essas propriedades.
Para mais detalhes, visite [esta página](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

O trecho abaixo mostra como recortar a página:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CropPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CropPageInput.pdf"))
    {
        Console.WriteLine(document.Pages[1].CropBox);
        Console.WriteLine(document.Pages[1].TrimBox);
        Console.WriteLine(document.Pages[1].ArtBox);
        Console.WriteLine(document.Pages[1].BleedBox);
        Console.WriteLine(document.Pages[1].MediaBox);
        // Create new Box rectangle
        var newBox = new Rectangle(200, 220, 2170, 1520);
        document.Pages[1].CropBox = newBox;
        document.Pages[1].TrimBox = newBox;
        document.Pages[1].ArtBox = newBox;
        document.Pages[1].BleedBox = newBox;
        // Save PDF document
        document.Save(dataDir + "CropPage_out.pdf");  
    }
}
```

Neste exemplo, usamos um arquivo de amostra [aqui](crop_page.pdf). Inicialmente, nossa página parece como mostrado na Figura 1.

Após a alteração, a página parecerá com a Figura 2.

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