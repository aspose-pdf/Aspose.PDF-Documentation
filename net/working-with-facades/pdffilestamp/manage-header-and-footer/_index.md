---
title: Manage Header and Footer
type: docs
weight: 40
url: /net/manage-header-and-footer/
description: This section explains how to manage Header and Footer with Aspose.PDF Facades using PdfFileStamp Class.
lastmod: "2021-06-05"
draft: false
---

## Add Header in a PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class allows you to add header in a PDF file. In order to add header, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. You can format the header text using [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) class. Once you’re ready to add header in the file, you need to call [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. You also need to specify at least the top margin in the [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) method. Finally, save the output PDF file using [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. The following code snippet shows you how to add header in a PDF file.

```csharp
public static void AddHeader()
{
    // Create PdfFileStamp object
    PdfFileStamp fileStamp = new PdfFileStamp();

    // Open Document
    fileStamp.BindPdf(_dataDir + "sample.pdf");

    // Create formatted text for page number
    FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!",
        System.Drawing.Color.Yellow,
        System.Drawing.Color.Black,
        FontStyle.Courier,
        EncodingType.Winansi, false, 14);

    // Add header
    fileStamp.AddHeader(formattedText, 10);

    // Save updated PDF file
    fileStamp.Save(_dataDir + "AddHeader_out.pdf");

    // Close fileStamp
    fileStamp.Close();
}
```

## Add Footer in a PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class allows you to add footer in a PDF file. In order to add footer, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. You can format the footer text using [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) class. Once you’re ready to add footer in the file, you need to call [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. You also need to specify at least the bottom margin in the [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) method. Finally, save the output PDF file using [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. The following code snippet shows you how to add footer in a PDF file.

```csharp
public static void AddFooter()
{
    // Create PdfFileStamp object
    PdfFileStamp fileStamp = new PdfFileStamp();

    // Open Document
    fileStamp.BindPdf(_dataDir + "sample.pdf");

    // Create formatted text for page number
    FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!",
        System.Drawing.Color.Blue,
        System.Drawing.Color.Gray,
        FontStyle.Courier,
        EncodingType.Winansi, false, 14);

    // Add footer
    fileStamp.AddFooter(formattedText, 10);

    // Save updated PDF file
    fileStamp.Save(_dataDir + "AddFooter_out.pdf");

    // Close fileStamp
    fileStamp.Close();
}
```

## Add Image in Header of an Existing PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class allows you to add image in the header of a PDF file. In order to add image in header, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. After that, you need to call [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. You can pass the image to the [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) method. Finally, save the output PDF file using [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. The following code snippet shows you how to add image in header of PDF file.

```csharp
public static void AddImageHeader()
{
    // Create PdfFileStamp object
    PdfFileStamp fileStamp = new PdfFileStamp();

    // Open Document
    fileStamp.BindPdf(_dataDir + "sample.pdf");
    using (var fs = new FileStream(_dataDir + "aspose-logo.png", FileMode.Open))
    {
        // Add Header
        fileStamp.AddHeader(fs, 10);

        // Save updated PDF file
        fileStamp.Save(_dataDir + "AddImage-Header_out.pdf");
        // Close fileStamp
        fileStamp.Close();
    }
}
```

## Add Image in Footer of an Existing PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class allows you to add image in the footer of a PDF file. In order to add image in footer, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. After that, you need to call [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. You can pass the image to the [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) method. Finally, save the output PDF file using [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. The following code snippet shows you how to add image in the footer of PDF file.

```csharp
public static void AddImageFooter()
{
    // Create PdfFileStamp object
    PdfFileStamp fileStamp = new PdfFileStamp();

    // Open Document
    fileStamp.BindPdf(_dataDir + "sample.pdf");
    using (var fs = new FileStream(_dataDir + "aspose-logo.png", FileMode.Open))
    {
        // Add footer
        fileStamp.AddFooter(fs, 10);

        // Save updated PDF file
        fileStamp.Save(_dataDir + "AddImage-Footer_out.pdf");

        // Close fileStamp
        fileStamp.Close();
    }
}
```
