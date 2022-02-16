---
title: Add Text to PDF using C#
linktitle: Add Text to PDF
type: docs
weight: 10
url: /net/add-text-to-pdf-file/
description: This article describes various aspects of working with text in Aspose.PDF. Learn how to add text to PDF, add HTML fragments, or use custom OTF fonts.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/add-text-to-a-pdf-file/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Text to PDF using C#",
    "alternativeHeadline": "Add Text to PDF using C#",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, document generation",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/add-text-to-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-text-to-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "This article describes various aspects of working with text in Aspose.PDF. Learn how to add text to PDF, add HTML fragments, or use custom OTF fonts."
}
</script>

To add text to existing PDF file:

1. Open the input PDF using the Document object.
2. Get the particular page to which you want to add the text.
3. Create a TextFragment object with the input text along with other text properties. The TextBuilder object created from that particular page – to which you want to add the text – allows you to add the TextFragment object to the page using the AppendText method.
4. Call the Document object's Save method and save the output PDF file.

## Adding Text

The following code snippet shows you how to add text in an existing PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Open document
Document pdfDocument = new Document(dataDir + "input.pdf");

// Get particular page
Page pdfPage = (Page)pdfDocument.Pages[1];

// Create text fragment
TextFragment textFragment = new TextFragment("main text");
textFragment.Position = new Position(100, 600);

// Set text properties
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray);
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Red);

// Create TextBuilder object
TextBuilder textBuilder = new TextBuilder(pdfPage);

// Append the text fragment to the PDF page
textBuilder.AppendText(textFragment);

dataDir = dataDir + "AddText_out.pdf";

// Save resulting PDF document.
pdfDocument.Save(dataDir);
```

## Loading Font from Stream

The following code snippet shows how to load Font from Stream object when adding text to PDF document.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
string fontFile = "";

// Load input PDF file
Document doc = new Document( dataDir + "input.pdf");
// Create text builder object for first page of document
TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
// Create text fragment with sample string
TextFragment textFragment = new TextFragment("Hello world");

if (fontFile != "")
{
    // Load the TrueType font into stream object
    using (FileStream fontStream = File.OpenRead(fontFile))
    {
        // Set the font name for text string
        textFragment.TextState.Font = FontRepository.OpenFont(fontStream, FontTypes.TTF);
        // Specify the position for Text Fragment
        textFragment.Position = new Position(10, 10);
        // Add the text to TextBuilder so that it can be placed over the PDF file
        textBuilder.AppendText(textFragment);
    }

    dataDir = dataDir + "LoadingFontFromStream_out.pdf";

    // Save resulting PDF document.
    doc.Save(dataDir);
}
```

## Add Text using TextParagraph

