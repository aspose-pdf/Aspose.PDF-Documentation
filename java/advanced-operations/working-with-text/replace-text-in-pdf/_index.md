---
title: Replace Text in PDF using Java
linktitle: Replace Text in PDF
type: docs
weight: 40
url: /java/replace-text-in-pdf/
description: Learn more about various ways of replacing and removing text from PDF. Aspose.PDF allows replacing text in a particular region or with a regular expression.
lastmod: "2021-03-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Replace Text in all pages of PDF document

{{% alert color="primary" %}}

You can try to find in replace the text in the document using Aspose.PDF and get the results online at this [link](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

To replace text on all pages in a PDF document using [Aspose.PDF for Java](https://products.aspose.com/pdf/java):

1. First use [TextFragmentAbsorber](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) to find the particular phrase to be replaced.
1. Then, go through all [TextFragments](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber#getTextFragments--) to replace the text and change any other attributes.
1. Finally, save the output PDF using the Document class [save](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document#save--) method.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleReplaceText {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    public static void ReplaceTextOnAllPages() {
        Document pdfDocument = new Document(_dataDir+"sample.pdf");

        // Create TextAbsorber object to find all instances of the input search phrase
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Web");
        
        // Accept the absorber for first page of document
        pdfDocument.getPages().accept(textFragmentAbsorber);
        
        // Get the extracted text fragments into collection
        TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
        
        // Loop through the fragments
        for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
            // Update text and other properties
            textFragment.setText("World Wide Web");
            textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
            textFragment.getTextState().setFontSize(12);
            textFragment.getTextState().setForegroundColor(Color.getBlue());
            textFragment.getTextState().setBackgroundColor(Color.getGray());
        }
        // Save the updated PDF file
        pdfDocument.save(_dataDir+"Updated_Text.pdf");
    }
}
```

## Replace Text in particular page region

In order to replace text in a particular page region, first, we need to instantiate TextFragmentAbsorber object, specify page region using [TextSearchOptions.setRectangle](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextSearchOptions#setRectangle-com.aspose.pdf.Rectangle-) and then iterate through all the TextFragments to replace the text. Once these operations are completed, we only need to save the output PDF using the save method of the Document object.

 The following code snippet shows you how to replace text in all pages of PDF document.

```java
 public static void ReplaceTextInParticularRegion(){
    // load PDF file
    Document pdfDocument = new Document(_dataDir+"sample.pdf");

    // instantiate TextFragment Absorber object
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("PDF");

    // search text within page bound
    textFragmentAbsorber.getTextSearchOptions().setLimitToPageBounds(true);

    // specify the page region for TextSearch Options
    textFragmentAbsorber.getTextSearchOptions().setRectangle(new Rectangle(100, 700, 400, 770));

    // search text from first page of PDF file
    pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);

    // iterate through individual TextFragment
    for(TextFragment tf : textFragmentAbsorber.getTextFragments())
    {
        // replace text with "---"
        tf.setText("---");
    }

    // Save the updated PDF file
    pdfDocument.save(_dataDir+"Updated_Text.pdf");
}
```

## Replace Text Based on a Regular Expression

If you want to replace some phrases based on regular expression, you first need to find all the phrases matching that particular regular expression using TextFragmentAbsorber. You will have to pass the regular expression as a parameter to the TextFragmentAbsorber constructor. You also need to create TextSearchOptions object which specifies whether the regular expression is being used or not. Once you get the matching phrases in TextFragments, you need to loop through all of them and update as required. Finally, you need to save the updated PDF using the Save method of the Document object.

The following code snippet shows you how to replace text based on a regular expression.

```java
public static void ReplaceTextWithRegularExpression() {
    // load PDF file
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    // Create TextAbsorber object to find all instances of the input search phrase
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); 
    // like 1999-2000

    // Set text search option to specify regular expression usage
    TextSearchOptions textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(textSearchOptions);

    // Accept the absorber for first page of document
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // Get the extracted text fragments into collection
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

    // Loop through the fragments
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // Update text and other properties
        textFragment.setText("ABCD-EFGH");
        textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
    }

    // Save the updated PDF file
    pdfDocument.save(_dataDir + "Updated_Text.pdf");
}
```

## Replace fonts in existing PDF file

Aspose.PDF for Java supports the capability to replace text in PDF document. However, sometimes you have a requirement to only replace the font being used inside PDF document. So instead of replacing the text, only font being used is replaced. One of the overloads of TextFragmentAbsorber constructor accepts TextEditOptions object as an argument and we can use RemoveUnusedFonts value from TextEditOptions.FontReplace enumeration to accomplish our requirements.

The following code snippet shows how to replace the font inside PDF document.

```java
public static void ReplaceFonts() {
    // Instantiate Document object
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Search text fragments and set edit option as remove unused fonts
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(
            new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

    // Accept the absorber for all pages of document
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // traverse through all the TextFragments
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection)
    {
        String fontName = textFragment.getTextState().getFont().getFontName();
        // if the font name is ArialMT, replace font name with Arial
        if (fontName.equals("ArialMT")) {
            textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        }
    }

    // Save the updated PDF file
    pdfDocument.save(_dataDir + "Updated_Text.pdf");
}
```

### Use Non-English (Japanese) Font When Replacing Text

The following code snippet shows how to replace text with Japanese characters. Please note that to add Japanese text, you need to use a font which supports Japanese characters (for example MSGothic).

```java
public static void UseNonEnglishFontWhenReplacingText() {

    // Instantiate Document object
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Lets to change every of word "page" to some Japan text with specific font
    // TakaoMincho that might be installed in the OS
    // Also, it may be another font that supports hieroglyphs
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("page");

    // Create instance of Text Search options
    TextSearchOptions searchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(searchOptions);

    // Accept the absorber for all pages of document
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // Get the extracted text fragments into collection
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
    
    // Loop through the fragments
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // Update text and other properties
        textFragment.setText("ファイル");
        textFragment.getTextState().setFont(FontRepository.findFont("MSGothic"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
    }
    // Save the updated document
    pdfDocument.save(_dataDir + "Japanese_Text.pdf");
}
```

## Text Replacement should automatically re-arrange Page Contents

Aspose.PDF for Java supports the feature to search and replace text inside the PDF file. However recently some customers encountered issues during text replace when particular TextFragment is replaced with smaller contents and some extra spaces are displayed in resultant PDF or in case the TextFragment is replaced with some longer string, then words overlap existing page contents. So the requirement was to introduce a mechanism that once the text inside a PDF document is replaced, the contents should be re-arranged.

In order to cater above-stated scenarios, Aspose.PDF for Java has been enhanced so that no such issues appear when replacing text inside PDF file. The following code snippet shows how to replace text inside PDF file and the page contents should be re-arranged automatically.

```java
public static void RearrangeContent() {
    // Load source PDF file
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Create TextFragment Absorber object with regular expression
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[PDF,Web]");

    TextSearchOptions textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
    
    //You also can specify the ReplaceAdjustment.WholeWordsHyphenation option to wrap text on the next or current line 
    //if the current line becomes too long or short after replacement:
    //textFragmentAbsorber.getTextReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.WholeWordsHyphenation);

    // Accept the absorber for all pages of document
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // Get the extracted text fragments into collection
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

    // Replace each TextFragment
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // Set font of text fragment being replaced
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        // Set font size
        textFragment.getTextState().setFontSize(10);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
        // Replace the text with larger string than placeholder
        textFragment.setText("This is a larger string for the testing of this feature");
    }
    // Save resultant PDF
    pdfDocument.save(_dataDir + "RearrangeContentsUsingTextReplacement_out.pdf");
}
```

## Rendering Replaceable Symbols during PDF creation

Replaceable symbols are special symbols in a text string that can be replaced with corresponding content at run time. Replaceable symbols currently support by new Document Object Model of Aspose.PDF namespace are `$P`, `$p,` `\n`, `\r`. The `$p` and `$P` are used to deal with the page numbering at run time. `$p` is replaced with the number of the page where the current Paragraph class is in. `$P` is replaced with the total number of pages in the document. When adding [TextFragment](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TeXFragment) to the paragraphs collection of PDF documents, it does not support line feed inside the text. However in order to add text with a line feed, please use [TextFragment](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TeXFragment) with [TextParagraph](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextParagraph):

- use "\r\n" or Environment.NewLine in TextFragment instead of single "\n";
- create a TextParagraph object. It will add text with line splitting;
- add the TextFragment with TextParagraph.AppendLine;
- add the TextParagraph with TextBuilder.AppendParagraph.

```java
public static void RenderingReplaceableSymbols() {
    // load PDF file
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    Page page = pdfDocument.getPages().add();

    // Initialize new TextFragment with text containing required newline markers
    TextFragment textFragment = new TextFragment("Applicant Name: " + System.lineSeparator() + " Joe Smoe");

    // Set text fragment properties if necessary
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());
    textFragment.getTextState().setForegroundColor(Color.getRed());

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

    _dataDir = _dataDir + "RenderingReplaceableSymbols_out.pdf";
    pdfDocument.save(_dataDir);
}
```

## Replaceable symbols in Header/Footer area

Replaceable symbols can also be placed inside the Header/Footer section of PDF file. Please take a look over the following code snippet for details on how to add replaceable symbol in the footer section.

```java
public static void ReplaceableSymbolsInHeaderFooterArea() {
    Document doc = new Document();
    Page page = doc.getPages().add();

    MarginInfo marginInfo = new MarginInfo();
    marginInfo.setTop(90);
    marginInfo.setBottom(50);
    marginInfo.setLeft(50);
    marginInfo.setRight(50);

    // Assign the marginInfo instance to Margin property of sec1.PageInfo
    page.getPageInfo().setMargin(marginInfo);

    HeaderFooter hfFirst = new HeaderFooter();
    page.setHeader(hfFirst);
    hfFirst.getMargin().setLeft(50);
    hfFirst.getMargin().setRight(50);

    // Instantiate a Text paragraph that will store the content to show as header
    TextFragment t1 = new TextFragment("report title");
    t1.getTextState().setFont(FontRepository.findFont("Arial"));
    t1.getTextState().setFontSize(16);
    t1.getTextState().setForegroundColor(Color.getBlack());
    t1.getTextState().setFontStyle(FontStyles.Bold);
    t1.getTextState().setHorizontalAlignment(HorizontalAlignment.Center);
    t1.getTextState().setLineSpacing(5f);
    hfFirst.getParagraphs().add(t1);

    TextFragment t2 = new TextFragment("Report_Name");
    t2.getTextState().setFont(FontRepository.findFont("Arial"));
    t2.getTextState().setForegroundColor(Color.getBlack());
    t2.getTextState().setHorizontalAlignment(HorizontalAlignment.Center);
    t2.getTextState().setLineSpacing(5f);
    t2.getTextState().setFontSize(12);
    hfFirst.getParagraphs().add(t2);

    // Create a HeaderFooter object for the section
    HeaderFooter hfFoot = new HeaderFooter();

    // Set the HeaderFooter object to odd & even footer
    page.setFooter(hfFoot);
    hfFoot.getMargin().setLeft(50);
    hfFoot.getMargin().setRight(50);

    // Add a text paragraph containing current page number of total number of pages
    TextFragment t3 = new TextFragment("Generated on test date");
    TextFragment t4 = new TextFragment("report name ");
    TextFragment t5 = new TextFragment("Page $p of $P");

    // Instantiate a table object
    Table tab2 = new Table();

    // Add the table in paragraphs collection of the desired section
    hfFoot.getParagraphs().add(tab2);

    // Set with column widths of the table
    tab2.setColumnWidths("165 172 165");

    // Create rows in the table and then cells in the rows
    Row row3 = tab2.getRows().add();

    row3.getCells().add();
    row3.getCells().add();
    row3.getCells().add();

    // Set the vertical allignment of the text as center alligned
    row3.getCells().get_Item(0).setAlignment(HorizontalAlignment.Left);
    row3.getCells().get_Item(1).setAlignment(HorizontalAlignment.Center);
    row3.getCells().get_Item(2).setAlignment(HorizontalAlignment.Right);

    row3.getCells().get_Item(0).getParagraphs().add(t3);
    row3.getCells().get_Item(1).getParagraphs().add(t4);
    row3.getCells().get_Item(2).getParagraphs().add(t5);

    Table table = new Table();

    table.setColumnWidths("33% 33% 34%");
    table.setDefaultCellPadding(new MarginInfo());
    table.getDefaultCellPadding().setTop(10);
    table.getDefaultCellPadding().setBottom(10);

    // Add the table in paragraphs collection of the desired section
    page.getParagraphs().add(table);

    // Set default cell border using BorderInfo object
    table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1f));

    // Set table border using another customized BorderInfo object
    table.setBorder(new BorderInfo(BorderSide.All, 1f));

    table.setRepeatingRowsCount(1);

    // Create rows in the table and then cells in the rows
    Row row1 = table.getRows().add();

    row1.getCells().add("col1");
    row1.getCells().add("col2");
    row1.getCells().add("col3");
    String CRLF = "\r\n";

    for (int i = 0; i <= 10; i++) {
        Row row = table.getRows().add();
        row.setRowBroken(true);
        for (int c = 0; c <= 2; c++) {
            Cell c1;
            if (c == 2)
                c1 = row.getCells().add(
                        "Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a"
                                + CRLF
                                + "daily basis to ensure it contains the most up to date versions of each of our Java components. "
                                + CRLF
                                + "daily basis to ensure it contains the most up to date versions of each of our Java components. "
                                + CRLF
                                + "Using Aspose.Total for Java developers can create a wide range of applications.");
            else
                c1 = row.getCells().add("item1" + c);
            c1.setMargin(new MarginInfo());
            c1.getMargin().setLeft(30);
            c1.getMargin().setTop(10);
            c1.getMargin().setBottom(10);
        }
    }

    _dataDir = _dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
    doc.save(_dataDir);
}
```

## Remove All Text from PDF Document

### Remove All Text using Operators

In some text operation, you need to remove all text from PDF document and for that, you need to set found text as empty string value usually. The point is that changing the text for multitude text fragments invokes a number of checking and text position adjustment operations. They are essential in the text editing scenarios. The difficulty is that you cannot determine how many text fragments will be removed in the scenario where they are processed in a loop.

Therefore, we recommend using another approach for the scenario of removing all text from PDF pages. Please consider the following code snippet that works very fast.

```java
public static void RemoveAllTextUsingOperators() {
    // Open document
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Loop through all pages of PDF Document
    for (int i = 1; i <= pdfDocument.getPages().size(); i++) {
        Page page = pdfDocument.getPages().get_Item(i);
        OperatorSelector operatorSelector = new OperatorSelector(new com.aspose.pdf.operators.TextShowOperator());
        // Select all text on the page
        page.getContents().accept(operatorSelector);
        // Delete all text
        page.getContents().delete(operatorSelector.getSelected());
    }
    // Save the document
    pdfDocument.save(_dataDir + "RemoveAllText_out.pdf");
}
```
