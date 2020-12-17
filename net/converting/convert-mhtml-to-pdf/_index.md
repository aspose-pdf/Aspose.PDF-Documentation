---
title: Convert MHTML to PDF 
type: docs
weight: 150
url: /net/convert-mhtml-to-pdf/
lastmod: "2020-12-15"
description: The release of Aspose.PDF for .NET 9.0.0  introduced a new feature that allows you convert MHT files to PDF format.
---

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/mhtml-to-pdf](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)

{{% /alert %}}

MHTML, short for MIME HTML, is a web page archive format used to combine resources that are typically represented by external links (such as images, Flash animations, Java applets, and audio files) with HTML code into a single file. The content of an MHTML file is encoded as if it were an HTML email message, using the MIME type multipart/related. Aspose.PDF for .NET can convert HTML files to PDF format and with the release of Aspose.PDF for .NET 9.0.0, we have introduced a new feature that lets you convert MHTML files to PDF format.
Next code snippet show how to covert MHTML files to PDF format with C#:

```csharp
public static void ConvertMHTtoPDF()
{
    MhtLoadOptions options = new MhtLoadOptions()
    {
        PageInfo = { Width = 842, Height = 1191, IsLandscape = true}
    };
    Document pdfDocument= new Document(_dataDir + "fileformatinfo.mht", options);
    pdfDocument.Save(_dataDir + "mhtml_test.PDF");
}
```
