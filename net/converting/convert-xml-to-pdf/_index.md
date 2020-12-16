---
title: Convert XML to PDF
type: docs
weight: 70
url: /net/convert-xml-to-pdf/
description: Aspose.PDF library presents several ways to convert XML to PDF. The first is a simple conversion with XslFoLoadOptions, and the second way is using incorrect file structure.
aliases:
    - /pdf/net/create-a-hello-world-pdf-document-through-xml-and-xslt/
---

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/xml-to-pdf](https://products.aspose.app/pdf/conversion/xml-to-pdf)

{{% /alert %}}

The XML format used to store structured data. There are several ways to convert XML to PDF in Aspose.PDF:

1. Transform any XML data to HTML using XSLT and convert HTML to PDF as described below
1. Generate XML document using Aspose.PDF XSD Schema
1. Use XML document based on XSL-FO standard

## Convert XSL-FO to PDF

The conversion of XSL-FO files to PDF can be implemented using the traditional Aspose.PDF technique - instantiate [`Document`](https://apireference.aspose.com/page/net/aspose.page/document) object with [`XslFoLoadOptions`](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.xsl_fo_load_options).

```csharp
public static void Convert_XSLFO_to_PDF()
{
    // Instantiate XslFoLoadOption object
    var options = new XslFoLoadOptions(".\\samples\\employees.xslt");
    // Create Document object
    var pdfDocument = new Aspose.Pdf.Document(".\\samples\\employees.xml", options);
    pdfDocument.Save(_dataDir + "data_xml.pdf");
}
```

The preceding sample shows simple convesrion but sometimes you can meet with incorrect file structure. For this case XSL-FO converter allow to set the error handling strategy. You can choose `ThrowExceptionImmediately`, `TryIgnore` or `InvokeCustomHandler`.

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
