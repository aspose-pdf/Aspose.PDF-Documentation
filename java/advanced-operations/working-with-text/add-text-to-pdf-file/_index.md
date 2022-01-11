---
title: Add Text to PDF file 
linktitle: Add Text to PDF file
type: docs
weight: 10
url: /java/add-text-to-pdf-file/
description: This article describes various aspects of working with text in Aspose.PDF. Learn how to add text to PDF, add HTML fragments, or use custom OTF fonts.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

To add text to existing PDF file:

1. Open the input PDF using the Document object.
2. Get the particular page to which you want to add the text.
3. Create a TextFragment object with the input text along with other text properties. The TextBuilder object created from that particular page – to which you want to add the text – allows you to add the TextFragment object to the page using the AppendText method.
4. Call the Document object's Save method and save the output PDF file.

## Adding Text

The following code snippet shows you how to add text in an existing PDF file.

```java
public static void AddingText() {
    // Load the PDF file
    Document document = new Document(_dataDir + "sample.pdf");

    // get particular page
    Page pdfPage = document.getPages().get_Item(1);
    // create text fragment
    TextFragment textFragment = new TextFragment("Aspose.PDF");
    textFragment.setPosition(new Position(80, 700));

    // set text properties
    textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
    textFragment.getTextState().setFontSize(14);
    textFragment.getTextState().setForegroundColor(Color.getBlue());
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());

    // create TextBuilder object
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // append the text fragment to the PDF page
    textBuilder.appendText(textFragment);

    // Save resulting PDF document.
    document.save(_dataDir + "AddText_out.pdf");
}
```

## Loading Font from Stream

The following code snippet shows how to load Font from Stream object when adding text to PDF document.

```java
import com.aspose.pdf.*;
import com.aspose.pdf.text.FontTypes;

import java.io.FileInputStream;
import java.io.FileNotFoundException;  
//...
public static void LoadingFontFromStream() throws FileNotFoundException{
    
    String fontFile = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf";

    // Load input PDF file
    Document doc = new Document(_dataDir + "input.pdf");
    // Create text builder object for first page of document
    TextBuilder textBuilder = new TextBuilder(doc.getPages().get_Item(1));
    // Create text fragment with sample string
    TextFragment textFragment = new TextFragment("Hello world");
    
    if (fontFile != "")
    {
        // Load the TrueType font into stream object
        FileInputStream fontStream=new FileInputStream(fontFile);            
        // Set the font name for text string
        textFragment.getTextState().setFont (FontRepository.openFont(fontStream, FontTypes.TTF));
        // Specify the position for Text Fragment
        textFragment.setPosition(new Position(10, 10));
        // Add the text to TextBuilder so that it can be placed over the PDF file
        textBuilder.appendText(textFragment);
        
        _dataDir = _dataDir + "LoadingFontFromStream_out.pdf";
    
        // Save resulting PDF document.
        doc.save(_dataDir); 
    }       
}
```

## Add Text using TextParagraph

The following code snippet shows you how to add text in PDF document using [TextParagraph](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextParagraph) class.

```java
public static void AddTextUsingTextParagraph() {
    // Open document
    Document doc = new Document();
    // Add page to pages collection of Document object
    Page page = doc.getPages().add();
    TextBuilder builder = new TextBuilder(page);
    // Create text paragraph
    TextParagraph paragraph = new TextParagraph();
    // Set subsequent lines indent
    paragraph.setSubsequentLinesIndent (20);
    // Specify the location to add TextParagraph
    paragraph.setRectangle(new Rectangle(100, 300, 200, 700));
    // Specify word wraping mode
    paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
    // Create text fragment
    TextFragment fragment1 = new TextFragment("the quick brown fox jumps over the lazy dog");
    fragment1.getTextState().setFont (FontRepository.findFont("Times New Roman"));
    fragment1.getTextState().setFontSize (12);
    // Add fragment to paragraph
    paragraph.appendLine(fragment1);
    // Add paragraph
    builder.appendParagraph(paragraph);

    _dataDir = _dataDir + "AddTextUsingTextParagraph_out.pdf";

    // Save resulting PDF document.
    doc.save(_dataDir);        
}
```

## Add Hyperlink to TextSegment

A PDF page may comprise of one or more TextFragment objects, where each TextFragment object can have one or more TextSegment instance. In order to set hyperlink for TextSegment, Hyperlink property of TextSegment class can be used while providing the object of Aspose.Pdf.WebHyperlink instance. Please try using the following code snippet to accomplish this requirement.

