---
title: Convert XML to PDF | C#
linktitle: Convert XML to PDF
type: docs
weight: 320
url: /net/convert-xml-to-pdf/
lastmod: "2021-01-15"
description: Aspose.PDF library presents several ways to convert XML to PDF. You can use the XslFoLoadOptions or do this with an incorrect file structure.
aliases:
    - /net/create-a-hello-world-pdf-document-through-xml-and-xslt/
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

The XML format used to store structured data. There are several ways to convert <abbr title="Extensible Markup Language">XML</abbr> to PDF in Aspose.PDF:

1. Transform any XML data to HTML using XSLT and convert HTML to PDF as described below
1. Generate XML document using Aspose.PDF XSD Schema
1. Use XML document based on XSL-FO standard

## Live Example

Aspose.PDF for .NET presents you online free application ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), where you may try to investigate the functionality and quality it works.

[![XML to PDF](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)

## Convert XSL-FO to PDF

The conversion of XSL-FO files to PDF can be implemented using the traditional Aspose.PDF technique - instantiate [`Document`](https://apireference.aspose.com/page/net/aspose.page/document) object with [`XslFoLoadOptions`](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.xsl_fo_load_options). But sometimes you can meet with the incorrect file structure. For this case, XSL-FO converter allows setting the error handling strategy. You can choose `ThrowExceptionImmediately`, `TryIgnore` or `InvokeCustomHandler`.

```csharp
public static void Convert_XSLFO_to_PDF()
{
    // Instantiate XslFoLoadOption object
    var options = new XslFoLoadOptions(".\\samples\\employees.xslt");
    // Set error handling strategy
    options.ParsingErrorsHandlingType = XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately;
    // Create Document object
    var pdfDocument = new Aspose.Pdf.Document(".\\samples\\employees.xml", options);
    pdfDocument.Save(_dataDir + "data_xml.pdf");
}
```
