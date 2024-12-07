---
title: Add PDF Page Stamp
type: docs
weight: 10
url: /java/add-pdf-page-stamp/
description: Learn how to add page stamps, such as text or image stamps, to existing PDF documents using Aspose.PDF for Java.
lastmod: "2021-06-05"
draft: false
---

## Add PDF Page Stamp on All Pages in a PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class allows you to add PDF page stamp on all the pages of a PDF file. In order to add PDF page stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) and [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes. You also need to create the PDF page stamp using [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp)  method of [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) class. You can set other attributes like origin, rotation, background etc. using [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) object as well. Then you can add the stamp in the PDF file using [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) method of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. Finally, save the output PDF file using [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) method of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. The following code snippet shows you how to add PDF page stamp on all pages in a PDF file.

```csharp
public static void AddPageStampOnAllPages()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create stamp
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Add stamp to PDF file
            fileStamp.AddStamp(stamp);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```

## Add PDF Page Stamp on Particular Pages in a PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class allows you to add PDF page stamp on particular pages of a PDF file. In order to add PDF page stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) and [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes. You also need to create the PDF page stamp using [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) method of [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) class. You can set other attributes like origin, rotation, background etc. using [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) object as well. As you want to add PDF page stamp on particular pages of the PDF file, you also need to set the [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) property of the [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) class. This property requires an integer array containing numbers of the pages on which you want to add the stamp. Then you can add the stamp in the PDF file using [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) method of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. Finally, save the output PDF file using [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) method of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. The following code snippet shows you how to add PDF page stamp on particular pages in a PDF file.

```csharp
public static void AddPageStampOnCertainPages()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create stamp
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;
            stamp.Pages = new[] { 1, 3 };
            // Add stamp to PDF file
            fileStamp.AddStamp(stamp);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // Close fileStamp
            fileStamp.Close();
        }

        // Add PDF Page Numbers
        public enum PageNumPosition
        {
            PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
        }
```

## Add Page Number in a PDF File (facades)

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class allows you to add page numbers in a PDF file. In order to add page numbers, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. If you want to show page number like “Page X of N” while X being the current page number and N the total number of pages in the PDF file then you first need to get the page count using getNumberOfpages property of [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) class. In order to get the current page number you can use **#** sign in your text anywhere you like. You can format the page number text using [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) class. If you want to start the page numbering from a specific number then you can set setStartingNumber property. Once you’re ready to add page number in the file, you need to call addPageNumber method of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. Finally, save the output PDF file using Save method of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class.

The following code snippet shows you how to add page number in a PDF file.

```java
 public static void AddPageNumberInPdfFile() {
        // Create PdfFileStamp object
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Open Document
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Get total number of pages
        int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").getNumberOfPages();

        // Create formatted text for page number
        FormattedText formattedText = new FormattedText("Page # of " + totalPages, java.awt.Color.WHITE,
                java.awt.Color.GRAY, FontStyle.TimesBoldItalic, EncodingType.Winansi, false, 12);

        // Set starting number for first page; you might want to start from 2 or more
        fileStamp.setStartingNumber(1);

        // Add page number
        fileStamp.addPageNumber(formattedText, (int) PageNumPosition.PosUpperRight.ordinal());

        // Save updated PDF file
        fileStamp.save(_dataDir + "AddPageNumber_out.pdf");

        // Close fileStamp
        fileStamp.close();
    }
```

### Custom Numbering style

The [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class offers the feature to add Page Number information as stamp object inside PDF document. Prior to this release, the class only supported 1,2,3,4 as page numbering style. However, there has been a requirement from some customers to use custom numbering style when placing page number stamp inside PDF document. In order to accomplish this requirement, [NumberingStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/numberingstyle) property has been introduced, which accepts the values from [NumberingStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/numberingstyle) enumeration. Specified below are values offered in this enumeration.

```java
 public static void AddCustomPageNumberInPdfFile() {
        // Create PdfFileStamp object
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Open Document
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Get total number of pages
        int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").getNumberOfPages();

        // Create formatted text for page number
        FormattedText formattedText = new FormattedText("Page # of " + totalPages, java.awt.Color.WHITE,
                java.awt.Color.GRAY, FontStyle.TimesBoldItalic, EncodingType.Winansi, false, 12);

        // Specify numbering style as Numerals Roman UpperCase
        fileStamp.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);

        // Set starting number for first page; you might want to start from 2 or more
        fileStamp.setStartingNumber(1);

        // Add page number
        fileStamp.addPageNumber(formattedText, PageNumPosition.PosUpperRight.ordinal());

        // Save updated PDF file
        fileStamp.save(_dataDir + "AddPageNumber_out.pdf");

        // Close fileStamp
        fileStamp.close();
    }
```