```java
public static void AddHyperlinkToTextSegment() {
    // Create document instance
    Document doc = new Document();
    // Add page to pages collection of PDF file
    Page page1 = doc.getPages().add();

    // Create TextFragment instance
    TextFragment tf = new TextFragment("Sample Text Fragment");
    // Set horizontal alignment for TextFragment
    tf.setHorizontalAlignment(HorizontalAlignment.Right);

    // Create a textsegment with sample text
    TextSegment segment = new TextSegment(" ... Text Segment 1...");
    // Add segment to segments collection of TextFragment
    tf.getSegments().add(segment);

    // Create a new TextSegment
    segment = new TextSegment("Link to Google");
    // Add segment to segments collection of TextFragment

    tf.getSegments().add(segment);

    // Set hyperlink for TextSegment
    segment.setHyperlink(new com.aspose.pdf.WebHyperlink("www.aspose.com"));

    // Set forground color for text segment
    segment.getTextState().setForegroundColor(com.aspose.pdf.Color.getBlue());

    // Set text formatting as italic
    segment.getTextState().setFontStyle(FontStyles.Italic);

    // Create another TextSegment object
    segment = new TextSegment("TextSegment without hyperlink");

    // Add segment to segments collection of TextFragment
    tf.getSegments().add(segment);

    // Add TextFragment to paragraphs collection of page object
    page1.getParagraphs().add(tf);

    _dataDir = _dataDir + "AddHyperlinkToTextSegment_out.pdf";

    // Save resulting PDF document.
    doc.save(_dataDir);

}
```

## Use OTF Font

Aspose.PDF for Java offers the feature to use Custom/TrueType fonts while creating/manipulating PDF file contents so that file contents are displayed using contents other than default system fonts. Starting release of Aspose.PDF for Java 10.4.0, we have provided the support for Open Type Fonts.

```java
public static void UseOTFFont() {
    // Create new document instance
    Document pdfDocument = new Document();
    // Add page to pages collection of PDF file
    Page page = pdfDocument.getPages().add();
    // Create TextFragment instnace with sample text
    TextFragment fragment = new TextFragment("Sample Text in OTF font");
    // Or you can even specify the path of OTF font in system directory
    fragment.getTextState().setFont(FontRepository.openFont("/home/aspose/.fonts/Montserrat-Black.otf"));
    // Specify to emend font inside PDF file, so that its displayed properly,
    // Even if specific font is not installed/present over target machine
    fragment.getTextState().getFont().setEmbedded(true);
    // Add TextFragment to paragraphs collection of Page instance
    page.getParagraphs().add(fragment);
    // Save resulting PDF document.
    pdfDocument.save(_dataDir + "OTFFont_out.pdf");
}
```

## Add HTML String using DOM

The Aspose.Pdf.Generator.Text class contains a property called IsHtmlTagSupported which makes it possible to add HTML tags/contents into PDF files. The added content is rendered in native HTML tags instead of appearing as a simple text string. To support a similar feature in the new Document Object Model (DOM) of the Aspose.Pdf namespace, the HtmlFragment class has been introduced.

