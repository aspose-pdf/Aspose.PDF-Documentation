---
title: 从PDF页面搜索和获取文本
linktitle: 搜索和获取文本
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /zh/net/search-and-get-text-from-pdf/
description: 了解如何使用Aspose.PDF在.NET中搜索和检索PDF文件中的文本，以进行文本分析和提取。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Search and Get Text from Pages of PDF",
    "alternativeHeadline": "Search and Extract Text from PDF Pages",
    "abstract": "Aspose.PDF for .NET使用户能够高效地搜索和提取PDF文档所有页面中的文本。此功能利用TextFragmentAbsorber类定位指定的短语或文本段落，并提供对正则表达式的高级支持，从而实现精确的文本检索和操作。对于开发人员来说，此功能通过简化文本提取过程增强了PDF文档处理能力。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2762",
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
    "url": "/net/search-and-get-text-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/search-and-get-text-from-pdf/"
    },
    "dateModified": "2024-11-26",
    "description": "本文解释了如何使用各种工具从Aspose.PDF for .NET中搜索和获取文本。"
}
</script>

以下代码片段也适用于[Aspose.PDF.Drawing](/pdf/net/drawing/)库。

## 从PDF文档的所有页面搜索和获取文本

[TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber)类允许您从PDF文档的所有页面中找到匹配特定短语的文本。为了从整个文档中搜索文本，您需要调用页面集合的Accept方法。[Accept](https://reference.aspose.com/pdf/net/aspose.pdf.page/accept/methods/3)方法将TextFragmentAbsorber对象作为参数，该对象返回TextFragment对象的集合。您可以遍历所有片段并获取它们的属性，如Text、Position (XIndent, YIndent)、FontName、FontSize、IsAccessible、IsEmbedded、IsSubset、ForegroundColor等。

以下代码片段向您展示了如何从所有页面搜索文本。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("text");

        // Accept the absorber for all the pages
        document.Pages.Accept(textFragmentAbsorber);

        // Get the extracted text fragments
        var textFragmentCollection = textFragmentAbsorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in textFragmentCollection)
        {
            Console.WriteLine("Text : {0} ", textFragment.Text);
            Console.WriteLine("Position : {0} ", textFragment.Position);
            Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
            Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
            Console.WriteLine("Font - Name : {0}", textFragment.TextState.Font.FontName);
            Console.WriteLine("Font - IsAccessible : {0} ", textFragment.TextState.Font.IsAccessible);
            Console.WriteLine("Font - IsEmbedded : {0} ", textFragment.TextState.Font.IsEmbedded);
            Console.WriteLine("Font - IsSubset : {0} ", textFragment.TextState.Font.IsSubset);
            Console.WriteLine("Font Size : {0} ", textFragment.TextState.FontSize);
            Console.WriteLine("Foreground Color : {0} ", textFragment.TextState.ForegroundColor);
        }
    }
}
```

如果您需要在特定的PDF页面内搜索文本，请指定文档实例的页面集合中的页面编号，并对该页面调用Accept方法（如下代码行所示）。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("text");

        // Accept the absorber for a particular page
        document.Pages[2].Accept(textFragmentAbsorber);
    }
}
```

### 在TextFragmentAbsorber中通过短语列表搜索

