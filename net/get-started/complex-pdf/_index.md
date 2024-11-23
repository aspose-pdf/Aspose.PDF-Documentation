---
title: Creating a complex PDF
linktitle: Creating a complex PDF
type: docs
weight: 60
url: /net/complex-pdf-example/
description: Aspose.PDF for NET allows you to create more complex documents that contain images, text fragments, and tables in one document.
aliases:
    - /net/complex-pdf/
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

The [Hello, World](/pdf/net/hello-world-example/) example showed simple steps to create a PDF document using C# and Aspose.PDF. In this article, we will take a look at creating a more complex document with C# and Aspose.PDF for .NET. As an example, we'll take a document from a fictitious company that operates passenger ferry services.
Our document will contain a image, two text fragments (header and paragraph), and a table. To build such a document, we will use DOM-base approach. You can read more in section [Basics of DOM API](/pdf/net/basics-of-dom-api/).

If we create a document from scratch we need to follow certain steps:

1. Instantiate a [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object. In this step we will create an empty PDF document with some metadata but without pages.
1. Add a [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) to the document object. So, now our document will have one page.
1. Add a [Image](https://reference.aspose.com/pdf/net/aspose.pdf/image/methods/index) to the Page.
1. Create a [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) for header. For the header we will use Arial font with font size 24pt and center alignment.
1. Add header to the page [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs).
1. Create a [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) for description. For the description we will use Arial font with font size 24pt and center alignment.
1. Add (description) to the page Paragraphs.
1. Create a table, add table properties.
1. Add (table) to the page [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs).
1. Save a document "Complex.pdf".

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

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
            // Initialize document object
            Document document = new Document();
            // Add page
            Page page = document.Pages.Add();

            // Add image
            var imageFileName = _dataDir + "logo.png";
            page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

            // Add Header
            var header = new TextFragment("New ferry routes in Fall 2020");
            header.TextState.Font = FontRepository.FindFont("Arial");
            header.TextState.FontSize = 24;
            header.HorizontalAlignment = HorizontalAlignment.Center;
            header.Position = new Position(130, 720);
            page.Paragraphs.Add(header);

            // Add description
            var descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. Ferry service is operating at half capacity and on a reduced schedule. Expect lineups.";
            var description = new TextFragment(descriptionText);
            description.TextState.Font = FontRepository.FindFont("Times New Roman");
            description.TextState.FontSize = 14;
            description.HorizontalAlignment = HorizontalAlignment.Left;
            page.Paragraphs.Add(description);

            // Add table
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
            headerRow.Cells.Add("Departs City");
            headerRow.Cells.Add("Departs Island");
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

            document.Save(_dataDir + "Complex.pdf");
        }
    }
}
```
