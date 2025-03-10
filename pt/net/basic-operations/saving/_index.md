---
title: Salvar documento PDF programaticamente
linktitle: Salvar PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /pt/net/save-pdf-document/
description: Aprenda como salvar arquivos PDF na biblioteca PDF C# Aspose.PDF for .NET. Salve documentos PDF no sistema de arquivos, em streams e em aplicações web.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Save PDF document programmatically",
    "alternativeHeadline": "Programmatic PDF Saving with C#",
    "abstract": "Descubra como os desenvolvedores salvam documentos PDF programaticamente com facilidade usando Aspose.PDF for .NET. Este recurso suporta o salvamento de PDFs no sistema de arquivos, streams e diretamente em aplicações web, acomodando diversos casos de uso enquanto garante conformidade com os padrões PDF/A e PDF/X para arquivamento de longo prazo e troca de gráficos. Otimize suas capacidades de manipulação de PDF com este robusto mecanismo de salvamento",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "471",
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
    "url": "/net/save-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/save-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

O próximo trecho de código também funciona com a biblioteca [Aspose.Drawing](/pdf/pt/net/drawing/).

## Salvar documento PDF no sistema de arquivos

Você pode salvar o documento PDF criado ou manipulado no sistema de arquivos usando o método `Save` da classe `Document`.
Quando você não fornece o tipo de formato (opções), o documento é salvo no formato Aspose.PDF v.1.7 (*.pdf).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Make some manipation, i.g add new empty page
        document.Pages.Add();
        // Save PDF document
        document.Save(dataDir + "SimpleResume_out.pdf");
    }
}
```

## Salvar documento PDF em stream

Você também pode salvar o documento PDF criado ou manipulado em stream usando sobrecargas dos métodos `Save`.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveDocumentStream()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Make some manipation, i.g add new empty page
        document.Pages.Add();
        // Save PDF document
        document.Save(dataDir + "SimpleResume_out.pdf");
    }
}
```

Para uma explicação mais detalhada, siga para a seção [Showcase](/pdf/pt/net/showcases/).

## Salvar formato PDF/A ou PDF/X

PDF/A é uma versão padronizada pela ISO do Formato de Documento Portátil (PDF) para uso em arquivamento e preservação de longo prazo de documentos eletrônicos.
PDF/A difere do PDF na medida em que proíbe recursos não adequados para arquivamento de longo prazo, como vinculação de fontes (em oposição à incorporação de fontes) e criptografia. Os requisitos da ISO para visualizadores PDF/A incluem diretrizes de gerenciamento de cores, suporte a fontes incorporadas e uma interface de usuário para leitura de anotações incorporadas.

PDF/X é um subconjunto do padrão ISO PDF. O objetivo do PDF/X é facilitar a troca de gráficos e, portanto, possui uma série de requisitos relacionados à impressão que não se aplicam a arquivos PDF padrão.

Em ambos os casos, o método `Save` é usado para armazenar os documentos, enquanto os documentos devem ser preparados usando o método `Convert`.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveDocumentAsPDFx()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Add page
        document.Pages.Add();
        // Convert a document to a PDF/X-3 format
        document.Convert(new Aspose.Pdf.PdfFormatConversionOptions(Aspose.Pdf.PdfFormat.PDF_X_3));
        // Save PDF document
        document.Save(dataDir + "SimpleResume_X3.pdf");
    }
}
```