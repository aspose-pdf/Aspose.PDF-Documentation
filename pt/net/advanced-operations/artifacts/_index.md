---
title: Trabalhando com Artefatos em .NET
linktitle: Trabalhando com Artefatos
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 170
url: /pt/net/artifacts/
description: Aspose.PDF for .NET permite que você adicione uma imagem de fundo às páginas PDF e obtenha cada marca d'água usando a classe Artifact.
lastmod: "2024-01-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Artifacts in .NET",
    "alternativeHeadline": "Enhance PDF Documents with Artifacts Management",
    "abstract": "Aspose.PDF for .NET introduz a classe Artifact, permitindo que os desenvolvedores gerenciem de forma integrada elementos não relacionados ao conteúdo, como imagens de fundo e marcas d'água em documentos PDF. Este recurso melhora a acessibilidade e o desempenho do documento, permitindo que tecnologias assistivas ignorem elementos decorativos, enquanto fornece opções personalizáveis para vários tipos e propriedades de artefatos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2501",
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
    "url": "/net/artifacts/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/artifacts/"
    },
    "dateModified": "2025-03-12",
    "description": "Aspose.PDF for .NET permite que você adicione uma imagem de fundo às páginas PDF e obtenha cada marca d'água usando a classe Artifact."
}
</script>

Artefatos em PDF são objetos gráficos ou outros elementos que não fazem parte do conteúdo real do documento. Eles são geralmente usados para decoração, layout ou propósitos de fundo. Exemplos de artefatos incluem cabeçalhos de página, rodapés, separadores ou imagens que não transmitem nenhum significado.

O objetivo dos artefatos em PDF é permitir a distinção entre elementos de conteúdo e não conteúdo. Isso é importante para acessibilidade, pois leitores de tela e outras tecnologias assistivas podem ignorar artefatos e se concentrar no conteúdo relevante. Artefatos também podem melhorar o desempenho e a qualidade dos documentos PDF, pois podem ser omitidos na impressão, pesquisa ou cópia.

Para criar um elemento como um artefato em PDF, você precisa usar a classe [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact).
Ela contém as seguintes propriedades úteis:

- **Artifact.Type** – obtém o tipo de artefato (suporta valores da enumeração Artifact.ArtifactType onde os valores incluem Background, Layout, Page, Pagination e Undefined).
- **Artifact.Subtype** – obtém o subtipo de artefato (suporta os valores da enumeração Artifact.ArtifactSubtype onde os valores incluem Background, Footer, Header, Undefined, Watermark).
- **Artifact.Image** – Obtém a imagem de um artefato (se uma imagem estiver presente, caso contrário, nulo).
- **Artifact.Text** – Obtém o texto de um artefato.
- **Artifact.Contents** – Obtém uma coleção de operadores internos de artefato. Seu tipo suportado é System.Collections.ICollection.
- **Artifact.Form** – Obtém o XForm de um artefato (se XForm for usado). Marcas d'água, cabeçalhos e rodapés de artefatos contêm XForm que mostra todos os conteúdos do artefato.
- **Artifact.Rectangle** – Obtém a posição de um artefato na página.
- **Artifact.Rotation** – Obtém a rotação de um artefato (em graus, valor positivo indica rotação anti-horária).
- **Artifact.Opacity** – Obtém a opacidade de um artefato. Os valores possíveis estão na faixa de 0...1, onde 1 é completamente opaco.

As seguintes classes também podem ser úteis para trabalhar com artefatos:

- [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection)
- [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/watermarkartifact/)

## Trabalhando com Marcas d'Água Existentes

Uma marca d'água criada com o Adobe Acrobat é chamada de artefato (conforme descrito na especificação PDF 14.8.2.2 Conteúdo Real e Artefatos).

Para obter todas as Marcas d'Água em uma página específica, a classe [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) possui a propriedade Artifacts.

O seguinte trecho de código mostra como obter todas as marcas d'água na primeira página de um arquivo PDF.