C#库只能将一个短语传递给TextFragmentAbsorber，但自Aspose.PDF 24.2版本以来，它实现了一种新的列表搜索算法。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // Create resular expressions
    var regexes = new Regex[]
    {
        new Regex(@"(?s)document\s+(?:(?:no\(?s?\)?\.?)|(?:number(?:\(?s\)?)?))\s+(?:(?:[\w-]*\d[\w-]*)+(?:[,;\s]|and)*)", RegexOptions.IgnoreCase),
        new Regex(@"[\s\r\n]+Tract[\s\r\n]+of:? ", RegexOptions.IgnoreCase),
        new Regex(@"vested[\s\r\n]+in", RegexOptions.IgnoreCase),
        new Regex("Vested in:", RegexOptions.IgnoreCase),
        new Regex(@"file.?[\s\r\n]+(?:nos?|numbers?|#s?|nums?).?[\s\r\n]+(\d+)-(\d+)", RegexOptions.IgnoreCase),
        new Regex(@"file.?[\s\r\n]+nos?.?:?[\s\r\n]+([\d\r\n-]+)", RegexOptions.IgnoreCase)
    };

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchRegularExpressionAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber(regexes, new Aspose.Pdf.Text.TextSearchOptions(true));
        document.Pages.Accept(absorber);
        // Get result
        var result = absorber.RegexResults;
    }
}
```

该代码片段使用正则表达式在PDF文档中搜索特定模式，如文档编号、关键字和文件编号。它加载PDF，应用搜索，并检索匹配结果以进行进一步处理。

## 从PDF文档的所有页面搜索和获取文本段

为了从所有页面搜索文本段，您首先需要从文档中获取TextFragment对象。TextFragmentAbsorber允许您从PDF文档的所有页面中找到匹配特定短语的文本。为了从整个文档中搜索文本，您需要调用页面集合的Accept方法。Accept方法将TextFragmentAbsorber对象作为参数，该对象返回TextFragment对象的集合。一旦从文档中获取TextFragmentCollection，您需要遍历该集合并获取每个TextFragment对象的TextSegmentCollection。之后，您可以获取每个TextSegment对象的所有属性。以下代码片段向您展示了如何从所有页面搜索文本段。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextPage.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Figure");

        // Accept the absorber for all the pages
        document.Pages.Accept(textFragmentAbsorber);

        // Get the extracted text fragments
        var textFragmentCollection = textFragmentAbsorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in textFragmentCollection)
        {
            foreach (var textSegment in textFragment.Segments)
            {
                Console.WriteLine("Text : {0} ", textSegment.Text);
                Console.WriteLine("Position : {0} ", textSegment.Position);
                Console.WriteLine("XIndent : {0} ", textSegment.Position.XIndent);
                Console.WriteLine("YIndent : {0} ", textSegment.Position.YIndent);
                Console.WriteLine("Font - Name : {0}", textSegment.TextState.Font.FontName);
                Console.WriteLine("Font - IsAccessible : {0} ", textSegment.TextState.Font.IsAccessible);
                Console.WriteLine("Font - IsEmbedded : {0} ", textSegment.TextState.Font.IsEmbedded);
                Console.WriteLine("Font - IsSubset : {0} ", textSegment.TextState.Font.IsSubset);
                Console.WriteLine("Font Size : {0} ", textSegment.TextState.FontSize);
                Console.WriteLine("Foreground Color : {0} ", textSegment.TextState.ForegroundColor);
            }
        }
    }
}
```

为了从特定的PDF页面搜索和获取TextSegments，您需要在调用Accept(..)方法时指定特定的页面索引。请查看以下代码行。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("text");

        // Accept the absorber for a particular page
        document.Pages[2].Accept(textFragmentAbsorber);
    }
}
```

## 使用正则表达式从所有页面搜索和获取文本

TextFragmentAbsorber帮助您根据正则表达式搜索和检索所有页面中的文本。首先，您需要将正则表达式作为短语传递给TextFragmentAbsorber构造函数。之后，您必须设置TextFragmentAbsorber对象的TextSearchOptions属性。该属性需要TextSearchOptions对象，并且在创建新对象时需要将true作为参数传递给其构造函数。由于您希望从所有页面中检索匹配的文本，因此需要调用页面集合的Accept方法。TextFragmentAbsorber返回一个TextFragmentCollection，其中包含所有符合正则表达式指定标准的片段。以下代码片段向您展示了如何根据正则表达式搜索和获取所有页面中的文本。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchRegularExpressionAll.pdf"))
    {
        // Create TextAbsorber object to find all the phrases matching the regular expression
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("\\d{4}-\\d{4}"); // Like 1999-2000

        // Set text search option to specify regular expression usage
        var textSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(true);

        textFragmentAbsorber.TextSearchOptions = textSearchOptions;

        // Accept the absorber for all the pages
        document.Pages.Accept(textFragmentAbsorber);

        // Get the extracted text fragments
        var textFragmentCollection = textFragmentAbsorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in textFragmentCollection)
        {
            Console.WriteLine("Text : {0} ", textFragment.Text);
            Console.WriteLine("Position : {0} ", textFragment.Position);
            Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
            Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
            Console.WriteLine("Font - Name : {0}", textFragment.TextState.Font.FontName);
            Console.WriteLine("Font - IsAccessible : {0} ", textFragment.TextState.Font.IsAccessible);
            Console.WriteLine("Font - IsEmbedded : {0} ", textFragment.TextState.Font.IsEmbedded);
            Console.WriteLine("Font - IsSubset : {0} ", textFragment.TextState.Font.IsSubset);
            Console.WriteLine("Font Size : {0} ", textFragment.TextState.FontSize);
            Console.WriteLine("Foreground Color : {0} ", textFragment.TextState.ForegroundColor);
        }
    }
}
```

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void TextFragmentAbsorberCtor()
{
    Aspose.Pdf.Text.TextFragmentAbsorber textFragmentAbsorber;
    // In order to search exact match of a word, you may consider using regular expression
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"\bWord\b", new Aspose.Pdf.Text.TextSearchOptions(true));

    // In order to search a string in either upper case or lowercase, you may consider using regular expression
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("(?i)Line", new Aspose.Pdf.Text.TextSearchOptions(true));

    // In order to search all the strings (parse all strings) inside PDF document, please try using following regular expression
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"[\S]+");

    // Find match of search string and get anything after the string till line break
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"(?i)the ((.)*)");

    // Please use following regular expression to find text following to the regex match
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"(?<=word).*");

    // In order to search Hyperlink/URL's inside PDF document, please try using following regular expression
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?");
}
```

## 基于正则表达式搜索文本并添加超链接

如果您想在基于正则表达式的文本短语上添加超链接，首先使用TextFragmentAbsorber找到所有匹配该特定正则表达式的短语，并在这些短语上添加超链接。

要找到短语并在其上添加超链接：

1. 将正则表达式作为参数传递给TextFragmentAbsorber构造函数。
2. 创建一个TextSearchOptions对象，指定是否使用正则表达式。
3. 将匹配的短语放入TextFragments中。
4. 遍历匹配项以获取它们的矩形尺寸，将前景色更改为蓝色（可选 - 使其看起来像超链接），并使用PdfContentEditor类的CreateWebLink(..)方法创建链接。
5. 使用Document对象的Save方法保存更新后的PDF。
以下代码片段向您展示了如何使用正则表达式在PDF文件中搜索文本并在匹配项上添加超链接。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create absorber object to find all instances of the input search phrase
    var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("\\d{4}-\\d{4}");

    // Enable regular expression search
    absorber.TextSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(true);

    // Create the editor
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "SearchRegularExpressionPage.pdf");

        // Accept the absorber for the page
        editor.Document.Pages[1].Accept(absorber);

        int[] dashArray = { };
        String[] LEArray = { };
        System.Drawing.Color blue = System.Drawing.Color.Blue;

        // Loop through the fragments
        foreach (var textFragment in absorber.TextFragments)
        {
            textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle((int)textFragment.Rectangle.LLX,
                (int)Math.Round(textFragment.Rectangle.LLY), (int)Math.Round(textFragment.Rectangle.Width + 2),
                (int)Math.Round(textFragment.Rectangle.Height + 1));
            Enum[] actionName = new Enum[2] { Aspose.Pdf.Annotations.PredefinedAction.Document_AttachFile, Aspose.Pdf.Annotations.PredefinedAction.Document_ExtractPages };
            editor.CreateWebLink(rect, "http:// Www.aspose.com", 1, blue, actionName);
            editor.CreateLine(rect, "", (float)textFragment.Rectangle.LLX + 1, (float)textFragment.Rectangle.LLY - 1,
                (float)textFragment.Rectangle.URX, (float)textFragment.Rectangle.LLY - 1, 1, 1, blue, "S", dashArray, LEArray);
        }

        // Save PDF document
        editor.Save(dataDir + "SearchTextAndAddHyperlink_out.pdf");
    }
}
```

