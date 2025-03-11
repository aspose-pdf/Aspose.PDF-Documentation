---
title: Extrair Texto de Carimbos usando C#
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /pt/net/extract-text-from-stamps/
description: Aprenda como usar o recurso especial de Aspose.PDF for .NET - extração de texto de anotações de carimbo
lastmod: "2021-01-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Text From Stamps using C#",
    "alternativeHeadline": "Extract Text from PDF Stamp Annotations with Ease",
    "abstract": "Descubra as poderosas capacidades de extração de texto de Aspose.PDF for .NET, projetadas especificamente para recuperar texto de anotações de carimbo em documentos PDF. Este novo recurso simplifica o processo, permitindo que os desenvolvedores acessem e manipulem facilmente o texto dentro das anotações de carimbo usando trechos de código concisos, aumentando a produtividade e a eficiência nas tarefas de gerenciamento de PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "168",
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
    "url": "/net/extract-text-from-stamps/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-text-from-stamps/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Extrair Texto de Anotações de Carimbo

Aspose.PDF para NET permite que você extraia texto de anotações de carimbo. Para extrair texto de Anotações de Carimbo em um PDF, os seguintes passos podem ser utilizados.

1. Crie um objeto da classe `Document`.
1. Obtenha a `Annotation` desejada da lista de anotações de uma página.
1. Defina um novo objeto da classe `TextAbsorber`.
1. Use o método visit do TextAbsorber para obter o Texto.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractStampText.pdf"))
    {
        Aspose.Pdf.Annotations.Annotation item = document.Pages[1].Annotations[1];
        if (item is Aspose.Pdf.Annotations.StampAnnotation annot)
        {
            var absorber = new Aspose.Pdf.Text.TextAbsorber();
            Aspose.Pdf.XForm appearance = annot.Appearance["N"];
            absorber.Visit(appearance);
            Console.WriteLine(absorber.Text);
        }
    }
}
```