---
title: Add Text to PDF using C++
linktitle: Add Text to PDF 
type: docs
weight: 10
url: /cpp/add-text-to-pdf-file/
description: This article describes various aspects of working with text in Aspose.PDF. Learn how to add text to PDF, add HTML fragments, or use custom OTF fonts.
lastmod: "2021-12-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Adding Text

To add text to existing PDF file:

1. Open the input PDF using the Document object.
2. Get the particular page to which you want to add the text.
3. Create a TextFragment object with the input text along with other text properties. The TextBuilder object created from that particular page – to which you want to add the text – allows you to add the TextFragment object to the page using the AppendText method.
4. Call the Document object's Save method and save the output PDF file.

The following code snippet shows you how to add text in an existing PDF file.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddingText() {
    
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("sample.pdf");
    // String for output file name
    String outputFileName("AddingText_out.pdf");

    // Load the PDF file
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // get particular page
    auto pdfPage = document->get_Pages()->idx_get(1);

    // create text fragment
    auto textFragment = MakeObject<TextFragment>("Aspose.PDF");
    textFragment->set_Position(MakeObject<Position>(80, 700));

    // set text properties
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
    textFragment->get_TextState()->set_FontSize(14);
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());

    // create TextBuilder object
    auto textBuilder = MakeObject<TextBuilder>(pdfPage);
    // append the text fragment to the PDF page
    textBuilder->AppendText(textFragment);

    // Save resulting PDF document.
    document->Save(_dataDir + outputFileName);
}
```

## Loading Font from Stream

The following code snippet shows how to load Font from Stream object when adding text to PDF document.

```cpp
void LoadingFontFromStream() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("sample.pdf");
    String outputFileName("LoadingFontFromStream_out.pdf");

    String fontFile("C:\\Windows\\Fonts\\Arial.ttf");

    // Load input PDF file
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Create text builder object for first page of document
    auto textBuilder = MakeObject<TextBuilder>(document->get_Pages()->idx_get(1));
    // Create text fragment with sample string
    auto textFragment = MakeObject<TextFragment>("Hello world");

    if (!fontFile.IsNullOrEmpty()) {
        // Load the TrueType font into stream object
        auto fontStream = System::IO::File::OpenRead(fontFile);
        // Set the font name for text string
        textFragment->get_TextState()->set_Font(FontRepository::OpenFont(fontStream, FontTypes::TTF));
        // Specify the position for Text Fragment
        textFragment->set_Position(MakeObject<Position>(10, 10));
        // Add the text to TextBuilder so that it can be placed over the PDF file
        textBuilder->AppendText(textFragment);

        // Save resulting PDF document.
        document->Save(_dataDir + outputFileName);
    }
}
```

## Add Text using TextParagraph

The following code snippet shows you how to add text in PDF document using [TextParagraph](https://apireference.aspose.com/pdf/net/aspose.pdf.text/textparagraph) class.

```cpp
void AddTextUsingTextParagraph() {

    String _dataDir("C:\\Samples\\");

    // Open document
    auto document = MakeObject<Document>();

    String outputFileName("AddTextUsingTextParagraph_out.pdf");

    // Add page to pages collection of Document object
    auto page = document->get_Pages()->Add();
    auto builder = MakeObject<TextBuilder>(page);

    // Create text paragraph
    auto paragraph = MakeObject<TextParagraph>();

    // Set subsequent lines indent
    paragraph->set_SubsequentLinesIndent(20);

    // Specify the location to add TextParagraph
    paragraph->set_Rectangle(MakeObject<Rectangle>(100, 300, 200, 700));

    // Specify word wraping mode
    paragraph->get_FormattingOptions()->set_WrapMode(TextFormattingOptions::WordWrapMode::ByWords);

    // Create text fragment
    auto fragment1 = MakeObject<TextFragment>("the quick brown fox jumps over the lazy dog");
    fragment1->get_TextState()->set_Font(FontRepository::FindFont(u"Times New Roman"));
    fragment1->get_TextState()->set_FontSize(12);
    // Add fragment to paragraph
    paragraph->AppendLine(fragment1);
    // Add paragraph
    builder->AppendParagraph(paragraph);

    // Save resulting PDF document.
    document->Save(_dataDir + outputFileName);
}

