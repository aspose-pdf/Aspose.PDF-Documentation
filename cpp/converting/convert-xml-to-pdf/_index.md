---
title: Convert XML to PDF 
linktitle: Convert XML to PDF
type: docs
weight: 320
url: /cpp/convert-xml-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF library presents several ways to convert XML to PDF. You can use the XslFoLoadOptions or do this with an incorrect file structure.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

The XML format used to store structured data. There are several ways to convert <abbr title="Extensible Markup Language">XML</abbr> to PDF in Aspose.PDF.

## Convert XSL-FO to PDF

1. Create a [String Class](https://apireference.aspose.com/pdf/cpp/class/system.string) for path name and file name.
1. Instantiate [XslFoLoadOption object](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.load_options).
1. Set error handling strategy.
1. Instantiate [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) Object.
1. [Save](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa) the input image file.

```cpp
void Convert_XSLFO_to_PDF()
{
	std::clog << "XSL-FO to PDF convert: Start" << std::endl;
	String _dataDir("C:\\Samples\\Conversion\\");
	String infilenameXSL("c:\\samples\\employees.xslt");
	String infilenameXML("c:\\samples\\employees.xml");

	String outfilename("XMLFOtoPDF.pdf");
	// Instantiate XslFoLoadOption object
	auto options = new XslFoLoadOptions(infilenameXSL);
	// Set error handling strategy
	options->ParsingErrorsHandlingType = XslFoLoadOptions::ParsingErrorsHandlingTypes::ThrowExceptionImmediately;
	// Create Document object
	auto document = MakeObject<Document>(infilenameXML, options);
	document->Save(_dataDir + outfilename);
}
```

## Live Example

Aspose.PDF for C++ presents you online free application ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), where you may try to investigate the functionality and quality it works.

[![Convert XML to PDF](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
