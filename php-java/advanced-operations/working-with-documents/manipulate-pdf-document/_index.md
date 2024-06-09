---
title: Manipulate PDF Document 
linktitle: Manipulate PDF Document
type: docs
weight: 30
url: /php-java/manipulate-pdf-document/
description: This article contains information on how to validate PDF Document for PDF A Standard, how to work with TOC, how to set PDF expiry date, and how to determine the Progress of PDF file generation.
lastmod: "2024-06-05"
---

## Validate PDF Document for PDF A Standard (A 1A and A 1B)

To validate a PDF document for PDF/A-1a or PDF/A-1b compatibility, use the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class' [validate(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#validate-java.io.OutputStream-int-) method. This method allows you to specify the name of the file in which the result is to be saved and the required validation type [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfFormat) enumeration: PDF_A_1A or PDF_A_1B.

The output XML format is a custom Aspose format. The XML contains a collection of tags with the name Problem; each tag contains the details of a particular problem. The Problem tag's ObjectID attribute represents the ID of the particular object this problem is related to. The Clause attribute represents a corresponding rule in the PDF specification.

```php

    // Open document
    $document = new Document($inputFile);
    
    $pdfFormat =  (new PdfFormat())->PDF_A_1A;
    // Validate PDF for PDF/A-1a
    $document->validate($outputFile, $pdfFormat);
    $document->close();
```

## Working with TOC

### Add TOC to Existing PDF

The ListSection class in the aspose.pdf package allows you to create a table of contents when creating a PDF document from scratch. To add headings, which are elements of the TOC, use the [aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) class.

To add a TOC to an existing PDF file, use the [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) class in the com.aspose.pdf package. The com.aspose.pdf package can both create new and manipulate existing PDF files. To add a TOC to an existing PDF, use com.aspose.pdf package.

The following code snippet shows how to create a table of contents inside an existing PDF file.

```php

    // Open document
    $document = new Document($inputFile);

    // Get access to first page of PDF file
    $tocPage = $document->getPages()->insert(1);

    // Create object to represent TOC information
    $tocInfo = new TocInfo();

    $title = new TextFragment("Table Of Contents");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // Set the title for TOC
    $tocInfo->setTitle($title);
    $tocPage->setTocInfo($tocInfo);

    // Create string objects which will be used as TOC elements
    $titles = ["First page", "Second page", "Third page", "Fourth page"];

    for ($i = 0; $i < 4; $i++) {
        // Create Heading object
        $heading2 = new Heading(1);

        $segment2 = new TextSegment();
        $heading2->setTocPage($tocPage);
        $heading2->getSegments()->add($segment2);

        // Specify the destination page for heading object
        $page = $document->getPages()->get_Item($i + 2);
        $heading2->setDestinationPage($page);

        // Destination page
        $heading2->setTop($page->getRect()->getHeight());

        // Destination coordinate
        $segment2->setText($titles[$i]);

        // Add heading to page containing TOC
        $tocPage->getParagraphs()->add($heading2);
    }
    // Save the updated document
    $document->save($outputFile);
    $document->close();
```

### Set different TabLeaderType for different TOC Levels

Aspose.PDF also allows setting different TabLeaderType for different TOC levels. You need to set LineDash property of FormatArray with the appropriate value of TabLeaderType enum as following.

