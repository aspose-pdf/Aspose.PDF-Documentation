---
title: Add Text to PDF file using Java
linktitle: Add Text to PDF file
type: docs
weight: 10
url: /java/add-text-to-pdf-file/
description: This article describes various aspects of working with text in Aspose.PDF. Learn how to add text to PDF, add HTML fragments, or use custom OTF fonts.
lastmod: "2021-03-01"
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

## How to add transparent Text in PDF

A PDF file contains Image, Text, Graph, attachment, Annotations objects and while creating TextFragment, you can set foreground, background color information as well as text formatting. Aspose.PDF for Java supports the feature to add text with Alpha color channel.

The following code snippet shows how to add text with transparent color.

```java
public static void AddingTransparentText() {
        // create Document instance
        Document document = new Document(_dataDir + "sample.pdf");

        Page page = document.getPages().get_Item(1);

        for (int i = 10; i < 100; i += 10) {
            // create TextFragment instance with sample value
            TextFragment text = new TextFragment(
                    "Aspose.PDF for Java transparent text transparent text transparent text");
            // create color object from Alpha channel
            Color color = Color.fromArgb(i, 0, 255, 0);
            // set color information for text instance
            text.getTextState().setForegroundColor(color);
            // add text to paragraphs collection of page instance
            page.getParagraphs().add(text);
        }

        // Save resulting PDF document.
        document.save(_dataDir + "sample_addText_out.pdf");
    }
```

## Add HTML String using DOM

The aspose.pdf.generator.text class contains a property called IsHtmlTagSupported which makes it possible to add HTML tags/contents into PDF files. The added content is rendered in native HTML tags instead of appearing as a simple text string. To support a similar feature in the new Document Object Model (DOM) of the Aspose.Pdf namespace, the HtmlFragment class has been introduced.

The [HtmlFragment](https://apireference.aspose.com/java/pdf/com.aspose.pdf/htmlfragment) instance can be used to specify the HTML contents which should be placed inside the PDF file. Similar to TextFragment, HtmlFragment is a paragraph level object and can be added to the Page object’s paragraphs collection. The following code snippets shows the steps to place HTML contents inside PDF file using DOM approach.

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

Following code snippet demonstrate steps how to add HTML ordered lists into document:

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

You can also set HTML string formatting using setTextState() method as following:

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

In case if you set some text attributes values via html markup and then provide the same values in setTextState() properties they will overwrite html parameters by properties form setTextState() instance. The following code snippets shows described behavior.

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

In a footnote referencing system, indicate a reference by:

- putting a small number above the line of type directly following the source material. This number is called a note identifier. It sits slightly above the line of text.
- putting the same number, followed by a citation of your source, at the bottom of the page. Footnoting should be numerical and chronological: the first reference is 1, the second is 2, and so on. The advantage of footnoting is that the reader can simply cast their eyes down the page to discover the source of a reference which interests them.

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
        text = new TextFragment("Aspose.Pdf for .NET");
        // set FootNote for second text fragment
        text.setFootNote(new Note("foot note for test text 2"));
        // add second text fragment to paragraphs collection of PDF file
        page.getParagraphs().add(text);

        document.save(_dataDir + "sample_footnote.pdf");
    }
```

Please follow the steps specified below to create a FootNote:

- Create a Document instance
- Create a Page object
- Create a TextFragment object
- Create a Note instance and pass it’s value to TextFragment.FootNote property
- Add TextFragment to paragraphs collection of page instance

### Custom line style for FootNote

The following example demonstrates how to add Footnotes to the bottom of the PDF page and define custom line style.

```java
public static void CustomFootNote_Line() {
        // create Document instance
        Document doc = new Document();
        // add page to pages collection of PDF
        Page page = doc.getPages().add();
        // create GraphInfo object
        GraphInfo graph = new GraphInfo();
        // set line width as 2
        graph.setLineWidth(2);
        // set the color for graph object
        graph.setColor(Color.getRed());
        // set dash array value as 3
        graph.setDashArray(new int[] { 3 });
        // set dash phase value as 1
        graph.setDashPhase(1);
        // set footnote line style for page as graph
        page.setNoteLineStyle(graph);
        // create TextFragment instance
        TextFragment text = new TextFragment("Hello World");
        // set FootNote value for TextFragment
        text.setFootNote(new Note("foot note for test text 1"));
        // add TextFragment to paragraphs collection of first page of document
        page.getParagraphs().add(text);
        // create second TextFragment
        text = new TextFragment("Aspose.Pdf for .NET");
        // set FootNote for second text fragment
        text.setFootNote(new Note("foot note for test text 2"));
        // add second text fragment to paragraphs collection of PDF file
        page.getParagraphs().add(text);
        // save the PDF file
        doc.save(_dataDir + "CustomFootNote_Line.pdf");
    }
