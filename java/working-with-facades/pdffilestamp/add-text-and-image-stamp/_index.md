---
title: Add Text and Image Stamp
type: docs
weight: 20
url: /java/add-text-and-image-stamp/
description: This section explains how to add Text and Image Stamp with com.aspose.pdf.facades using PdfFileStamp Class.
lastmod: "2021-06-05"
draft: false
---

## Add Text Stamp on All Pages in a PDF File

[PdfFileStamp](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileStamp) class allows you to add text stamp on all the pages of a PDF file. In order to add text stamp, you first need to create objects of [PdfFileStamp](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileStamp) and [Stamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes. You also need to create the text stamp using BindLogo method of [Stamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) class. You can set other attributes like origin, rotation, background etc. using [Stamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) object as well. Then you can add the stamp in the PDF file using [addStamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) method of [PdfFileStamp](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileStamp) class. Finally, save the output PDF file using [close](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) method of [PdfFileStamp](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileStamp) class. The following code snippet shows you how to add text stamp on all pages in a PDF file.

```java
 public static void AddTextStampOnAllPagesInPdfFile() {
        // Create PdfFileStamp object
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Open Document
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Create stamp
        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("Hello World!", java.awt.Color.BLUE, java.awt.Color.GRAY, FontStyle.Helvetica,
                EncodingType.Winansi, true, 14));
        stamp.setOrigin(10, 400);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // Add stamp to PDF file
        fileStamp.addStamp(stamp);

        // Save updated PDF file
        fileStamp.save(_dataDir + "AddTextStamp-All_out.pdf");

        // Close fileStamp
        fileStamp.close();
    }
```

## Add Text Stamp on Particular Pages in a PDF File

[PdfFileStamp](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileStamp) class allows you to add text stamp on particular pages of a PDF file. In order to add text stamp, you first need to create objects of [PdfFileStamp](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileStamp)and [Stamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes. You also need to create the text stamp using [bindPdf](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) method of [Stamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) class. You can set other attributes like origin, rotation, background etc. using [Stamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) object as well. As you want to add text stamp on particular pages of the PDF file, you also need to set the  [Pages](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) property of the [Stamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) class. This property requires an integer array containing numbers of the pages on which you want to add the stamp. Then you can add the stamp in the PDF file using [addStamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) method of [PdfFileStamp](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileStamp) class. Finally, save the output PDF file using [close](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) method of [PdfFileStamp](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileStamp) class. The following code snippet shows you how to add text stamp on particular pages in a PDF file.

```java
 public static void AddTextStampOnParticularPagesInPdfFile() {
        // Create PdfFileStamp object
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Open Document
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Create stamp
        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("Hello World!", java.awt.Color.BLUE, java.awt.Color.GRAY, FontStyle.Helvetica,
                EncodingType.Winansi, true, 14));
        stamp.setOrigin(10, 400);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // Set particular pages
        stamp.setPages(new int[] { 2 });

        // Add stamp to PDF file
        fileStamp.addStamp(stamp);

        // Save updated PDF file
        fileStamp.save(_dataDir + "AddTextStamp-Page_out.pdf");

        // Close fileStamp
        fileStamp.close();
    }
```

## Add Image Stamp on All Pages in a PDF File

[PdfFileStamp](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileStamp) class allows you to add image stamp on all the pages of a PDF file. In order to add image stamp, you first need to create objects of [PdfFileStamp](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileStamp) and [Stamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes. You also need to create the image stamp using [bindPdf](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) method of [Stamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) class. You can set other attributes like origin, rotation, background etc. using [Stamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) object as well. Then you can add the stamp in the PDF file using [addStamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) method of [PdfFileStamp](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileStamp) class. Finally, save the output PDF file using [close](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) method of [PdfFileStamp](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileStamp) class. The following code snippet shows you how to add image stamp on all pages in a PDF file.

```java
public static void AddImageStampOnParticularPagesInPdfFile() {
        // Create PdfFileStamp object
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Open Document
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Create stamp
        Stamp stamp = new Stamp();
        stamp.bindImage(_dataDir + "aspose-logo.png");
        stamp.setOrigin(10, 200);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // Add stamp to PDF file
        fileStamp.addStamp(stamp);

        // Save updated PDF file
        fileStamp.save(_dataDir + "AddImageStamp-All_out.pdf");

        // Close fileStamp
        fileStamp.close();
    }
```

### Control image quality when adding as stamp

When adding Image as stamp object, you can also control the quality of image. In order to accomplish this requirement, Quality property is added for [Stamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) class. It indicates the quality of image in percents (valid values are 0..100).

## Add Image Stamp on Particular Pages in a PDF File

[PdfFileStamp](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileStamp) class allows you to add image stamp on particular pages of a PDF file. In order to add image stamp, you first need to create objects of [PdfFileStamp](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileStamp) and [Stamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes. You also need to create the image stamp using [bindPdf](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) method of [Stamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) class. You can set other attributes like origin, rotation, background etc. using [Stamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) object as well. As you want to add image stamp on particular pages of the PDF file, you also need to set the [Pages](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) property of the [Stamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) class. This property requires an integer array containing numbers of the pages on which you want to add the stamp. Then you can add the stamp in the PDF file using [addStamp](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) method of [PdfFileStamp](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileStamp) class. Finally, save the output PDF file using [close](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) method of [PdfFileStamp](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileStamp) class. The following code snippet shows you how to add image stamp on particular pages in a PDF file.

```java
  public static void AddImageStampOnAllPagesInPdfFile() {
        // Create PdfFileStamp object
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Open Document
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Create stamp
        Stamp stamp = new Stamp();
        stamp.bindImage(_dataDir + "aspose-logo.png");
        stamp.setOrigin(10, 200);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // Set particular pages
        stamp.setPages(new int[] { 2 });

        // Add stamp to PDF file
        fileStamp.addStamp(stamp);

        // Save updated PDF file
        fileStamp.save(_dataDir + "AddImageStamp-Page_out.pdf");

        // Close fileStamp
        fileStamp.close();
    }
```