```php

    // Open document
    $document = new Document($inputFile);
    $tocPage = $document->getPages()->add();

    $tocInfo = new TocInfo();

    // set LeaderType
    $tocInfo->setLineDash(TabLeaderType->Solid);

    $title = new TextFragment("Table Of Contents");
    $title->getTextState()->setFontSize(30);
    $tocInfo->setTitle($title);

    // Add the list section to the sections collection of the Pdf document
    $tocPage->setTocInfo($tocInfo);

    // Define the format of the four levels list by setting the left margins and
    // text format settings of each level
    $fontStyles = new FontStyles();
    $tabLeaderTypes = new TabLeaderType();

    $tocInfo->setFormatArrayLength(4);
    $tocInfo->getFormatArray()[0]->getMargin()->setLeft(0);
    $tocInfo->getFormatArray()[0]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[0]->setLineDash($tabLeaderTypes->getDot());
    $tocInfo->getFormatArray()[0]->getTextState()->setFontStyle($fontStyles->getBold() | $fontStyles->getItalic());
    $tocInfo->getFormatArray()[1]->getMargin()->setLeft(10);
    $tocInfo->getFormatArray()[1]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[1]->setLineDash($tabLeaderTypes->getNone());
    $tocInfo->getFormatArray()[1]->getTextState()->setFontSize(10);
    $tocInfo->getFormatArray()[2]->getMargin()->setLeft(20);
    $tocInfo->getFormatArray()[2]->getMargin()->setRight(0);
    $tocInfo->getFormatArray()[2]->getTextState()->setFontStyle($fontStyles->getBold());
    $tocInfo->getFormatArray()[3]->setLineDash($tabLeaderTypes->getSolid());
    $tocInfo->getFormatArray()[3]->getMargin()->setLeft(30);
    $tocInfo->getFormatArray()[3]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[3]->getTextState()->setFontStyle($fontStyles->getBold());

    // Create a section in the Pdf document
    $page = $document->getPages()->add();

    // Add four headings in the section
    for ($Level = 1; $Level <= 4; $Level++) {
      $heading2 = new Heading($Level);
      $segment2 = new TextSegment();

      $heading2->getSegments()->add($segment2);
      $heading2->setAutoSequence(true);
      $heading2->setTocPage($tocPage);

      $segment2->setText("Sample Heading" . $Level);
      $fontRepository = new FontRepository();
      $heading2->getTextState()->setFont($fontRepository->findFont("Arial UnicodeMS"));

      // Add the heading into Table Of Contents.
      $heading2->setInList(true);
      $page->getParagraphs()->add($heading2);
    }

    // Save the updated document
    $document->save($outputFile);
    $document->close();
```

### Hide Page Numbers in TOC