```

### Customize FootNote label

By default, the FootNote number is incremental starting from 1. However we may have a requirement to set custom FootNote label. In order to accomplish this requirement, please try using following code snippet:

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
        text = new TextFragment("Aspose.Pdf for .NET");
        // set FootNote for second text fragment
        text.setFootNote(new Note("foot note for test text 2"));
        // add second text fragment to paragraphs collection of PDF file
        page.getParagraphs().add(text);

        document.save(_dataDir + "sample_footnote.pdf");
    }
```

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
        text = new TextFragment("Aspose.Pdf for .NET");
        // set FootNote for second text fragment
        text.setFootNote(new Note("foot note for test text 2"));
        // add second text fragment to paragraphs collection of PDF file
        page.getParagraphs().add(text);

        document.save(_dataDir + "sample_footnote.pdf");
    }
```

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

In earlier release versions, the Footnote support was provided but it was only applicable to TextFragment object. The following code snippet shows the steps to add Footnote to TextFragment object and then add Image and Table object to paragraphs collection of Footnote section.

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

An EndNote is source citation that refers the readers to a specific place at the end of the paper where they can find out the source of the information or words quoted or mentioned in the paper.
When using Endnotes, your quoted or paraphrased sentence or summarized material is followed by a superscript number.

The following example demonstrates how to add an Endnote in PDF page.

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

## Specify character Spacing when adding Text

A text can be added inside paragraphs collection of PDF files using TextFragment instance or by using TextParagraph object and even you can stamp the text inside PDF by using TextStamp class.
Please take a look at the following approaches to fulfill this requirement.

The following approaches show the steps to specify character spacing when adding text inside a PDF document.

### Using TextBuilder and TextFragment

```java
   // Specify Character Spacing when adding Text using TextBuilder and TextFragment
    public static void CharacterSpacing01(){
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

## Add Rotated Text inside PDF Document

Aspose.PDF for Java provides setRotation() method in TextState Class, which helps specifying different rotation angles of text inside PDF document. In various scenarios, text rotation can be an important requirement and in order to implement this functionality, please check following code snippet:

```java
   public static void TextFragmentTests_Rotated() {

        // Open document
        Document pdfDocument = new Document();
        // Get particular page
        Page pdfPage = pdfDocument.getPages().add();

        // Create rotated text fragment
        TextFragment tf = new TextFragment("rotated text");
        tf.setPosition(new Position(200, 600));

        // Set text properties
        tf.getTextState().setFontSize(12);
        tf.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        tf.getTextState().setBackgroundColor(com.aspose.pdf.Color.getLightGray());
        tf.getTextState().setForegroundColor(com.aspose.pdf.Color.getRed());
        tf.getTextState().setRotation(45);
        tf.getTextState().setUnderline(true);

        // Create TextBuilder object
        TextBuilder textBuilder = new TextBuilder(pdfPage);
        // Append the text fragment to the PDF page
        textBuilder.appendText(tf);

        // Save document
        pdfDocument.save(_dataDir + "TextFragmentTests_Rotated.pdf");
    }
```

## Loading Font from Stream

The following code snippet shows how to load Font from Stream object when adding text to PDF document.

```java
    public static void LoadingFontFromStream() throws FileNotFoundException {

        String fontFile = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf";

        // Load input PDF file
        Document doc = new Document(_dataDir + "input.pdf");
        // Create text builder object for first page of document
        TextBuilder textBuilder = new TextBuilder(doc.getPages().get_Item(1));
        // Create text fragment with sample string
        TextFragment textFragment = new TextFragment("Hello world");

        if (fontFile != "") {
            // Load the TrueType font into stream object
            FileInputStream fontStream = new FileInputStream(fontFile);
            // Set the font name for text string
            textFragment.getTextState().setFont(FontRepository.openFont(fontStream, FontTypes.TTF));
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

Aspose.PDF for Java offers the feature to use Custom/TrueType fonts while creating/manipulating PDF file contents so that file contents are displayed using contents other than default system fonts.

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
