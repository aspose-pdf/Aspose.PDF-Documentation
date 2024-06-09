---
title: Formatting PDF Document 
linktitle: Formatting PDF Document
type: docs
weight: 20
url: /php-java/formatting-pdf-document/
description: Format the PDF Document with Aspose.PDF for PHP via Java. Use the next code snippet to resolve your tasks.
lastmod: "2024-06-05"
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

```php  

    // Open document
    $document = new Document($inputFile);

    // Get different document properties
    // Position of document's window - Default: false
    $responseData = "CenterWindow : " . $document->isCenterWindow();

    // Predominant reading order; determine the position of page
    // when displayed side by side - Default: L2R
    $responseData = $responseData . "Direction : " . $document->getDirection();

    // Whether window's title bar should display document title.
    // If false, title bar displays PDF file name - Default: false
    $responseData = $responseData . "DisplayDocTitle : " . $document->isDisplayDocTitle();

    // Whether to resize the document's window to fit the size of
    // first displayed page - Default: false
    $responseData = $responseData . "FitWindow : " . $document->isFitWindow();

    // Whether to hide menu bar of the viewer application - Default: false
    $responseData = $responseData . "HideMenuBar :" . $document->isHideMenubar();

    // Whether to hide toolbar of the viewer application - Default: false
    $responseData = $responseData . "HideToolBar :" . $document->isHideToolBar();

    // Whether to hide UI elements like scroll bars
    // and leaving only the page contents displayed - Default: false
    $responseData = $responseData . "HideWindowUI :" . $document->isHideWindowUI();

    // The document's page mode. How to display document on exiting
    // full-screen mode.
    $responseData = $responseData . "NonFullScreenPageMode :" . $document->getNonFullScreenPageMode();

    // The page layout i.e. single page, one column
    $responseData = $responseData . "PageLayout :" . $document->getPageLayout();

    // How the document should display when opened.
    $responseData = $responseData . "Page Mode :" . $document->getPageMode();
    $document->close();  
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

```php

    // Open document
    $document = new Document($inputFile);
    // Set different document properties
    // specify to position document's window - Default: false
    $document->setCenterWindow(true);
    // Predominant reading order; determine the position of page
    // when displayed side by side - Default: L2R
    $document->setDirection(Direction::$R2L);
    // Specify whether window's title bar should display document title
    // if false, title bar displays PDF file name - Default: false
    $document->setDisplayDocTitle(true);
    // Specify whether to resize the document's window to fit the size of
    // first displayed page - Default: false
    $document->setFitWindow(true);
    // Specify whether to hide menu bar of the viewer application - Default:
    // false
    $document->setHideMenubar(true);
    // Specify whether to hide toolbar of the viewer application - Default:
    // false
    $document->setHideToolBar(true);
    // Specify whether to hide UI elements like scroll bars
    // and leaving only the page contents displayed - Default: false
    $document->setHideWindowUI(true);
    // Document's page mode. specify how to display document on exiting
    // full-screen mode.
    $document->setNonFullScreenPageMode(PageMode::$UseOC);
    // Specify the page layout i.e. single page, one column
    $document->setPageLayout(PageLayout::$TwoColumnLeft);
    // Specify how the document should display when opened
    // i.e. show thumbnails, full-screen, show attachment panel
    $document->setPageMode(PageMode::$UseThumbs);
    // Save updated PDF file
    $document->save($outputFile);
    $document->close();

```

## Embedding Fonts in an Existing PDF File

PDF readers support [a core of 14 fonts](http://en.wikipedia.org/wiki/Portable_Document_Format#Fonts) so that documents can be displayed the same way regardless of the platform the document is displayed on. When a PDF contains a font that is outside the core fonts, embed the font to avoid font substitution.

Aspose.PDF for PHP via Java supports font embedding in existing PDF documents. You can embed a complete font or a subset. To embed the font:

1. Open an existing PDF file using the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class.
1. Use the [com.aspose.pdf.Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) class to embed the font.
   1. The setEmbedded(true) method embeds the full font.
   1. The pageFont.isSubset(true) method embeds a subset of the font.

A font subset embeds only the characters that are used and is useful where fonts are used for short sentences or slogans, for example where a corporate font is used for a logo, but not for the body text. Using a subset reduces the file size of the output PDF.

However, if a custom font is used for the body text, embed it in its entirety.

The following code snippet shows how to embed a font in a PDF file.

```php

  // Open document
    $document = new Document($inputFile);
    // Iterate through all the pages
    foreach ($document->getPages() as $page) {
      $fonts = $page->getResources()->getFonts();
      if (!is_null($fonts)) {
        foreach ($fonts as $pageFont) {
          // Check if font is already embedded
          if (!$pageFont->isEmbedded())
            $pageFont->setEmbedded(true);
        }
      }
      $forms = $page->getResources()->getForms();
      // Check for the Form objects
      foreach ($forms as $form) {
        $formFonts = $form->getResources()->getFonts();
        if (!is_null($formFonts)) {
          foreach ($formFonts as $formFont) {
            // Check if the font is embedded
            if (!$formFont->isEmbedded())
              $formFont->setEmbedded(true);
          }
        }
      }
    }
    // Save updated PDF file
    $document->save(DATA_DIR + "UpdatedFile_output.pdf");
    $document->close();