The following code snippet shows you how to add text in PDF document using [TextParagraph](https://apireference.aspose.com/pdf/net/aspose.pdf.text/textparagraph) class.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Open document
Document doc = new Document();
// Add page to pages collection of Document object
Page page = doc.Pages.Add();
TextBuilder builder = new TextBuilder(page);
// Create text paragraph
TextParagraph paragraph = new TextParagraph();
// Set subsequent lines indent
paragraph.SubsequentLinesIndent = 20;
// Specify the location to add TextParagraph
paragraph.Rectangle = new Aspose.Pdf.Rectangle(100, 300, 200, 700);
// Specify word wraping mode
paragraph.FormattingOptions.WrapMode = TextFormattingOptions.WordWrapMode.ByWords;
// Create text fragment
TextFragment fragment1 = new TextFragment("the quick brown fox jumps over the lazy dog");
fragment1.TextState.Font = FontRepository.FindFont("Times New Roman");
fragment1.TextState.FontSize = 12;
// Add fragment to paragraph
paragraph.AppendLine(fragment1);
// Add paragraph
builder.AppendParagraph(paragraph);

dataDir = dataDir + "AddTextUsingTextParagraph_out.pdf";

// Save resulting PDF document.
doc.Save(dataDir);
```

## Add Hyperlink to TextSegment

A PDF page may comprise of one or more TextFragment objects, where each TextFragment object can have one or more TextSegment instance. In order to set hyperlink for TextSegment, Hyperlink property of [TextSegment](https://apireference.aspose.com/pdf/net/aspose.pdf.text/textsegment) class can be used while providing the object of Aspose.Pdf.WebHyperlink instance. Please try using the following code snippet to accomplish this requirement.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Create document instance
Document doc = new Document();
// Add page to pages collection of PDF file
Page page1 = doc.Pages.Add();
// Create TextFragment instance
TextFragment tf = new TextFragment("Sample Text Fragment");
// Set horizontal alignment for TextFragment
tf.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
// Create a textsegment with sample text
TextSegment segment = new TextSegment(" ... Text Segment 1...");
// Add segment to segments collection of TextFragment
tf.Segments.Add(segment);
// Create a new TextSegment
segment = new TextSegment("Link to Google");
// Add segment to segments collection of TextFragment
tf.Segments.Add(segment);
// Set hyperlink for TextSegment
segment.Hyperlink = new Aspose.Pdf.WebHyperlink("www.google.com");
// Set forground color for text segment
segment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
// Set text formatting as italic
segment.TextState.FontStyle = FontStyles.Italic;
// Create another TextSegment object
segment = new TextSegment("TextSegment without hyperlink");
// Add segment to segments collection of TextFragment
tf.Segments.Add(segment);
// Add TextFragment to paragraphs collection of page object
page1.Paragraphs.Add(tf);

dataDir = dataDir + "AddHyperlinkToTextSegment_out.pdf";

// Save resulting PDF document.
doc.Save(dataDir);
```

## Use OTF Font

Aspose.PDF for .NET offers the feature to use Custom/TrueType fonts while creating/manipulating PDF file contents so that file contents are displayed using contents other than default system fonts. Starting release of Aspose.PDF for .NET 10.3.0, we have provided the support for Open Type Fonts.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Create new document instance
Document pdfDocument = new Document();
// Add page to pages collection of PDF file
Aspose.Pdf.Page page = pdfDocument.Pages.Add();
// Create TextFragment instnace with sample text
TextFragment fragment = new TextFragment("Sample Text in OTF font");
// Find font inside system font directory
// Fragment.TextState.Font = FontRepository.FindFont("HelveticaNeueLT Pro 45 Lt");
// Or you can even specify the path of OTF font in system directory
fragment.TextState.Font = FontRepository.OpenFont(dataDir + "space age.otf");
// Specify to emend font inside PDF file, so that its displayed properly,
// Even if specific font is not installed/present over target machine
fragment.TextState.Font.IsEmbedded = true;
// Add TextFragment to paragraphs collection of Page instance
page.Paragraphs.Add(fragment);

dataDir = dataDir + "OTFFont_out.pdf";

// Save resulting PDF document.
pdfDocument.Save(dataDir);
```

## Add HTML String using DOM

The Aspose.Pdf.Generator.Text class contains a property called IsHtmlTagSupported which makes it possible to add HTML tags/contents into PDF files. The added content is rendered in native HTML tags instead of appearing as a simple text string. To support a similar feature in the new Document Object Model (DOM) of the Aspose.Pdf namespace, the HtmlFragment class has been introduced.

The [HtmlFragment](https://apireference.aspose.com/pdf/net/aspose.pdf/htmlfragment) instance can be used to specify the HTML contents which should be placed inside the PDF file. Similar to TextFragment, HtmlFragment is a paragraph level object and can be added to the Page object's paragraphs collection. The following code snippets show the steps to place HTML contents inside PDF file using the DOM approach.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Instantiate Document object
Document doc = new Document();
// Add a page to pages collection of PDF file
Page page = doc.Pages.Add();
// Instantiate HtmlFragment with HTML contnets
HtmlFragment title = new HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");
// Set bottom margin information
title.Margin.Bottom = 10;
// Set top margin information
title.Margin.Top = 200;
// Add HTML Fragment to paragraphs collection of page
page.Paragraphs.Add(title);

dataDir = dataDir + "AddHTMLUsingDOM_out.pdf";
// Save PDF file
doc.Save(dataDir);
```

Following code snippet demonstrate steps how to add HTML ordered lists into the document:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// The path to the output document. 
string outFile = dataDir + "AddHTMLOrderedListIntoDocuments_out.pdf";
// Instantiate Document object 
Document doc = new Document();
// Instantiate HtmlFragment object with corresponding HTML fragment 
HtmlFragment t = new HtmlFragment("`<body style='line-height: 100px;'><ul><li>First</li><li>Second</li><li>Third</li><li>Fourth</li><li>Fifth</li></ul>Text after the list.<br/>Next line<br/>Last line</body>`");
// Add Page in Pages Collection 
Page page = doc.Pages.Add();
// Add HtmlFragment inside page 
page.Paragraphs.Add(t);
// Save resultant PDF file 
doc.Save(outFile);
```

You can also set HTML string formatting using TextState object as following:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
HtmlFragment html = new HtmlFragment("some text");
html.TextState = new TextState();
html.TextState.Font = FontRepository.FindFont("Calibri");
```

In case if you set some text attributes values via HTML markup and then provide the same values in TextState properties they will overwrite HTML parameters by properties form TextState instance. The following code snippets show described behavior.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Instantiate Document object
Document doc = new Document();
// Add a page to pages collection of PDF file
Page page = doc.Pages.Add();
// Instantiate HtmlFragment with HTML contnets
HtmlFragment title = new HtmlFragment("<p style='font-family: Verdana'><b><i>Table contains text</i></b></p>");
//Font-family from 'Verdana' will be reset to 'Arial'
title.TextState = new TextState("Arial");
title.TextState.FontSize = 20;
// Set bottom margin information
title.Margin.Bottom = 10;
// Set top margin information
title.Margin.Top = 400;
// Add HTML Fragment to paragraphs collection of page
page.Paragraphs.Add(title);
// Save PDF file
dataDir = dataDir + "AddHTMLUsingDOMAndOverwrite_out.pdf";
// Save PDF file
doc.Save(dataDir);
```

## FootNotes and EndNotes (DOM)

FootNotes indicate notes in the text of your paper by using consecutive superscript numbers. The actual note is indented and can occur as a footnote at the bottom of the page.

### Adding FootNote

In a footnote referencing system, indicate a reference by:

- putting a small number above the line of type directly following the source material. This number is called a note identifier. It sits slightly above the line of text.
- putting the same number, followed by a citation of your source, at the bottom of the page. Footnoting should be numerical and chronological: the first reference is 1, the second is 2, and so on.

The advantage of footnoting is that the reader can simply cast their eyes down the page to discover the source of a reference that interests them.

Please follow the steps specified below to create a FootNote:

- Create a Document instance
- Create a Page object
- Create a TextFragment object
- Create a Note instance and pass it's value to TextFragment.FootNote property
- Add TextFragment to paragraphs collection of a page instance

### Custom line style for FootNote

The following example demonstrates how to add Footnotes to the bottom of the Pdf page and define a custom line style.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Create Document instance
Document doc = new Document();
// Add page to pages collection of PDF
Page page = doc.Pages.Add();
// Create GraphInfo object
Aspose.Pdf.GraphInfo graph = new Aspose.Pdf.GraphInfo();
// Set line width as 2
graph.LineWidth = 2;
// Set the color for graph object
graph.Color = Aspose.Pdf.Color.Red;
// Set dash array value as 3
graph.DashArray = new int[] { 3 };
// Set dash phase value as 1
graph.DashPhase = 1;
// Set footnote line style for page as graph
page.NoteLineStyle = graph;
// Create TextFragment instance
TextFragment text = new TextFragment("Hello World");
// Set FootNote value for TextFragment
text.FootNote = new Note("foot note for test text 1");
// Add TextFragment to paragraphs collection of first page of document
page.Paragraphs.Add(text);
// Create second TextFragment
text = new TextFragment("Aspose.Pdf for .NET");
// Set FootNote for second text fragment
text.FootNote = new Note("foot note for test text 2");
// Add second text fragment to paragraphs collection of PDF file
page.Paragraphs.Add(text);

dataDir = dataDir + "CustomLineStyleForFootNote_out.pdf";

// Save resulting PDF document.
doc.Save(dataDir);
```

We can set Footnote Label (note identifier) formatting using TextState object as following:

```csharp
TextFragment text = new TextFragment("test text 1");
text.FootNote = new Note("foot note for test text 1");
text.FootNote.Text = "21";
text.FootNote.TextState = new TextState();
text.FootNote.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
text.FootNote.TextState.FontStyle = FontStyles.Italic;
```

### Customize Footnote label

By default, the FootNote number is incremental starting from 1. However, we may have a requirement to set a custom FootNote label. In order to accomplish this requirement, please try using the following code snippet

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Create Document instance
Document doc = new Document();
// Add page to pages collection of PDF
Page page = doc.Pages.Add();
// Create GraphInfo object
Aspose.Pdf.GraphInfo graph = new Aspose.Pdf.GraphInfo();
// Set line width as 2
graph.LineWidth = 2;
// Set the color for graph object
graph.Color = Aspose.Pdf.Color.Red;
// Set dash array value as 3
graph.DashArray = new int[] { 3 };
// Set dash phase value as 1
graph.DashPhase = 1;
// Set footnote line style for page as graph
page.NoteLineStyle = graph;
// Create TextFragment instance
TextFragment text = new TextFragment("Hello World");
// Set FootNote value for TextFragment
text.FootNote = new Note("foot note for test text 1");
// Specify custom label for FootNote
text.FootNote.Text = " Aspose(2015)";
// Add TextFragment to paragraphs collection of first page of document
page.Paragraphs.Add(text);

dataDir = dataDir + "CustomizeFootNoteLabel_out.pdf";
```

## Adding Image and Table to Footnote

In earlier release versions, the Footnote support was provided but it was only applicable to TextFragment object. However starting release Aspose.PDF for .NET 10.7.0, you can also add Footnote to other objects inside PDF document such as Table, Cells etc. The following code snippet shows the steps to add Footnote to TextFragment object and then add Image and Table object to paragraphs collection of Footnote section.

```csharp

// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();
TextFragment text = new TextFragment("some text");
page.Paragraphs.Add(text);

text.FootNote = new Note();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = dataDir + "aspose-logo.jpg";
image.FixHeight = 20;
text.FootNote.Paragraphs.Add(image);
TextFragment footNote = new TextFragment("footnote text");
footNote.TextState.FontSize = 20;
footNote.IsInLineParagraph = true;
text.FootNote.Paragraphs.Add(footNote);
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.Rows.Add().Cells.Add().Paragraphs.Add(new TextFragment("Row 1 Cell 1"));
text.FootNote.Paragraphs.Add(table);

dataDir = dataDir + "AddImageAndTable_out.pdf";

// Save resulting PDF document.
doc.Save(dataDir);
```

## How to Create EndNotes

An EndNote is a source citation that refers the readers to a specific place at the end of the paper where they can find out the source of the information or words quoted or mentioned in the paper. When using endnotes, your quoted or paraphrased sentence or summarized material is followed by a superscript number.

The following example demonstrates how to add an Endnote in the Pdf page.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Create Document instance
Document doc = new Document();
// Add page to pages collection of PDF
Page page = doc.Pages.Add();
// Create TextFragment instance
TextFragment text = new TextFragment("Hello World");
// Set FootNote value for TextFragment
text.EndNote = new Note("sample End note");
// Specify custom label for FootNote
text.EndNote.Text = " Aspose(2015)";
// Add TextFragment to paragraphs collection of first page of document
page.Paragraphs.Add(text);

dataDir = dataDir + "CreateEndNotes_out.pdf";
// Save resulting PDF document.
doc.Save(dataDir);
```

## Text and Image as InLine Paragraph

The default layout of the PDF file is flow layout (Top-Left to Bottom-Right). Therefore every new element being added to PDF file is added in the bottom right flow. However, we may have a requirement to display various page elements i.e. Image and Text at the same level (one after another). One approach can be to create a Table instance and add both elements to individual cell objects. However, another approach can be InLine paragraph. By setting IsInLineParagraph property of Image and Text as true, these paragraphs will appear as inline to other page elements.

The following code snippet shows you how to add text and Image as InLine paragraphs in PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Instantiate Document instance
Document doc = new Document();
// Add page to pages collection of Document instance
Page page = doc.Pages.Add();
// Create TextFragmnet
TextFragment text = new TextFragment("Hello World.. ");
// Add text fragment to paragraphs collection of Page object
page.Paragraphs.Add(text);
// Create an image instance
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
// Set image as inline paragraph so that it appears right after
// The previous paragraph object (TextFragment)
image.IsInLineParagraph = true;
// Specify image file path
image.File = dataDir + "aspose-logo.jpg";
// Set image Height (optional)
image.FixHeight = 30;
// Set Image Width (optional)
image.FixWidth = 100;
// Add image to paragraphs collection of page object
page.Paragraphs.Add(image);
// Re-initialize TextFragment object with different contents
text = new TextFragment(" Hello Again..");
// Set TextFragment as inline paragraph
text.IsInLineParagraph = true;
// Add newly created TextFragment to paragraphs collection of page
page.Paragraphs.Add(text);

dataDir = dataDir + "TextAndImageAsParagraph_out.pdf";
doc.Save(dataDir);
```

## Specify character Spacing when adding Text

A text can be added inside paragraphs collection of PDF files using TextFragment instance or by using TextParagraph object and even you can stamp the text inside PDF by using TextStamp class. While adding the text, we may have a requirement to specify character spacing for the text objects. In order to accomplish this requirement, a new property named CharacterSpacing property has been introduced. Please take a look at the following approaches to fulfill this requirement.

The following approaches show the steps to specify character spacing when adding text inside a PDF document.

### Using TextBuilder and TextFragment

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Create Document instance
Document pdfDocument = new Document();
// Add page to pages collection of Document
Page page = pdfDocument.Pages.Add();
// Create TextBuilder instance
TextBuilder builder = new TextBuilder(pdfDocument.Pages[1]);
// Create text fragment instance with sample contents
TextFragment wideFragment = new TextFragment("Text with increased character spacing");
wideFragment.TextState.ApplyChangesFrom(new TextState("Arial", 12));
// Specify character spacing for TextFragment
wideFragment.TextState.CharacterSpacing = 2.0f;
// Specify the position of TextFragment
wideFragment.Position = new Position(100, 650);
// Append TextFragment to TextBuilder instance
builder.AppendText(wideFragment);
dataDir = dataDir + "CharacterSpacingUsingTextBuilderAndFragment_out.pdf";
// Save resulting PDF document.
pdfDocument.Save(dataDir);
```

### Using TextParagraph

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Create Document instance
Document pdfDocument = new Document();
// Add page to pages collection of Document
Page page = pdfDocument.Pages.Add();
// Create TextBuilder instance
TextBuilder builder = new TextBuilder(pdfDocument.Pages[1]);
// Instantiate TextParagraph instance
TextParagraph paragraph = new TextParagraph();
// Create TextState instance to specify font name and size
TextState state = new TextState("Arial", 12);
// Specify the character spacing
state.CharacterSpacing = 1.5f;
// Append text to TextParagraph object
paragraph.AppendLine("This is paragraph with character spacing", state);
// Specify the position for TextParagraph
paragraph.Position = new Position(100, 550);
// Append TextParagraph to TextBuilder instance
builder.AppendParagraph(paragraph);

dataDir = dataDir + "CharacterSpacingUsingTextBuilderAndParagraph_out.pdf";
// Save resulting PDF document.
pdfDocument.Save(dataDir);
```

### Using TextStamp

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Create Document instance
Document pdfDocument = new Document();
// Add page to pages collection of Document
Page page = pdfDocument.Pages.Add();
// Instantiate TextStamp instance with sample text
TextStamp stamp = new TextStamp("This is text stamp with character spacing");
// Specify font name for Stamp object
stamp.TextState.Font = FontRepository.FindFont("Arial");
// Specify Font size for TextStamp
stamp.TextState.FontSize = 12;
// Specify character specing as 1f
stamp.TextState.CharacterSpacing = 1f;
// Set the XIndent for Stamp
stamp.XIndent = 100;
// Set the YIndent for Stamp
stamp.YIndent = 500;
// Add textual stamp to page instance
stamp.Put(page);
dataDir = dataDir + "CharacterSpacingUsingTextStamp_out.pdf";
// Save resulting PDF document.
pdfDocument.Save(dataDir);
```

## Create Multi-Column PDF document

In magazines and newspapers, we mostly see that news are displayed in multiple columns on the single pages instead of the books where text paragraphs are mostly printed on the whole pages from left to right position. Many document processing applications like Microsoft Word and Adobe Acrobat Writer allow users to create multiple columns on a single page and then add data to them.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) also offers the feature to create multiple columns inside the pages of PDF documents. In order to create multi-column PDF file, we can make use of Aspose.Pdf.FloatingBox class as it provides ColumnInfo.ColumnCount property to specify the number of columns inside FloatingBox and we can also specify the spacing between columns and columns widths using ColumnInfo.ColumnSpacing and ColumnInfo.ColumnWidths properties accordingly. Please note that FloatingBox is an element inside Document Object Model and it can have obsolete positioning as compared to relative positioning (i.e. Text, Graph, Image, etc).

