---
title: Text Formatting inside PDF 
linktitle: Text Formatting inside PDF
type: docs
weight: 30
url: /java/text-formatting-inside-pdf/
description: This page explains how to format text inside your PDF file. There are adding line Indent, adding text border, adding underline text, adding a border around the added text, text alignment for floating box contents and etc.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## How to add Line Indent to PDF

Aspose.PDF for Java offers SubsequentLinesIndent property into [TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions) class. Which can be used to specify line indent in PDF generation scenarios with TextFragment and Paragraphs collection.

Please use the following code snippet to use the property:

```java
public static void AddLineIndentToPDF() {
        // Create new document object
        Document document = new Document();
        Page page = document.getPages().add();

        TextFragment text = new TextFragment(
                "A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog.");

        // Initilize TextFormattingOptions for the text fragment and specify
        // SubsequentLinesIndent value
        TextFormattingOptions textOptions = new TextFormattingOptions();
        textOptions.setSubsequentLinesIndent(20);
        text.getTextState().setFormattingOptions(textOptions);

        page.getParagraphs().add(text);

        text = new TextFragment("Line2");
        page.getParagraphs().add(text);

        text = new TextFragment("Line3");
        page.getParagraphs().add(text);

        text = new TextFragment("Line4");
        page.getParagraphs().add(text);

        text = new TextFragment("Line5");
        page.getParagraphs().add(text);

        document.save(_dataDir + "SubsequentIndent_out.pdf");
    }
```

## How to add Text Border

The following code snippet shows, how to add a border to a text using TextBuilder and setting DrawTextRectangleBorder method of TextState:

```java
public static void AddTextBorder() {
    // Create new document object
    Document pdfDocument = new Document();
    // Get particular page
    Page pdfPage = pdfDocument.getPages().add();
    // Create text fragment
    TextFragment textFragment = new TextFragment("main text");
    textFragment.setPosition(new Position(100, 600));
    // Set text properties
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    textFragment.getTextState().setBackgroundColor (Color.getLightGray());
    textFragment.getTextState().setForegroundColor (Color.getRed());
    // Use setStrokingColor for drawing border (stroking) around text rectangle
    textFragment.getTextState().setStrokingColor (Color.getDarkRed());
    // Use setDrawTextRectangleBorder method to set value to true
    textFragment.getTextState().setDrawTextRectangleBorder(true);
    TextBuilder tb = new TextBuilder(pdfPage);
    tb.appendText(textFragment);
    // Save the document
    pdfDocument.save(_dataDir + "PDFWithTextBorder_out.pdf");
}
```

## How to add Underline Text

The following code snippet shows you how to add Underline text while creating a new PDF file.

```java
public static void AddUnderlineText(){
    // Create documentation object
    Document pdfDocument = new Document();
    // Add age page to PDF document
    Page page = pdfDocument.getPages().add();
    // Create TextBuilder for first page
    TextBuilder tb = new TextBuilder(page);
    // TextFragment with sample text
    TextFragment fragment = new TextFragment("Text with underline decoration");
    // Set the font for TextFragment
    fragment.getTextState().setFont (FontRepository.findFont("Arial"));
    fragment.getTextState().setFontSize (10);
    // Set the formatting of text as Underline
    fragment.getTextState().setUnderline(true);
    // Specify the position where TextFragment needs to be placed
    fragment.setPosition (new Position(10, 800));
    // Append TextFragment to PDF file
    tb.appendText(fragment);

    // Save resulting PDF document.
    pdfDocument.save(_dataDir + "AddUnderlineText_out.pdf");
}
```

## How to add Border Around Added Text

You have control over the look and feel of the text you add. The example below shows how to add a border around a piece of text that you have added by drawing a rectangle around it. Find out more about the [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) class.

```java
public static void AddBorderAroundAddedText() {
    PdfContentEditor editor = new PdfContentEditor();
    editor.bindPdf(_dataDir + "input.pdf");
    LineInfo lineInfo = new LineInfo();
    lineInfo.setLineWidth(2);
    lineInfo.setVerticeCoordinate (new float[] { 0, 0, 100, 100, 50, 100 });
    lineInfo.setVisibility(true);
    editor.createPolygon(lineInfo, 1, new java.awt.Rectangle(0, 0, 0, 0), "");

    // Save resulting PDF document.
    editor.save(_dataDir + "AddingBorderAroundAddedText_out.pdf");
}
```

## How to add NewLine feed

TextFragment doesn’t support line feed inside the text. However in order to add text with line feed, please use TextFragment with TextParagraph:

- use "\r\n" or Environment.NewLine in TextFragment instead of single “\n”;
- create TextParagraph object. It will add text with line splitting;
- add the TextFragment with TextParagraph.AppendLine;
- add the TextParagraph with TextBuilder.AppendParagraph.
Please use below code snippet.