_Nota:_ Este código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractWatermarkFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample-w.pdf"))
    {
        // Get the watermarks from the first page artifacts
        var watermarks = document.Pages[1].Artifacts
            .Where(artifact =>
                artifact.Type == Aspose.Pdf.Artifact.ArtifactType.Pagination
                && artifact.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Watermark);

        // Iterate through the found watermark artifacts and print details
        foreach (Aspose.Pdf.WatermarkArtifact item in watermarks.Cast<Aspose.Pdf.WatermarkArtifact>())
        {
            Console.WriteLine($"{item.Text} {item.Rectangle}");
        }
    }
}
```

## Trabalhando com Fundos como Artefatos

Imagens de fundo podem ser usadas para adicionar uma marca d'água ou outro design sutil a documentos. Em Aspose.PDF for .NET, cada documento PDF é uma coleção de páginas e cada página contém uma coleção de artefatos. A classe [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact) pode ser usada para adicionar uma imagem de fundo a um objeto de página.

O seguinte trecho de código mostra como adicionar uma imagem de fundo às páginas PDF usando o objeto BackgroundArtifact.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBackgroundImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Create a new BackgroundArtifact and set the background image
        var background = new Aspose.Pdf.BackgroundArtifact()
        {
            BackgroundImage = File.OpenRead(dataDir + "background.jpg")
        };

        // Add the background image to the first page's artifacts
        document.Pages[1].Artifacts.Add(background);

        // Save PDF document with the added background
        document.Save(dataDir + "SampleArtifactsBackground_out.pdf");
    }
}
```

Se você quiser, por algum motivo, usar um fundo de cor sólida, por favor, altere o código anterior da seguinte maneira:

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

 private static void AddBackgroundColorToPDF()
 {
    // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
     {
         // Create a new BackgroundArtifact and set the background color
         var background = new Aspose.Pdf.BackgroundArtifact()
         {
             BackgroundColor = Aspose.Pdf.Color.DarkKhaki
         };

         // Add the background color to the first page's artifacts
         document.Pages[1].Artifacts.Add(background);

         // Save PDF document
         document.Save(dataDir + "SampleArtifactsBackground_out.pdf");
     }
 }
```

## Contando Artefatos de um Tipo Específico

Para calcular a contagem total de artefatos de um tipo específico (por exemplo, o número total de marcas d'água), use o seguinte código:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CountPDFArtifacts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Get pagination artifacts from the first page
        var paginationArtifacts = document.Pages[1].Artifacts
            .Where(artifact => artifact.Type == Aspose.Pdf.Artifact.ArtifactType.Pagination);

        // Count and display the number of each artifact type
        Console.WriteLine("Watermarks: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Watermark));
        Console.WriteLine("Backgrounds: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Background));
        Console.WriteLine("Headers: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Header));
        Console.WriteLine("Footers: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Footer));
    }
}
```

## Adicionando Artefato de Numeração Bates

