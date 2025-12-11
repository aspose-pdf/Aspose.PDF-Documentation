---
title: Formatting PDF Document
linktitle: Formatting PDF Document
type: docs
weight: 20
url: /java/formatting-pdf-document/
description: Format the PDF Document with Aspose.PDF for Java. Use the next code snippet to resolve your tasks.
lastmod: "2025-02-17"
TechArticle: true
AlternativeHeadline: Guide on managing document window and page display properties using the Aspose.PDF library in Java
Abstract: The article provides a comprehensive guide on managing document window and page display properties using the Aspose.PDF library in Java. It details how to retrieve and set various PDF document properties, such as window centering, reading direction, title display, and interface visibility, using methods from the `Document` class. The article includes code snippets demonstrating how to implement these changes programmatically. Additionally, it covers embedding fonts in existing and new PDF files to ensure consistent document appearance across different platforms. This involves using the `Font` class to embed fonts fully or partially, which is useful for reducing file size without compromising on font integrity for specific uses like logos. The article further explains how to set a default font name when saving a PDF, ensuring that missing fonts in a document are replaced with a specified default font. It also includes instructions for extracting all fonts from a PDF and managing the zoom factor using the `GoToAction` object for precise control over document presentation.
SoftwareApplication: java
---

## Get Document Window and Page Display Properties

This topic helps you understand how to get the properties of the document window, viewer application, and how pages are displayed.

To set these different properties, open the PDF file using the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class. You can now get the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object's methods, such as

- [IsCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isCenterWindow--) – Center the document window on screen. Default: false.
- [SetDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-) – Reading order. This determines how pages are laid out when displayed side by side. Default: left to right.
- [isDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isDisplayDocTitle--) – Display the document title in the document window title bar. Default: false (the title is displayed).
- [setHideMenuBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideMenubar-boolean-) – Hide or display the document window's menu bar. Default: false (menu bar is displayed).
- [setHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideToolBar-boolean-) – Hide or display the document window's toolbar. Default: false (toolbar is displayed).
- [setHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideWindowUI-boolean-) – Hide or display document window elements like scroll bars. Default: false (UI elements are displayed).
- [setNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setNonFullScreenPageMode-int-) – How the document is displayed when it is not displayed in full-page mode.
- [setPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageLayout-int-) – The page layout.
- [setPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageMode-int-) – How the document is displayed when first opened. The options are show thumbnails, full-screen, show attachment panel.

