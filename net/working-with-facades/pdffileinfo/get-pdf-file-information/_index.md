---
title: Get PDF file information
type: docs
weight: 50
url: /net/get-pdf-file-information/
description: This section explains how to get PDF File Information with Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

In order to get file specific information of a PDF file, you need to create an object of [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) class. After that, you can get values of the individual properties like Subject, Title, Keywords and Creator etc.

The following code snippet shows you how to get PDF file information.

```csharp
public static void GetPdfInfo()
{
    // Open document
    PdfFileInfo fileInfo = new PdfFileInfo(dataDir + "sample.pdf");
    // Get PDF information
    Console.WriteLine("Subject: {0}", fileInfo.Subject);
    Console.WriteLine("Title: {0}", fileInfo.Title);
    Console.WriteLine("Keywords: {0}", fileInfo.Keywords);
    Console.WriteLine("Creator: {0}", fileInfo.Creator);
    Console.WriteLine("Creation Date: {0}", fileInfo.CreationDate);
    Console.WriteLine("Modification Date: {0}", fileInfo.ModDate);
    // Find whether is it valid PDF and it is encrypted as well
    Console.WriteLine("Is Valid PDF: {0}", fileInfo.IsPdfFile);
    Console.WriteLine("Is Encrypted: {0}", fileInfo.IsEncrypted);

    Console.WriteLine("Page width:{0}", fileInfo.GetPageWidth(1));
    Console.WriteLine("Page height:{0}", fileInfo.GetPageHeight(1));
}
```

## Get Meta Info

In order to get information, we use the [Header](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/header) property. With 'Hashtable'  we get all the possible values.

```csharp
public static void GetMetaInfo()
{
    // Create instance of PdfFileInfo object
    Aspose.Pdf.Facades.PdfFileInfo fInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "SetMetaInfo_out.pdf");
    // Retrieve all existing custom attributes
    Hashtable hTable = new Hashtable(fInfo.Header);

    IDictionaryEnumerator enumerator = hTable.GetEnumerator();
    while (enumerator.MoveNext())
    {
        string output = enumerator.Key.ToString() + " " + enumerator.Value;
        Console.WriteLine(output);
    }

    // Retrieve one custom attributes
    Console.WriteLine(fInfo.GetMetaInfo("Reviewer"));
}
```