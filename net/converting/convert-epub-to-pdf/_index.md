---
title: Convert EPUB to PDF
type: docs
weight: 40
url: /net/convert-epub-to-pdf/
description: Epub is free and open format of the electronic version of books with the .epub extension. You may easily convert epub files to PDF format with Aspose.PDF.
---

# Convert EPUB to PDF

EPUB (short for electronic publication) is a free and open e-book standard from the International Digital Publishing Forum (IDPF). Files have the extension .epub. EPUB is designed for reflowable content, meaning that an EPUB reader can optimize text for a particular display device.

EPUB also supports fixed-layout content. The format is intended as a single format that publishers and conversion houses can use in-house, as well as for distribution and sale. It supersedes the Open eBook standard.The version EPUB 3 is also endorsed by the Book Industry Study Group (BISG), a leading book trade association for standardized best practices, research, information and events, for packaging of content.

{{% alert color="primary" %}} 

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/epub-to-pdf](https://products.aspose.app/pdf/conversion/epub-to-pdf)

{{% /alert %}}

Conversion steps:

1. Create an instance of `EpubLoadOptions` class.
1. Create an instance of `Document` class with mention source filename and options.
1. Save the document with the desired file name.

```csharp
public static void ConvertEPUBtoPDF()
{
    EpubLoadOptions option = new EpubLoadOptions();
    Document pdfDocument= new Document(_dataDir + "WebAssembly.epub", option);
    pdfDocument.Save(_dataDir + "epub_test.pdf");
}
```

You can also set page size for conversion. To define new page size you `SizeF` object and pass it to `EpubLoadOptions` constructor.

```csharp
public static void ConvertEPUBtoPDFAdv()
{
    EpubLoadOptions option = new EpubLoadOptions(new SizeF(1190, 1684));
    Document pdfDocument= new Document(_dataDir + "WebAssembly.epub", option);
    pdfDocument.Save(_dataDir + "epub_test.pdf");
}
```
