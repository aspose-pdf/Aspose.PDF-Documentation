---
title: Adicionar marca d'água ao PDF usando C#
linktitle: Adicionar marca d'água
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /pt/net/add-watermarks/
description: Este artigo explica os recursos de trabalho com artefatos e obtenção de marcas d'água em PDFs usando programaticamente o C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add watermark to PDF using C#",
    "alternativeHeadline": "Add Custom Watermarks to PDF with C#",
    "abstract": "O novo recurso em Aspose.PDF for .NET permite que os desenvolvedores adicionem programaticamente marcas d'água personalizáveis a documentos PDF usando a funcionalidade de Artefato. Este recurso melhora o gerenciamento de documentos ao suportar várias propriedades de artefato, incluindo tipo, opacidade, rotação e personalização de texto, permitindo que os usuários criem arquivos PDF profissionais e identificáveis com facilidade.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "462",
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
    "url": "/net/add-watermarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-watermarks/"
    },
    "dateModified": "2024-11-26",
    "description": "Este artigo explica os recursos de trabalho com artefatos e obtenção de marcas d'água em PDFs usando programaticamente o C#."
}
</script>

**Aspose.PDF for .NET** permite adicionar marcas d'água ao seu documento PDF usando Artefatos. Por favor, consulte este artigo para resolver sua tarefa.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

Uma marca d'água criada com o Adobe Acrobat é chamada de artefato (conforme descrito na 14.8.2.2 Conteúdo Real e Artefatos da especificação PDF). Para trabalhar com artefatos, Aspose.PDF possui duas classes: [Artifact](https://reference.aspose.com/pdf/pt/net/aspose.pdf/artifact) e [ArtifactCollection](https://reference.aspose.com/pdf/pt/net/aspose.pdf/artifactcollection).

Para obter todos os artefatos em uma página específica, a classe [Page](https://reference.aspose.com/pdf/pt/net/aspose.pdf/page) possui a propriedade Artifacts. Este tópico explica como trabalhar com artefatos em arquivos PDF.

## Trabalhando com Artefatos

A classe [Artifact](https://reference.aspose.com/pdf/pt/net/aspose.pdf/artifact) contém as seguintes propriedades:

- **Artifact.Type**: obtém o tipo de artefato (suporta valores da enumeração Artifact.ArtifactType onde os valores incluem Background, Layout, Page, Pagination e Undefined).
- **Artifact.Subtype**: obtém o subtipo de artefato (suporta os valores da enumeração Artifact.ArtifactSubtype onde os valores incluem Background, Footer, Header, Undefined, Watermark).

{{% alert color="primary" %}}

Por favor, note que marcas d'água criadas com o Adobe Acrobat têm o tipo Pagination e subtipo Watermark.

{{% /alert %}}

- **Artifact.Contents**: Obtém uma coleção de operadores internos de artefato. Seu tipo suportado é System.Collections.ICollection.
- **Artifact.Form**: Obtém um XForm de um artefato (se XForm for usado). Marcas d'água, cabeçalhos e rodapés contêm XForm que mostra todo o conteúdo do artefato.
- **Artifact.Image**: Obtém a imagem de um artefato (se uma imagem estiver presente, caso contrário, nulo).
- **Artifact.Text**: Obtém o texto de um artefato.
- **Artifact.Rectangle**: Obtém a posição de um artefato na página.
- **Artifact.Rotation**: Obtém a rotação de um artefato (em graus, valor positivo indica rotação anti-horária).
- **Artifact.Opacity**: Obtém a opacidade de um artefato. Os valores possíveis estão na faixa de 0…1, onde 1 é completamente opaco.

## Como Adicionar Marca d'água em Arquivos PDF

O seguinte trecho de código mostra como obter cada marca d'água na primeira página de um arquivo PDF com C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddWatermarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddWatermarksInput.pdf"))
    {
        // Create a new watermark artifact
        var artifact = new Aspose.Pdf.WatermarkArtifact();
        artifact.SetTextAndState(
            "WATERMARK",
            new Aspose.Pdf.Text.TextState()
            {
                FontSize = 72,
                ForegroundColor = Aspose.Pdf.Color.Blue,
                Font = Aspose.Pdf.Text.FontRepository.FindFont("Courier")
            });
        // Set watermark properties
        artifact.ArtifactHorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        artifact.ArtifactVerticalAlignment = Aspose.Pdf.VerticalAlignment.Center;
        artifact.Rotation = 45;
        artifact.Opacity = 0.5;
        artifact.IsBackground = true;
        // Add watermark artifact to the first page
        document.Pages[1].Artifacts.Add(artifact);
        // Save PDF document
        document.Save(dataDir + "AddWatermarks_out.pdf");
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