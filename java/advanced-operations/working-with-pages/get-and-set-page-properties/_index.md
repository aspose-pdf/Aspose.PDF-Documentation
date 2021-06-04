---
title: Get and Set Page Properties
type: docs
weight: 30
url: /java/get-and-set-page-properties/
description: This topic explain how to get numbers in PDF file, get page properties and determine page color using Aspose.PDF for Java.
lastmod: "2021-06-05"
---

Aspose.PDF for Java lets you read and set properties of pages in a PDF file in your Java applications. This section shows how to get the number of pages in a PDF file, get information about PDF page properties such as color and set page properties. 

## Get Number of Pages in PDF File

When working with documents, you often want to know how many pages they contain. With Aspose.PDF this takes no more than two lines of code.

To get the number of pages in a PDF file:

1. Open the PDF file using the [Document](https://apireference.aspose.com/java/pdf/com.aspose.pdf/Document) class.
1. Then use the [PageCollection](https://apireference.aspose.com/pdf/java/com.aspose.pdf.class-use/PageCollection) collection's Count property (from the Document object) to get the total number of pages in the document.

The following code snippet shows how to get the number of pages of a PDF file.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleGetAndSetPageProperties {
    // The path to the documents directory.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void GetNumberOfPagesInaPDFFile() {

        // Open document
        Document pdfDocument = new Document(_dataDir + "GetNumberofPages.pdf");

        // Get page count
        System.out.println("Page Count : " + pdfDocument.getPages().size());
        _dataDir = _dataDir + "ApplyNumberStyle_out.pdf";
        pdfDocument.save(_dataDir);

    }
```

### Get page count without saving the document

Unless the PDF file is saved and all the elements are actually placed inside the PDF file, we cannot get the page count for particular document (because we cannot be certain about the number of pages in which all the elements will be accommodated). However starting with release Aspose.PDF for Java 10.1.0, we have introduced a method named [processParagraphs(...)](https://apireference.aspose.com/java/pdf/com.aspose.pdf/Document#processParagraphs--) which provides the feature to get page count for PDF document, without saving the file. So we can get page count information on the fly. Please try using following code snippet to accomplish this requirement.

```java
public static void GetPageCountWithoutSavingTheDocument() {

        // For complete examples and data files, please go to
        // https://github.com/aspose-pdf/Aspose.Pdf-for-Java
        // instantiate Document instance
        Document doc = new Document();
        // add page to pages collection of PDF file
        Page page = doc.getPages().add();
        // create a loop to add 300 TextFragment instances
        for (int i = 0; i < 300; i++)
            // add TextFragment to paragraphs collection of first page of PDF
            page.getParagraphs().add(new TextFragment("Pages count test"));
        // process paragraphs to get page count information
        doc.processParagraphs();
        System.out.println("Number of Pages in PDF = " + doc.getPages().size());
    }
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

The [Page](https://apireference.aspose.com/java/pdf/com.aspose.pdf/Page) class provides all the properties related to a particular PDF page. All the pages of the PDF files are contained in the of the [Document](https://apireference.aspose.com/java/pdf/com.aspose.pdf/Document) object's [PageCollection](https://apireference.aspose.com/pdf/java/com.aspose.pdf.class-use/PageCollection)  collection.

From there, it is possible to access either individual Page objects using their index, or loop through the collection, using a foreach loop, to get all pages. Once an individual page is accessed, we can get its properties. The following code snippet shows how to get page properties.

```java
    public static void AccessingPageProperties() {

        Document pdfDocument = new Document("input.pdf");

        // Get the page collection
        PageCollection pageCollection = pdfDocument.getPages();

        // Get a specific page
        Page pdfPage = pageCollection.get_Item(1);

        // Get the page properties
        System.out.printf("\n ArtBox : Height = " + pdfPage.getArtBox().getHeight() + ", Width = "
                + pdfPage.getArtBox().getWidth() + ", LLX = " + pdfPage.getArtBox().getLLX() + ", LLY = "
                + pdfPage.getArtBox().getLLY() + ", URX = " + pdfPage.getArtBox().getURX() + ", URY = "
                + pdfPage.getArtBox().getURY());
        System.out.printf("\n BleedBox : Height = " + pdfPage.getBleedBox().getHeight() + ", Width = "
                + pdfPage.getBleedBox().getWidth() + ", LLX = " + pdfPage.getBleedBox().getLLX() + ", LLY = "
                + pdfPage.getBleedBox().getLLY() + ", URX = " + pdfPage.getBleedBox().getURX() + ", URY = "
                + pdfPage.getBleedBox().getURY());
        System.out.printf("\n CropBox : Height = " + pdfPage.getCropBox().getHeight() + ", Width = "
                + pdfPage.getCropBox().getWidth() + ", LLX = " + pdfPage.getCropBox().getLLX() + ", LLY = "
                + pdfPage.getCropBox().getLLY() + ", URX = " + pdfPage.getCropBox().getURX() + ", URY = "
                + pdfPage.getCropBox().getURY());
        System.out.printf("\n MediaBox : Height = " + pdfPage.getMediaBox().getHeight() + ", Width = "
                + pdfPage.getMediaBox().getWidth() + ", LLX = " + pdfPage.getMediaBox().getLLX() + ", LLY = "
                + pdfPage.getMediaBox().getLLY() + ", URX = " + pdfPage.getMediaBox().getURX() + ", URY = "
                + pdfPage.getMediaBox().getURY());
        System.out.printf("\n TrimBox : Height = " + pdfPage.getTrimBox().getHeight() + ", Width = "
                + pdfPage.getTrimBox().getWidth() + ", LLX = " + pdfPage.getTrimBox().getLLX() + ", LLY = "
                + pdfPage.getTrimBox().getLLY() + ", URX = " + pdfPage.getTrimBox().getURX() + ", URY = "
                + pdfPage.getTrimBox().getURY());
        System.out.printf(
                "\n Rect : Height = " + pdfPage.getRect().getHeight() + ", Width = " + pdfPage.getRect().getWidth()
                        + ", LLX = " + pdfPage.getRect().getLLX() + ", LLY = " + pdfPage.getRect().getLLY() + ", URX = "
                        + pdfPage.getRect().getURX() + ", URY = " + pdfPage.getRect().getURY());
        System.out.printf("\n Page Number :- " + pdfPage.getNumber());
        System.out.printf("\n Rotate :-" + pdfPage.getRotate());
    }
```

## Determine Page Color

The [Page](https://apireference.aspose.com/java/pdf/com.aspose.pdf/Page) class provides the properties related to a particular page in a PDF document, including what type of colour - RGB, black and white, grayscale or undefined - the page uses.

All the pages of the PDF files are contained by the [PageCollection](https://apireference.aspose.com/java/pdf/com.aspose.pdf/PageCollection) collection. The [ColorType](https://apireference.aspose.com/java/pdf/com.aspose.pdf/ColorType) property specifies the color of elements on page. To get or determine the color information for particular PDF page, use the [Page](https://apireference.aspose.com/java/pdf/com.aspose.pdf/Page) class object's [ColorType](https://apireference.aspose.com/java/pdf/com.aspose.pdf/ColorType) property.

The following code snippet shows how to iterate through individual page of PDF file to get color information.

```java
    public static void DeterminePageColor () {

        Document pdfDocument = new Document("input.pdf");
        // Iterate through all the page of PDF file
        for (int pageCount = 1; pageCount <= pdfDocument.getPages().size(); pageCount++) {
            // Get the color type information for particular PDF page
            int pageColorType = pdfDocument.getPages().get_Item(pageCount).getColorType();
            switch (pageColorType) {
            case 2:
                System.out.println("Page # -" + pageCount + " is Black and white..");
                break;
            case 1:
                System.out.println("Page # -" + pageCount + " is Gray Scale...");
                break;
            case 0:
                System.out.println("Page # -" + pageCount + " is RGB..");
                break;
            case 3:
                System.out.println("Page # -" + pageCount + " Color is undefined..");
                break;
            }
        }
    }
}
```