```java
public static void AddNewLineFeed() {        
    Document pdfDocument = new Document();
    Page page = pdfDocument.getPages().add();

    // Initialize new TextFragment with text containing required newline markers
    TextFragment textFragment = new TextFragment("Applicant Name: " + System.lineSeparator() + " Joe Smoe");

    // Set text fragment properties if necessary
    textFragment.getTextState().setFontSize (12);
    textFragment.getTextState().setFont(FontRepository.findFont("DejaVu Serif"));
    textFragment.getTextState().setBackgroundColor (Color.getLightGray());
    textFragment.getTextState().setForegroundColor (Color.getRed());

    // Create TextParagraph object
    TextParagraph par = new TextParagraph();

    // Add new TextFragment to paragraph
    par.appendLine(textFragment);

    // Set paragraph position
    par.setPosition (new Position(100, 600));

    // Create TextBuilder object
    TextBuilder textBuilder = new TextBuilder(page);
    // Add the TextParagraph using TextBuilder
    textBuilder.appendParagraph(par);

    // Save resulting PDF document.
    pdfDocument.save(_dataDir + "AddNewLineFeed_out.pdf");
}
```

## How to add StrikeOut Text

The TextState class provides the capabilities to set formatting for TextFragments being placed inside PDF document. You can use this class to set text formatting as Bold, Italic, Underline and starting this release, the API has provided the capabilities to mark text formatting as Strikeout. Please try using the following code snippet to add TextFragment with Strikeout formatting.

Please use complete code snippet:

```java
public static void AddStrikeOutText(){
    // Open document
    Document pdfDocument = new Document();
    // Get particular page
    Page pdfPage = (Page)pdfDocument.getPages().add();

    // Create text fragment
    TextFragment textFragment = new TextFragment("main text");
    textFragment.setPosition (new Position(100, 600));

    // Set text properties
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("DejaVu Serif"));
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());
    textFragment.getTextState().setForegroundColor(Color.getRed());
    // use setStrikeOut method to enable StrikeOut Text
    textFragment.getTextState().setStrikeOut(true);
    // Mark text as Bold
    textFragment.getTextState().setFontStyle(FontStyles.Bold);

    // Create TextBuilder object
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // Append the text fragment to the PDF page
    textBuilder.appendText(textFragment);

    // Save resulting PDF document.
    pdfDocument.save(_dataDir + "AddStrikeOutText_out.pdf");        
}
```

## Apply Gradient Shading to the Text

Text formatting has been further enhanced in the API for text editing scenarios and now you can add text with pattern colorspace inside PDF document. com.aspose.pdf.Color Class has further been enhanced by introducing new methodw `setPatternColorSpace`, which can be used to specify shading colors for the text. This new method adds different Gradient Shading to the text e.g. Axial Shading, Radial (Type 3) Shading as shown in the following code snippet:

```java
public static void ApplyGradientShading() {
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("always print correctly");
    pdfDocument.getPages().accept(absorber);

    TextFragment textFragment = absorber.getTextFragments().get_Item(1);

    Color foregroundColor = new com.aspose.pdf.Color();
    foregroundColor.setPatternColorSpace(new GradientAxialShading(Color.getRed(), Color.getBlue()));

    // Create new color with pattern colorspace
    textFragment.getTextState().setForegroundColor (foregroundColor);

    textFragment.getTextState().setUnderline(true);

    pdfDocument.save(_dataDir + "text_out.pdf");
}
```

In order to apply a Radial Gradient, you can use `setPatternColorSpace` method equal with `GradientRadialShading(startingColor, endingColor)`in the above code snippet.

```java
public static void ApplyGradientShadingRadial() {
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("always print correctly");
    pdfDocument.getPages().accept(absorber);

    TextFragment textFragment = absorber.getTextFragments().get_Item(1);

    Color foregroundColor = new com.aspose.pdf.Color();
    foregroundColor.setPatternColorSpace(new GradientRadialShading(Color.getRed(), Color.getBlue()));

    // Create new color with pattern colorspace
    textFragment.getTextState().setForegroundColor (foregroundColor);

    textFragment.getTextState().setUnderline(true);

    pdfDocument.save(_dataDir + "text_out.pdf");
}
```

## How to align text to float content

Aspose.PDF supports setting text alignment for contents inside a Floating Box element. The alignment properties of Aspose.Pdf.FloatingBox instance can be used to achieve this as shown in the following code sample.

```java
public static void AlignTextToFloatContent() {
    Document pdfDocument = new Document();
    Page page = pdfDocument.getPages().add();

    FloatingBox floatBox = new FloatingBox(100, 100);
    floatBox.setVerticalAlignment(VerticalAlignment.Bottom);
    floatBox.setHorizontalAlignment (HorizontalAlignment.Right);
    floatBox.getParagraphs().add(new TextFragment("FloatingBox_bottom"));
    floatBox.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
    
    page.getParagraphs().add(floatBox);

    FloatingBox floatBox1 = new FloatingBox(100, 100);
    floatBox1.setVerticalAlignment(VerticalAlignment.Center);
    floatBox1.setHorizontalAlignment (HorizontalAlignment.Right);
    floatBox1.getParagraphs().add(new TextFragment("FloatingBox_center"));
    floatBox1.setBorder (new BorderInfo(BorderSide.All, Color.getBlue()));
    page.getParagraphs().add(floatBox1);

    FloatingBox floatBox2 = new FloatingBox(100, 100);
    floatBox2.setVerticalAlignment(VerticalAlignment.Top);
    floatBox2.setHorizontalAlignment (HorizontalAlignment.Right);
    floatBox2.getParagraphs().add(new TextFragment("FloatingBox_top"));
    floatBox2.setBorder (new BorderInfo(BorderSide.All, Color.getBlue()));
    page.getParagraphs().add(floatBox2);

    pdfDocument.save(_dataDir + "FloatingBox_alignment_review_out.pdf");        
}
```