Column spacing means the space between the columns and the default spacing between the columns is 1.25cm. If the column width is not specified, then [Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) calculates width for each column automatically according to the page size and column spacing.

An example is given below to demonstrate the creation of two columns with Graphs objects (Line) and they are added to paragraphs collection of FloatingBox, which is then added paragraphs collection of Page instance.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
// Specify the left margin info for the PDF file
doc.PageInfo.Margin.Left = 40;
// Specify the Right margin info for the PDF file
doc.PageInfo.Margin.Right = 40;
Page page = doc.Pages.Add();

Aspose.Pdf.Drawing.Graph graph1 = new Aspose.Pdf.Drawing.Graph(500, 2);
// Add the line to paraphraphs collection of section object
page.Paragraphs.Add(graph1);

// Specify the coordinates for the line
float[] posArr = new float[] { 1, 2, 500, 2 };
Aspose.Pdf.Drawing.Line l1 = new Aspose.Pdf.Drawing.Line(posArr);
graph1.Shapes.Add(l1);
// Create string variables with text containing html tags

string s = "<font face=\"Times New Roman\" size=4>" +

"<strong> How to Steer Clear of money scams</<strong> "
+ "</font>";
// Create text paragraphs containing HTML text

HtmlFragment heading_text = new HtmlFragment(s);
page.Paragraphs.Add(heading_text);

