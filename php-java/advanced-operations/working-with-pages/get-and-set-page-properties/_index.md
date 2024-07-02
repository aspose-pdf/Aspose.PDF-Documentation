---
title: Get and Set Page Properties
type: docs
weight: 30
url: /php-java/get-and-set-page-properties/
description: This topic explain how to get numbers in PDF file, get page properties and determine page color using Aspose.PDF for PHP via Java.
lastmod: "2024-06-05"
---

Aspose.PDF for PHP via Java lets you read and set properties of pages in a PDF file in your Java applications. This section shows how to get the number of pages in a PDF file, get information about PDF page properties such as color and set page properties. 

## Get Number of Pages in PDF File

When working with documents, you often want to know how many pages they contain. With Aspose.PDF this takes no more than two lines of code.

To get the number of pages in a PDF file:

1. Open the PDF file using the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class.
1. Then the pages of the document are retrieved. An attempt is made to get the page count from the retrieved pages.

The following code snippet shows how to get the number of pages of a PDF file.

```php

    // Open document
    $document = new Document($inputFile);      

    $pages = $document->getPages();

    // Get page count
    $responseData = $responseData . "Page Count : " + $pages->size();
```

### Get page count without saving the document

Unless the PDF file is saved and all the elements are actually placed inside the PDF file, we cannot get the page count for particular document (because we cannot be certain about the number of pages in which all the elements will be accommodated). However starting with release Aspose.PDF for PHP via Java, we have introduced a method named [processParagraphs(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#processParagraphs--) which provides the feature to get page count for PDF document, without saving the file. So we can get page count information on the fly. Please try using following code snippet to accomplish this requirement.

```php

    // Open document
    $document = new Document($inputFile);      

    // add page to pages collection of PDF file
    $page = $document->getPages()->add();
    
    // create a loop to add 300 TextFragment instances
    for ($i=0; $i < 300; $i++) { 
       // add TextFragment to paragraphs collection of first page of PDF
       $page->getParagraphs()->add(new TextFragment("Pages count test"));
    }
    
    // process paragraphs to get page count information
    $document->processParagraphs();

    $pages = $document->getPages();

    // Get page count
    $responseData = $responseData . "Page Count : " + $pages->size();
```

## Get Page Properties

Each page in a PDF file has a number of properties, such as the width, height, bleed-, crop- and trimbox. Aspose.PDF allows you to access these properties.

### **Understanding Page Properties: the Difference between Artbox, BleedBox, CropBox, MediaBox, TrimBox and Rect property**

- **Media box**: The media box is the largest page box. It corresponds to the page size (for example A4, A5, US Letter, etc.) selected when the document was printed to PostScript or PDF. In other words, the media box determines the physical size of the media on which the PDF document is displayed or printed.
- **Bleed box**: If the document has bleed, the PDF will also have a bleed box. Bleed is the amount of color (or artwork) that extends beyond the edge of a page. It is used to make sure that when the document is printed and cut to size (“trimmed”), the ink will go all the way to the edge of the page. Even if the page is mistrimmed - cut slightly off the trim marks - no white edges will appear on the page.
- **Trim box**: The trim box indicates the final size of a document after printing and trimming.
- **Art box**: The art box is the box drawn around the actual contents of the pages in your documents. This page box is used when importing PDF documents in other applications.
- **Crop box**: The crop box is the “page” size at which your PDF document is displayed in Adobe Acrobat. In normal view, only the contents of the crop box are displayed in Adobe Acrobat.
  For detailed descriptions of these properties, read the Adobe.Pdf specification, particularly 10.10.1 Page Boundaries.
- **Page.Rect**: the intersection (commonly visible rectangle) of the MediaBox and DropBox. The picture below illustrates these properties.

For further details, please visit [this page](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### Accessing Page Properties

The following code snippet gets properties such as ArtBox, BleedBox, CropBox, MediaBox, TrimBox, Rect, Page Number, and Rotate for a specific page in the document. It then stores the extracted data in separate variables and concatenates them into a response string.

1. Create a new Document object using the $inputFile variable.
1. Get the collection of pages from the document using the getPages() method.
1. Get a specific page from the page collection using the get_Item() method.
1. Extract various properties (ArtBox, BleedBox, CropBox, MediaBox, TrimBox, Rect, Page Number, Rotate) from the specific page object and stores them in separate variables.
1. The code concatenates the extracted property values into separate response strings ($responseData1, $responseData2, etc.).
1. Next, it attempts to retrieve the page count using the size() method on the $pages object, but the $pages variable is not defined.


The following code snippet shows how to get page properties.

```php

   // Open document
    $document = new Document($inputFile);

    // Get the page collection
    $pageCollection = $document->getPages();

    // Get a specific page
    $page = $pageCollection->get_Item(1);

    // Get the page properties
    $responseData1 = "ArtBox : Height = " . $page->getArtBox()->getHeight()
        . ", Width = " . $page->getArtBox()->getWidth()
        . ", LLX = " . $page->getArtBox()->getLLX()
        . ", LLY = " . $page->getArtBox()->getLLY()
        . ", URX = " . $page->getArtBox()->getURX()
        . ", URY = " . $page->getArtBox()->getURY()
        . PHP_EOL;

    $responseData2 = "BleedBox : Height = " . $page->getBleedBox()->getHeight() . ", Width = "
        . $page->getBleedBox()->getWidth() . ", LLX = " . $page->getBleedBox()->getLLX() . ", LLY = "
        . $page->getBleedBox()->getLLY() . ", URX = " . $page->getBleedBox()->getURX() . ", URY = "
        . $page->getBleedBox()->getURY()
        . PHP_EOL;

    $responseData3 = "CropBox : Height = " . $page->getCropBox()->getHeight() . ", Width = "
        . $page->getCropBox()->getWidth() . ", LLX = " . $page->getCropBox()->getLLX() . ", LLY = "
        . $page->getCropBox()->getLLY() . ", URX = " . $page->getCropBox()->getURX() . ", URY = "
        . $page->getCropBox()->getURY()
        . PHP_EOL;

    $responseData4 = " MediaBox : Height = " . $page->getMediaBox()->getHeight() . ", Width = "
        . $page->getMediaBox()->getWidth() . ", LLX = " . $page->getMediaBox()->getLLX() . ", LLY = "
        . $page->getMediaBox()->getLLY() . ", URX = " . $page->getMediaBox()->getURX() . ", URY = "
        . $page->getMediaBox()->getURY()
        . PHP_EOL;

    $responseData5 = " TrimBox : Height = " . $page->getTrimBox()->getHeight() . ", Width = "
        . $page->getTrimBox()->getWidth() . ", LLX = " . $page->getTrimBox()->getLLX() . ", LLY = "
        . $page->getTrimBox()->getLLY() . ", URX = " . $page->getTrimBox()->getURX() . ", URY = "
        . $page->getTrimBox()->getURY()
        . PHP_EOL;

    $responseData5 = " Rect : Height = " . $page->getRect()->getHeight() . ", Width = " . $page->getRect()->getWidth()
        . ", LLX = " . $page->getRect()->getLLX() . ", LLY = " . $page->getRect()->getLLY() . ", URX = "
        . $page->getRect()->getURX() . ", URY = " . $page->getRect()->getURY()
        . PHP_EOL;
        
    $responseData6 = " Page Number :- " . $page->getNumber() . PHP_EOL;
    $responseData7 = " Rotate :-" . $page->getRotate() . PHP_EOL;

    // Get page count
    $responseData8 = $responseData8 . "Page Count : " . $pages->size();
```

## Determine Page Color

The [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) class provides the properties related to a particular page in a PDF document, including what type of colour - RGB, black and white, grayscale or undefined - the page uses.

All the pages of the PDF files are contained by the [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection) collection. The [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) property specifies the color of elements on page. To get or determine the color information for particular PDF page, use the [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) class object's [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) property.

The following code snippet shows how to iterate through individual page of PDF file to get color information.

```php

    // Open document
    $document = new Document($inputFile);

    // Iterate through all the page of PDF file
    for ($pageCount = 1; $pageCount <= $document->getPages()->size(); $pageCount++) {

        // Get the color type information for particular PDF page
        $pageColorType = $document->getPages()->get_Item($pageCount)->getColorType();

        switch ($pageColorType) {
            case 2:
                $responseData ="Page # -" . $pageCount . " is Black and white..";
                break;
            case 1:
                $responseData ="Page # -" . $pageCount . " is Gray Scale...";
                break;
            case 0:
                $responseData ="Page # -" . $pageCount . " is RGB..";
                break;
            case 3:
                $responseData ="Page # -" . $pageCount . " Color is undefined..";
                break;
        }
    }
```