In case if you do not want to display page numbers, along with the headings in TOC, you can use [ShowPageNumbers](https://reference.aspose.com/pdf/java/com.aspose.pdf/TocInfo) property of [TOCInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo) Class as false. Please check following code snippet to hide page numbers in the table of contents:

```php

    // Open document
    $document = new Document();
    $tocPage = $document->getPages()->add();
    
    // Create object to represent TOC information
    $tocInfo = new TocInfo();

    $title = new TextFragment("Table Of Contents");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // Set the title for TOC
    $tocInfo->setTitle($title);

    // Add the list section to the sections collection of the Pdf document
    $tocPage->setTocInfo($tocInfo);

    // Define the format of the four levels list by setting the left margins and
    // text format settings of each level

    $tocInfo->setShowPageNumbers(false);
    $tocInfo->setFormatArrayLength(4);
    $tocInfo->getFormatArray()[0]->getMargin()->setRight(0);
    $tocInfo->getFormatArray()[0]->getTextState()->setFontStyle(FontStyles::$Bold | FontStyles::$Italic);

    $tocInfo->getFormatArray()[1]->getMargin()->setLeft(30);
    $tocInfo->getFormatArray()[1]->getTextState()->setUnderline(true);
    $tocInfo->getFormatArray()[1]->getTextState()->setFontSize(10);

    $tocInfo->getFormatArray()[2]->getTextState()->setFontStyle(FontStyles::$Bold);
    $tocInfo->getFormatArray()[3]->getTextState()->setFontStyle(FontStyles::$Bold);

    $page = $document->getPages()->add();

    // Add four headings in the section
    for ($Level = 1; $Level < 5; $Level++) {
      $heading2 = new Heading($Level);
      $segment2 = new TextSegment();
      $heading2->setTocPage($tocPage);
      $heading2->getSegments()->add($segment2);
      $heading2->setAutoSequence(true);
      $segment2->setText("this is heading of level " + $Level);
      $heading2->setInList(true);
      $page->getParagraphs()->add($heading2);
    }
     
    // Save the updated document
    $document->save($outputFile);
    $document->close();
```

### Customize Page Numbers while adding TOC

It is common to customize the page numbering in the TOC while adding TOC in a PDF document. For example, we may need to add some prefix before page number like P1, P2, P3 and so on. In such a case, Aspose.PDF for PHP via Java provides PageNumbersPrefix property of TocInfo class that can be used to customize page numbers as shown in the following code sample.

```php

    // Open document
    $document = new Document($inputFile);

    // Get access to first page of PDF file
    $tocPage = $document->getPages()->insert(1);

    // Create object to represent TOC information
    $tocInfo = new TocInfo();

    $title = new TextFragment("Table Of Contents");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // Set the title for TOC
    $tocInfo->setTitle($title);
    $tocInfo->setPageNumbersPrefix("P");
    $tocPage->setTocInfo($tocInfo);

    // Create string objects which will be used as TOC elements
    $titles = ["First page", "Second page", "Third page", "Fourth page"];

    for ($i = 0; $i < 4; $i++) {
        // Create Heading object
        $heading2 = new Heading(1);

        $segment2 = new TextSegment();
        $heading2->setTocPage($tocPage);
        $heading2->getSegments()->add($segment2);

        // Specify the destination page for heading object
        $page = $document->getPages()->get_Item($i + 2);
        $heading2->setDestinationPage($page);

        // Destination page
        $heading2->setTop($page->getRect()->getHeight());

        // Destination coordinate
        $segment2->setText($titles[$i]);

        // Add heading to page containing TOC
        $tocPage->getParagraphs()->add($heading2);
    }
    // Save the updated document
    $document->save($outputFile);
    $document->close();
```

## Add Layers to PDF File

Layers can be used in PDF documents in many ways. You might have a multi-lingual file that you want to distribute and want text in each language to appear on different layers, with the background design appearing on a separate layer. You might also create documents with animation that appears on a separate layer. One example could be to add a license agreement to your file, and you don’t want a user to view the content until they agree to the terms of the agreement.

Aspose.PDF for PHP via Java supports adding layers to PDF files.

To work with layers in PDF files, use the following API members.

The [layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) class represents a layer and contains the following properties:

- **Name** – the layer's name.
- **Id** – the layer's ID.
- **Contents** – a list of layer operators.

Once the [layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) objects have been defined, add them to the [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) object's Layers collection. The code below shows how to add layers to a PDF document.

```php

    // Open document
    $document = new Document($inputFile);
    $page = $document->getPages()->add();
    $arrayList = new java("java.util.ArrayList");
    $page->setLayers($arrayList);

    $layer = new $layer("oc1", "Red Line");
    $layer->getContents()->add(new operators_SetRGBColorStroke(1, 0, 0));
    $layer->getContents()->add(new operators_MoveTo(500, 700));
    $layer->getContents()->add(new operators_LineTo(400, 700));
    $layer->getContents()->add(new operators_Stroke());    
    $page->getLayers()->add($layer);

    $layer = new $layer("oc2", "Green Line");
    $layer->getContents()->add(new operators_SetRGBColorStroke(0, 1, 0));
    $layer->getContents()->add(new operators_MoveTo(500, 750));
    $layer->getContents()->add(new operators_LineTo(400, 750));
    $layer->getContents()->add(new operators_Stroke());
    $page->getLayers()->add($layer);

    $layer = new $layer("oc3", "Blue Line");
    $layer->getContents()->add(new operators_SetRGBColorStroke(0, 0, 1));
    $layer->getContents()->add(new operators_MoveTo(500, 800));
    $layer->getContents()->add(new operators_LineTo(400, 800));
    $layer->getContents()->add(new operators_Stroke());
    $page->getLayers()->add($layer);
    
    // Save the updated document
    $document->save($outputFile);
    $document->close();
```

## Set PDF Expiration

The PDF expiration feature sets how long a PDF file is valid for. On a particular date, if someone tries to access it, a pop-up is displayed, explaining that the file has expired and that they need a new one.

Aspose.PDF allows you to set expiration when creating and editing PDF files.

The code snippet below shows how to set the expiration date for a PDF file. You need to use JavaScript as files saved by third party components (for example OwnerGuard) cannot be viewed on other workstations without that utility.

The PDF file can be created using PDF OwnerGuard using an existing file with an expiration date. But the new file can be opened only on a workstation that has PDF OwnerGuard installed. Workstations without PDF OwnerGuard will give an ExpirationFeatureError. For example, PDF Reader opens the file if OwnerGuard is installed, but Adobe Acrobat returns an error.

```php

    // Open document
    $document = new Document($inputFile);
       
    $javaScript = new JavascriptAction(
      "var year=2020;" + 
      "var month=4;" + 
      "var today = new Date(); today = new Date(today.getFullYear(), today.getMonth());" +
      "var expiry = new Date(year, month);" +
      "if (today.getTime() > expiry.getTime())" + 
      "app.alert('The file is expired. You need a new one.');"
      );
    $document->setOpenAction($javaScript);
    $document->save($outputFile);
    $document->close();
```