Para adicionar um artefato de numeração Bates a um documento, chame o ```AddBatesNumbering(BatesNArtifact batesNArtifact)``` método de extensão no ```PageCollection```, passando o objeto ```BatesNArtifact``` como parâmetro:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBatesNArtifact()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create or open PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add 10 pages
        for (int i = 0; i < 10; i++)
        {
            document.Pages.Add();
        }

        // Add Bates numbering to all pages
        document.Pages.AddBatesNumbering(new BatesNArtifact
        {
            // These properties are set to their default values, as if they were not specified
            StartPage = 1,
            EndPage = 0,
            Subset = Subset.All,
            NumberOfDigits = 6,
            StartNumber = 1,
            Prefix = "",
            Suffix = "",
            ArtifactVerticalAlignment = VerticalAlignment.Bottom,
            ArtifactHorizontalAlignment = HorizontalAlignment.Right,
            RightMargin = 72,
            LeftMargin = 72,
            TopMargin = 36,
            BottomMargin = 36
        });

        // Save PDF document
        document.Save(dataDir + "SampleBatesNArtifact_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// The path to the documents directory
var dataDir = RunExamples.GetDataDir_AsposePdf();

// Create or open PDF document
using var document = new Aspose.Pdf.Document();

// Add 10 pages
for (int i = 0; i < 10; i++)
{
    document.Pages.Add();
}

// Add Bates numbering to all pages
document.Pages.AddBatesNumbering(new BatesNArtifact
{
    // These properties are set to their default values, as if they were not specified
    StartPage = 1,
    EndPage = 0,
    Subset = Subset.All,
    NumberOfDigits = 6,
    StartNumber = 1,
    Prefix = "",
    Suffix = "",
    ArtifactVerticalAlignment = VerticalAlignment.Bottom,
    ArtifactHorizontalAlignment = HorizontalAlignment.Right,
    RightMargin = 72,
    LeftMargin = 72,
    TopMargin = 36,
    BottomMargin = 36
});

// Save PDF document
document.Save(dataDir + "SampleBatesNArtifact_out.pdf");
```
{{< /tab >}}
{{< /tabs >}}

Ou, você pode passar uma coleção de ```PaginationArtifacts```:

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBatesNArtifact()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create or open PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add 10 pages
        for (int i = 0; i < 10; i++)
        {
            document.Pages.Add();
        }

        // Add Bates numbering to all pages
        document.Pages.AddPagination(new List<Aspose.Pdf.PaginationArtifact>
        {
            new Aspose.Pdf.BatesNArtifact
            {
                // These properties are set to their default values, as if they were not specified
                StartPage = 1,
                EndPage = 0,
                Subset = Subset.All,
                NumberOfDigits = 6,
                StartNumber = 1,
                Prefix = "",
                Suffix = "",
                ArtifactVerticalAlignment = VerticalAlignment.Bottom,
                ArtifactHorizontalAlignment = HorizontalAlignment.Right,
                RightMargin = 72,
                LeftMargin = 72,
                TopMargin = 36,
                BottomMargin = 36
            }
        });

        // Save PDF document
        document.Save(dataDir + "SampleBatesNArtifact_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBatesNArtifact()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create or open PDF document
    using var document = new Aspose.Pdf.Document();

    // Add 10 pages
    for (int i = 0; i < 10; i++)
    {
        document.Pages.Add();
    }

    // Add Bates numbering to all pages
    document.Pages.AddPagination(new List<Aspose.Pdf.PaginationArtifact>
    {
        new Aspose.Pdf.BatesNArtifact
        {
            // These properties are set to their default values, as if they were not specified
            StartPage = 1,
            EndPage = 0,
            Subset = Subset.All,
            NumberOfDigits = 6,
            StartNumber = 1,
            Prefix = "",
            Suffix = "",
            ArtifactVerticalAlignment = VerticalAlignment.Bottom,
            ArtifactHorizontalAlignment = HorizontalAlignment.Right,
            RightMargin = 72,
            LeftMargin = 72,
            TopMargin = 36,
            BottomMargin = 36
        }
    });

    // Save PDF document
    document.Save(dataDir + "SampleBatesNArtifact_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

Alternativamente, você pode adicionar um artefato de numeração Bates usando um delegado de ação:

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBatesNArtifact()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create or open PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add 10 pages
        for (int i = 0; i < 10; i++)
        {
            document.Pages.Add();
        }

        // Add Bates numbering to all pages
        document.Pages.AddBatesNumbering(batesN =>
        {
            // These properties are set to their default values, as if they were not specified
            batesN.StartPage = 1;
            batesN.EndPage = 0;
            batesN.Subset = Subset.All;
            batesN.NumberOfDigits = 6;
            batesN.StartNumber = 1;
            batesN.Prefix = "";
            batesN.Suffix = "";
            batesN.ArtifactVerticalAlignment = VerticalAlignment.Bottom;
            batesN.ArtifactHorizontalAlignment = HorizontalAlignment.Right;
            batesN.ArtifactVerticalAlignment = VerticalAlignment.Bottom;
            batesN.RightMargin = 72;
            batesN.LeftMargin = 72;
            batesN.TopMargin = 36;
            batesN.BottomMargin = 36;
            batesN.TextState.FontSize = 10;
        });

        // Save PDF document
        document.Save(dataDir + "SampleBatesNArtifact_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBatesNArtifact()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create or open PDF document
    using var document = new Aspose.Pdf.Document();

    // Add 10 pages
    for (int i = 0; i < 10; i++)
    {
        document.Pages.Add();
    }

    // Add Bates numbering to all pages
    document.Pages.AddBatesNumbering(batesN =>
    {
        // These properties are set to their default values, as if they were not specified
        batesN.StartPage = 1;
        batesN.EndPage = 0;
        batesN.Subset = Subset.All;
        batesN.NumberOfDigits = 6;
        batesN.StartNumber = 1;
        batesN.Prefix = "";
        batesN.Suffix = "";
        batesN.ArtifactVerticalAlignment = VerticalAlignment.Bottom;
        batesN.ArtifactHorizontalAlignment = HorizontalAlignment.Right;
        batesN.ArtifactVerticalAlignment = VerticalAlignment.Bottom;
        batesN.RightMargin = 72;
        batesN.LeftMargin = 72;
        batesN.TopMargin = 36;
        batesN.BottomMargin = 36;
        batesN.TextState.FontSize = 10;
    });

    // Save PDF document
    document.Save(dataDir + "SampleBatesNArtifact_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

Para excluir a numeração Bates, use o seguinte código:

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteBatesNArtifacts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SampleBatesNArtifact_out.pdf"))
    {
        // Delete Bates numbering from all pages
        document.Pages.DeleteBatesNumbering();

        //Save PDF document
        document.Save(dataDir + "DeleteBatesNArtifacts_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteBatesNArtifacts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "SampleBatesNArtifact_out.pdf");

    // Delete Bates numbering from all pages
    document.Pages.DeleteBatesNumbering();

    //Save PDF document
    document.Save(dataDir + "DeleteBatesNArtifacts_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

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