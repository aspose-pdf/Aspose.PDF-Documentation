---
title: Convert PDF to XPS 
linktitle: Convert PDF to XPS
type: docs
weight: 160
url: /cpp/convert-pdf-to-xps/
lastmod: "2021-06-05"
description: This page describes the definition of an XPS document and how to use it. Convert PDF to XPS with Aspose.PDF for C++, using XpsSaveOptions class.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for C++* gives a possibility to convert PDF files to <abbr title="XML Paper Specification">XPS</abbr> format. Let try to use the presented code snippet for converting PDF files to XPS format with C++.

## Live Example

Aspose.PDF for C++ presents you online free application ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), where you may try to investigate the functionality and quality it works.

[![PDF to XPS](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)

The XPS file type is primarily associated with the XML Paper Specification by Microsoft Corporation. The XML Paper Specification (XPS), formerly codenamed Metro and subsuming the Next Generation Print Path (NGPP) marketing concept, is Microsoft's initiative to integrate document creation and viewing into the Windows operating system.

To convert PDF files to XPS, Aspose.PDF has the class [XpsSaveOptions](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.xps_save_options) that is used as the second argument to the [Document.Save(..)](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) method to generate the XPS file.

The following code snippet shows the process of converting PDF file into XPS format.

```cpp
void ConvertPDFtoXPS()
{
 std::clog << __func__ << ": Start" << std::endl;
 // String for path name
 String _dataDir("C:\\Samples\\Conversion\\");

 // String for input file name
 String infilename("sample.pdf");
 // String for output file name
 String outfilename("PDFToXPS_out.xps");

 // Open document
 auto document = MakeObject<Document>(_dataDir + infilename);

 // Instantiate LaTex save option
 auto saveOptions = MakeObject<XpsSaveOptions>();

 // Save PDF file into XPS format
 document->Save(_dataDir + outfilename, saveOptions);
 std::clog << __func__ << ": Finish" << std::endl;
}
```
