---
title: Set PDF File Information
type: docs
weight: 40
url: /net/set-pdf-file-information/
description: This section explains how to set PDF File Information with Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---


[PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) class allows you to set file specific information of a PDF file. You need to create an object of [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) class and then set different file specific properties like Author, Title, Keyword, and Creator etc. Finally, save the updated PDF file using [SaveNewInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileinfo/savenewinfo/methods/1) method of the [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) object.

The following code snippet shows you how to set PDF file information.

```csharp
public static void SetPdfInfo()
{
    PdfFileInfo fileInfo = new PdfFileInfo(dataDir + "sample.pdf")
    {
        // Set PDF information
        Author = "Aspose",
        Title = "Hello World!",
        Keywords = "Peace and Development",
        Creator = "Aspose"
    };
    // Save updated file
    fileInfo.SaveNewInfo(dataDir + "SetFileInfo_out.pdf");
}
```

## Set Meta Info

[SetMetaInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/methods/setmetainfo) method allows you to add any information. In our example, we added a field. Check next code snippet:

```csharp
public static void SetMetaInfo()
{
    // Create instance of PdfFileInfo object
    Aspose.Pdf.Facades.PdfFileInfo fInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample.pdf");

    // Set new customer attribute as meta info
    fInfo.SetMetaInfo("Reviewer", "Aspose.PDF user");

    // Save updated file
    fInfo.SaveNewInfo(dataDir + "SetMetaInfo_out.pdf");
}
```