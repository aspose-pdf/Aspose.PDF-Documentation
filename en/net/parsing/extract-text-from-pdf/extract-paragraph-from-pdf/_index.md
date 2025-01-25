---
title: Extract Paragraph from PDF C#
linktitle: Extract Paragraph from PDF
type: docs
weight: 20
url: /net/extract-paragraph-from-pdf/
description: Learn how to extract paragraphs from PDF documents in .NET using Aspose.PDF for structured text retrieval.
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
    "abstract": "The new ParagraphAbsorber feature in Aspose.PDF allows developers to efficiently extract and manipulate paragraphs from PDF documents. With this tool, users can not only retrieve text in an organized paragraph format but also visualize sections through customizable borders, enhancing PDF text extraction precision. This functionality simplifies working with structured PDF data, making it invaluable for applications requiring in-depth text analysis",
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
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Extract Text from PDF document in Paragraphs form

We can get text from a PDF document by searching a particular text (using "plain text" or "regular expressions") from a single page or whole document, or we can get the complete text of a single page, range of pages or complete document. However, in some cases, you require to extract paragraphs from a PDF document or text in the form of Paragraphs. We have implemented functionality for searching sections and paragraphs in the text of PDF document pages. We have introduced ParagraphAbsorber Class (like TextFragmentAbsorber and TextAbsorber), which can be used to extract paragraphs from PDF documents. There are two following ways in which you can use ParagraphAbsorber:

**By drawing the border of sections and paragraphs of text on PDF page:**

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

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

**By iterating through paragraphs collection and get the text of them:**

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

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

