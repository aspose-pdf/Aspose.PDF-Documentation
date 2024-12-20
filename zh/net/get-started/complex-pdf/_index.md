---
title: 创建复杂的PDF文档
linktitle: 创建复杂的PDF文档
type: docs
weight: 60
url: /zh/net/complex-pdf-example/
description: Aspose.PDF for NET允许您创建包含图片、文本片段和表格的更复杂的文档。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

[Hello, World](/pdf/zh/net/hello-world-example/) 示例展示了使用C#和Aspose.PDF创建PDF文档的简单步骤。在本文中，我们将探讨使用C#和Aspose.PDF for .NET创建更复杂的文档。作为示例，我们将采用一家虚构公司运营的客运渡轮服务的文档。
我们的文档将包含一个图像、两个文本片段（标题和段落）和一个表格。为了构建这样的文档，我们将采用基于DOM的方法。您可以在[Basics of DOM API](/pdf/zh/net/basics-of-dom-api/)部分阅读更多信息。

如果我们从头开始创建文档，我们需要遵循以下步骤：

1.
1. 向文档对象添加一个[页面](https://reference.aspose.com/pdf/net/aspose.pdf/page)。所以，现在我们的文档将有一页。
1. 向页面添加一个[图像](https://reference.aspose.com/pdf/net/aspose.pdf/image/methods/index)。
1. 为标题创建一个[文本片段](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment)。对于标题，我们将使用Arial字体，字体大小为24pt，居中对齐。
1. 将标题添加到页面[段落](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs)中。
1. 为描述创建一个[文本片段](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment)。对于描述，我们将使用Arial字体，字体大小为24pt，居中对齐。
1. 将（描述）添加到页面段落中。
1. 创建一个表格，添加表格属性。
1. 将（表格）添加到页面[段落](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs)中。
1. 保存文档“Complex.pdf”。

以下代码片段也适用于[Aspose.PDF.Drawing](/pdf/zh/net/drawing/)库。
以下代码片段也适用于[Aspose.PDF.Drawing](/pdf/zh/net/drawing/)库。

```csharp
using Aspose.Pdf.Text;
using System;
using System.IO;

namespace Aspose.Pdf.Examples
{
    public static class ExampleGetStarted
    {
        private static readonly string _dataDir = "..\\..\\..\\Samples";
public static void MakeComplexDocument()
        {
            // 初始化文档对象
            Document document = new Document();
            // 添加页面
            Page page = document.Pages.Add();

            // -------------------------------------------------------------
            // 添加图片
            var imageFileName = System.IO.Path.Combine(_dataDir, "logo.png");
            page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

            // -------------------------------------------------------------
            // 添加头部
            var header = new TextFragment("2020年秋季新的渡轮路线");
            header.TextState.Font = FontRepository.FindFont("Arial");
            header.TextState.FontSize = 24;
            header.HorizontalAlignment = HorizontalAlignment.Center;
            header.Position = new Position(130, 720);
            page.Paragraphs.Add(header);

            // 添加描述
            var descriptionText = "游客必须在线购票，每天的票数限制为5000张。渡轮服务以半载量和缩减的时间表运行。请预计排队等候。";
            var description = new TextFragment(descriptionText);
            description.TextState.Font = FontRepository.FindFont("Times New Roman");
            description.TextState.FontSize = 14;
            description.HorizontalAlignment = HorizontalAlignment.Left;
            page.Paragraphs.Add(description);


            // 添加表格
            var table = new Table
            {
                ColumnWidths = "200",
                Border = new BorderInfo(BorderSide.Box, 1f, Color.DarkSlateGray),
                DefaultCellBorder = new BorderInfo(BorderSide.Box, 0.5f, Color.Black),
                DefaultCellPadding = new MarginInfo(4.5, 4.5, 4.5, 4.5),
                Margin =
                {
                    Bottom = 10
                },
                DefaultCellTextState =
                {
                    Font =  FontRepository.FindFont("Helvetica")
                }
            };

            var headerRow = table.Rows.Add();
            headerRow.Cells.Add("出发城市");
            headerRow.Cells.Add("出发岛屿");
            foreach (Cell headerRowCell in headerRow.Cells)
            {
                headerRowCell.BackgroundColor = Color.Gray;
                headerRowCell.DefaultCellTextState.ForegroundColor = Color.WhiteSmoke;
            }

            var time = new TimeSpan(6, 0, 0);
            var incTime = new TimeSpan(0, 30, 0);
            for (int i = 0; i < 10; i++)
            {
                var dataRow = table.Rows.Add();
                dataRow.Cells.Add(time.ToString(@"hh\:mm"));
                time=time.Add(incTime);
                dataRow.Cells.Add(time.ToString(@"hh\:mm"));
            }

            page.Paragraphs.Add(table);

            document.Save(System.IO.Path.Combine(_dataDir, "Complex.pdf"));

        }
    }
}
```

