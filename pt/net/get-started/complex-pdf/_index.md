---
title: Criando um PDF complexo
linktitle: Criando um PDF complexo
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /pt/net/complex-pdf-example/
description: Aspose.PDF para NET permite que você crie documentos mais complexos que contêm imagens, fragmentos de texto e tabelas em um único documento.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Creating a complex PDF",
    "alternativeHeadline": "Create Complex PDFs with Images, Text, and Tables in C#",
    "abstract": "Aspose.PDF for .NET introduz um recurso poderoso para criar PDFs complexos, permitindo que os desenvolvedores integrem imagens, fragmentos de texto e tabelas em um único documento de forma contínua. Essa funcionalidade utiliza uma abordagem baseada em DOM, permitindo personalização detalhada e controle de layout na geração de PDF, tornando-a ideal para criar documentos de qualidade profissional de forma eficiente.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "632",
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
    "url": "/net/complex-pdf-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/complex-pdf-example/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

O exemplo [Hello, World](/pdf/pt/net/hello-world-example/) mostrou passos simples para criar um documento PDF usando C# e Aspose.PDF. Neste artigo, vamos dar uma olhada em como criar um documento mais complexo com C# e Aspose.PDF for .NET. Como exemplo, pegaremos um documento de uma empresa fictícia que opera serviços de ferry para passageiros. 
Nosso documento conterá uma imagem, dois fragmentos de texto (cabeçalho e parágrafo) e uma tabela. Para construir tal documento, usaremos uma abordagem baseada em DOM. Você pode ler mais na seção [Fundamentos da API DOM](/pdf/pt/net/basics-of-dom-api/).

Se criarmos um documento do zero, precisamos seguir certas etapas:

1. Instanciar um objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Nesta etapa, criaremos um documento PDF vazio com alguns metadados, mas sem páginas.
1. Adicionar uma [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) ao objeto documento. Assim, agora nosso documento terá uma página.
1. Adicionar uma [Image](https://reference.aspose.com/pdf/net/aspose.pdf/image/methods/index) à página.
1. Criar um [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) para o cabeçalho. Para o cabeçalho, usaremos a fonte Arial com tamanho de fonte 24pt e alinhamento central.
1. Adicionar o cabeçalho aos [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) da página.
1. Criar um [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) para a descrição. Para a descrição, usaremos a fonte Arial com tamanho de fonte 24pt e alinhamento central.
1. Adicionar (descrição) aos Paragraphs da página.
1. Criar uma tabela, adicionar propriedades da tabela.
1. Adicionar (tabela) aos [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) da página.
1. Salvar um documento "Complex.pdf".

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreatingComplexPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Add image
        page.AddImage(dataDir + "logo.png", new Aspose.Pdf.Rectangle(20, 730, 120, 830));

        // Add Header
        var header = new Aspose.Pdf.Text.TextFragment("New ferry routes in Fall 2020");
        header.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        header.TextState.FontSize = 24;
        header.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        header.Position = new Aspose.Pdf.Text.Position(130, 720);
        page.Paragraphs.Add(header);

        // Add description
        var descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. Ferry service is operating at half capacity and on a reduced schedule. Expect lineups.";
        var description = new Aspose.Pdf.Text.TextFragment(descriptionText);
        description.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Times New Roman");
        description.TextState.FontSize = 14;
        description.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Left;
        page.Paragraphs.Add(description);

        // Add table
        var table = new Aspose.Pdf.Table
        {
            ColumnWidths = "200",
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1f, Aspose.Pdf.Color.DarkSlateGray),
            DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 0.5f, Aspose.Pdf.Color.Black),
            DefaultCellPadding = new Aspose.Pdf.MarginInfo(4.5, 4.5, 4.5, 4.5),
            Margin =
            {
                Bottom = 10
            },
            DefaultCellTextState =
            {
                Font =  Aspose.Pdf.Text.FontRepository.FindFont("Helvetica")
            }
        };

        var headerRow = table.Rows.Add();
        headerRow.Cells.Add("Departs City");
        headerRow.Cells.Add("Departs Island");
        foreach (Aspose.Pdf.Cell headerRowCell in headerRow.Cells)
        {
            headerRowCell.BackgroundColor = Aspose.Pdf.Color.Gray;
            headerRowCell.DefaultCellTextState.ForegroundColor = Aspose.Pdf.Color.WhiteSmoke;
        }

        var time = new TimeSpan(6, 0, 0);
        var incTime = new TimeSpan(0, 30, 0);
        for (int i = 0; i < 10; i++)
        {
            var dataRow = table.Rows.Add();
            dataRow.Cells.Add(time.ToString(@"hh\:mm"));
            time = time.Add(incTime);
            dataRow.Cells.Add(time.ToString(@"hh\:mm"));
        }

        page.Paragraphs.Add(table);
        // Save PDF document
        document.Save(dataDir + "Complex_out.pdf");
    }
}
```