---
title: Manipular Tabelas em PDF existente
linktitle: Manipular Tabelas
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /pt/net/manipulate-tables-in-existing-pdf/
description: Aprenda como trabalhar com tabelas em PDFs existentes usando Aspose.PDF for .NET, proporcionando flexibilidade na modificação de documentos.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipulate Tables in existing PDF",
    "alternativeHeadline": "Enhance Table Editing in Existing PDF Documents",
    "abstract": "Aspose.PDF for .NET introduz um recurso poderoso para manipular tabelas PDF existentes, permitindo que os usuários pesquisem, analisem e modifiquem o conteúdo das tabelas com facilidade. A nova classe TableAbsorber permite atualizações dinâmicas e substituições de tabelas diretamente dentro dos documentos PDF, simplificando o processo de gerenciamento de dados tabulares em PDFs para uma funcionalidade aprimorada. Explore essa capacidade inovadora para otimizar suas tarefas de edição de PDF e integração de dados.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
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
    "url": "/net/manipulate-tables-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-tables-in-existing-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Manipular tabelas em PDF existente

Uma das primeiras funcionalidades suportadas por Aspose.PDF for .NET é sua capacidade de Trabalhar com Tabelas e oferece um ótimo suporte para adicionar tabelas em arquivos PDF gerados do zero ou em qualquer arquivo PDF existente. Você também obtém a capacidade de Integrar Tabela com Banco de Dados (DOM) para criar tabelas dinâmicas com base no conteúdo do banco de dados. Nesta nova versão, implementamos um novo recurso de pesquisa e análise de tabelas simples que já existem na página do documento PDF. Uma nova classe chamada **Aspose.PDF.Text.TableAbsorber** fornece essas capacidades. O uso do TableAbsorber é muito semelhante à classe existente TextFragmentAbsorber. O seguinte trecho de código mostra os passos para atualizar o conteúdo em uma célula de tabela específica.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ManipulateTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create TableAbsorber object to find tables
        var absorber = new Aspose.Pdf.Text.TableAbsorber();

        // Visit first page with absorber
        absorber.Visit(document.Pages[1]);

        // Get access to first table on page, their first cell and text fragments in it
        Aspose.Pdf.Text.TextFragment fragment = absorber.TableList[0].RowList[0].CellList[0].TextFragments[1];

        // Change text of the first text fragment in the cell
        fragment.Text = "hi world";

        // Save PDF document
        document.Save(dataDir + "ManipulateTable_out.pdf");
    }
}
```

## Substituir tabela antiga por uma nova no documento PDF

Caso você precise encontrar uma tabela específica e substituí-la pela desejada, você pode usar o método Replace() da classe [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) para fazer isso. O exemplo a seguir demonstra a funcionalidade de substituir a tabela dentro do documento PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Table_input2.pdf"))
    {
        // Create TableAbsorber object to find tables
        var absorber = new Aspose.Pdf.Text.TableAbsorber();

        // Visit first page with absorber
        absorber.Visit(document.Pages[1]);

        // Get first table on the page
        Aspose.Pdf.Text.AbsorbedTable table = absorber.TableList[0];

        // Create new table
        var newTable = new Aspose.Pdf.Table();
        newTable.ColumnWidths = "100 100 100";
        newTable.DefaultCellBorder = new Aspose.Pdf.BorderInfo(BorderSide.All, 1F);

        Row row = newTable.Rows.Add();
        row.Cells.Add("Col 1");
        row.Cells.Add("Col 2");
        row.Cells.Add("Col 3");

        // Replace the table with new one
        absorber.Replace(document.Pages[1], table, newTable);

        // Save PDF document
        document.Save(dataDir + "ReplaceTable_out.pdf");
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