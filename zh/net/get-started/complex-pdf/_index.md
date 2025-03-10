---
title: 创建复杂的PDF
linktitle: 创建复杂的PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /zh/net/complex-pdf-example/
description: Aspose.PDF for NET 允许您创建包含图像、文本片段和表格的更复杂的文档。
aliases:
    - /net/complex-pdf/
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
    "abstract": "Aspose.PDF for .NET 引入了一项强大的功能，用于创建复杂的PDF，使开发人员能够无缝地将图像、文本片段和表格集成到一个文档中。此功能利用基于DOM的方法，允许在PDF生成中进行详细的自定义和布局控制，使其非常适合高效创建专业级文档。",
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
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

[Hello, World](/pdf/net/hello-world-example/) 示例展示了使用 C# 和 Aspose.PDF 创建 PDF 文档的简单步骤。在本文中，我们将看看如何使用 C# 和 Aspose.PDF for .NET 创建更复杂的文档。作为示例，我们将使用一家虚构公司的文档，该公司经营客运渡轮服务。
我们的文档将包含一张图像、两个文本片段（标题和段落）以及一个表格。为了构建这样的文档，我们将使用基于DOM的方法。您可以在 [DOM API 基础知识](/pdf/net/basics-of-dom-api/) 部分中阅读更多内容。

如果我们从头开始创建文档，我们需要遵循以下步骤：

1. 实例化一个 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 对象。在这一步中，我们将创建一个带有一些元数据但没有页面的空 PDF 文档。
1. 向文档对象添加一个 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)。现在我们的文档将有一页。
1. 向页面添加一个 [Image](https://reference.aspose.com/pdf/net/aspose.pdf/image/methods/index)。
1. 为标题创建一个 [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment)。对于标题，我们将使用 Arial 字体，字体大小为 24pt，居中对齐。
1. 将标题添加到页面的 [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs)。
1. 为描述创建一个 [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment)。对于描述，我们将使用 Arial 字体，字体大小为 24pt，居中对齐。
1. 将（描述）添加到页面的段落中。
1. 创建一个表格，添加表格属性。
1. 将（表格）添加到页面的 [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs)。
1. 保存文档为 "Complex.pdf"。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

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