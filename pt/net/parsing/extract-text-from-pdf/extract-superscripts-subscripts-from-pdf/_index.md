---
title: Extrair texto de SuperScripts e SubScripts de PDF
linktitle: Extrair SuperScripts e SubScripts
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /pt/net/extract-superscripts-subscripts-from-pdf/
description: Este artigo descreve várias maneiras de extrair texto de SuperScripts e SubScripts de PDF usando Aspose.PDF em C#.
lastmod: "2022-10-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract SuperScripts and SubScripts text from PDF",
    "alternativeHeadline": "Extract SuperScripts and SubScripts from PDF Documents",
    "abstract": "O novo recurso de extrair texto de SuperScripts e SubScripts de documentos PDF usando a biblioteca Aspose.PDF for .NET permite que os usuários recuperem com precisão a formatação de texto especializada encontrada em documentos técnicos. Essa melhoria simplifica o processo de manipulação de expressões matemáticas e especificações químicas, fornecendo aos desenvolvedores ferramentas para manipular esses elementos textuais facilmente.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "323",
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
    "url": "/net/extract-superscripts-subscripts-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-superscripts-subscripts-from-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Extrair Texto de SuperScripts e SubScripts

Extrair texto de um documento PDF é uma tarefa comum. No entanto, nesse texto, quando extraído, os **SuperScripts e SubScripts** contidos nele, que são típicos de documentos e artigos técnicos, podem não ser exibidos. Um SubScript ou SuperScript é um caractere, número ou letra colocado abaixo ou acima de uma linha regular de texto. Geralmente, é menor que o restante do texto.

**SubScripts e SuperScripts** são mais frequentemente usados em fórmulas, expressões matemáticas e especificações de compostos químicos. É difícil editá-los quando pode haver muitos deles na mesma passagem de texto. Em uma das últimas versões, a biblioteca **Aspose.PDF for .NET** adicionou suporte para extrair texto de SuperScripts e SubScripts de PDF.

Use a classe **TextFragmentAbsorber** e você já pode fazer qualquer coisa com o texto encontrado, ou seja, você pode simplesmente usar todo o texto. Tente o próximo trecho de código:

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSuperScriptsAndSubScripts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SuperScriptExample.pdf"))
    {
        // Create an absorber
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        document.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(dataDir + "SuperScriptExample_out.txt"))
        {
            // Write the extracted text in text file
            writer.WriteLine(absorber.Text);
        }
    }
}
```

Ou use **TextFragments** separadamente e faça todo tipo de manipulações com eles, por exemplo, classificar por coordenadas ou por tamanho.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSuperScriptsAndSubScriptsWithTextFragments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SuperScriptExample.pdf"))
    {
        // Create an absorber
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        document.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(dataDir + "SuperScriptExample_out.txt"))
        {
            foreach (var textFragment in absorber.TextFragments)
            {
                // Write the extracted text in text file
                writer.Write(textFragment.Text);
            }

        }
    }
}
```