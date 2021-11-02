---
title: Convert SVG to PDF
linktitle: Convert SVG to PDF
type: docs
weight: 240
url: /cpp/convert-svg-to-pdf/
lastmod: "2021-06-05"
description: This page shows the possibility of converting SVG to PDF with Aspose.PDF and describes how to get SVG dimensions and overview SVG Supported Features.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for C++** explains how to convert SVG images to PDF format and how to get dimensions of the source <abbr title="Scalable Vector Graphics">SVG</abbr> file.

Scalable Vector Graphics (SVG) is a family of specifications of an XML-based file format for two-dimensional vector graphics, both static and dynamic (interactive or animated). The SVG specification is an open standard that has been under development by the World Wide Web Consortium (W3C) since 1999.

SVG images and their behaviors are defined in XML text files. This means that they can be searched, indexed, scripted, and if required, compressed. As XML files, SVG images can be created and edited with any text editor, but it is often more convenient to create them with drawing programs such as Inkscape.

## Live Example

Aspose.PDF for C++ presents you online free application ["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), where you may try to investigate the functionality and quality it works.

[![Convert SVG to PDF](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)

1. Create a [String Class](https://apireference.aspose.com/pdf/cpp/class/system.string) for path name and file name.
1. Create an instance of [`SvgLoadOptions`](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.svg_load_options) class.
1. Create an instance of [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document)class with mention source filename and options.
1. Save the document with the desired file name.

The following code snippet shows the process of converting SVG file into PDF format with Aspose.PDF for C++.

```cpp
void ConvertSVGtoPDF() {
 std::clog << "SVG to PDF convert: Start" << std::endl;

 String _dataDir("C:\\Samples\\Conversion\\");
 String infilename("sample.svg");
 String outfilename("ImageToPDF-SVG.pdf");

 auto options = MakeObject<SvgLoadOptions>();
 try {
  auto document = MakeObject<Document>(_dataDir + infilename, options);
  document->Save(_dataDir + outfilename);
 }
 catch (System::Exception ex) {
  std::cerr << ex->get_Message() << std::endl;
 }
 std::clog << "SVG to PDF convert: Finish" << std::endl;
}
```

Сonsider an example with advanced features:

```cpp
void ConvertSVGtoPDF_Advanced()
{
 std::clog << "SVG to PDF convert: Start" << std::endl;

 String _dataDir("C:\\Samples\\Conversion\\");
 String infilename("Sweden-Royal-flag-grand-coa.svg");
 String outfilename("ImageToPDF-SVG.pdf");

 auto options = MakeObject<SvgLoadOptions>();
 options->set_AdjustPageSize(true);
 options->ConversionEngine = SvgLoadOptions::ConversionEngines::NewEngine;

 try {
  auto document = MakeObject<Document>(_dataDir + infilename, options);
  document->Save(_dataDir + outfilename);
 }
 catch (System::Exception ex) {
  std::cerr << ex->get_Message() << std::endl;
 }

 std::clog << "SVG to PDF convert: Finish" << std::endl;
}
```
