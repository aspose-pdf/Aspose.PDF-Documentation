---
title: Text Formatting inside PDF
type: docs
weight: 30
url: /net/text-formatting-inside-pdf/
---

## Add Line Indent

Aspose.PDF for .NET offers SubsequentLinesIndent property into TextFormattingOptions class. Which can be used to specify line indent in PDF generation scenarios with TextFragment and Paragraphs collection.

Please use the following code snippet to use the property:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Create new document object
Aspose.Pdf.Document document = new Aspose.Pdf.Document();
Aspose.Pdf.Page page = document.Pages.Add();

Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment("A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog.");

// Initilize TextFormattingOptions for the text fragment and specify SubsequentLinesIndent value
text.TextState.FormattingOptions = new Aspose.Pdf.Text.TextFormattingOptions()
{
    SubsequentLinesIndent = 20
};

page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line2");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line3");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line4");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line5");
page.Paragraphs.Add(text);

document.Save(dataDir + "SubsequentIndent_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
```

## Add Text Border

The following code snippet shows, how to add a border to a text using TextBuilder and setting DrawTextRectangleBorder property of TextState:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Create new document object
Document pdfDocument = new Document();
// Get particular page
Page pdfPage = (Page)pdfDocument.Pages.Add();
// Create text fragment
TextFragment textFragment = new TextFragment("main text");
textFragment.Position = new Position(100, 600);
// Set text properties
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// Set StrokingColor property for drawing border (stroking) around text rectangle
textFragment.TextState.StrokingColor = Aspose.Pdf.Color.DarkRed;
// Set DrawTextRectangleBorder property value to true
textFragment.TextState.DrawTextRectangleBorder = true;
TextBuilder tb = new TextBuilder(pdfPage);
tb.AppendText(textFragment);
// Save the document
pdfDocument.Save(dataDir + "PDFWithTextBorder_out.pdf");
```

## Add Underline Text

The following code snippet shows you how to add Underline text while creating a new PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Create documentation object
Document pdfDocument = new Document();
// Add age page to PDF document
pdfDocument.Pages.Add();
// Create TextBuilder for first page
TextBuilder tb = new TextBuilder(pdfDocument.Pages[1]);
// TextFragment with sample text
TextFragment fragment = new TextFragment("Test message");
// Set the font for TextFragment
fragment.TextState.Font = FontRepository.FindFont("Arial");
fragment.TextState.FontSize = 10;
// Set the formatting of text as Underline
fragment.TextState.Underline = true;
// Specify the position where TextFragment needs to be placed
fragment.Position = new Position(10, 800);
// Append TextFragment to PDF file
tb.AppendText(fragment);

dataDir = dataDir + "AddUnderlineText_out.pdf";

// Save resulting PDF document.
pdfDocument.Save(dataDir);
```

## Adding a Border Around Added Text

You have control over the look and feel of the text you add. The example below shows how to add a border around a piece of text that you have added by drawing a rectangle around it. Find out more about the [PdfContentEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

PdfContentEditor editor = new PdfContentEditor();
editor.BindPdf(dataDir + "input.pdf");
LineInfo lineInfo = new LineInfo();
lineInfo.LineWidth = 2;
lineInfo.VerticeCoordinate = new float[] { 0, 0, 100, 100, 50, 100 };
lineInfo.Visibility = true;
editor.CreatePolygon(lineInfo, 1, new System.Drawing.Rectangle(0, 0, 0, 0), "");

dataDir = dataDir + "AddingBorderAroundAddedText_out.pdf";

// Save resulting PDF document.
editor.Save(dataDir);
```

## Adding NewLine feed

TextFragment doesn’t support line feed inside the text. However in order to add text with line feed, please use TextFragment with TextParagraph:

- use “\r\n” or Environment.NewLine in TextFragment instead of single “\n”;
- create TextParagraph object. It will add text with line splitting;
- add the TextFragment with TextParagraph.AppendLine;
- add the TextParagraph with TextBuilder.AppendParagraph.
Please use below code snippet.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// Initialize new TextFragment with text containing required newline markers
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Applicant Name: " + Environment.NewLine + " Joe Smoe");

// Set text fragment properties if necessary
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// Create TextParagraph object
TextParagraph par = new TextParagraph();

// Add new TextFragment to paragraph
par.AppendLine(textFragment);

// Set paragraph position
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// Create TextBuilder object
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// Add the TextParagraph using TextBuilder
textBuilder.AppendParagraph(par);


dataDir = dataDir + "AddNewLineFeed_out.pdf";

// Save resulting PDF document.
pdfApplicationDoc.Save(dataDir);
```

## Adding StrikeOut Text

The TextState class provides the capabilities to set formatting for TextFragments being placed inside PDF document. You can use this class to set text formatting as Bold, Italic, Underline and starting this release, the API has provided the capabilities to mark text formatting as Strikeout. Please try using the following code snippet to add TextFragment with Strikeout formatting.

Please use complete code snippet:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Open document
Document pdfDocument = new Document();
// Get particular page
Page pdfPage = (Page)pdfDocument.Pages.Add();

// Create text fragment
TextFragment textFragment = new TextFragment("main text");
textFragment.Position = new Position(100, 600);

// Set text properties
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// Set StrikeOut property
textFragment.TextState.StrikeOut = true;
// Mark text as Bold
textFragment.TextState.FontStyle = FontStyles.Bold;

// Create TextBuilder object
TextBuilder textBuilder = new TextBuilder(pdfPage);
// Append the text fragment to the PDF page
textBuilder.AppendText(textFragment);


dataDir = dataDir + "AddStrikeOutText_out.pdf";

// Save resulting PDF document.
pdfDocument.Save(dataDir);
```

## Apply Gradient Shading to the Text

Text formatting has been further enhanced in the API for text editing scenarios and now you can add text with pattern colorspace inside PDF document. Aspose.Pdf.Color Class has further been enhanced by introducing new property of PatternColorSpace, which can be used to specify shading colors for the text. This new property adds different Gradient Shading to the text e.g. Axial Shading, Radial (Type 3) Shading as shown in the following code snippet:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

using (Document pdfDocument = new Document(dataDir + "text_sample4.pdf"))
{
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("Lorem ipsum");
    pdfDocument.Pages.Accept(absorber);

    TextFragment textFragment = absorber.TextFragments[1];

    // Create new color with pattern colorspace
    textFragment.TextState.ForegroundColor = new Aspose.Pdf.Color()
    {
        PatternColorSpace = new Aspose.Pdf.Drawing.GradientAxialShading(Color.Red, Color.Blue)
    };
    textFragment.TextState.Underline = true;

    pdfDocument.Save(dataDir + "text_out.pdf");
}
```

>In order to apply a Radial Gradient, you can set ‘PatternColorSpace’ property equal to ‘Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)’ in the above code snippet.

## Text Alignment for Floating Box Contents

Aspose.PDF supports setting text alignment for contents inside a Floating Box element. The alignment properties of Aspose.Pdf.FloatingBox instance can be used to achieve this as shown in the following code sample.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document doc = new Document();
doc.Pages.Add();

Aspose.Pdf.FloatingBox floatBox = new Aspose.Pdf.FloatingBox(100, 100);
floatBox.VerticalAlignment = VerticalAlignment.Bottom;
floatBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox.Paragraphs.Add(new TextFragment("FloatingBox_bottom"));
floatBox.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox);

Aspose.Pdf.FloatingBox floatBox1 = new Aspose.Pdf.FloatingBox(100, 100);
floatBox1.VerticalAlignment = VerticalAlignment.Center;
floatBox1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox1.Paragraphs.Add(new TextFragment("FloatingBox_center"));
floatBox1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox1);

Aspose.Pdf.FloatingBox floatBox2 = new Aspose.Pdf.FloatingBox(100, 100);
floatBox2.VerticalAlignment = VerticalAlignment.Top;
floatBox2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox2.Paragraphs.Add(new TextFragment("FloatingBox_top"));
floatBox2.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox2);

doc.Save(dataDir + "FloatingBox_alignment_review_out.pdf");
```
