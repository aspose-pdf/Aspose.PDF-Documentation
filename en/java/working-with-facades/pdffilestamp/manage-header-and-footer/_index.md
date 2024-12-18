---
title: Manage Header and Footer
type: docs
weight: 40
url: /java/manage-header-and-footer/
description: Learn how to add, remove, or modify headers and footers in a PDF document using Aspose.PDF in Java.
lastmod: "2021-06-05"
draft: false
---

## Add Header in a PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class allows you to add header in a PDF file. In order to add header, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. You can format the header text using [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) class. Once you’re ready to add header in the file, you need to call [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) method of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. You also need to specify at least the top margin in the [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) method. Finally, save the output PDF file using [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) method of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. The following code snippet shows you how to add header in a PDF file.

```java
 public static void AddHeader() {
        // Create PdfFileStamp object
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Open Document
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Create formatted text for page number
        FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!", java.awt.Color.YELLOW,
                java.awt.Color.BLACK, FontStyle.Courier, EncodingType.Winansi, false, 14);

        // Add header
        fileStamp.addHeader(formattedText, 20);

        // Save updated PDF file
        fileStamp.save(_dataDir + "AddHeader_out.pdf");

        // Close fileStamp
        fileStamp.close();
    }
```

## Add Footer in a PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class allows you to add footer in a PDF file. In order to add footer, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. You can format the footer text using [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) class. Once you’re ready to add footer in the file, you need to call [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) method of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. You also need to specify at least the bottom margin in the [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) method. Finally, save the output PDF file using [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) method of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. The following code snippet shows you how to add footer in a PDF file.

```java
 public static void AddFooter() {
        // Create PdfFileStamp object
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Open Document
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Create formatted text for page number
        FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!", java.awt.Color.BLUE,
                java.awt.Color.GRAY, FontStyle.Courier, EncodingType.Winansi, false, 14);

        // Add footer
        fileStamp.addFooter(formattedText, 10);

        // Save updated PDF file
        fileStamp.save(_dataDir + "AddFooter_out.pdf");

        // Close fileStamp
        fileStamp.close();
    }
```

## Add Image in Header of an Existing PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class allows you to add image in the header of a PDF file. In order to add image in header, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. After that, you need to call [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) method of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. You can pass the image to the [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) method. Finally, save the output PDF file using [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) method of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. The following code snippet shows you how to add image in header of PDF file.

```java
public static void AddImageHeader() {
        // Create PdfFileStamp object
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Open Document
        fileStamp.bindPdf(_dataDir + "sample.pdf");
        FileInputStream fs;
        try {
            fs = new FileInputStream(_dataDir + "aspose-logo.png");
            // Add Header
            fileStamp.addHeader(fs, 10);

            // Save updated PDF file
            fileStamp.save(_dataDir + "AddImage-Header_out.pdf");
        } catch (FileNotFoundException e) {

            e.printStackTrace();
        }

        // Close fileStamp
        fileStamp.close();
    }
```

## Add Image in Footer of an Existing PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class allows you to add image in the footer of a PDF file. In order to add image in footer, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. After that, you need to call [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) method of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. You can pass the image to the [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) method. Finally, save the output PDF file using [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) method of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. The following code snippet shows you how to add image in the footer of PDF file.

```java
    public static void AddImageFooter() {
        // Create PdfFileStamp object
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Open Document
        fileStamp.bindPdf(_dataDir + "sample.pdf");
        FileInputStream fs;
        try {
            fs = new FileInputStream(_dataDir + "aspose-logo.png");
            // Add footer
            fileStamp.addFooter(fs, 10);

            // Save updated PDF file
            fileStamp.save(_dataDir + "AddImage-Footer_out.pdf");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        // Close fileStamp
        fileStamp.close();
    }
```