Aspose.Pdf.FloatingBox box = new Aspose.Pdf.FloatingBox();
// Add four columns in the section
box.ColumnInfo.ColumnCount = 2;
// Set the spacing between the columns
box.ColumnInfo.ColumnSpacing = "5";

box.ColumnInfo.ColumnWidths = "105 105";
TextFragment text1 = new TextFragment("By A Googler (The Official Google Blog)");
text1.TextState.FontSize = 8;
text1.TextState.LineSpacing = 2;
box.Paragraphs.Add(text1);
text1.TextState.FontSize = 10;

text1.TextState.FontStyle = FontStyles.Italic;
// Create a graphs object to draw a line
Aspose.Pdf.Drawing.Graph graph2 = new Aspose.Pdf.Drawing.Graph(50, 10);
// Specify the coordinates for the line
float[] posArr2 = new float[] { 1, 10, 100, 10 };
Aspose.Pdf.Drawing.Line l2 = new Aspose.Pdf.Drawing.Line(posArr2);
graph2.Shapes.Add(l2);

// Add the line to paragraphs collection of section object
box.Paragraphs.Add(graph2);

TextFragment text2 = new TextFragment(@"Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue. Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.");
box.Paragraphs.Add(text2);

page.Paragraphs.Add(box);

dataDir = dataDir + "CreateMultiColumnPdf_out.pdf";
// Save PDF file
doc.Save(dataDir);
```

## Working with custom Tab Stops

A Tab Stop is a stop point for tabbing. In word processing, each line contains a number of tab stops placed at regular intervals (for example, every half inch). They can be changed, however, as most word processors allow you to set tab stops wherever you want. When you press the Tab key, the cursor or insertion point jumps to the next tab stop, which itself is invisible. Although tab stops do not exist in the text file, the word processor keeps track of them so that it can react correctly to the Tab key.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) allows developers to use custom tab stops in PDF documents. The Aspose.Pdf.Text.TabStop class is used to set custom TAB stops in the [TextFragment](https://apireference.aspose.com/pdf/net/aspose.pdf.text/textfragment) class.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/)  also offers some pre-defined tab leader types as an enumeration named, TabLeaderType whose pre-defined values and their descriptions are given below:

|**Tab Leader Type**|**Description**|
| :- | :- |
|None|No tab leader|
|Solid|Solid tab leader|
|Dash|Dash tab leader|
|Dot|Dot tab leader|

Here is an example of how to set custom TAB stops.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document _pdfdocument = new Document();
Page page = _pdfdocument.Pages.Add();

Aspose.Pdf.Text.TabStops ts = new Aspose.Pdf.Text.TabStops();
Aspose.Pdf.Text.TabStop ts1 = ts.Add(100);
ts1.AlignmentType = TabAlignmentType.Right;
ts1.LeaderType = TabLeaderType.Solid;
Aspose.Pdf.Text.TabStop ts2 = ts.Add(200);
ts2.AlignmentType = TabAlignmentType.Center;
ts2.LeaderType = TabLeaderType.Dash;
Aspose.Pdf.Text.TabStop ts3 = ts.Add(300);
ts3.AlignmentType = TabAlignmentType.Left;
ts3.LeaderType = TabLeaderType.Dot;

TextFragment header = new TextFragment("This is a example of forming table with TAB stops", ts);
TextFragment text0 = new TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts);

TextFragment text1 = new TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts);
TextFragment text2 = new TextFragment("#$TABdata21 ", ts);
text2.Segments.Add(new TextSegment("#$TAB"));
text2.Segments.Add(new TextSegment("data22 "));
text2.Segments.Add(new TextSegment("#$TAB"));
text2.Segments.Add(new TextSegment("data23"));

page.Paragraphs.Add(header);
page.Paragraphs.Add(text0);
page.Paragraphs.Add(text1);
page.Paragraphs.Add(text2);

dataDir = dataDir + "CustomTabStops_out.pdf";
_pdfdocument.Save(dataDir);
```

