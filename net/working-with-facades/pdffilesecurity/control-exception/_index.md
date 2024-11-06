---
title: Control Exception PDF File
type: docs
weight: 30
url: /net/control-exception/
description: This topic explains how control exception on PDF File using PdfFileSecurity Class Class.
lastmod: "2021-06-05"
draft: false
---

[PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) class allows you to control exceptions. To do this, you need to set [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) property to false or true. If you set the operation to false, the result of [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile) will return true or false depending on the correctness of the password. 

```csharp
public static void ControlExceptionPDFFile()
{
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
    fileSecurity.AllowExceptions = false;
    // Decrypt PDF document
    if (!fileSecurity.DecryptFile("IncorrectPassword"))
    {
        Console.WriteLine("Something wrong...");
        Console.WriteLine($"Last exception: {fileSecurity.LastException.Message}");
    }
    fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
}
```

If you set [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) property to true, then you can get the result of the operation using the try-catch operator.


```csharp
public static void ControlExceptionPDFFile2()
{
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
    fileSecurity.AllowExceptions = true;
    try
    {
        // Decrypt PDF document
        fileSecurity.DecryptFile("IncorrectPassword");
    }
    catch (Exception ex)
    {
        Console.WriteLine("Something wrong...");
        Console.WriteLine($"Exception: {ex.Message}");
    }
    fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
}
```