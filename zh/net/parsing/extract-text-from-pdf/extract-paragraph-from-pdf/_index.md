---
title: 从 PDF 中提取段落 C#
linktitle: 从 PDF 中提取段落
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/extract-paragraph-from-pdf/
description: 学习如何使用 Aspose.PDF 在 .NET 中从 PDF 文档中提取段落以进行结构化文本检索。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Paragraph from PDF C#",
    "alternativeHeadline": "Extract Text from PDF as Paragraphs Efficiently",
    "abstract": "Aspose.PDF 中的新 ParagraphAbsorber 功能允许开发人员高效地从 PDF 文档中提取和操作段落。使用此工具，用户不仅可以以组织良好的段落格式检索文本，还可以通过可自定义的边框可视化部分，从而提高 PDF 文本提取的精确度。此功能简化了处理结构化 PDF 数据的工作，使其对需要深入文本分析的应用程序变得不可或缺。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "590",
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
    "url": "/net/extract-paragraph-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-paragraph-from-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单易行的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 以段落形式从 PDF 文档中提取文本

我们可以通过搜索特定文本（使用“纯文本”或“正则表达式”）从单个页面或整个文档中获取 PDF 文档的文本，或者我们可以获取单个页面、页面范围或完整文档的完整文本。然而，在某些情况下，您需要从 PDF 文档中提取段落或以段落形式提取文本。我们已经实现了在 PDF 文档页面的文本中搜索部分和段落的功能。我们引入了 ParagraphAbsorber 类（类似于 TextFragmentAbsorber 和 TextAbsorber），可以用于从 PDF 文档中提取段落。您可以通过以下两种方式使用 ParagraphAbsorber：

**通过在 PDF 页面上绘制文本的部分和段落的边框：**

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractParagraphWithDrawingTheBorder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentForExtract.pdf"))
    {
        var page = document.Pages[2];

        var absorber = new Aspose.Pdf.Text.ParagraphAbsorber();
        absorber.Visit(page);

        Aspose.Pdf.Text.PageMarkup markup = absorber.PageMarkups[0];

        foreach (Aspose.Pdf.Text.MarkupSection section in markup.Sections)
        {
            DrawRectangleOnPage(section.Rectangle, page);
            foreach (Aspose.Pdf.Text.MarkupParagraph paragraph in section.Paragraphs)
            {
                DrawPolygonOnPage(paragraph.Points, page);
            }
        }

        // Save PDF document
        document.Save(dataDir + "DocumentWithBorder_out.pdf");
    }
}

private static void DrawRectangleOnPage(Aspose.Pdf.Rectangle rectangle, Aspose.Pdf.Page page)
{
    page.Contents.Add(new Aspose.Pdf.Operators.GSave());
    page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 0, 0));
    page.Contents.Add(new Aspose.Pdf.Operators.SetRGBColorStroke(0, 1, 0));
    page.Contents.Add(new Aspose.Pdf.Operators.SetLineWidth(2));
    page.Contents.Add(
        new Aspose.Pdf.Operators.Re(rectangle.LLX,
            rectangle.LLY,
            rectangle.Width,
            rectangle.Height));
    page.Contents.Add(new Aspose.Pdf.Operators.ClosePathStroke());
    page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
}

private static void DrawPolygonOnPage(Aspose.Pdf.Point[] polygon, Aspose.Pdf.Page page)
{
    page.Contents.Add(new Aspose.Pdf.Operators.GSave());
    page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 0, 0));
    page.Contents.Add(new Aspose.Pdf.Operators.SetRGBColorStroke(0, 0, 1));
    page.Contents.Add(new Aspose.Pdf.Operators.SetLineWidth(1));
    page.Contents.Add(new Aspose.Pdf.Operators.MoveTo(polygon[0].X, polygon[0].Y));
    for (int i = 1; i < polygon.Length; i++)
    {
        page.Contents.Add(new Aspose.Pdf.Operators.LineTo(polygon[i].X, polygon[i].Y));
    }
    page.Contents.Add(new Aspose.Pdf.Operators.LineTo(polygon[0].X, polygon[0].Y));
    page.Contents.Add(new Aspose.Pdf.Operators.ClosePathStroke());
    page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
}
```

**通过迭代段落集合并获取它们的文本：**

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractParagraphByIteratingThroughParagraphsCollection()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentForExtract.pdf"))
    {
        // Instantiate ParagraphAbsorber
        var absorber = new Aspose.Pdf.Text.ParagraphAbsorber();
        absorber.Visit(document);

        foreach (Aspose.Pdf.Text.PageMarkup markup in absorber.PageMarkups)
        {
            int i = 1;
            foreach (Aspose.Pdf.Text.MarkupSection section in markup.Sections)
            {
                int j = 1;
                foreach (Aspose.Pdf.Text.MarkupParagraph paragraph in section.Paragraphs)
                {
                    StringBuilder paragraphText = new StringBuilder();
                    foreach (List<Aspose.Pdf.Text.TextFragment> line in paragraph.Lines)
                    {
                        foreach (Aspose.Pdf.Text.TextFragment fragment in line)
                        {
                            paragraphText.Append(fragment.Text);
                        }
                        paragraphText.Append("\r\n");
                    }
                    paragraphText.Append("\r\n");

                    Console.WriteLine("Paragraph {0} of section {1} on page {2}:", j, i, markup.Number);
                    Console.WriteLine(paragraphText.ToString());

                    j++;
                }
                i++;
            }
        }
    }
}
```