## How to Add Transparent Text in PDF

A PDF file contains Image, Text, Graph, attachment, Annotations objects and while creating TextFragment, you can set foreground, background-color information as well as text formatting. Aspose.PDF for .NET supports the feature to add text with Alpha color channel. The following code snippet shows how to add text with transparent color.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Create Document instance
Document doc = new Document();
// Create page to pages collection of PDF file
Aspose.Pdf.Page page = doc.Pages.Add();

// Create Graph object
Aspose.Pdf.Drawing.Graph canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
// Create rectangle instance with certain dimensions
Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 400, 400);
// Create color object from Alpha color channel
rect.GraphInfo.FillColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.FromArgb(128, System.Drawing.Color.FromArgb(12957183)));
// Add rectanlge to shapes collection of Graph object
canvas.Shapes.Add(rect);
// Add graph object to paragraphs collection of page object
page.Paragraphs.Add(canvas);
// Set value to not change position for graph object
canvas.IsChangePosition = false;

// Create TextFragment instance with sample value
TextFragment text = new TextFragment("transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text ");
// Create color object from Alpha channel
Aspose.Pdf.Color color = Aspose.Pdf.Color.FromArgb(30, 0, 255, 0);
// Set color information for text instance
text.TextState.ForegroundColor = color;
// Add text to paragraphs collection of page instance
page.Paragraphs.Add(text);