The following code snippet shows you how to get the properties using the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleFormatting {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void GetDocumentWindowAndPageDisplayProperties() {

    // Open document
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Get different document properties
    // Position of document's window - Default: false
    System.out.printf("CenterWindow : " + pdfDocument.isCenterWindow());

    // Predominant reading order; determine the position of page
    // when displayed side by side - Default: L2R
    System.out.printf("Direction :- " + pdfDocument.getDirection());

    // Whether window's title bar should display document title.
    // If false, title bar displays PDF file name - Default: false
    System.out.printf("DisplayDocTitle :- " + pdfDocument.isDisplayDocTitle());

    // Whether to resize the document's window to fit the size of
    // first displayed page - Default: false
    System.out.printf("FitWindow :- " + pdfDocument.isFitWindow());

    // Whether to hide menu bar of the viewer application - Default: false
    System.out.printf("HideMenuBar :-" + pdfDocument.isHideMenubar());

    // Whether to hide tool bar of the viewer application - Default: false
    System.out.printf("HideToolBar :-" + pdfDocument.isHideToolBar());

    // Whether to hide UI elements like scroll bars
    // and leaving only the page contents displayed - Default: false
    System.out.printf("HideWindowUI :-" + pdfDocument.isHideWindowUI());

    // The document's page mode. How to display document on exiting
    // full-screen mode.
    System.out.printf("NonFullScreenPageMode :-" + pdfDocument.getNonFullScreenPageMode());

    // The page layout i.e. single page, one column
    System.out.printf("PageLayout :-" + pdfDocument.getPageLayout());

    // How the document should display when opened.
    System.out.printf("pageMode :-" + pdfDocument.getPageMode());

  }

```
## Set Document Window and Page Display Properties

This topic explains how to set the properties of the document window, viewer application and page display.

To set these different properties:

1. Open the PDF file using the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class.
1. Set the Document object's properties.
1. Save the updated PDF file using the Save method.

Properties available are:

- [setCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setCenterWindow-boolean-)
- [setDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-)
- [setDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDisplayDocTitle-boolean-)
- [setFitWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setFitWindow-boolean-)
- [setHideMenuBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideMenubar-boolean-)
- [setHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideToolBar-boolean-)
- [setHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideWindowUI-boolean-)
- [setNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setNonFullScreenPageMode-int-)
- [setPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageLayout-int-)
- [setPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageMode-int-)

The following code snippet shows you how to set the properties using the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class.

```java
  public static void SetDocumentWindowAndPageDisplayProperties() {

    // Open document
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Set different document properties
    // specify to position document's window - Default: false
    pdfDocument.setCenterWindow(true);

    // Predominant reading order; determine the position of page
    // when displayed side by side - Default: L2R
    pdfDocument.setDirection(com.aspose.pdf.Direction.R2L);

    // Specify whether window's title bar should display document title
    // if false, title bar displays PDF file name - Default: false
    pdfDocument.setDisplayDocTitle(true);

    // Specify whether to resize the document's window to fit the size of
    // first displayed page - Default: false
    pdfDocument.setFitWindow(true);

    // Specify whether to hide menu bar of the viewer application - Default:
    // false
    pdfDocument.setHideMenubar(true);

    // Specify whether to hide tool bar of the viewer application - Default:
    // false
    pdfDocument.setHideToolBar(true);

    // Specify whether to hide UI elements like scroll bars
    // and leaving only the page contents displayed - Default: false
    pdfDocument.setHideWindowUI(true);

    // Document's page mode. specify how to display document on exiting
    // full-screen mode.
    pdfDocument.setNonFullScreenPageMode(com.aspose.pdf.PageMode.UseOC);

    // Specify the page layout i.e. single page, one column
    pdfDocument.setPageLayout(com.aspose.pdf.PageLayout.TwoColumnLeft);

    // Specify how the document should display when opened
    // i.e. show thumbnails, full-screen, show attachment panel
    pdfDocument.setPageMode(com.aspose.pdf.PageMode.UseThumbs);

    // Save updated PDF file
    pdfDocument.save(_dataDir + "UpdatedFile_output.pdf");

  }
```
## Embedding Fonts in an Existing PDF File

PDF readers support [a core of 14 fonts](http://en.wikipedia.org/wiki/Portable_Document_Format#Fonts) so that documents can be displayed the same way regardless of the platform the document is displayed on. When a PDF contains a font that is outside the core fonts, embed the font to avoid font substitution.

Aspose.PDF for Java supports font embedding in existing PDF documents. You can embed a complete font or a subset. To embed the font:

1. Open an existing PDF file using the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class.
1. Use the [com.aspose.pdf.Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) class to embed the font.
   1. The setEmbedded(true) method embeds the full font.
   1. The pageFont.isSubset(true) method embeds a subset of the font.

A font subset embeds only the characters that are used and is useful where fonts are used for short sentences or slogans, for example where a corporate font is used for a logo, but not for the body text. Using a subset reduces the file size of the output PDF.

However, if a custom font is used for the body text, embed it in its entirety.

The following code snippet shows how to embed a font in a PDF file.
```java
public static void EmbeddingFontsInAnExistingPDFFile() {
    // Open document
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    // Iterate through all the pages
    for (com.aspose.pdf.Page page : (Iterable<com.aspose.pdf.Page>) pdfDocument.getPages()) {
      if (page.getResources().getFonts() != null) {
        for (com.aspose.pdf.Font pageFont : (Iterable<com.aspose.pdf.Font>) page.getResources().getFonts()) {
          // Check if font is already embedded
          if (!pageFont.isEmbedded())
            pageFont.setEmbedded(true);
        }
      }

      // Check for the Form objects
      for (com.aspose.pdf.XForm form : (Iterable<com.aspose.pdf.XForm>) page.getResources().getForms()) {
        if (form.getResources().getFonts() != null) {
          for (com.aspose.pdf.Font formFont : (Iterable<com.aspose.pdf.Font>) form.getResources().getFonts()) {
            // Check if the font is embedded
            if (!formFont.isEmbedded())
              formFont.setEmbedded(true);
          }
        }
      }
    }
    // Save updated PDF file
    pdfDocument.save(_dataDir + "UpdatedFile_output.pdf");
  }
```

## Embedding Fonts while creating PDF

If you need to use any font other than the 14 core fonts supported by Adobe Reader, then you must embed the font description while generating a PDF file. If font information is not embedded, Adobe Reader will take it from the Operating System if it's installed over the system, or it will construct a substitute font according to the font descriptor in the PDF. Please note that embedded font must be installed on the host machine i.e. in case of the following code ‘Univers Condensed’ font is installed over the system.

We use the property setEmbedded of [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) class to embed the font information into PDF file. Setting the value of this property to ‘true’ will embed the complete font file into the PDF, knowing the fact that it will increase the PDF file size. Following is the code snippet that can be used to embed the font information into PDF.

```java
public static void EmbeddingFontsWhileCreatingPDF() {

    // Instantiate PDF object by calling its empty constructor
    com.aspose.pdf.Document document = new com.aspose.pdf.Document();

    // Create a section in the Pdf object
    com.aspose.pdf.Page page = document.getPages().add();

    com.aspose.pdf.TextFragment fragment = new com.aspose.pdf.TextFragment("");

    com.aspose.pdf.TextSegment segment = new com.aspose.pdf.TextSegment(" This is a sample text using Custom font.");
    com.aspose.pdf.TextState ts = new com.aspose.pdf.TextState();
    ts.setFont(FontRepository.findFont("Univers Condensed"));
    ts.getFont().setEmbedded(true);
    segment.setTextState(ts);
    fragment.getSegments().add(segment);
    page.getParagraphs().add(fragment);

    // Save updated PDF file
    document.save(_dataDir + "UpdatedFile_output.pdf");
  }
```
## Set Default Font Name while Saving PDF

When a PDF document contains fonts, which are not available in the document itself and on the device, API replaces these fonts with the default font. When a font is available (is installed on the device or is embedded into the document), output PDF should have the same font (should not be replaced with default font). The value of the default font should contain the name of the font (not the path to the font files). We have implemented a feature to set default font name while saving a document as PDF. Following code snippet can be used to set default font:

```java
public static void SetDefaultFontNameWhileSavingPDF() {

    // Load an exisiting PDF document
    Document document = new Document("input.pdf");

    String newName = "Arial";

    // Initialize save options for PDF format
    PdfSaveOptions ops = new PdfSaveOptions();

    // Set default font name
    ops.setDefaultFontName(newName);

    // Save PDF file
    document.save(_dataDir + "output_out.pdf", ops);
  }
```

## Get All Fonts from PDF Document

In case you want to get all fonts from a PDF document, you can use **Document.getFontUtilities().getAllFonts()** method provided in [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class. Please check following code snippet in order to get all fonts from an existing PDF document:

```java
public static void GetAllFontsFromPDFDocument() {

    // Load an exisiting PDF document
    Document document = new Document(_dataDir + "sample.pdf");

    // Get all fonts from document
    com.aspose.pdf.Font[] fonts = document.getFontUtilities().getAllFonts();
    for (com.aspose.pdf.Font f : fonts) {
      System.out.println(f.getFontName());
    }
  }
```


### Get Warnings for Font Substitution

Aspose.PDF for Java provides methods to get notifications about font substitution for handling font substitution cases. 
The code snippets below show how to use corresponding functionality.

```java
private static void NotificationFontSubstitution()
{
    // Open PDF document
        try (Document document = new Document(dataDir + "input.pdf"))
        {
            // Attach the FontSubstitution event handler
            document.FontSubstitution.add(new Document.FontSubstitutionHandler() {
                public void invoke(Font font, Font newFont) {
                    // Handle the font substitution event here, as example - print substituted FontNames into console
                    System.out.println("Warning: Font " + font.getFontName() + " was substituted with another font -> "
                            + newFont.getFontName());
                }
            });

            // Save PDF document
            document.save(dataDir + "NotificationFontSubstitution_out.pdf");
        }
}
```


### Improve Fonts Embedding using FontSubsetStrategy

The feature to embed the fonts as a subset can be accomplished by using the isSubset/setSubset property, but sometimes you want to reduce a fully embedded font set to only subsets that are used in the document. 
Document has property FontUtilities which includes method SubsetFonts(FontSubsetStrategy subsetStrategy). In the method subsetFonts(), the parameter subsetStrategy helps to tune the subset strategy. FontSubsetStrategy supports two following variants of font subsetting.

- SubsetAllFonts - This will subset all fonts, used in a document.
- SubsetEmbeddedFontsOnly - This will subset only those fonts which are fully embedded into the document.

Following code snippet shows how to set FontSubsetStrategy:

```java

private static void setFontSubsetStrategy()
{
    // Open PDF document
        try (Document document = new Document(dataDir + "input.pdf"))
        {
            // All fonts will be embedded as subset into document in case of SubsetAllFonts.
            document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetAllFonts);

            // Font subset will be embedded for fully embedded fonts but fonts which are not embedded into document will not be affected.
            document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);

            // Save PDF document
            document.save(dataDir + "SetFontSubsetStrategy_out.pdf");
        }
}
```

## Get-Set Zoom Factor of PDF File

Sometimes, you want to set or get the zoom factor of a PDF document. You can easily accomplish this requirement with Aspose.PDF.

The [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToAction) object allows you to get the zoom value associated with a PDF file. Similarly, it can be used to set a file's Zoom factor.

```java
  public static void GetSetZoomFactorOfPDFFile() {
    // Load an exisiting PDF document
    Document document = new Document(_dataDir + "sample.pdf");
    double zoom = .5;
    // setting zoom factor of document
    GoToAction actionzoom = new GoToAction(new XYZExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getWidth(),
        document.getPages().get_Item(1).getMediaBox().getHeight(), zoom));

    // setting action to fit to page width zoom
    GoToAction actionFittoWidth = new GoToAction(new FitHExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getWidth()));

    // setting action to fit to page height zoom
    GoToAction actionFittoHeight = new GoToAction(new FitVExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getHeight()));

    document.setOpenAction(actionzoom);
    document.setOpenAction(actionFittoWidth);
    document.setOpenAction(actionFittoHeight);
```

The following code snippet shows how to get the Zoom factor of a PDF file.

```java
    // Instantiate new Document object
    Document doc1 = new Document(_dataDir + "Zoomed_actionzoom.pdf");
    // Create GoToAction object
    GoToAction action = (GoToAction) doc1.getOpenAction();
    // Get the Zoom factor of PDF file
    System.out.println(((XYZExplicitDestination) action.getDestination()).getZoom());

    // Save updated PDF file
    document.save(_dataDir + "UpdatedFile_output.pdf");
  }
}
```