The [HtmlFragment](https://apireference.aspose.com/pdf/java/com.aspose.pdf/HtmlFragment) instance can be used to specify the HTML contents which should be placed inside the PDF file. Similar to TextFragment, HtmlFragment is a paragraph level object and can be added to the Page object's paragraphs collection. The following code snippets show the steps to place HTML contents inside PDF file using the DOM approach.

```java
public static void AddingHtmlString() {
    // Instantiate Document object
    Document doc = new Document();
    // Add a page to pages collection of PDF file
    Page page = doc.getPages().add();
    // Instantiate HtmlFragment with HTML contents
    HtmlFragment title = new HtmlFragment("<h1 style=\"color:blue\"><strong>HTML String Demo</strong></h1>");
    // set MarginInfo for margin details
    MarginInfo Margin = new MarginInfo();
    Margin.setBottom(10);
    Margin.setTop(200);
    // Set margin information
    title.setMargin(Margin);
    // Add HTML Fragment to paragraphs collection of page
    page.getParagraphs().add(title);
    // Save PDF file
    doc.save(_dataDir + "sample_html_out.pdf");
}
```

Following code snippet demonstrate steps how to add HTML ordered lists into the document:

```java
public static void AddHTMLOrderedListIntoDocuments() {
    // Instantiate Document object
    Document doc = new Document();
    // Instantiate HtmlFragment object with corresponding HTML fragment
    HtmlFragment t = new HtmlFragment(
            "<div style=\"font-family: sans-serif\"><ul><li>First</li><li>Second</li><li>Third</li><li>Fourth</li><li>Fifth</li></ul><p>Text after the list.</p><p>Next line<br/>Last line</p></div>");
    // Add Page in Pages Collection
    Page page = doc.getPages().add();
    // Add HtmlFragment inside page
    page.getParagraphs().add(t);
    // Save resultant PDF file
    doc.save(_dataDir + "AddHTMLOrderedListIntoDocuments_out.pdf");
}
```

You can also set HTML string formatting using TextState object as following:

```java
public static void AddHTMLStringFormatting() {
    // Instantiate Document object
    Document doc = new Document();
    // Add a page to pages collection of PDF file
    Page page = doc.getPages().add();
    // Instantiate HtmlFragment with HTML contents
    HtmlFragment title = new HtmlFragment("<h1><strong>HTML String Demo</strong></h1>");
    TextState textState = new TextState(12);
    textState.setFont(FontRepository.findFont("Calibri"));
    textState.setForegroundColor(Color.getGreen());
    textState.setBackgroundColor(Color.getCoral());
    title.setTextState(textState);

    // Add HTML Fragment to paragraphs collection of page
    page.getParagraphs().add(title);
    // Save PDF file
    doc.save(_dataDir + "sample_html_out.pdf");
}
```

In case if you set some text attributes values via HTML markup and then provide the same values in TextState properties they will overwrite HTML parameters by properties form TextState instance. The following code snippets show described behavior.

```java
public static void AddHTMLUsingDOMAndOverwrite() {
    // Instantiate Document object
    Document doc = new Document();
    // Add a page to pages collection of PDF file
    Page page = doc.getPages().add();
    // Instantiate HtmlFragment with HTML contnets
    HtmlFragment title = new HtmlFragment("<p style='font-family: Verdana'><b><i>Table contains text</i></b></p>");
    // Font-family from 'Verdana' will be reset to 'Arial'
    title.setTextState(new TextState("Arial Black"));
    title.setTextState(new TextState(20));
    // Set bottom margin information
    title.getMargin().setBottom(10);
    // Set top margin information
    title.getMargin().setTop(400);
    // Add HTML Fragment to paragraphs collection of page
    page.getParagraphs().add(title);
    // Save PDF file
    doc.save(_dataDir + "AddHTMLUsingDOMAndOverwrite_out.pdf");
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

### Custom line style for FootNote

The following example demonstrates how to add Footnotes to the bottom of the Pdf page and define a custom line style.

```java
public static void AddFootNote() {
    // create Document instance
    Document document = new Document(_dataDir + "sample.pdf");

    Page page = document.getPages().get_Item(1);
    TextFragmentAbsorber tfa = new TextFragmentAbsorber("Portable Document Format");
    tfa.visit(page);

    TextFragment t = tfa.getTextFragments().get_Item(1);
    Note note = new Note();
    note.setText("Demo");
    t.setFootNote(note);

    // create TextFragment instance
    TextFragment text = new TextFragment("Hello World");
    // set FootNote value for TextFragment
    text.setFootNote(new Note("foot note for test text 1"));
    // add TextFragment to paragraphs collection of first page of document
    page.getParagraphs().add(text);
    // create second TextFragment
    text = new TextFragment("Aspose.Pdf for Java");
    // set FootNote for second text fragment
    text.setFootNote(new Note("foot note for test text 2"));
    // add second text fragment to paragraphs collection of PDF file
    page.getParagraphs().add(text);

    document.save(_dataDir + "sample_footnote.pdf");
}
```

We can set Footnote Label (note identifier) formatting using TextState object as following:

```java
public static void AddCustomFootNoteLabel() {
    // create Document instance
    Document document = new Document(_dataDir + "sample.pdf");

    Page page = document.getPages().get_Item(1);
    TextFragmentAbsorber tfa = new TextFragmentAbsorber("Portable Document Format");
    tfa.visit(page);

    TextFragment t = tfa.getTextFragments().get_Item(1);
    Note note = new Note();
    note.setText("Demo");
    t.setFootNote(note);

    // create TextFragment instance
    TextFragment text = new TextFragment("Hello World");
    // set FootNote value for TextFragment
    text.setFootNote(new Note("foot note for test text 1"));
    text.getFootNote().setText("21");
    TextState ts = new TextState();
    ts.setForegroundColor(Color.getBlue());
    ts.setFontStyle(FontStyles.Italic);
    text.getFootNote().setTextState(ts);

    // add TextFragment to paragraphs collection of first page of document
    page.getParagraphs().add(text);
    // create second TextFragment
    text = new TextFragment("Aspose.Pdf for Java");
    // set FootNote for second text fragment
    text.setFootNote(new Note("foot note for test text 2"));
    // add second text fragment to paragraphs collection of PDF file
    page.getParagraphs().add(text);

    document.save(_dataDir + "sample_footnote.pdf");
}
```

### Customize Footnote label

By default, the FootNote number is incremental starting from 1. However, we may have a requirement to set a custom FootNote label. In order to accomplish this requirement, please try using the following code snippet

```java
public static void CustomFootNote_Label() {
    // Create Document instance
    Document document = new Document();
    // Add page to pages collection of PDF
    Page page = document.getPages().add();
    // Create GraphInfo object
    GraphInfo graph = new GraphInfo();
    // Set line width as 2
    graph.setLineWidth(2);
    // Set the color for graph object
    graph.setColor(Color.getRed());
    // Set dash array value as 3
    graph.setDashArray(new int[] { 3 });
    // Set dash phase value as 1
    graph.setDashPhase(1);
    // Set footnote line style for page as graph
    page.setNoteLineStyle(graph);

    // Create TextFragment instance
    TextFragment text = new TextFragment("Hello World");
    // Set FootNote value for TextFragment
    text.setFootNote(new Note("foot note for test text 1"));
    // Specify custom label for FootNote
    text.getFootNote().setText(" Aspose(2021)");
    // Add TextFragment to paragraphs collection of first page of document
    page.getParagraphs().add(text);

    document.save(_dataDir + "CustomizeFootNoteLabel_out.pdf");
}
```

## Adding Image and Table to Footnote

In earlier release versions, the Footnote support was provided but it was only applicable to TextFragment object. However starting release Aspose.PDF for Java 10.7.0, you can also add Footnote to other objects inside PDF document such as Table, Cells etc. The following code snippet shows the steps to add Footnote to TextFragment object and then add Image and Table object to paragraphs collection of Footnote section.

```java
public static void AddingImageAndTableToFootnote() {
    // Create Document instance
    Document document = new Document();
    // Add page to pages collection of PDF
    Page page = document.getPages().add();
    // Create TextFragment instance
    TextFragment text = new TextFragment("Hello World");

    page.getParagraphs().add(text);

    text.setFootNote(new Note());
    Image image = new Image();
    image.setFile(_dataDir + "aspose-logo.jpg");
    image.setFixHeight(20);
    text.getFootNote().getParagraphs().add(image);
    TextFragment footNote = new TextFragment("footnote text");
    footNote.getTextState().setFontSize(20);
    footNote.setInLineParagraph(true);
    text.getFootNote().getParagraphs().add(footNote);
    Table table = new Table();
    table.getRows().add().getCells().add().getParagraphs().add(new TextFragment("Row 1 Cell 1"));
    text.getFootNote().getParagraphs().add(table);

    page.getParagraphs().add(text);

    document.save(_dataDir + "AddImageAndTable_out.pdf");
}
```

## How to Create EndNotes

An EndNote is a source citation that refers the readers to a specific place at the end of the paper where they can find out the source of the information or words quoted or mentioned in the paper. When using endnotes, your quoted or paraphrased sentence or summarized material is followed by a superscript number.

The following example demonstrates how to add an Endnote in the Pdf page.

```java
public static void HowToCreateEndNotes() {
    Document doc = new Document();
    // add page to pages collection of PDF
    Page page = doc.getPages().add();
    // create TextFragment instance
    TextFragment text = new TextFragment("Hello World");
    // set FootNote value for TextFragment
    text.setEndNote(new Note("sample End note"));
    // specify custom label for FootNote
    text.getEndNote().setText(" Aspose(2021)");
    // add TextFragment to paragraphs collection of first page of document
    page.getParagraphs().add(text);
    // save the PDF file
    doc.save(_dataDir + "EndNote.pdf");
}
```

## Text and Image as InLine Paragraph

The default layout of the PDF file is flow layout (Top-Left to Bottom-Right). Therefore every new element being added to PDF file is added in the bottom right flow. However, we may have a requirement to display various page elements i.e. Image and Text at the same level (one after another). One approach can be to create a Table instance and add both elements to individual cell objects. However, another approach can be InLine paragraph. By setting IsInLineParagraph property of Image and Text as true, these paragraphs will appear as inline to other page elements.

The following code snippet shows you how to add text and Image as InLine paragraphs in PDF file.

```java
 public static void TextAndImageAsInLineParagraph() {
    // Instantiate Document instance
    Document doc = new Document();
    // Add page to pages collection of Document instance
    Page page = doc.getPages().add();
    // Create TextFragmnet
    TextFragment text = new TextFragment("Hello World.. ");
    // Add text fragment to paragraphs collection of Page object
    page.getParagraphs().add(text);
    // Create an image instance
    Image image = new Image();
    // Set image as inline paragraph so that it appears right after
    // The previous paragraph object (TextFragment)
    image.setInLineParagraph (true);
    // Specify image file path
    image.setFile(_dataDir + "aspose-logo.jpg");
    // Set image Height (optional)
    image.setFixHeight(30);
    // Set Image Width (optional)
    image.setFixWidth(100);
    // Add image to paragraphs collection of page object
    page.getParagraphs().add(image);
    // Re-initialize TextFragment object with different contents
    text = new TextFragment(" Hello Again..");
    // Set TextFragment as inline paragraph
    text.setInLineParagraph (true);
    // Add newly created TextFragment to paragraphs collection of page
    page.getParagraphs().add(text);
    
    doc.save(_dataDir+"TextAndImageAsParagraph_out.pdf");
}
```

## Specify character Spacing when adding Text

A text can be added inside paragraphs collection of PDF files using TextFragment instance or by using TextParagraph object and even you can stamp the text inside PDF by using TextStamp class. While adding the text, we may have a requirement to specify character spacing for the text objects. In order to accomplish this requirement, a new property named CharacterSpacing property has been introduced. Please take a look at the following approaches to fulfill this requirement.

The following approaches show the steps to specify character spacing when adding text inside a PDF document.

## Using TextBuilder and TextFragment

```java
 public static void CharacterSpacing_TextFragment(){
    // Create Document instance
    Document pdfDocument = new Document();
    // Add page to pages collection of Document
    Page page = pdfDocument.getPages().add();
    // Create TextBuilder instance
    TextBuilder builder = new TextBuilder(page);
    // Create text fragment instance with sample contents
    TextFragment wideFragment = new TextFragment("Text with increased character spacing");
    wideFragment.getTextState().applyChangesFrom(new TextState("Arial", 12));
    // Specify character spacing for TextFragment
    wideFragment.getTextState().setCharacterSpacing(2.0f);
    // Specify the position of TextFragment
    wideFragment.setPosition(new Position(100, 650));
    // Append TextFragment to TextBuilder instance
    builder.appendText(wideFragment);        
    // Save resulting PDF document.
    pdfDocument.save(_dataDir+ "CharacterSpacingUsingTextBuilderAndFragment_out.pdf");
}
```

## Using TextBuilder and TextParagraph

```java
public static void CharacterSpacing_TextParagraph() {
    // Create Document instance
    Document pdfDocument = new Document();
    // Add page to pages collection of Document
    Page page = pdfDocument.getPages().add();
    // Create TextBuilder instance
    TextBuilder builder = new TextBuilder(page);
    // Instantiate TextParagraph instance
    TextParagraph paragraph = new TextParagraph();
    // Create TextState instance to specify font name and size
    TextState state = new TextState("Arial", 12);
    // Specify the character spacing
    state.setCharacterSpacing (1.5f);
    // Append text to TextParagraph object
    paragraph.appendLine("This is paragraph with character spacing", state);
    // Specify the position for TextParagraph
    paragraph.setPosition (new Position(100, 550));
    // Append TextParagraph to TextBuilder instance
    builder.appendParagraph(paragraph);
    // Save resulting PDF document.
    pdfDocument.save(_dataDir + "CharacterSpacingUsingTextBuilderAndParagraph_out.pdf");
}
```

## Using TextStamp

```java
public static void CharacterSpacing_TextStamp() {
    // Create Document instance
    Document pdfDocument = new Document();
    // Add page to pages collection of Document
    Page page = pdfDocument.getPages().add();
    // Instantiate TextStamp instance with sample text
    TextStamp stamp = new TextStamp("This is text stamp with character spacing");
    // Specify font name for Stamp object
    stamp.getTextState().setFont(FontRepository.findFont("Arial"));
    // Specify Font size for TextStamp
    stamp.getTextState().setFontSize(12);
    // Specify character specing as 1f
    stamp.getTextState().setCharacterSpacing (1f);
    // Set the XIndent for Stamp
    stamp.setXIndent(100);
    // Set the YIndent for Stamp
    stamp.setYIndent(500);
    // Add textual stamp to page instance
    stamp.put(page);        
    // Save resulting PDF document.
    pdfDocument.save(_dataDir+"CharacterSpacingUsingTextStamp_out.pdf");        
}
```

## Create Multi-Column PDF document

In magazines and newspapers, we mostly see that news are displayed in multiple columns on the single pages instead of the books where text paragraphs are mostly printed on the whole pages from left to right position. Many document processing applications like Microsoft Word and Adobe Acrobat Writer allow users to create multiple columns on a single page and then add data to them.

Aspose.PDF for Java also offers the feature to create multiple columns inside the pages of PDF documents. In order to create multi-column PDF file, we can make use of Aspose.Pdf.FloatingBox class as it provides ColumnInfo.ColumnCount property to specify the number of columns inside FloatingBox and we can also specify the spacing between columns and columns widths using ColumnInfo.ColumnSpacing and ColumnInfo.ColumnWidths properties accordingly. Please note that FloatingBox is an element inside Document Object Model and it can have obsolete positioning as compared to relative positioning (i.e. Text, Graph, Image, etc).

Column spacing means the space between the columns and the default spacing between the columns is 1.25cm. If the column width is not specified, then Aspose.PDF for Java calculates width for each column automatically according to the page size and column spacing.

An example is given below to demonstrate the creation of two columns with Graphs objects (Line) and they are added to paragraphs collection of FloatingBox, which is then added paragraphs collection of Page instance.

```java
public static void CreateMultiColumn() {
    Document doc = new Document();
    // Specify the left margin info for the PDF file
    doc.getPageInfo().getMargin().setLeft(40);
    
    // Specify the Right margin info for the PDF file
    doc.getPageInfo().getMargin().setRight(40);
    
    Page page = doc.getPages().add();

    com.aspose.pdf.drawing.Graph graph1 = new com.aspose.pdf.drawing.Graph(500, 2);
    
    // Add the line to paraphraphs collection of section object
    page.getParagraphs().add(graph1);

    // Specify the coordinates for the line
    float[] posArr = new float[] { 1, 2, 500, 2 };
    com.aspose.pdf.drawing.Line l1 = new com.aspose.pdf.drawing.Line(posArr);
    graph1.getShapes().add(l1);
    
    // Create string variables with text containing html tags
    String s = "<span style=\"font-family: \"Times New Roman\", Times, serif;\" font-size=\"14pt\" \">"
                +"<strong> How to Steer Clear of money scams</<strong> </span>";
    
    // Create text paragraphs containing HTML text

    HtmlFragment heading_text = new HtmlFragment(s);
    page.getParagraphs().add(heading_text);

    FloatingBox box = new FloatingBox();
    
    // Add four columns in the section
    box.getColumnInfo().setColumnCount(2);
    // Set the spacing between the columns
    box.getColumnInfo().setColumnSpacing("5");

    box.getColumnInfo().setColumnWidths("105 105");
    TextFragment text1 = new TextFragment("By A Googler (The Official Google Blog)");
    text1.getTextState().setFontSize (8);
    text1.getTextState().setLineSpacing (2);
    text1.getTextState().setFontSize (10);
    text1.getTextState().setFontStyle (FontStyles.Italic);

    box.getParagraphs().add(text1);
    
    // Create a graphs object to draw a line
    com.aspose.pdf.drawing.Graph graph2 = new com.aspose.pdf.drawing.Graph(50, 10);
    // Specify the coordinates for the line
    float[] posArr2 = new float[] { 1, 10, 100, 10 };
    com.aspose.pdf.drawing.Line l2 = new com.aspose.pdf.drawing.Line(posArr2);
    graph2.getShapes().add(l2);

    // Add the line to paragraphs collection of section object
    box.getParagraphs().add(graph2);

    TextFragment text2 = new TextFragment("Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. "
    +"Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue."
    +"Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur "
    +"ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean "
    +"posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. "
    +"Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, "
    +"risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam "
    +"luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, "
    +"sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, "
    +"pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut,"
    +"iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus "
    +"mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla."
    +"Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam,"
    +"iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique"
    +"ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
    +"Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. "
    +"Praesent porttitor turpis eleifend ante. Morbi sodales.");
    box.getParagraphs().add(text2);

    page.getParagraphs().add(box);

    // Save PDF file
    doc.save(_dataDir + "CreateMultiColumnPdf_out.pdf");        
}
```

## Working with custom Tab Stops

A Tab Stop is a stop point for tabbing. In word processing, each line contains a number of tab stops placed at regular intervals (for example, every half inch). They can be changed, however, as most word processors allow you to set tab stops wherever you want. When you press the Tab key, the cursor or insertion point jumps to the next tab stop, which itself is invisible. Although tab stops do not exist in the text file, the word processor keeps track of them so that it can react correctly to the Tab key.

[Aspose.PDF for Java](https://docs.aspose.com/pdf/java/) allows developers to use custom tab stops in PDF documents. The Aspose.Pdf.Text.TabStop class is used to set custom TAB stops in the [TextFragment](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) class.

[Aspose.PDF for Java](https://docs.aspose.com/pdf/java/) also offers some pre-defined tab leader types as an enumeration named, TabLeaderType whose pre-defined values and their descriptions are given below:

|**Tab Leader Type**|**Description**|
| :- | :- |
|None|No tab leader|
|Solid|Solid tab leader|
|Dash|Dash tab leader|
|Dot|Dot tab leader|

Here is an example of how to set custom TAB stops.

```java
public static void CustomTabStops() {
    Document pdfdocument = new Document();
    Page page = pdfdocument.getPages().add();

    com.aspose.pdf.TabStops ts = new com.aspose.pdf.TabStops();
    com.aspose.pdf.TabStop ts1 = ts.add(100);
    ts1.setAlignmentType(TabAlignmentType.Right);
    ts1.setLeaderType (TabLeaderType.Solid);
    
    com.aspose.pdf.TabStop ts2 = ts.add(200);
    ts2.setAlignmentType(TabAlignmentType.Center);
    ts2.setLeaderType (TabLeaderType.Dash);

    com.aspose.pdf.TabStop ts3 = ts.add(300);
    ts3.setAlignmentType(TabAlignmentType.Left);
    ts3.setLeaderType (TabLeaderType.Dot);

    TextFragment header = new TextFragment("This is a example of forming table with TAB stops", ts);
    TextFragment text0 = new TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts);

    TextFragment text1 = new TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts);
    TextFragment text2 = new TextFragment("#$TABdata21 ", ts);
    text2.getSegments().add(new TextSegment("#$TAB"));
    text2.getSegments().add(new TextSegment("data22 "));
    text2.getSegments().add(new TextSegment("#$TAB"));
    text2.getSegments().add(new TextSegment("data23"));

    page.getParagraphs().add(header);
    page.getParagraphs().add(text0);
    page.getParagraphs().add(text1);
    page.getParagraphs().add(text2);
    
    pdfdocument.save(_dataDir + "CustomTabStops_out.pdf"); 
}
```

## How to Add Transparent Text in PDF

A PDF file contains Image, Text, Graph, attachment, Annotations objects and while creating TextFragment, you can set foreground, background-color information as well as text formatting. Aspose.PDF for Java supports the feature to add text with Alpha color channel. The following code snippet shows how to add text with transparent color.

```java
  public static void AddTransparentText() {
    // Create Document instance
    Document pdfdocument = new Document();
    // Create page to pages collection of PDF file
    Page page = pdfdocument.getPages().add();

    // Create Graph object
    Graph canvas = new Graph(100, 400);
    // Create rectangle instance with certain dimensions
    com.aspose.pdf.drawing.Rectangle rect = new com.aspose.pdf.drawing.Rectangle(100, 100, 400, 400);
    // Create color object from Alpha color channel
    int alpha = 10;
    int green = 0;
    int red = 100;
    int blue = 0;
    Color alphaColor = Color.fromArgb(alpha, red, green, blue);
    rect.getGraphInfo().setFillColor(alphaColor);
    // Add rectanlge to shapes collection of Graph object
    canvas.getShapes().add(rect);
    // Add graph object to paragraphs collection of page object
    page.getParagraphs().add(canvas);
    // Set value to not change position for graph object
    canvas.setChangePosition(false);

    // Create TextFragment instance with sample value
    TextFragment text = new TextFragment(
            "transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text ");
    // Create color object from Alpha channel
    alpha = 30;
    alphaColor = Color.fromArgb(alpha, red, green, blue);
    // Set color information for text instance
    text.getTextState().setForegroundColor (alphaColor);
    // Add text to paragraphs collection of page instance
    page.getParagraphs().add(text);
    
    pdfdocument.save(_dataDir + "AddTransparentText_out.pdf");
}
```

## Specify LineSpacing for Fonts

Every font has an abstract square, whose height is the intended distance between lines of type in the same type size. This square is called the `em square` and it is the design grid on which the glyph outlines are defined. Many letters of input font have points that are placed out of font's `em square` bounds, so in order to display the font correctly, usage of special setting is needed. The object TextFragment has a set of text formatting options which are accessible via method [TextState.getFormattingOptions](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentState#getFormattingOptions--).
This method returns [TextFormattingOptions](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions) class. This class has a an enumeration [LineSpacingMode](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions.LineSpacingMode) which is designed for specific fonts e.g input font "HPSimplified.ttf". Also class [TextFormattingOptions](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions) has a method [setLineSpacing](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions#setLineSpacing-int-) of type LineSpacingMode. You just need to set LineSpacing into LineSpacingMode.FullSize. The code snippet to get a font displayed correctly, would be like as follows:

```java
public static void SpecifyLineSpacingForFonts() {
    String fontFile = _dataDir + "hp-simplified.ttf";
    // Load input PDF file
    Document doc = new Document();
    // Create TextFormattingOptions with LineSpacingMode.FullSize
    TextFormattingOptions formattingOptions = new TextFormattingOptions();
    formattingOptions.setLineSpacing(TextFormattingOptions.LineSpacingMode.FullSize);

    // Create text builder object for first page of document
    // TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
    // Create text fragment with sample string
    TextFragment textFragment = new TextFragment("Hello world");

    // Load the TrueType font into stream object
    FileInputStream fontStream;
    try {
        fontStream = new FileInputStream(fontFile);
    } catch (FileNotFoundException e) {
        e.printStackTrace();
        return;
    }

    // Set the font name for text string
    textFragment.getTextState().setFont(FontRepository.openFont(fontStream, FontTypes.TTF));
    // Specify the position for Text Fragment
    textFragment.setPosition(new Position(100, 600));
    // Set TextFormattingOptions of current fragment to predefined(which points to
    // LineSpacingMode.FullSize)
    textFragment.getTextState().setFormattingOptions(formattingOptions);
    // Add the text to TextBuilder so that it can be placed over the PDF file
    // textBuilder.AppendText(textFragment);
    Page page = doc.getPages().add();
    page.getParagraphs().add(textFragment);

    // Save resulting PDF document
    doc.save(_dataDir + "SpecifyLineSpacing_out.pdf");
}
```


## Get Text Width Dynamically

Sometimes, it is required to get the text width dynamically. Aspose.PDF for Java includes two methods for string width measurement. You can invoke the [MeasureString](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextState#measureString--) method of com.aspose.pdf.Font or com.aspose.pdf.TextState classes (or both). The code snippet below shows how to use this functionality.

```java
public static void GetTextWidthDynamicaly() {
    Font font = FontRepository.findFont("Arial");
    TextState ts = new TextState();
        ts.setFont(font);
        ts.setFontSize(14);
        if (Math.abs(font.measureString("A", 14) - 9.337) > 0.001)
            System.out.println("Unexpected font string measure!");

        if (Math.abs(ts.measureString("z") - 7.0) > 0.001)
        System.out.println("Unexpected font string measure!");

        for (char c = 'A'; c <= 'z'; c++)
        {
            double fnMeasure = font.measureString(String.valueOf(c), 14);
            double tsMeasure = ts.measureString(String.valueOf(c));

            if (Math.abs(fnMeasure - tsMeasure) > 0.001)
                System.out.println("Font and state string measuring doesn't match!");
        }
}
```