```

## Add Hyperlink to TextSegment

A PDF page may comprise of one or more TextFragment objects, where each TextFragment object can have one or more TextSegment instance. In order to set hyperlink for TextSegment, Hyperlink property of [TextSegment](https://apireference.aspose.com/pdf/net/aspose.pdf.text/textsegment) class can be used while providing the object of Aspose.Pdf.WebHyperlink instance. Please try using the following code snippet to accomplish this requirement.

```cpp
void AddHyperlinkToTextSegment() {
    
    String _dataDir("C:\\Samples\\");
    String outputFileName("AddHyperlinkToTextSegment_out.pdf");

    // Create document instance
    auto document = MakeObject<Document>();

    // Add page to pages collection of PDF file
    auto page1 = document->get_Pages()->Add();

    // Create TextFragment instance
    auto tf = MakeObject<TextFragment>("Sample Text Fragment");
    // Set horizontal alignment for TextFragment
    tf->set_HorizontalAlignment(HorizontalAlignment::Right);

    // Create a textsegment with sample text
    auto segment = MakeObject<TextSegment>(" ... Text Segment 1...");
    // Add segment to segments collection of TextFragment
    tf->get_Segments()->Add(segment);

    // Create a new TextSegment
    segment = MakeObject<TextSegment>("Link to Google");
    // Add segment to segments collection of TextFragment

    tf->get_Segments()->Add(segment);

    // Set hyperlink for TextSegment
    segment->set_Hyperlink(MakeObject<Aspose::Pdf::WebHyperlink>("www.aspose.com"));

    // Set forground color for text segment
    segment->get_TextState()->set_ForegroundColor(Color::get_Blue());

    // Set text formatting as italic
    segment->get_TextState()->set_FontStyle(FontStyles::Italic);

    // Create another TextSegment object
    segment = MakeObject<TextSegment>(u"TextSegment without hyperlink");

    // Add segment to segments collection of TextFragment
    tf->get_Segments()->Add(segment);

    // Add TextFragment to paragraphs collection of page object
    page1->get_Paragraphs()->Add(tf);

    // Save resulting PDF document.
    document->Save(_dataDir + outputFileName);

}
```

## Use OTF Font

Aspose.PDF for .NET offers the feature to use Custom/TrueType fonts while creating/manipulating PDF file contents so that file contents are displayed using contents other than default system fonts. Starting release of Aspose.PDF for .NET 10.3.0, we have provided the support for Open Type Fonts.

```cpp
void UseOTFFont() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("OTFFont_out.pdf");

    // Create new document instance    
    auto document = MakeObject<Document>();

    // Add page to pages collection of PDF file
    auto page = document->get_Pages()->Add();

    // Create TextFragment instnace with sample text
    auto fragment = MakeObject<TextFragment>("Sample Text in OTF font");

    // Or you can even specify the path of OTF font in system directory
    fragment->get_TextState()->set_Font(FontRepository::OpenFont(u"C:\\Samples\\Fonts\\Montserrat-Black.otf"));
    // Specify to emend font inside PDF file, so that its displayed properly,
    // Even if specific font is not installed/present over target machine
    fragment->get_TextState()->get_Font()->set_IsEmbedded(true);
    // Add TextFragment to paragraphs collection of Page instance
    page->get_Paragraphs()->Add(fragment);
    // Save resulting PDF document.
    document->Save(_dataDir + outputFileName);
}
```

## Add HTML String using DOM

The Aspose.Pdf.Generator.Text class contains a property called IsHtmlTagSupported which makes it possible to add HTML tags/contents into PDF files. The added content is rendered in native HTML tags instead of appearing as a simple text string. To support a similar feature in the new Document Object Model (DOM) of the Aspose.Pdf namespace, the HtmlFragment class has been introduced.

The [HtmlFragment](https://apireference.aspose.com/pdf/net/aspose.pdf/htmlfragment) instance can be used to specify the HTML contents which should be placed inside the PDF file. Similar to TextFragment, HtmlFragment is a paragraph level object and can be added to the Page object's paragraphs collection. The following code snippets show the steps to place HTML contents inside PDF file using the DOM approach.

```cpp
void AddingHtmlString() {
    
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("sample.pdf");

    // String for output file name
    String outputFileName("sample_html_out.pdf");

    // create Document instance
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Add a page to pages collection of PDF file
    auto page = document->get_Pages()->Add();

    // Instantiate HtmlFragment with HTML contents
    auto title = MakeObject<HtmlFragment>("<h1 style=\"color:blue\"><strong>HTML String Demo</strong></h1>");

    // set MarginInfo for margin details
    auto margin = MakeObject<MarginInfo>();
    margin->set_Bottom(10);
    margin->set_Top(200);
    // Set margin information
    title->set_Margin(margin);

    // Add HTML Fragment to paragraphs collection of page
    page->get_Paragraphs()->Add(title);
    // Save PDF file
    document->Save(_dataDir + outputFileName);
}
```

Following code snippet demonstrate steps how to add HTML ordered lists into the document:

```cpp
void AddHTMLOrderedListIntoDocuments() {
    
    String _dataDir("C:\\Samples\\");

    // String for output file name
    String outputFileName("AddHTMLOrderedListIntoDocuments_out.pdf");

    // Instantiate Document object    
    auto document = MakeObject<Document>();

    // Instantiate HtmlFragment object with corresponding HTML fragment
    auto htmlFragment = MakeObject<HtmlFragment>(
        "<div style=\"font-family: sans-serif\"><ul><li>First</li><li>Second</li><li>Third</li><li>Fourth</li><li>Fifth</li></ul><p>Text after the list.</p><p>Next line<br/>Last line</p></div>");
    // Add Page in Pages Collection
    auto page = document->get_Pages()->Add();

    // Add HtmlFragment inside page
    page->get_Paragraphs()->Add(htmlFragment);

    // Save resultant PDF file
    document->Save(_dataDir + outputFileName);
}
```

You can also set HTML string formatting using TextState object as following:

```cpp
void AddHTMLStringFormatting() {
    
    String _dataDir("C:\\Samples\\");

    // String for output file name
    String outputFileName("sample_html_out.pdf");

    // Instantiate Document object    
    auto document = MakeObject<Document>();

    // Add Page in Pages Collection
    auto page = document->get_Pages()->Add();

    // Instantiate HtmlFragment with HTML contents
    auto title = MakeObject<HtmlFragment>("<h1><strong>HTML String Demo</strong></h1>");

    auto textState = MakeObject<TextState>(12);

    textState->set_Font(FontRepository::FindFont(u"Calibri"));
    textState->set_ForegroundColor(Color::get_Green());
    textState->set_BackgroundColor(Color::get_Coral());
    title->set_TextState(textState);

    // Add HTML Fragment to paragraphs collection of page
    page->get_Paragraphs()->Add(title);
    // Save PDF file
    document->Save(_dataDir + outputFileName);
}

