---
title: Trabalhando com Artefatos em .NET
linktitle: Trabalhando com Artefatos
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 170
url: /pt/net/artifacts/
description: Aspose.PDF for .NET permite adicionar uma imagem de fundo às páginas PDF e obter cada marca d'água usando a classe Artifact.
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
    "alternativeHeadline": "Add and Manage Artifacts in PDF Documents",
    "abstract": "Aspose.PDF for .NET introduz a classe Artifact, permitindo que os desenvolvedores gerenciem de forma eficiente elementos não relacionados ao conteúdo, como imagens de fundo e marcas d'água dentro de documentos PDF. Essa funcionalidade melhora a estrutura do documento enquanto melhora a acessibilidade e o desempenho, já que os artefatos podem ser ignorados por tecnologias assistivas. Com opções personalizáveis para tipos e propriedades, os usuários podem manipular facilmente esses elementos para criar PDFs visualmente atraentes.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Artifacts, PDF document generation, Aspose.PDF for .NET, BackgroundArtifact, WatermarkArtifact, Artifact class, PDF artifacts, Artifact types, Accessibility in PDF, PDF watermark handling",
    "wordcount": "779",
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
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NET permite adicionar uma imagem de fundo às páginas PDF e obter cada marca d'água usando a classe Artifact."
}
</script>

Artefatos em PDF são objetos gráficos ou outros elementos que não fazem parte do conteúdo real do documento. Eles são geralmente usados para decoração, layout ou propósitos de fundo. Exemplos de artefatos incluem cabeçalhos de página, rodapés, separadores ou imagens que não transmitem nenhum significado.

O propósito dos artefatos em PDF é permitir a distinção entre elementos de conteúdo e não conteúdo. Isso é importante para acessibilidade, pois leitores de tela e outras tecnologias assistivas podem ignorar artefatos e se concentrar no conteúdo relevante. Artefatos também podem melhorar o desempenho e a qualidade dos documentos PDF, pois podem ser omitidos na impressão, pesquisa ou cópia.

Para criar um elemento como um artefato em PDF, você precisa usar a classe [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact).
Ela contém as seguintes propriedades úteis:

- **Artifact.Type** – obtém o tipo de artefato (suporta valores da enumeração Artifact.ArtifactType onde os valores incluem Background, Layout, Page, Pagination e Undefined).
- **Artifact.Subtype** – obtém o subtipo de artefato (suporta os valores da enumeração Artifact.ArtifactSubtype onde os valores incluem Background, Footer, Header, Undefined, Watermark).
- **Artifact.Image** – Obtém a imagem de um artefato (se uma imagem estiver presente, caso contrário, null).
- **Artifact.Text** – Obtém o texto de um artefato.
- **Artifact.Contents** – Obtém uma coleção de operadores internos do artefato. Seu tipo suportado é System.Collections.ICollection.
- **Artifact.Form** – Obtém o XForm de um artefato (se o XForm for usado). Marcas d'água, cabeçalhos e rodapés de artefatos contêm XForm que mostra todos os conteúdos do artefato.
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

Uma marca d'água criada com o Adobe Acrobat é chamada de artefato (conforme descrito em 14.8.2.2 Conteúdo Real e Artefatos da especificação PDF).

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