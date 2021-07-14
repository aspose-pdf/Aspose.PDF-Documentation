---
title: Rotate Text Inside PDF using Java
linktitle: Rotate Text Inside PDF
type: docs
weight: 50
url: /java/rotate-text-inside-pdf/
description: Learn different ways to rotate text to PDF. Aspose.PDF allows you to rotate text to any angle, rotate text fragment or a whole paragraph.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Rotate Text Inside PDF using Rotation Property

By using the [setRotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentState#setRotation-double-) method of [TextFragment](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) Class, you can rotate text at various angles. The text rotation can be used in different scenarios of document generation. You can specify the rotation angle in degrees to rotate the text as per your requirement. Please check the following different scenarios, in which you can implement text rotation.

## Implement Rotation using TextFragment and TextBuilder

```java
public class ExampleRotateText {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ImplementRotationUsingTextFragmentAndTextBuilder() {

        // Initialize document object
        Document pdfDocument = new Document();
        // Get particular page
        Page pdfPage = pdfDocument.getPages().add();
        // Create text fragment
        TextFragment textFragment1 = new TextFragment("main text");
        textFragment1.setPosition(new Position(100, 600));

        // Set text properties
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

        // Create rotated text fragment
        TextFragment textFragment2 = new TextFragment("rotated text");
        textFragment2.setPosition(new Position(200, 600));
        // Set text properties
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment2.getTextState().setRotation(45);

        // Create rotated text fragment
        TextFragment textFragment3 = new TextFragment("rotated text");
        textFragment3.setPosition(new Position(300, 600));

        // Set text properties
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setRotation(90);

        // create TextBuilder object
        TextBuilder textBuilder = new TextBuilder(pdfPage);
        // Append the text fragment to the PDF page
        textBuilder.appendText(textFragment1);
        textBuilder.appendText(textFragment2);
        textBuilder.appendText(textFragment3);

        // Save document
        pdfDocument.save(_dataDir + "TextFragmentTests_Rotated1_out.pdf");
    }
}
```

## Implement Rotation using TextParagraph and TextBuilder (Rotated Fragments)

```java
public static void ImplementRotationUsingTextParagraphAndTextBuilder_RotatedFragments() {

    // Initialize document object
    Document pdfDocument = new Document();
    // Get particular page
    Page pdfPage = (Page) pdfDocument.getPages().add();
    TextParagraph paragraph = new TextParagraph();
    paragraph.setPosition(new Position(200, 600));
    // Create text fragment
    TextFragment textFragment1 = new TextFragment("rotated text");
    // Set text properties
    textFragment1.getTextState().setFontSize(12);
    textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    // Set rotation
    textFragment1.getTextState().setRotation(45);

    // Create text fragment
    TextFragment textFragment2 = new TextFragment("main text");
    // Set text properties
    textFragment2.getTextState().setFontSize(12);
    textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // Create text fragment
    TextFragment textFragment3 = new TextFragment("another rotated text");
    // Set text properties
    textFragment3.getTextState().setFontSize(12);
    textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    // Set rotation
    textFragment3.getTextState().setRotation(-45);

    // Append the text fragments to the paragraph
    paragraph.appendLine(textFragment1);
    paragraph.appendLine(textFragment2);
    paragraph.appendLine(textFragment3);
    // Create TextBuilder object
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // Append the text paragraph to the PDF page
    textBuilder.appendParagraph(paragraph);
    // Save document
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated2_out.pdf");
}
```

## Implement Rotation using TextFragment and Page.Paragraphs

```csharp
public static void ImplementRotationUsingTextFragmentAndPageParagraphs() {
    // Initialize document object
    Document pdfDocument = new Document();
    // Get particular page
    Page pdfPage = (Page) pdfDocument.getPages().add();
    // Create text fragment
    TextFragment textFragment1 = new TextFragment("main text");
    // Set text properties
    textFragment1.getTextState().setFontSize(12);
    textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // Create text fragment
    TextFragment textFragment2 = new TextFragment("rotated text");

    // Set text properties
    textFragment2.getTextState().setFontSize(12);
    textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // Set rotation
    textFragment2.getTextState().setRotation(315);

    // Create text fragment
    TextFragment textFragment3 = new TextFragment("rotated text");
    // Set text properties
    textFragment3.getTextState().setFontSize(12);
    textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // Set rotation
    textFragment3.getTextState().setRotation(270);
    pdfPage.getParagraphs().add(textFragment1);
    pdfPage.getParagraphs().add(textFragment2);
    pdfPage.getParagraphs().add(textFragment3);

    // Save document
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated3_out.pdf");
    }
```

## Implement Rotation using TextParagraph and TextBuilder (Whole Paragraph Rotated)

```java
public static void ImplementRotationUsingTextParagraphAndTextBuilder() {

    // Initialize document object
    Document pdfDocument = new Document();
    // Get particular page
    Page pdfPage = pdfDocument.getPages().add();
    for (int i = 0; i < 4; i++) {
        TextParagraph paragraph = new TextParagraph();
        paragraph.setPosition(new Position(200, 600));
        // Specify rotation
        paragraph.setRotation(i * 90 + 45);
        // Create text fragment
        TextFragment textFragment1 = new TextFragment("Paragraph Text");
        // Create text fragment
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment1.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment1.getTextState().setForegroundColor(Color.getBlue());

        // Create text fragment
        TextFragment textFragment2 = new TextFragment("Second line of text");
        // Set text properties
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment2.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment2.getTextState().setForegroundColor(Color.getBlue());

        // Create text fragment
        TextFragment textFragment3 = new TextFragment("And some more text...");
        // Set text properties
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment3.getTextState().setForegroundColor(Color.getBlue());
        textFragment3.getTextState().setUnderline(true);

        paragraph.appendLine(textFragment1);
        paragraph.appendLine(textFragment2);
        paragraph.appendLine(textFragment3);
        // Create TextBuilder object
        TextBuilder textBuilder = new TextBuilder(pdfPage);
        // Append the text fragment to the PDF page
        textBuilder.appendParagraph(paragraph);
    }
    // Save document
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated4_out.pdf");
}
```
