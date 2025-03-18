---
title: Search and Get Text from Pages of PDF
linktitle: Search and Get Text
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /net/search-and-get-text-from-pdf/
description: Discover how to search and retrieve text from a PDF file in .NET using Aspose.PDF for text analysis and extraction.
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
    "abstract": "Aspose.PDF for .NET enables users to efficiently search and extract text from all pages of a PDF document. This functionality leverages the TextFragmentAbsorber class to locate specified phrases or text segments, along with advanced support for regular expressions, allowing for precise text retrieval and manipulation. Ideal for developers, this feature enhances PDF document handling capabilities by simplifying text extraction processes",
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
    "description": "This article explains how to use various tools to search and get a text from Aspose.PDF for .NET."
}
</script>

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Search and Get Text from All the Pages of PDF Document

[TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber) class allows you to find text, matching a particular phrase, from all the pages of a PDF document. In order to search text from the whole document, you need to call the Accept method of Pages collection. The [Accept](https://reference.aspose.com/pdf/net/aspose.pdf.page/accept/methods/3) method takes TextFragmentAbsorber object as a parameter, which returns a collection of TextFragment objects. You can loop through all the fragments and get their properties like Text, Position (XIndent, YIndent), FontName, FontSize, IsAccessible, IsEmbedded, IsSubset, ForegroundColor, etc.

The following code snippet shows you how to search for text from all the pages.

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

In case you need to search text inside any particular PDF page, please specify the page number from pages collection of Document instance and call Accept method against that page (as shown in code line below).

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

### Search through a list of phrases in a TextFragmentAbsorber

The C# library can only pass one phrase to the TextFragmentAbsorber, but since the 24.2 release of Aspose.PDF, it implemented a new algorithm for searching the list search algorithm.

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

The code snippet searches for specific patterns like document numbers, keywords, and file numbers in a PDF document using regular expressions. It loads the PDF, applies the search, and retrieves the matching results for further processing.

## Search and Get Text Segments from All Pages of PDF Document

In order to search text segments from all the pages, you first need to get the TextFragment objects from the document. TextFragmentAbsorber allows you to find text, matching a particular phrase, from all the pages of a PDF document. In order to search text from the whole document, you need to call the Accept method of Pages collection. The Accept method takes TextFragmentAbsorber object as a parameter, which returns a collection of TextFragment objects. Once the TextFragmentCollection is fetched from the document, you need to loop through this collection and get TextSegmentCollection of each TextFragment object. After that, you can get all the properties of the individual TextSegment object. The following code snippet shows you how to search text segments from all the pages.

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

In order to search and get TextSegments from a particular page of PDF, you need to specify the particular page index when calling Accept(..) method. Please take a look at the following code lines.

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

## Search and Get Text from all pages using Regular Expression

TextFragmentAbsorber helps you search and retrieve text, from all the pages, based on a regular expression. First, you need to pass a regular expression to TextFragmentAbsorber constructor as the phrase. After that, you have to set the TextSearchOptions property of the TextFragmentAbsorber object. This property requires TextSearchOptions object and you need to pass true as a parameter to its constructor while creating new objects. As you want to retrieve matching text from all the pages, you need to call Accept method of Pages collection. TextFragmentAbsorber returns a TextFragmentCollection containing all the fragments matching the criteria specified by the regular expression. The following code snippet shows you how to search and get text from all the pages based on a regular expression.

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

## Search Text based on Regex and Add Hyperlink

If you want to add hyperlink over a text phrase based on regular expression, first find all the phrases matching that particular regular expression using TextFragmentAbsorber and add hyperlink over these phrases.

To find a phrase and add hyperlink over it:

1. Pass the regular expression as a parameter to the TextFragmentAbsorber constructor.
2. Create a TextSearchOptions object which specifies whether the regular expression is used or not.
3. Get the matching phrases into TextFragments.
4. Loop through the matches to get their rectangular dimensions, change the foreground color to blue (optional - to make it appear like a hyperlink and create a link using the PdfContentEditor class’ CreateWebLink(..) method.
5. Save the updated PDF using Save method of Document object.
The following code snippet shows you how to search text inside a PDF file using a regular expression and adding hyperlinks over the matches.

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

## Search and Draw Rectangle around each TextFragment

Aspose.PDF for .NET supports the feature to search and get the coordinates of each character or text fragments. So in order to be certain about the coordinates being returned for each character, we may consider highlighting (adding rectangle) around each character.

In case of a text paragraph, you may consider using some regular expression to determine the paragraph break and draw a rectangle around it. Please take a look at the following code snippet. The following code snippet gets coordinates of each character and creates a rectangle around each character.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
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
        var textAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(".");

        var textSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(true);
        textAbsorber.TextSearchOptions = textSearchOptions;

        document.Pages.Accept(textAbsorber);

        foreach (var textFragment in textAbsorber.TextFragments)
        {
            DrawRectangleOnPage(textFragment.Rectangle, textFragment.Page, new Aspose.Pdf.Operators.SetRGBColorStroke(System.Drawing.Color.Red));
        }   
        // Save PDF document
        document.Save(dataDir + "SearchTextAndDrawRectangle_out.pdf");
    }
}

 private static void DrawRectangleOnPage(Aspose.Pdf.Rectangle rectangle, Aspose.Pdf.Page page, Aspose.Pdf.Operators.SetRGBColorStroke colorStroke = null)
 {
     if (colorStroke == null)
     {
         colorStroke = new Aspose.Pdf.Operators.SetRGBColorStroke(0.7, 0, 0);
     }

     page.Contents.Add(new Aspose.Pdf.Operators.GSave());
     page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 0, 0));
     page.Contents.Add(colorStroke);
     page.Contents.Add(
         new Re(rectangle.LLX,
             rectangle.LLY,
             rectangle.Width,
             rectangle.Height));
     page.Contents.Add(new Aspose.Pdf.Operators.ClosePathStroke());
     page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
 }