## 搜索并在每个TextFragment周围绘制矩形

Aspose.PDF for .NET支持搜索并获取每个字符或文本片段的坐标的功能。因此，为了确保返回每个字符的坐标，我们可以考虑在每个字符周围高亮显示（添加矩形）。

在文本段落的情况下，您可以考虑使用某些正则表达式来确定段落的换行，并在其周围绘制矩形。请查看以下代码片段。以下代码片段获取每个字符的坐标并在每个字符周围创建一个矩形。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SearchAndDraw()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf"))
    {

        // Create TextAbsorber object to find all the phrases matching the regular expression
        var textAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"[\S]+");

        var textSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(true);
        textAbsorber.TextSearchOptions = textSearchOptions;

        document.Pages.Accept(textAbsorber);

        using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(document))
        {
            foreach (var textFragment in textAbsorber.TextFragments)
            {
                foreach (var textSegment in textFragment.Segments)
                {
                    //DrawBox(editor, textFragment.Page.Number, textSegment, System.Drawing.Color.Red);
                }
            }
        }
        // Save PDF document
        document.Save(dataDir + "SearchTextAndDrawRectangle_out.pdf");
    }
}
```

## 在PDF文档中高亮显示每个字符

{{% alert color="primary" %}}

您可以尝试使用Aspose.PDF在文档中搜索文本，并在此[链接](https://products.aspose.app/pdf/search)上获取结果。

{{% /alert %}}

Aspose.PDF for .NET支持搜索并获取每个字符或文本片段的坐标的功能。因此，为了确保返回每个字符的坐标，我们可以考虑在每个字符周围高亮显示（添加矩形）。以下代码片段获取每个字符的坐标并在每个字符周围创建一个矩形。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SearchAndHighlight()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    int resolution = 150;

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf"))
    {

        using (MemoryStream stream = new MemoryStream())
        {
            var conv = new Aspose.Pdf.Facades.PdfConverter(document);
            conv.Resolution = new Aspose.Pdf.Devices.Resolution(resolution, resolution);
            conv.GetNextImage(stream, System.Drawing.Imaging.ImageFormat.Png);

            using (var bmp = System.Drawing.Bitmap.FromStream(stream))
            {

                using (System.Drawing.Graphics gr = System.Drawing.Graphics.FromImage(bmp))
                {
                    float scale = resolution / 72f;
                    gr.Transform = new System.Drawing.Drawing2D.Matrix(scale, 0, 0, -scale, 0, bmp.Height);

                    for (int i = 0; i < document.Pages.Count; i++)
                    {
                        var page = document.Pages[1];
                        // Create TextAbsorber object to find all words
                        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"[\S]+");
                        textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;
                        page.Accept(textFragmentAbsorber);
                        // Get the extracted text fragments
                        var textFragmentCollection = textFragmentAbsorber.TextFragments;
                        // Loop through the fragments
                        foreach (var textFragment in textFragmentCollection)
                        {
                            if (i == 0)
                            {
                                gr.DrawRectangle(
                                    System.Drawing.Pens.Yellow,
                                    (float)textFragment.Position.XIndent,
                                    (float)textFragment.Position.YIndent,
                                    (float)textFragment.Rectangle.Width,
                                    (float)textFragment.Rectangle.Height);

                                for (int segNum = 1; segNum <= textFragment.Segments.Count; segNum++)
                                {
                                    var segment = textFragment.Segments[segNum];

                                    for (int charNum = 1; charNum <= segment.Characters.Count; charNum++)
                                    {
                                        var characterInfo = segment.Characters[charNum];

                                        Aspose.Pdf.Rectangle rect = page.GetPageRect(true);
                                        Console.WriteLine("TextFragment = " + textFragment.Text + "    Page URY = " + rect.URY +
                                            "   TextFragment URY = " + textFragment.Rectangle.URY);

                                        gr.DrawRectangle(
                                            System.Drawing.Pens.Black,
                                            (float)characterInfo.Rectangle.LLX,
                                            (float)characterInfo.Rectangle.LLY,
                                            (float)characterInfo.Rectangle.Width,
                                            (float)characterInfo.Rectangle.Height);
                                    }

                                    gr.DrawRectangle(
                                        System.Drawing.Pens.Green,
                                        (float)segment.Rectangle.LLX,
                                        (float)segment.Rectangle.LLY,
                                        (float)segment.Rectangle.Width,
                                        (float)segment.Rectangle.Height);
                                }
                            }
                        }
                    }
                }
                
                // Save result
                bmp.Save(dataDir + "HighlightCharacterInPDF_out.png", System.Drawing.Imaging.ImageFormat.Png);
            }
        }
    }
}
```