```

In case if you set some text attributes values via HTML markup and then provide the same values in TextState properties they will overwrite HTML parameters by properties form TextState instance. The following code snippets show described behavior.

```cpp
void AddHTMLUsingDOMAndOverwrite() {

    String _dataDir("C:\\Samples\\");
    // String for output file name
    String outputFileName("AddHTMLUsingDOMAndOverwrite_out.pdf");

    // Instantiate Document object    
    auto document = MakeObject<Document>();

    // Add Page in Pages Collection
    auto page = document->get_Pages()->Add();

    // Instantiate HtmlFragment with HTML contnets
    auto title = MakeObject<HtmlFragment>("<p style='font-family: Verdana'><b><i>Table contains text</i></b></p>");

    // Font-family from 'Verdana' will be reset to 'Arial'
    title->set_TextState(new TextState(u"Arial Black"));
    title->set_TextState(new TextState(20));

    // Set bottom margin information
    title->get_Margin()->set_Bottom(10);
    // Set top margin information
    title->get_Margin()->set_Top(400);
    // Add HTML Fragment to paragraphs collection of page
    page->get_Paragraphs()->Add(title);
    // Save PDF file
    document->Save(_dataDir + outputFileName);
}
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

```cpp
void AddFootNote() {
    
    String _dataDir("C:\\Samples\\");

    // String for output file name
    String inputFileName("sample.pdf");
    String outputFileName("sample_footnote_out.pdf");

    // Instantiate Document object    
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Add Page in Pages Collection
    auto page = document->get_Pages()->idx_get(1);

    auto tfa = MakeObject<TextFragmentAbsorber>("Portable Document Format");
    tfa->Visit(page);

    auto t = tfa->get_TextFragments()->idx_get(1);
    auto note = MakeObject<Note>();
    note->set_Text(u"Demo");
    t->set_FootNote(note);

    // create TextFragment instance
    auto text = MakeObject<TextFragment>("Hello World");
    // set FootNote value for TextFragment
    text->set_FootNote(MakeObject<Note>("foot note for test text 1"));
    // add TextFragment to paragraphs collection of first page of document
    page->get_Paragraphs()->Add(text);
    // create second TextFragment
    text = MakeObject<TextFragment>("Aspose.Pdf for Java");
    // set FootNote for second text fragment
    text->set_FootNote(MakeObject<Note>("foot note for test text 2"));
    // add second text fragment to paragraphs collection of PDF file
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

### Custom line style for FootNote

The following example demonstrates how to add Footnotes to the bottom of the Pdf page and define a custom line style.

```cpp
void CustomFootNote_Line() {
    
    String _dataDir("C:\\Samples\\");

    // String for output file name    
    String outputFileName("customFootNote_Line.pdf");

    // Create Document instance
    auto document = MakeObject<Document>();

    // add page to pages collection of PDF
    auto page = document->get_Pages()->Add();
    
    // create GraphInfo object
    auto graph = MakeObject<GraphInfo>();
    // set line width as 2
    graph->set_LineWidth(2);
    // set the color for graph object
    graph->set_Color(Color::get_Red());
    // set dash array value as 3
    graph->set_DashArray(MakeArray<int>(3));
    // set dash phase value as 1
    graph->set_DashPhase(1);
    // set footnote line style for page as graph
    page->set_NoteLineStyle(graph);

    // create TextFragment instance
    auto text = MakeObject<TextFragment>("Hello World");
    // set FootNote value for TextFragment
    text->set_FootNote(MakeObject<Note>("foot note for test text 1"));
    // add TextFragment to paragraphs collection of first page of document
    page->get_Paragraphs()->Add(text);
    // create second TextFragment
    text = MakeObject<TextFragment>("Aspose.Pdf for Java");
    // set FootNote for second text fragment
    text->set_FootNote(MakeObject<Note>("foot note for test text 2"));
    // add second text fragment to paragraphs collection of PDF file
    page->get_Paragraphs()->Add(text);
    // save the PDF file
    document->Save(_dataDir + outputFileName);
}
```

We can set Footnote Label (note identifier) formatting using TextState object as following:

```csharp
void AddCustomFootNoteLabel() {
    
    String _dataDir("C:\\Samples\\");

    // String for input file name    
    String inputFileName("sample.pdf");

    // String for output file name    
    String outputFileName("sample_footnote.pdf");

    // Create Document instance
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto page = document->get_Pages()->idx_get(1);

    auto tfa = MakeObject<TextFragmentAbsorber>("Portable Document Format");
    tfa->Visit(page);

    auto t = tfa->get_TextFragments()->idx_get(1);
    auto note = MakeObject<Note>("Demo");
    t->set_FootNote(note);

    // create TextFragment instance
    auto text = MakeObject<TextFragment>("Hello World");
    // set FootNote value for TextFragment
    text->set_FootNote(MakeObject<Note>("foot note for test text 1"));
    text->get_FootNote()->set_Text(u"21");

    auto ts = MakeObject<TextState>();
    ts->set_ForegroundColor(Color::get_Blue());
    ts->set_FontStyle(FontStyles::Italic);
    text->get_FootNote()->set_TextState(ts);

    // add TextFragment to paragraphs collection of first page of document
    page->get_Paragraphs()->Add(text);
    // create second TextFragment
    text = MakeObject<TextFragment>(u"Aspose.Pdf for C++");
    // set FootNote for second text fragment
    text->set_FootNote(MakeObject<Note>("foot note for test text 2"));
    // add second text fragment to paragraphs collection of PDF file
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

### Customize Footnote label

By default, the FootNote number is incremental starting from 1. However, we may have a requirement to set a custom FootNote label. In order to accomplish this requirement, please try using the following code snippet

```cpp
void CustomFootNote_Label() {

    String _dataDir("C:\\Samples\\");
    // String for output file name    
    String outputFileName("CustomizeFootNoteLabel_out.pdf");

    // Create Document instance
    auto document = MakeObject<Document>();

    // Add page to pages collection of PDF
    auto page = document->get_Pages()->Add();

    // Create GraphInfo object
    auto graph = MakeObject<GraphInfo>();

    // Set line width as 2
    graph->set_LineWidth(2);

    // Set the color for graph object
    graph->set_Color(Color::get_Red());

    // Set dash array value as 3
    graph->set_DashArray(MakeArray<int>(3));

    // Set dash phase value as 1
    graph->set_DashPhase(1);

    // Set footnote line style for page as graph
    page->set_NoteLineStyle(graph);

    // Create TextFragment instance
    auto text = MakeObject<TextFragment>("Hello World");
    // Set FootNote value for TextFragment
    text->set_FootNote(MakeObject<Note>("foot note for test text 1"));
    // Specify custom label for FootNote
    text->get_FootNote()->set_Text(u" Aspose(2021)");
    // Add TextFragment to paragraphs collection of first page of document
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## Adding Image and Table to Footnote

In earlier release versions, the Footnote support was provided but it was only applicable to TextFragment object. However starting release Aspose.PDF for .NET 10.7.0, you can also add Footnote to other objects inside PDF document such as Table, Cells etc. The following code snippet shows the steps to add Footnote to TextFragment object and then add Image and Table object to paragraphs collection of Footnote section.

```cpp

void AddingImageAndTableToFootnote() {
    
    String _dataDir("C:\\Samples\\");

    // String for output file name    
    String outputFileName("AddImageAndTableToFootNote_out.pdf");

    // Create Document instance
    auto document = new Document();
    // Add page to pages collection of PDF
    auto page = document->get_Pages()->Add();

    // Create TextFragment instance
    auto text = MakeObject<TextFragment>("Hello World");

    page->get_Paragraphs()->Add(text);

    text->set_FootNote(MakeObject<Note>());
    auto image = MakeObject<Image>();
    image->set_File(_dataDir + u"aspose-logo.jpg");
    image->set_FixHeight(20);

    text->get_FootNote()->get_Paragraphs()->Add(image);

    auto footNote = MakeObject<TextFragment>("footnote text");
    footNote->get_TextState()->set_FontSize(20);
    footNote->set_IsInLineParagraph(true);
    text->get_FootNote()->get_Paragraphs()->Add(footNote);
    
    auto table = MakeObject<Table>();
    table->get_Rows()->Add()->get_Cells()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("Row 1 Cell 1"));
    text->get_FootNote()->get_Paragraphs()->Add(table);

    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## How to Create EndNotes

An EndNote is a source citation that refers the readers to a specific place at the end of the paper where they can find out the source of the information or words quoted or mentioned in the paper. When using endnotes, your quoted or paraphrased sentence or summarized material is followed by a superscript number.

The following example demonstrates how to add an Endnote in the Pdf page.

```cpp
void HowToCreateEndNotes() {
    
    String _dataDir("C:\\Samples\\");

    // String for output file name    
    String outputFileName("endNote_out.pdf");

    // Create Document instance
    auto document = new Document();
    // Add page to pages collection of PDF
    auto page = document->get_Pages()->Add();

    // create TextFragment instance
    auto text = MakeObject<TextFragment>("Hello World");

    // set FootNote value for TextFragment
    text->set_EndNote(MakeObject<Note>("sample End note"));

    // specify custom label for FootNote
    text->get_EndNote()->set_Text(u" Aspose(2021)");
    // add TextFragment to paragraphs collection of first page of document
    page->get_Paragraphs()->Add(text);
    // save the PDF file
    document->Save(_dataDir + outputFileName);
}
```

## Text and Image as InLine Paragraph

The default layout of the PDF file is flow layout (Top-Left to Bottom-Right). Therefore every new element being added to PDF file is added in the bottom right flow. However, we may have a requirement to display various page elements i.e. Image and Text at the same level (one after another). One approach can be to create a Table instance and add both elements to individual cell objects. However, another approach can be InLine paragraph. By setting IsInLineParagraph property of Image and Text as true, these paragraphs will appear as inline to other page elements.

The following code snippet shows you how to add text and Image as InLine paragraphs in PDF file.

```cpp
void TextAndImageAsInLineParagraph() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("TextAndImageAsParagraph_out.pdf");

    // Instantiate Document instance
    auto document = MakeObject<Document>();

    // Add page to pages collection of Document instance
    auto page = document->get_Pages()->Add();

    // Create TextFragmnet
    auto text = MakeObject<TextFragment>("Hello World.. ");
    // Add text fragment to paragraphs collection of Page object
    page->get_Paragraphs()->Add(text);

    // Create an image instance
    auto image = MakeObject<Image>();

    // Set image as inline paragraph so that it appears right after
    // The previous paragraph object (TextFragment)
    image->set_IsInLineParagraph(true);

    // Specify image file path
    image->set_File(_dataDir + u"aspose-logo.jpg");
    // Set image Height (optional)
    image->set_FixHeight(30);
    // Set Image Width (optional)
    image->set_FixWidth(100);
    // Add image to paragraphs collection of page object
    page->get_Paragraphs()->Add(image);
    // Re-initialize TextFragment object with different contents
    text = MakeObject<TextFragment>(" Hello Again..");
    // Set TextFragment as inline paragraph
    text->set_IsInLineParagraph(true);
    // Add newly created TextFragment to paragraphs collection of page
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## Specify character Spacing when adding Text

A text can be added inside paragraphs collection of PDF files using TextFragment instance or by using TextParagraph object and even you can stamp the text inside PDF by using TextStamp class. While adding the text, we may have a requirement to specify character spacing for the text objects. In order to accomplish this requirement, a new property named CharacterSpacing property has been introduced. Please take a look at the following approaches to fulfill this requirement.

The following approaches show the steps to specify character spacing when adding text inside a PDF document.

### Using TextBuilder and TextFragment

```cpp
// Specify Character Spacing when adding Text using TextBuilder and TextFragment
void CharacterSpacing_TextFragment() {
    
    String _dataDir("C:\\Samples\\");

    // String for output file name    
    String outputFileName("CharacterSpacingUsingTextBuilderAndFragment_out.pdf");

    // Create Document instance
    auto document = MakeObject<Document>();
    // Add page to pages collection of Document
    auto page = document->get_Pages()->Add();

    // Create TextBuilder instance
    auto builder = MakeObject<TextBuilder>(page);

    // Create text fragment instance with sample contents
    auto wideFragment = MakeObject<TextFragment>("Text with increased character spacing");
    wideFragment->get_TextState()->ApplyChangesFrom(MakeObject<TextState>("Arial", 12));

    // Specify character spacing for TextFragment
    wideFragment->get_TextState()->set_CharacterSpacing(2.0f);

    // Specify the position of TextFragment
    wideFragment->set_Position(MakeObject<Position>(100, 650));

    // Append TextFragment to TextBuilder instance
    builder->AppendText(wideFragment);

    // Save resulting PDF document.
    document->Save(_dataDir + outputFileName);
}
```

### Using TextParagraph

```cpp
void CharacterSpacing_TextParagraph() {
    
    String _dataDir("C:\\Samples\\");

    // String for output file name    
    String outputFileName("CharacterSpacingUsingTextBuilderAndFragment_out.pdf");

    // Create Document instance
    auto document = MakeObject<Document>();

    // Add page to pages collection of Document
    auto page = document->get_Pages()->Add();

    // Create TextBuilder instance
    auto builder = MakeObject<TextBuilder>(page);

    // Instantiate TextParagraph instance
    auto paragraph = MakeObject<TextParagraph>();

    // Create TextState instance to specify font name and size
    auto state = MakeObject<TextState>("Arial", 12);

    // Specify the character spacing
    state->set_CharacterSpacing(1.5f);

    // Append text to TextParagraph object
    paragraph->AppendLine(u"This is paragraph with character spacing", state);

    // Specify the position for TextParagraph
    paragraph->set_Position(MakeObject<Position>(100, 550));

    // Append TextParagraph to TextBuilder instance
    builder->AppendParagraph(paragraph);

    // Save resulting PDF document.
    document->Save(_dataDir + outputFileName);
}
```

### Using TextStamp

```cpp
void CharacterSpacing_TextStamp() {
    
    String _dataDir("C:\\Samples\\");
    String outputFileName("CharacterSpacingUsingTextStamp_out.pdf");
    // Create Document instance
    auto document = MakeObject<Document>();

    // Add page to pages collection of Document    
    auto page = document->get_Pages()->Add();

    // Instantiate TextStamp instance with sample text
    auto stamp = MakeObject<TextStamp>("This is text stamp with character spacing");

    // Specify font name for Stamp object
    stamp->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    // Specify Font size for TextStamp
    stamp->get_TextState()->set_FontSize(12);
    // Specify character specing as 1f
    stamp->get_TextState()->set_CharacterSpacing(1.0f);
    // Set the XIndent for Stamp
    stamp->set_XIndent(100);
    // Set the YIndent for Stamp
    stamp->set_YIndent(500);
    // Add textual stamp to page instance
    stamp->Put(page);
    // Save resulting PDF document.
    document->Save(_dataDir + outputFileName);
}
```

## Create Multi-Column PDF document

In magazines and newspapers, we mostly see that news are displayed in multiple columns on the single pages instead of the books where text paragraphs are mostly printed on the whole pages from left to right position. Many document processing applications like Microsoft Word and Adobe Acrobat Writer allow users to create multiple columns on a single page and then add data to them.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) also offers the feature to create multiple columns inside the pages of PDF documents. In order to create multi-column PDF file, we can make use of Aspose.Pdf.FloatingBox class as it provides ColumnInfo.ColumnCount property to specify the number of columns inside FloatingBox and we can also specify the spacing between columns and columns widths using ColumnInfo.ColumnSpacing and ColumnInfo.ColumnWidths properties accordingly. Please note that FloatingBox is an element inside Document Object Model and it can have obsolete positioning as compared to relative positioning (i.e. Text, Graph, Image, etc).

Column spacing means the space between the columns and the default spacing between the columns is 1.25cm. If the column width is not specified, then [Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) calculates width for each column automatically according to the page size and column spacing.

An example is given below to demonstrate the creation of two columns with Graphs objects (Line) and they are added to paragraphs collection of FloatingBox, which is then added paragraphs collection of Page instance.

```cpp
void CreateMultiColumn() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("CreateMultiColumnPdf_out.pdf");

    // Create new document instance    
    auto document = MakeObject<Document>();

    // Specify the left margin info for the PDF file
    document->get_PageInfo()->get_Margin()->set_Left(40);

    // Specify the Right margin info for the PDF file
    document->get_PageInfo()->get_Margin()->set_Right(40);

    // Add page to pages collection of PDF file
    auto page = document->get_Pages()->Add();

    auto graph1 = MakeObject<Aspose::Pdf::Drawing::Graph>(500, 2);

    // Add the line to paraphraphs collection of section object
    page->get_Paragraphs()->Add(graph1);

    // Specify the coordinates for the line
    auto posArr = MakeArray<float>({ 1, 2, 500, 2 });
    auto l1 = MakeObject<Aspose::Pdf::Drawing::Line>(posArr);
    graph1->get_Shapes()->Add(l1);

    // Create string variables with text containing html tags
    String s ("<span style=\"font-family: \"Times New Roman\", Times, serif;\" font-size=\"14pt\" \">\
<strong> How to Steer Clear of money scams</<strong> </span>");

    // Create text paragraphs containing HTML text

    auto heading_text = MakeObject<HtmlFragment>(s);
    page->get_Paragraphs()->Add(heading_text);

    auto box = MakeObject<FloatingBox>();

    // Add four columns in the section
    box->get_ColumnInfo()->set_ColumnCount(2);
    // Set the spacing between the columns
    box->get_ColumnInfo()->set_ColumnSpacing(u"5");

    box->get_ColumnInfo()->set_ColumnWidths(u"105 105");
    auto text1 = MakeObject<TextFragment>("By A Googler (The Official Google Blog)");
    text1->get_TextState()->set_FontSize(8);
    text1->get_TextState()->set_LineSpacing(2);
    text1->get_TextState()->set_FontSize(10);
    text1->get_TextState()->set_FontStyle(FontStyles::Italic);

    box->get_Paragraphs()->Add(text1);

    // Create a graphs object to draw a line
    auto graph2 = MakeObject<Aspose::Pdf::Drawing::Graph>(50, 10);
    // Specify the coordinates for the line
    auto posArr2 = MakeArray<float>({ 1, 10, 100, 10 });

    auto l2 = MakeObject<Aspose::Pdf::Drawing::Line>(posArr2);
    graph2->get_Shapes()->Add(l2);

    // Add the line to paragraphs collection of section object
    box->get_Paragraphs()->Add(graph2);

    auto text2 = MakeObject<TextFragment>(
        "Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. \
        Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue.\
        Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur \
        ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean \
        posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. \
        Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, \
        risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam \
        luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, \
        sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, \
        pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut,\
        iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus \
        mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla.\
        Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam,\
        iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique\
        ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.\
        Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. \
        Praesent porttitor turpis eleifend ante. Morbi sodales.");
    box->get_Paragraphs()->Add(text2);

    page->get_Paragraphs()->Add(box);

    // Save PDF file
    document->Save(_dataDir + outputFileName);
}
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
void CustomTabStops() {
    String _dataDir("C:\\Samples\\");
    String outputFileName("CustomTabStops_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto ts = MakeObject<TabStops>();
    auto ts1 = ts->Add(100);

    ts1->set_AlignmentType(TabAlignmentType::Right);
    ts1->set_LeaderType(TabLeaderType::Solid);

    auto ts2 = ts->Add(200);
    ts2->set_AlignmentType(TabAlignmentType::Center);
    ts2->set_LeaderType(TabLeaderType::Dash);

    auto ts3 = ts->Add(300);
    ts3->set_AlignmentType(TabAlignmentType::Left);
    ts3->set_LeaderType(TabLeaderType::Dot);

    auto header = MakeObject<TextFragment>("This is a example of forming table with TAB stops", ts);
    auto text0 =  MakeObject<TextFragment>("#$TABHead1 #$TABHead2 #$TABHead3", ts);

    auto text1 = MakeObject<TextFragment>("#$TABdata11 #$TABdata12 #$TABdata13", ts);
    auto text2 = MakeObject<TextFragment>("#$TABdata21 ", ts);
    text2->get_Segments()->Add(MakeObject<TextSegment>("#$TAB"));
    text2->get_Segments()->Add(MakeObject<TextSegment>("data22 "));
    text2->get_Segments()->Add(MakeObject<TextSegment>("#$TAB"));
    text2->get_Segments()->Add(MakeObject<TextSegment>("data23"));
              
    page->get_Paragraphs()->Add(header);
    page->get_Paragraphs()->Add(text0);
    page->get_Paragraphs()->Add(text1);
    page->get_Paragraphs()->Add(text2);

    document->Save(_dataDir + outputFileName);
}
```

## How to Add Transparent Text in PDF

A PDF file contains Image, Text, Graph, attachment, Annotations objects and while creating TextFragment, you can set foreground, background-color information as well as text formatting. Aspose.PDF for .NET supports the feature to add text with Alpha color channel. The following code snippet shows how to add text with transparent color.

```cpp
void AddTransparentText() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("AddTransparentText_out.pdf");

    // Create Document instance
    auto document = MakeObject<Document>();    
    // Create page to pages collection of PDF file
    auto page = document->get_Pages()->Add();

    // Create Graph object
    auto canvas = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);

    // Create rectangle instance with certain dimensions
    auto rect = MakeObject<Aspose::Pdf::Drawing::Rectangle>(100, 100, 400, 400);
    // Create color object from Alpha color channel
    int alpha = 10;
    int green = 0;
    int red = 100;
    int blue = 0;

    auto alphaColor = Color::FromArgb(alpha, red, green, blue);

    rect->get_GraphInfo()->set_FillColor(alphaColor);

    // Add rectanlge to shapes collection of Graph object
    canvas->get_Shapes()->Add(rect);

    // Add graph object to paragraphs collection of page object
    page->get_Paragraphs()->Add(canvas);

    // Set value to not change position for graph object
    canvas->set_IsChangePosition(false);

    // Create TextFragment instance with sample value
    auto text = MakeObject<TextFragment>(
        "transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text ");
    // Create color object from Alpha channel
    alpha = 30;
    alphaColor = Color::FromArgb(alpha, red, green, blue);
    // Set color information for text instance
    text->get_TextState()->set_ForegroundColor(alphaColor);
    // Add text to paragraphs collection of page instance
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## Specify LineSpacing for Fonts