```

## Highlight each character in PDF document

{{% alert color="primary" %}}

You can try searching for text in a document using Aspose.PDF and get the results online at this [link](https://products.aspose.app/pdf/search)

{{% /alert %}}

Aspose.PDF for .NET supports the feature to search and get the coordinates of each character or text fragments. So in order to be certain about the coordinates being returned for each character, we may consider highlighting (adding rectangle) around each character. The following code snippet gets coordinates of each character and creates a rectangle around each character.

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

## Add and Search Hidden Text

Sometimes we want to add hidden text in a PDF document and then search hidden text and use its position for post-processing. For your convenience, Aspose.PDF for .NET provides these abilities. You can add hidden text during document generation. Also, you can find hidden text using TextFragmentAbsorber. To add hidden text ,set TextState.Invisible to ‘true’ for the added text. TextFragmentAbsorber finds all text that matches the pattern (if specified). It is the default behavior that can’t be changed. In order to verify if the found text is actually invisible, the TextState.Invisible property can be used. The code snippet below shows how to use this feature.

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

## Searching Text With .NET Regex

Aspose.PDF for .NET provides the ability to search documents using the standard .NET Regex option. The TextFragmentAbsorber can be used for this purpose as shown in the code sample below.

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

## Searching bold text 

Aspose.PDF for .NET allows users to search documents using font style properties. The TextFragmentAbsorber can be used for this purpose, as shown in the code sample below.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractBoldText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractBoldText.pdf"))
    {
        // Create TextFragmentAbsorber object to extract text
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

        // Accept the absorber for all document
        textFragmentAbsorber.Visit(document);

        // Loop through the fragments
        foreach (var textFragment in textFragmentAbsorber.TextFragments)
        {
            // Get the text properties of the text fragment
            var textState = textFragment.TextState;
            // Check if text is bold
            if (textState.FontStyle == FontStyles.Bold)
            {
                // Print the text from the text fragment
                Console.WriteLine("Text :- " + textFragment.Text);
            }
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
