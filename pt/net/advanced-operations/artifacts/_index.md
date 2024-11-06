---
title: Trabalhando com Artefatos em .NET
linktitle: Trabalhando com Artefatos
type: docs
weight: 110
url: pt/net/artifacts/
description: Aspose.PDF para .NET permite que você adicione uma imagem de fundo às páginas PDF e obtenha cada marca d'água usando a classe Artifact.
lastmod: "2024-01-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabalhando com Artefatos em .NET",
    "alternativeHeadline": "Artefatos em documento PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, artefatos em pdf",
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
    "url": "/net/artifacts/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/artifacts/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF para .NET permite que você adicione uma imagem de fundo às páginas PDF e obtenha cada marca d'água usando a classe Artifact."
}
</script>
Artefatos em PDF são objetos gráficos ou outros elementos que não fazem parte do conteúdo real do documento. Eles são geralmente usados para decoração, layout ou fins de fundo. Exemplos de artefatos incluem cabeçalhos de página, rodapés, separadores ou imagens que não transmitem nenhum significado.

O propósito dos artefatos em PDF é permitir a distinção entre elementos de conteúdo e não conteúdo. Isso é importante para acessibilidade, pois leitores de tela e outras tecnologias assistivas podem ignorar artefatos e focar no conteúdo relevante. Artefatos também podem melhorar o desempenho e a qualidade dos documentos PDF, pois podem ser omitidos de impressão, pesquisa ou cópia.

Para criar um elemento como um artefato em PDF, você precisa usar a classe [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact).
Ela contém as seguintes propriedades úteis:

- **Artifact.Type** – obtém o tipo de artefato (suporta valores da enumeração Artifact.ArtifactType onde os valores incluem Background, Layout, Page, Pagination e Undefined).
- **Artifact.Type** – Obtém o tipo de artefato (suporta valores da enumeração Artifact.ArtifactType onde valores incluem Background, Layout, Page, Pagination e Undefined).
- **Artifact.Subtype** – Obtém o subtipo de artefato (suporta os valores da enumeração Artifact.ArtifactSubtype onde valores incluem Background, Footer, Header, Undefined, Watermark).
- **Artifact.Image** – Obtém a imagem de um artefato (se uma imagem estiver presente, caso contrário null).
- **Artifact.Text** – Obtém o texto de um artefato.
- **Artifact.Contents** – Obtém uma coleção de operadores internos do artefato. Seu tipo suportado é System.Collections.ICollection.
- **Artifact.Form** – Obtém o XForm de um artefato (se XForm é utilizado). Artefatos de marca d'água, cabeçalho e rodapé contêm XForm que mostra todos os conteúdos do artefato.
- **Artifact.Rectangle** – Obtém a posição de um artefato na página.
- **Artifact.Rotation** – Obtém a rotação de um artefato (em graus, valor positivo indica rotação no sentido anti-horário).
- **Artifact.Opacity** – Obtém a opacidade de um artefato.
- **Artifact.Opacity** – Obtém a opacidade de um artefato.

As seguintes classes também podem ser úteis para trabalhar com artefatos:

- [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection)
- [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/watermarkartifact/)

## Trabalhando com Marcas D'água Existentes

Uma marca d'água criada com o Adobe Acrobat é chamada de artefato (conforme descrito em 14.8.2.2 Conteúdo Real e Artefatos da especificação PDF).

Para obter todas as marcas d'água em uma página específica, a classe [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) possui a propriedade Artifacts.

O seguinte trecho de código mostra como obter todas as marcas d'água na primeira página de um arquivo PDF.

_Nota:_ Este código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).
_Nota:_ Este código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample-w.pdf"));
var watermarks = document.Pages[1].Artifacts
    .Where(artifact =>
    artifact.Type == Artifact.ArtifactType.Pagination
    && artifact.Subtype == Artifact.ArtifactSubtype.Watermark);
foreach (WatermarkArtifact item in watermarks.Cast<WatermarkArtifact>())
{
    Console.WriteLine($"{item.Text} {item.Rectangle}");
}
```

## Trabalhando com Fundos como Artefatos

Imagens de fundo podem ser usadas para adicionar uma marca d'água ou outro design sutil aos documentos. Em Aspose.PDF para .NET, cada documento PDF é uma coleção de páginas e cada página contém uma coleção de artefatos. A classe [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact) pode ser usada para adicionar uma imagem de fundo a um objeto de página.

O seguinte trecho de código mostra como adicionar uma imagem de fundo às páginas de um PDF usando o objeto BackgroundArtifact.

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var background = new BackgroundArtifact()
{
    BackgroundImage = System.IO.File.OpenRead(System.IO.Path.Combine(_dataDir, "background.jpg"))
};
document.Pages[1].Artifacts.Add(background);
document.Save(System.IO.Path.Combine(_dataDir, "sample_artifacts_background.pdf"));
```
Se, por algum motivo, você quiser usar um fundo de cor sólida, altere o código anterior da seguinte maneira:

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var background = new BackgroundArtifact()
{
    BackgroundColor = Color.DarkKhaki,
};
document.Pages[1].Artifacts.Add(background);
document.Save(System.IO.Path.Combine(_dataDir, "sample_artifacts_background.pdf"));
```

## Contando Artefatos de um Tipo Particular

Para calcular a contagem total de artefatos de um tipo particular (por exemplo, o número total de marcas d'água), use o seguinte código:

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var paginationArtifacts = document.Pages[1].Artifacts.Where(artifact => artifact.Type == Artifact.ArtifactType.Pagination);
Console.WriteLine("Marcas d'água: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Watermark));
Console.WriteLine("Fundos: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Background));
Console.WriteLine("Cabeçalhos: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Header));
Console.WriteLine("Rodapés: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Footer));
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
```