Every font has an abstract square, whose height is the intended distance between lines of type in the same type size. This square is called the em square and it is the design grid on which the glyph outlines are defined. Many letters of input font have points that are placed out of font's em square bounds, so in order to display the font correctly, usage of special setting is needed. The object TextFragment has a set of text formatting options which are accessible via properties TextState.FormattingOptions. Last property of this path is property of type Aspose.Pdf.Text.TextFormattingOptions. This class has a an enumeration [LineSpacingMode](https://apireference.aspose.com/pdf/net/aspose.pdf.text.textformattingoptions/linespacingmode) which is designed for specific fonts e.g input font "HPSimplified.ttf". Also class [Aspose.Pdf.Text.TextFormattingOptions](https://apireference.aspose.com/pdf/net/aspose.pdf.text/textformattingoptions) has a property [LineSpacing](https://apireference.aspose.com/pdf/net/aspose.pdf.text/textformattingoptions/properties/linespacing) of type LineSpacingMode. You just need to set LineSpacing into LineSpacingMode.FullSize. The code snippet to get a font displayed correctly, would be like as follows:

```cpp
void SpecifyLineSpacingForFonts() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("SpecifyLineSpacing_out.pdf");

    String fontFile ("hp-simplified-265.ttf");

    // Load input PDF file
    auto document = MakeObject<Document>();
    
    // Create TextFormattingOptions with LineSpacingMode.FullSize
    auto formattingOptions = MakeObject<TextFormattingOptions>();
    formattingOptions->set_LineSpacing(TextFormattingOptions::LineSpacingMode::FullSize);
    
    // Create text fragment with sample string
    auto textFragment = MakeObject<TextFragment>("Hello world");

    // Load the TrueType font into stream object
    auto fontStream = System::IO::File::OpenRead(_dataDir + fontFile);
    
    // Set the font name for text string
    textFragment->get_TextState()->set_Font(FontRepository::OpenFont(fontStream, FontTypes::TTF));
    // Specify the position for Text Fragment
    textFragment->set_Position(MakeObject<Position>(100, 600));
    // Set TextFormattingOptions of current fragment to predefined(which points to
    // LineSpacingMode.FullSize)
    textFragment->get_TextState()->set_FormattingOptions(formattingOptions);
    
    // Add the text to TextBuilder so that it can be placed over the PDF file    
    auto page = document->get_Pages()->Add();
    page->get_Paragraphs()->Add(textFragment);

    // Save resulting PDF document
    document->Save(_dataDir + outputFileName);
}
```