## 添加和搜索隐藏文本

有时我们希望在PDF文档中添加隐藏文本，然后搜索隐藏文本并使用其位置进行后处理。为了方便您，Aspose.PDF for .NET提供了这些功能。您可以在文档生成期间添加隐藏文本。此外，您可以使用TextFragmentAbsorber查找隐藏文本。要添加隐藏文本，请将TextState.Invisible设置为‘true’。TextFragmentAbsorber查找所有与模式匹配的文本（如果指定）。这是无法更改的默认行为。为了验证找到的文本是否实际上是不可见的，可以使用TextState.Invisible属性。以下代码片段展示了如何使用此功能。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateAndSearchText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var frag1 = new Aspose.Pdf.Text.TextFragment("This is common text.");
        var frag2 = new Aspose.Pdf.Text.TextFragment("This is invisible text.");

        //Set text property - invisible
        frag2.TextState.Invisible = true;

        page.Paragraphs.Add(frag1);
        page.Paragraphs.Add(frag2);
        // Save PDF document
        document.Save(dataDir + "CreateAndSearchText_out.pdf");
    }

    // Search text in the document
    using (var document = new Aspose.Pdf.Document(dataDir + "CreateAndSearchText_out.pdf"))
    {
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        absorber.Visit(document.Pages[1]);

        foreach (var fragment in absorber.TextFragments)
        {
            //Do something with fragments
            Console.WriteLine("Text '{0}' on pos {1} invisibility: {2} ",
            fragment.Text, fragment.Position.ToString(), fragment.TextState.Invisible);
        }
    }
}
```

## 使用.NET正则表达式搜索文本

Aspose.PDF for .NET提供了使用标准.NET正则表达式选项搜索文档的能力。TextFragmentAbsorber可以用于此目的，如下面的代码示例所示。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create Regex object to find all words
    var regex = new System.Text.RegularExpressions.Regex(@"[\S]+");

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchTextRegex.pdf"))
    {

        // Get a particular page
        var page = document.Pages[1];

        // Create TextAbsorber object to find all instances of the input regex
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(regex);
        textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;

        // Accept the absorber for the page
        page.Accept(textFragmentAbsorber);

        // Get the extracted text fragments
        var textFragmentCollection = textFragmentAbsorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in textFragmentCollection)
        {
            Console.WriteLine(textFragment.Text);
        }
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