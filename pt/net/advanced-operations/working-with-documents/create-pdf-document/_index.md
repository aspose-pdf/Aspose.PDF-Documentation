---
title: Como Criar PDF usando C#
linktitle: Criar Documento PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/create-pdf-document/
description: Crie e formate o Documento PDF com Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to Create PDF using C#",
    "alternativeHeadline": "Create and Format PDFs Effortlessly with C#",
    "abstract": "A nova funcionalidade em Aspose.PDF for .NET capacita os desenvolvedores a criar e formatar documentos PDF sem esforço usando C#. Com esta API intuitiva, os usuários podem gerar PDFs pesquisáveis, manipular conteúdo marcado para acessibilidade e integrar perfeitamente a geração de PDF em várias aplicações .NET, aumentando a produtividade e otimizando fluxos de trabalho.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF creation, C# PDF generation, Aspose.PDF for .NET, searchable PDF, accessible PDF, Document class, TextFragment, PDF document manipulation, .NET applications, BDC operations",
    "wordcount": "871",
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
    "url": "/net/create-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Crie e formate o Documento PDF com Aspose.PDF for .NET."
}
</script>

Estamos sempre em busca de uma maneira de gerar documentos PDF e trabalhar com eles em projetos C# de forma mais exata, precisa e eficaz. Ter funções fáceis de usar de uma biblioteca nos permite acompanhar mais do trabalho e menos os detalhes que consomem tempo ao tentar gerar PDFs, seja em .NET.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Criar (ou Gerar) documento PDF usando a linguagem C#

A API Aspose.PDF for .NET permite que você crie e leia arquivos PDF usando C# e VB.NET. A API pode ser usada em uma variedade de aplicações .NET, incluindo WinForms, ASP.NET e várias outras. Neste artigo, vamos mostrar como usar a API Aspose.PDF for .NET para gerar e ler arquivos PDF facilmente em aplicações .NET.

### Como Criar um Arquivo PDF Simples

Para criar um arquivo PDF usando C#, os seguintes passos podem ser utilizados.

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Adicione um objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) à coleção [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/pages) do objeto Document.
1. Adicione [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) à coleção [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) da página.
1. Salve o documento PDF resultante.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateHelloWorldDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Add text to new page
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
        // Save PDF document
        document.Save(dataDir + "HelloWorld_out.pdf");
    }
}
```

### Como Criar um documento PDF pesquisável

Aspose.PDF for .NET fornece a funcionalidade para criar e manipular documentos PDF existentes. Ao adicionar elementos de texto dentro do arquivo PDF, o PDF resultante é pesquisável. No entanto, se estivermos convertendo uma imagem contendo texto em um arquivo PDF, o conteúdo dentro do PDF não é pesquisável. No entanto, como uma solução alternativa, podemos usar OCR sobre o arquivo resultante, para que ele se torne pesquisável.

Esta lógica especificada abaixo reconhece texto para imagens PDF. Para reconhecimento, você pode usar suporte externo de OCR que siga o padrão HOCR. Para fins de teste, usamos um OCR gratuito do Google Tesseract. Portanto, primeiro você precisa instalar o Tesseract-OCR em seu sistema, e você terá o aplicativo de console do Tesseract.

A seguir está o código completo para atender a esse requisito:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateSearchableDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchableDocument.pdf"))
    {
        document.Convert(CallBackGetHocr);

        // Save PDF document
        document.Save(dataDir + "SearchableDocument_out.pdf");
    }
}

private static string CallBackGetHocr(System.Drawing.Image img)
{
    var tmpFile = Path.GetTempFileName();
    try
    {
        using (var bmp = new System.Drawing.Bitmap(img))
        {
            bmp.Save(tmpFile, System.Drawing.Imaging.ImageFormat.Bmp);
        }

        var inputFile = string.Concat('"', tmpFile, '"');
        var outputFile = string.Concat('"', tmpFile, '"');
        var arguments = string.Concat(inputFile, " ", outputFile, " -l eng hocr");
        var tesseractProcessName = RunExamples.GetTesseractExePath();

        var psi = new System.Diagnostics.ProcessStartInfo(tesseractProcessName, arguments)
        {
            UseShellExecute = true,
            CreateNoWindow = true,
            WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden,
            WorkingDirectory = Path.GetDirectoryName(tesseractProcessName)
        };

        var p = new System.Diagnostics.Process
        {
            StartInfo = psi
        };
        p.Start();
        p.WaitForExit();

        using (var streamReader = new StreamReader(tmpFile + ".hocr"))
        {
            string text = streamReader.ReadToEnd();
            return text;
        }
    }
    finally
    {
        if (File.Exists(tmpFile))
        {
            File.Delete(tmpFile);
        }
        if (File.Exists(tmpFile + ".hocr"))
        {
            File.Delete(tmpFile + ".hocr");
        }
    }
}
```

### Como Criar um PDF acessível usando funções de baixo nível

Este trecho de código trabalha com um documento PDF e seu conteúdo marcado, utilizando uma biblioteca Aspose.PDF para processá-lo.

O exemplo cria um novo elemento span no conteúdo marcado da primeira página de um PDF, encontra todos os elementos BDC e os associa ao span. O documento modificado é então salvo.

Você pode criar uma declaração bdc especificando mcid, lang e texto de expansão usando o objeto BDCProperties:

```cs
var bdc = new Aspose.Pdf.Operators.BDC("P", new Aspose.Pdf.Facades.BDCProperties(1, "de", "Hallo, welt!"));
```

Após criar a árvore de estrutura, é possível vincular o operador BDC ao elemento especificado da estrutura com o método Tag no objeto do elemento:

```cs
Aspose.Pdf.LogicalStructure.SpanElement span = content.CreateSpanElement();
span.Tag(bdc);
```

Passos para criar um PDF acessível:

1. Carregue o Documento PDF.
1. Acesse o Conteúdo Marcado.
1. Crie um Elemento Span.
1. Anexe o Span ao Elemento Raiz.
1. Itere Sobre o Conteúdo da Página.
1. Verifique os Elementos BDC e Marque-os.
1. Salve o Documento Modificado.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateAnAccessibleDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "tourguidev2_gb_tags.pdf"))
    {
        // Access tagged content
        Aspose.Pdf.Tagged.ITaggedContent content = document.TaggedContent;
        // Create a span element
        Aspose.Pdf.LogicalStructure.SpanElement span = content.CreateSpanElement();
        // Append span to root element
        content.RootElement.AppendChild(span);
        // Iterate over page contents
        foreach (var op in document.Pages[1].Contents)
        {
            var bdc = op as Aspose.Pdf.Operators.BDC;
            if (bdc != null)
            {
                span.Tag(bdc);
            }
        }
        // Save PDF document
        document.Save(dataDir + "AccessibleDocument_out.pdf");
    }
}
```

Este código modifica um PDF criando um elemento span dentro do conteúdo marcado do documento e marcando conteúdo específico (operações BDC) da primeira página com este span. O PDF modificado é então salvo em um novo arquivo.

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