## Get Text Width Dynamically

Sometimes, it is required to get the text width dynamically. Aspose.PDF for .NET includes two methods for string width measurement. You can invoke the [MeasureString](https://apireference.aspose.com/pdf/net/aspose.pdf.text/font/methods/measurestring) method of Aspose.Pdf.Text.Font or Aspose.Pdf.Text.TextState classes (or both). The code snippet below shows how to use this functionality.

```cpp
void GetTextWidthDynamicaly() {
    auto font = FontRepository::FindFont(u"Arial");
    auto ts = MakeObject<TextState>();

    ts->set_Font(font);
    ts->set_FontSize(14);

    if (Math::Abs(font->MeasureString(u"A", 14) - 9.337) > 0.001)
        Console::WriteLine(u"Unexpected font string measure!");

    if (Math::Abs(ts->MeasureString(u"z") - 7.0) > 0.001)
        Console::WriteLine(u"Unexpected font string measure!");

    for (char c = 'A'; c <= 'z'; c++) {
        String v(c);
        double fnMeasure = font->MeasureString(v, 14);
        double tsMeasure = ts->MeasureString(v);

        if (Math::Abs(fnMeasure - tsMeasure) > 0.001)
            Console::WriteLine(u"Font and state string measuring doesn't match!");
    }
}
```