dataDir = dataDir + "AddTransparentText_out.pdf";
doc.Save(dataDir);
```

## Specify LineSpacing for Fonts

Every font has an abstract square, whose height is the intended distance between lines of type in the same type size. This square is called the em square and it is the design grid on which the glyph outlines are defined. Many letters of input font have points that are placed out of font's em square bounds, so in order to display the font correctly, usage of special setting is needed. The object TextFragment has a set of text formatting options which are accessible via properties TextState.FormattingOptions. Last property of this path is property of type Aspose.Pdf.Text.TextFormattingOptions. This class has a an enumeration [LineSpacingMode](https://apireference.aspose.com/pdf/net/aspose.pdf.text.textformattingoptions/linespacingmode) which is designed for specific fonts e.g input font "HPSimplified.ttf". Also class [Aspose.Pdf.Text.TextFormattingOptions](https://apireference.aspose.com/pdf/net/aspose.pdf.text/textformattingoptions) has a property [LineSpacing](https://apireference.aspose.com/pdf/net/aspose.pdf.text/textformattingoptions/properties/linespacing) of type LineSpacingMode. You just need to set LineSpacing into LineSpacingMode.FullSize. The code snippet to get a font displayed correctly, would be like as follows:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string fontFile = dataDir + "HPSimplified.TTF";
// Load input PDF file
Document doc = new Document();
//Create TextFormattingOptions with LineSpacingMode.FullSize
TextFormattingOptions formattingOptions = new TextFormattingOptions();
formattingOptions.LineSpacing = TextFormattingOptions.LineSpacingMode.FullSize;

// Create text builder object for first page of document
//TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
// Create text fragment with sample string
TextFragment textFragment = new TextFragment("Hello world");

if (fontFile != "")
{
    // Load the TrueType font into stream object
    using (FileStream fontStream = System.IO.File.OpenRead(fontFile))
    {
        // Set the font name for text string
        textFragment.TextState.Font = FontRepository.OpenFont(fontStream, FontTypes.TTF);
        // Specify the position for Text Fragment
        textFragment.Position = new Position(100, 600);
        //Set TextFormattingOptions of current fragment to predefined(which points to LineSpacingMode.FullSize)
        textFragment.TextState.FormattingOptions = formattingOptions;
        // Add the text to TextBuilder so that it can be placed over the PDF file
        //textBuilder.AppendText(textFragment);
        var page = doc.Pages.Add();
        page.Paragraphs.Add(textFragment);
    }

    dataDir = dataDir + "SpecifyLineSpacing_out.pdf";
    // Save resulting PDF document
    doc.Save(dataDir);
}
```

## Get Text Width Dynamically

Sometimes, it is required to get the text width dynamically. Aspose.PDF for .NET includes two methods for string width measurement. You can invoke the [MeasureString](https://apireference.aspose.com/pdf/net/aspose.pdf.text/font/methods/measurestring) method of Aspose.Pdf.Text.Font or Aspose.Pdf.Text.TextState classes (or both). The code snippet below shows how to use this functionality.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Text.Font font = FontRepository.FindFont("Arial");
TextState ts = new TextState();
ts.Font = font;
ts.FontSize = 14;

if (Math.Abs(font.MeasureString("A", 14) - 9.337) > 0.001)
    Console.WriteLine("Unexpected font string measure!");

if (Math.Abs(ts.MeasureString("z") - 7.0) > 0.001)
    Console.WriteLine("Unexpected font string measure!");

for (char c = 'A'; c <= 'z'; c++)
{
    double fnMeasure = font.MeasureString(c.ToString(), 14);
    double tsMeasure = ts.MeasureString(c.ToString());

    if (Math.Abs(fnMeasure - tsMeasure) > 0.001)
        Console.WriteLine("Font and state string measuring doesn't match!");
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
