---
title: Search Text in PDF | C#
linktitle: Search and Get Text
type: docs
weight: 60
url: /net/search-and-get-text-from-pdf/
description: This article explains how to use various tools to search and get a text from PDF docs. We can search with regular expression from particular or whole pages.
lastmod: "2021-02-26"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Search and Get Text from All the Pages of PDF Document

[TextFragmentAbsorber](https://apireference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber) class allows you to find text, matching a particular phrase, from all the pages of a PDF document. In order to search text from the whole document, you need to call the Accept method of Pages collection. The [Accept](https://apireference.aspose.com/pdf/net/aspose.pdf.page/accept/methods/3) method takes TextFragmentAbsorber object as a parameter, which returns a collection of TextFragment objects. You can loop through all the fragments and get their properties like Text, Position (XIndent, YIndent), FontName, FontSize, IsAccessible, IsEmbedded, IsSubset, ForegroundColor, etc.

The following code snippet shows you how to search for text from all the pages.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Open document
Document pdfDocument = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// Create TextAbsorber object to find all instances of the input search phrase
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("text");

// Accept the absorber for all the pages
pdfDocument.Pages.Accept(textFragmentAbsorber);

// Get the extracted text fragments
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Loop through the fragments
foreach (TextFragment textFragment in textFragmentCollection)
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
```

In case you need to search text inside any particular PDF page, please specify the page number from pages collection of Document instance and call Accept method against that page (as shown in code line below).

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Accept the absorber for a particular page
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## Search and Get Text Segments from All Pages of PDF Document

In order to search text segments from all the pages, you first need to get the TextFragment objects from the document. TextFragmentAbsorber allows you to find text, matching a particular phrase, from all the pages of a PDF document. In order to search text from the whole document, you need to call the Accept method of Pages collection. The Accept method takes TextFragmentAbsorber object as a parameter, which returns a collection of TextFragment objects. Once the TextFragmentCollection is fetched from the document, you need to loop through this collection and get TextSegmentCollection of each TextFragment object. After that, you can get all the properties of the individual TextSegment object. The following code snippet shows you how to search text segments from all the pages.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Open document
Document pdfDocument = new Document(dataDir + "SearchAndGetTextPage.pdf");

// Create TextAbsorber object to find all instances of the input search phrase
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Figure");
// Accept the absorber for all the pages
pdfDocument.Pages.Accept(textFragmentAbsorber);
// Get the extracted text fragments
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// Loop through the fragments
foreach (TextFragment textFragment in textFragmentCollection)
{
    foreach (TextSegment textSegment in textFragment.Segments)
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
```

In order to search and get TextSegments from a particular page of PDF, you need to specify the particular page index when calling Accept(..) method. Please take a look at the following code lines.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Accept the absorber for all the pages
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## Search and Get Text from all pages using Regular Expression

TextFragmentAbsorber helps you search and retrieve text, from all the pages, based on a regular expression. First, you need to pass a regular expression to TextFragmentAbsorber constructor as the phrase. After that, you have to set the TextSearchOptions property of the TextFragmentAbsorber object. This property requires TextSearchOptions object and you need to pass true as a parameter to its constructor while creating new objects. As you want to retrieve matching text from all the pages, you need to call Accept method of Pages collection. TextFragmentAbsorber returns a TextFragmentCollection containing all the fragments matching the criteria specified by the regular expression. The following code snippet shows you how to search and get text from all the pages based on a regular expression.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Open document
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionAll.pdf");

// Create TextAbsorber object to find all the phrases matching the regular expression
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // Like 1999-2000

// Set text search option to specify regular expression usage
TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// Accept the absorber for all the pages
pdfDocument.Pages.Accept(textFragmentAbsorber);

// Get the extracted text fragments
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Loop through the fragments
foreach (TextFragment textFragment in textFragmentCollection)
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
```

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
TextFragmentAbsorber textFragmentAbsorber;
// In order to search exact match of a word, you may consider using regular expression.
textFragmentAbsorber = new TextFragmentAbsorber(@"\bWord\b", new TextSearchOptions(true));

// In order to search a string in either upper case or lowercase, you may consider using regular expression.
textFragmentAbsorber = new TextFragmentAbsorber("(?i)Line", new TextSearchOptions(true));

// In order to search all the strings (parse all strings) inside PDF document, please try using following regular expression.
textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");

// Find match of search string and get anything after the string till line break.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?i)the ((.)*)");

// Please use following regular expression to find text following to the regex match.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?<=word).*");

// In order to search Hyperlink/URL's inside PDF document, please try using following regular expression.
textFragmentAbsorber = new TextFragmentAbsorber(@"(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?");
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
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Create absorber object to find all instances of the input search phrase
TextFragmentAbsorber absorber = new TextFragmentAbsorber("\\d{4}-\\d{4}");
// Enable regular expression search
absorber.TextSearchOptions = new TextSearchOptions(true);
// Open document
PdfContentEditor editor = new PdfContentEditor();
// Bind source PDF file
editor.BindPdf(dataDir + "SearchRegularExpressionPage.pdf");
// Accept the absorber for the page
editor.Document.Pages[1].Accept(absorber);

int[] dashArray = { };
String[] LEArray = { };
System.Drawing.Color blue = System.Drawing.Color.Blue;

// Loop through the fragments
foreach (TextFragment textFragment in absorber.TextFragments)
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

dataDir = dataDir + "SearchTextAndAddHyperlink_out.pdf";
editor.Save(dataDir);
editor.Close();
```

## Search and Draw Rectangle around each TextFragment

Aspose.PDF for .NET supports the feature to search and get the coordinates of each character or text fragments. So in order to be certain about the coordinates being returned for each character, we may consider highlighting (adding rectangle) around each character.

In case of a text paragraph, you may consider using some regular expression to determine the paragraph break and draw a rectangle around it. Please take a look at the following code snippet. The following code snippet gets coordinates of each character and creates a rectangle around each character.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Open document
Document document = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// Create TextAbsorber object to find all the phrases matching the regular expression

TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber(@"[\S]+");

TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textAbsorber.TextSearchOptions = textSearchOptions;

document.Pages.Accept(textAbsorber);

var editor = new PdfContentEditor(document);

foreach (TextFragment textFragment in textAbsorber.TextFragments)
{
    foreach (TextSegment textSegment in textFragment.Segments)
    {
        DrawBox(editor, textFragment.Page.Number, textSegment, System.Drawing.Color.Red);
    }

}
dataDir = dataDir + "SearchTextAndDrawRectangle_out.pdf";
document.Save(dataDir);
```

## Highlight each character in PDF document

{{% alert color="primary" %}}

You can try searching for text in a document using Aspose.PDF and get the results online at this [link](https://products.aspose.app/pdf/search)

{{% /alert %}}

Aspose.PDF for .NET supports the feature to search and get the coordinates of each character or text fragments. So in order to be certain about the coordinates being returned for each character, we may consider highlighting (adding rectangle) around each character. The following code snippet gets coordinates of each character and creates a rectangle around each character.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

int resolution = 150;

Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "input.pdf");

using (MemoryStream ms = new MemoryStream())
{
    PdfConverter conv = new PdfConverter(pdfDocument);
    conv.Resolution = new Resolution(resolution, resolution);
    conv.GetNextImage(ms, System.Drawing.Imaging.ImageFormat.Png);

    Bitmap bmp = (Bitmap)Bitmap.FromStream(ms);

    using (System.Drawing.Graphics gr = System.Drawing.Graphics.FromImage(bmp))
    {
        float scale = resolution / 72f;
        gr.Transform = new System.Drawing.Drawing2D.Matrix(scale, 0, 0, -scale, 0, bmp.Height);

        for (int i = 0; i < pdfDocument.Pages.Count; i++)
        {
Page page = pdfDocument.Pages[1];
// Create TextAbsorber object to find all words
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;
page.Accept(textFragmentAbsorber);
// Get the extracted text fragments
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// Loop through the fragments
foreach (TextFragment textFragment in textFragmentCollection)
{
    if (i == 0)
    {
        gr.DrawRectangle(
        Pens.Yellow,
        (float)textFragment.Position.XIndent,
        (float)textFragment.Position.YIndent,
        (float)textFragment.Rectangle.Width,
        (float)textFragment.Rectangle.Height);

        for (int segNum = 1; segNum <= textFragment.Segments.Count; segNum++)
        {
TextSegment segment = textFragment.Segments[segNum];

for (int charNum = 1; charNum <= segment.Characters.Count; charNum++)
{
    CharInfo characterInfo = segment.Characters[charNum];

    Aspose.Pdf.Rectangle rect = page.GetPageRect(true);
    Console.WriteLine("TextFragment = " + textFragment.Text + "    Page URY = " + rect.URY +
          "   TextFragment URY = " + textFragment.Rectangle.URY);

    gr.DrawRectangle(
    Pens.Black,
    (float)characterInfo.Rectangle.LLX,
    (float)characterInfo.Rectangle.LLY,
    (float)characterInfo.Rectangle.Width,
    (float)characterInfo.Rectangle.Height);
}

gr.DrawRectangle(
Pens.Green,
(float)segment.Rectangle.LLX,
(float)segment.Rectangle.LLY,
(float)segment.Rectangle.Width,
(float)segment.Rectangle.Height);
        }
    }
}
        }
    }
    dataDir = dataDir + "HighlightCharacterInPDF_out.png";
    bmp.Save(dataDir, System.Drawing.Imaging.ImageFormat.Png);
}
```

## Add and Search Hidden Text

Sometimes we want to add hidden text in a PDF document and then search hidden text and use its position for post-processing. For your convenience, Aspose.PDF for .NET provides these abilities. You can add hidden text during document generation. Also, you can find hidden text using TextFragmentAbsorber. To add hidden text ,set TextState.Invisible to ‘true’ for the added text. TextFragmentAbsorber finds all text that matches the pattern (if specified). It is the default behavior that can’t be changed. In order to verify if the found text is actually invisible, the TextState.Invisible property can be used. The code snippet below shows how to use this feature.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

//Create document with hidden text
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
Page page = doc.Pages.Add();
TextFragment frag1 = new TextFragment("This is common text.");
TextFragment frag2 = new TextFragment("This is invisible text.");

//Set text property - invisible
frag2.TextState.Invisible = true;

page.Paragraphs.Add(frag1);
page.Paragraphs.Add(frag2);
doc.Save(dataDir + "39400_out.pdf");
doc.Dispose();

//Search text in the document
doc = new Aspose.Pdf.Document(dataDir + "39400_out.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber();
absorber.Visit(doc.Pages[1]);

foreach (TextFragment fragment in absorber.TextFragments)
{
    //Do something with fragments
    Console.WriteLine("Text '{0}' on pos {1} invisibility: {2} ",
    fragment.Text, fragment.Position.ToString(), fragment.TextState.Invisible);
}
doc.Dispose();
```

## Searching Text With .NET Regex

Aspose.PDF for .NET provides the ability to search documents using the standard .NET Regex option. The TextFragmentAbsorber can be used for this purpose as shown in the code sample below.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Create Regex object to find all words
System.Text.RegularExpressions.Regex regex = new System.Text.RegularExpressions.Regex(@"[\S]+");

// Open document
Aspose.Pdf.Document document = new Aspose.Pdf.Document(dataDir + "SearchTextRegex.pdf");

// Get a particular page
Page page = document.Pages[1];

// Create TextAbsorber object to find all instances of the input regex
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(regex);
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;

// Accept the absorber for the page
page.Accept(textFragmentAbsorber);

// Get the extracted text fragments
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Loop through the fragments
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine(textFragment.Text);
}
```
