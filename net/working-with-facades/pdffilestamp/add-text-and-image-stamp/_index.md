---
title: Add Text and Image Stamp
type: docs
weight: 20
url: /net/add-text-and-image-stamp/
description: This section explains how to add Text and Image Stamp with Aspose.PDF Facades using PdfFileStamp Class.
lastmod: "2021-06-05"
draft: false
---

## Add Text Stamp on All Pages in a PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class allows you to add text stamp on all the pages of a PDF file. In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes. You also need to create the text stamp using [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) method of [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class. You can set other attributes like origin, rotation, background etc. using [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) object as well. Then you can add the stamp in the PDF file using [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. Finally, save the output PDF file using [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. The following code snippet shows you how to add text stamp on all pages in a PDF file.

```csharp
public static void AddTextStampOnAllPagesInPdfFile()
{
    // Create PdfFileStamp object
    PdfFileStamp fileStamp = new PdfFileStamp();

    // Open Document
    fileStamp.BindPdf(dataDir + "sample.pdf");

    // Create stamp
    Stamp stamp = new Stamp();
    stamp.BindLogo(new FormattedText("Hello World!", System.Drawing.Color.Blue, System.Drawing.Color.Gray, Aspose.Pdf.Facades.FontStyle.Helvetica, EncodingType.Winansi, true, 14));
    stamp.SetOrigin(10, 400);
    stamp.Rotation = 90.0F;
    stamp.IsBackground = true;

    // Add stamp to PDF file
    fileStamp.AddStamp(stamp);

    // Save updated PDF file
    fileStamp.Save(dataDir + "AddTextStamp-All_out.pdf");

    // Close fileStamp
    fileStamp.Close();
}
```

## Add Text Stamp on Particular Pages in a PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class allows you to add text stamp on particular pages of a PDF file. In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes. You also need to create the text stamp using [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) method of [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class. You can set other attributes like origin, rotation, background etc. using [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) object as well. As you want to add text stamp on particular pages of the PDF file, you also need to set the  [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) property of the [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class. This property requires an integer array containing numbers of the pages on which you want to add the stamp. Then you can add the stamp in the PDF file using [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. Finally, save the output PDF file using [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. The following code snippet shows you how to add text stamp on particular pages in a PDF file.

```csharp
public static void AddTextStampOnParticularPagesInPdfFile()
{
    // Create PdfFileStamp object
    PdfFileStamp fileStamp = new PdfFileStamp();

    // Open Document
    fileStamp.BindPdf(dataDir + "sample.pdf");

    // Create stamp
    Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
    stamp.BindLogo(new FormattedText("Hello World!", System.Drawing.Color.Blue, System.Drawing.Color.Gray, Aspose.Pdf.Facades.FontStyle.Helvetica, EncodingType.Winansi, true, 14));
    stamp.SetOrigin(10, 400);
    stamp.Rotation = 90.0F;
    stamp.IsBackground = true;

    // Set particular pages
    stamp.Pages = new int[] { 2 };

    // Add stamp to PDF file
    fileStamp.AddStamp(stamp);

    // Save updated PDF file
    fileStamp.Save(dataDir + "AddTextStamp-Page_out.pdf");

    // Close fileStamp
    fileStamp.Close();
}
```

## Add Image Stamp on All Pages in a PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class allows you to add image stamp on all the pages of a PDF file. In order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes. You also need to create the image stamp using [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) method of [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class. You can set other attributes like origin, rotation, background etc. using [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) object as well. Then you can add the stamp in the PDF file using [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. Finally, save the output PDF file using [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. The following code snippet shows you how to add image stamp on all pages in a PDF file.

```csharp
public static void AddImageStampOnAllPagesInPdfFile()
{
    // Create PdfFileStamp object
    PdfFileStamp fileStamp = new PdfFileStamp();

    // Open Document
    fileStamp.BindPdf(dataDir + "sample.pdf");

    // Create stamp
    Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
    stamp.BindImage(dataDir + "aspose-logo.png");
    stamp.SetOrigin(10, 200);
    stamp.Rotation = 90.0F;
    stamp.IsBackground = true;

    // Set particular pages
    stamp.Pages = new int[] { 2 };

    // Add stamp to PDF file
    fileStamp.AddStamp(stamp);

    // Save updated PDF file
    fileStamp.Save(dataDir + "AddImageStamp-Page_out.pdf");

    // Close fileStamp
    fileStamp.Close();
}
```

### Control image quality when adding as stamp

When adding Image as stamp object, you can also control the quality of image. In order to accomplish this requirement, Quality property is added for [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class. It indicates the quality of image in percents (valid values are 0..100).

## Add Image Stamp on Particular Pages in a PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class allows you to add image stamp on particular pages of a PDF file. In order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes. You also need to create the image stamp using [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) method of [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class. You can set other attributes like origin, rotation, background etc. using [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) object as well. As you want to add image stamp on particular pages of the PDF file, you also need to set the [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) property of the [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class. This property requires an integer array containing numbers of the pages on which you want to add the stamp. Then you can add the stamp in the PDF file using [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. Finally, save the output PDF file using [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. The following code snippet shows you how to add image stamp on particular pages in a PDF file.

```csharp
public static void AddImageStampOnParticularPagesInPdfFile()
{
    // Create PdfFileStamp object
    PdfFileStamp fileStamp = new PdfFileStamp();

    // Open Document
    fileStamp.BindPdf(dataDir + "sample.pdf");

    // Create stamp
    Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
    stamp.BindImage(dataDir + "aspose-logo.png");
    stamp.SetOrigin(10, 200);
    stamp.Rotation = 90.0F;
    stamp.IsBackground = true;

    // Add stamp to PDF file
    fileStamp.AddStamp(stamp);

    // Save updated PDF file
    fileStamp.Save(dataDir + "AddImageStamp-All_out.pdf");

    // Close fileStamp
    fileStamp.Close();
}
```
