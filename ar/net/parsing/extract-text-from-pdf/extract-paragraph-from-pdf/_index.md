---
title: استخراج الفقرات من PDF C#
linktitle: استخراج الفقرات من PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ar/net/extract-paragraph-from-pdf/
description: تعلم كيفية استخراج الفقرات من مستندات PDF في .NET باستخدام Aspose.PDF لاسترجاع النص المنظم.
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
    "abstract": "تتيح ميزة ParagraphAbsorber الجديدة في Aspose.PDF للمطورين استخراج الفقرات والتلاعب بها بكفاءة من مستندات PDF. مع هذه الأداة، يمكن للمستخدمين استرجاع النص ليس فقط في تنسيق فقرة منظم ولكن أيضًا تصور الأقسام من خلال حدود قابلة للتخصيص، مما يعزز دقة استخراج النص من PDF. تبسط هذه الوظيفة العمل مع بيانات PDF المنظمة، مما يجعلها لا تقدر بثمن للتطبيقات التي تتطلب تحليل نصوص متعمق.",
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
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة، ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## استخراج النص من مستند PDF على شكل فقرات

يمكننا الحصول على النص من مستند PDF من خلال البحث عن نص معين (باستخدام "نص عادي" أو "تعبيرات منتظمة") من صفحة واحدة أو المستند بالكامل، أو يمكننا الحصول على النص الكامل لصفحة واحدة، أو مجموعة من الصفحات أو المستند بالكامل. ومع ذلك، في بعض الحالات، تحتاج إلى استخراج الفقرات من مستند PDF أو النص على شكل فقرات. لقد قمنا بتنفيذ وظيفة للبحث عن الأقسام والفقرات في نص صفحات مستند PDF. لقد قدمنا فئة ParagraphAbsorber (مثل TextFragmentAbsorber و TextAbsorber)، والتي يمكن استخدامها لاستخراج الفقرات من مستندات PDF. هناك طريقتان يمكنك من خلالهما استخدام ParagraphAbsorber:

**عن طريق رسم حدود الأقسام والفقرات من النص على صفحة PDF:**

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

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

**عن طريق التكرار عبر مجموعة الفقرات والحصول على نصها:**

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

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