```

## Embedding Fonts while creating PDF

If you need to use any font other than the 14 core fonts supported by Adobe Reader, then you must embed the font description while generating a PDF file. If font information is not embedded, Adobe Reader will take it from the Operating System if it’s installed over the system, or it will construct a substitute font according to the font descriptor in the PDF. Please note that embedded font must be installed on the host machine i.e. in case of the following code ‘Univers Condensed’ font is installed over the system.

We use the property setEmbedded of [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) class to embed the font information into PDF file. Setting the value of this property to ‘true’ will embed the complete font file into the PDF, knowing the fact that it will increase the PDF file size. Following is the code snippet that can be used to embed the font information into PDF.

```php

    // Instantiate PDF object by calling its empty constructor
    $document = new Document();

    // Create a section in the Pdf object
    $page = $document->getPages()->add();
    $fragment = new TextFragment("");
    $segment = new TextSegment("This is a sample text using Custom font.");

    $fontRepository = new FontRepository();

    $ts = new TextState();
    $ts->setFont($fontRepository->findFont("Univers Condensed"));
    $ts->getFont()->setEmbedded(true);
    $segment->setTextState($ts);
    $fragment->getSegments()->add($segment);
    $page->getParagraphs()->add($fragment);

    // Save updated PDF file
    $document->save($outputFile);
    $document->close();
```

## Set Default Font Name while Saving PDF

When a PDF document contains fonts, which are not available in the document itself and on the device, API replaces these fonts with the default font. When a font is available (is installed on the device or is embedded into the document), output PDF should have the same font (should not be replaced with default font). The value of the default font should contain the name of the font (not the path to the font files). We have implemented a feature to set default font name while saving a document as PDF. Following code snippet can be used to set default font:

```php

    // Load an existing PDF document
    $document = new Document($inputFile);
    $newName = "Arial";

    // Initialize save options for PDF format
    $ops = new PdfSaveOptions();

    // Set default font name
    $ops->setDefaultFontName($newName);

    // Save PDF file
    $document->save($outputFile, $ops);
    // Save updated PDF file
    $document->close();
```

## Get All Fonts from PDF Document

In case you want to get all fonts from a PDF document, you can use **Document.getFontUtilities().getAllFonts()** method provided in [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class. Please check following code snippet in order to get all fonts from an existing PDF document:

```php

    // Load an existing PDF document
    $document = new Document($inputFile);

    // Get all fonts from document
    $fonts = $document->getFontUtilities()->getAllFonts();
    foreach ($fonts as $font) {
      $responseData = $responseData . $f->getFontName() . PHP_EOL;
    }

    // Save updated PDF file
    $document->close();
```

## Get-Set Zoom Factor of PDF File

Sometimes, you want to set or get the zoom factor of a PDF document. You can easily accomplish this requirement with Aspose.PDF.

The [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToAction) object allows you to get the zoom value associated with a PDF file. Similarly, it can be used to set a file's Zoom factor.

```php

    // Load an existing PDF document
    $document = new Document($inputFile);

    // Create GoToAction object
    $action = $document->getOpenAction();

    // Get the Zoom factor of PDF file
    $responseData = $action->getDestination()->getZoom();

    // Save updated PDF file
    $document->close();  
```

The following code snippet shows how to get the Zoom factor of a PDF file.

```php

    // Load an existing PDF document
    $document = new Document($inputFile);
    $zoom = 0.5;
    // setting zoom factor of document
    $page = $document->getPages()->get_Item(1);
    $actionzoom = new GoToAction(
      new XYZExplicitDestination($page, $page->getMediaBox()->getWidth(), $page->getMediaBox()->getHeight(), $zoom)
    );

    // setting action to fit to page width zoom
    $actionFitToWidth = new GoToAction(
      new FitHExplicitDestination($page, $page->getMediaBox()->getWidth())
    );

    // setting action to fit to page height zoom
    $actionFittoHeight = new GoToAction(
      new FitVExplicitDestination( $page, $page->getMediaBox()->getHeight())
    );

    $document->setOpenAction($actionzoom);
    $document->setOpenAction($actionFittoWidth);
    $document->setOpenAction($actionFittoHeight);

    // Save updated PDF file
    $document->save($outputFile);
    $document->close();  
```
