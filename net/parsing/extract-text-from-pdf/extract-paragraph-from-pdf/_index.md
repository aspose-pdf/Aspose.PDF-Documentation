---
title: Extract Paragraph from PDF C#
linktitle: Extract Paragraph from PDF
type: docs
weight: 20
url: /net/extract-paragraph-from-pdf/
description: This article describes how to use ParagraphAbsorber - a special tool in Aspose.PDF to extract text from PDF documents.
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
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractParagraph()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    Document document = new Document(dataDir + "input.pdf");
    Page page = document.Pages[2];

    ParagraphAbsorber absorber = new ParagraphAbsorber();
    absorber.Visit(page);

    PageMarkup markup = absorber.PageMarkups[0];

    foreach (MarkupSection section in markup.Sections)
    {
        DrawRectangleOnPage(section.Rectangle, page);
        foreach (MarkupParagraph paragraph in section.Paragraphs)
        {
            DrawPolygonOnPage(paragraph.Points, page);
        }
    }

    document.Save(dataDir + "output_out.pdf");
}

private static void DrawRectangleOnPage(Rectangle rectangle, Page page)
{
    page.Contents.Add(new Operators.GSave());
    page.Contents.Add(new Operators.ConcatenateMatrix(1, 0, 0, 1, 0, 0));
    page.Contents.Add(new Operators.SetRGBColorStroke(0, 1, 0));
    page.Contents.Add(new Operators.SetLineWidth(2));
    page.Contents.Add(
        new Operators.Re(rectangle.LLX,
            rectangle.LLY,
            rectangle.Width,
            rectangle.Height));
    page.Contents.Add(new Operators.ClosePathStroke());
    page.Contents.Add(new Operators.GRestore());
}

private static void DrawPolygonOnPage(Point[] polygon, Page page)
{
    page.Contents.Add(new Operators.GSave());
    page.Contents.Add(new Operators.ConcatenateMatrix(1, 0, 0, 1, 0, 0));
    page.Contents.Add(new Operators.SetRGBColorStroke(0, 0, 1));
    page.Contents.Add(new Operators.SetLineWidth(1));
    page.Contents.Add(new Operators.MoveTo(polygon[0].X, polygon[0].Y));
    for (int i = 1; i < polygon.Length; i++)
    {
        page.Contents.Add(new Operators.LineTo(polygon[i].X, polygon[i].Y));
    }
    page.Contents.Add(new Operators.LineTo(polygon[0].X, polygon[0].Y));
    page.Contents.Add(new Operators.ClosePathStroke());
    page.Contents.Add(new Operators.GRestore());
}
```

**By iterating through paragraphs collection and get the text of them:**

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Open an existing PDF file
Document document = new Document(dataDir + "input.pdf");
// Instantiate ParagraphAbsorber
ParagraphAbsorber absorber = new ParagraphAbsorber();
absorber.Visit(document);

foreach (PageMarkup markup in absorber.PageMarkups)
{
    int i = 1;
    foreach (MarkupSection section in markup.Sections)
    {
        int j = 1;
        foreach (MarkupParagraph paragraph in section.Paragraphs)
        {
            StringBuilder paragraphText = new StringBuilder();
            foreach (List<TextFragment> line in paragraph.Lines)
            {
                foreach (TextFragment fragment in line)
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
```

