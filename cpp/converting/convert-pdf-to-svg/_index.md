---
title: Convert PDF to SVG 
linktitle: Convert PDF to SVG
type: docs
weight: 60
url: /cpp/convert-pdf-to-svg/
lastmod: "2021-06-05"
description: Aspose.PDF for C++ supports the feature to convert SVG images to PDF format using SvgSaveOptions class.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

In order to convert PDF to SVG, Aspose.PDF for CPP offers [Save](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) method of [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) class. You need to pass the output path and enum SaveFormat:: svg to the Save method to convert PDF to SVG. The following code snippet shows how to convert PDF to SVG:

This article teacher you how to convert PDF to <abbr title="Scalable Vector Graphics">SVG</abbr> using C++.

## Live Example

Aspose.PDF for C++ presents you online free application ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), where you may try to investigate the functionality and quality it works.

[![PDF to SVG](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)

**Scalable Vector Graphics (SVG)** is a family of specifications of an XML-based file format for two-dimensional vector graphics, both static and dynamic (interactive or animated). The SVG specification is an open standard that has been under development by the World Wide Web Consortium (W3C) since 1999.

SVG images and their behaviors are defined in XML text files. This means that they can be searched, indexed, scripted and if required, compressed. As XML files, SVG images can be created and edited with any text editor, but it is often more convenient to create them with drawing programs such as Inkscape.

Aspose.PDF for C++ supports the feature to convert SVG image to PDF format and also offers the capability to convert PDF files to SVG format. To accomplish this requirement, the `SvgSaveOptions` class has been introduced into the Aspose.PDF namespace. Instantiate an object of SvgSaveOptions and pass it as a second argument to the [Save](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) method .

The following code snippet shows the steps for converting a PDF file to SVG format with C++.

```cpp
void ConvertPDFtoSvgSinglePage()
{
 std::clog << __func__ << ": Start" << std::endl;
 // String for path name
 String _dataDir("C:\\Samples\\Conversion\\");

 // String for file name
 String infilename("PageToSvg.pdf");
 String outfilename("PageToSvg_out.svg");

 // Open document
 auto document = MakeObject<Document>(_dataDir + infilename);

 // Instantiate an object of SvgSaveOptions
 auto saveOptions = MakeObject<SvgSaveOptions>();
 // Do not compress SVG image to Zip archive
 saveOptions->CompressOutputToZipArchive = false;

 try {
  // Save the output in SVG files
  document->Save(_dataDir+outfilename, saveOptions);
 }
 catch (Exception ex) {
  std::cerr << ex->get_Message();
 }

 std::clog << __func__ << ": Finish" << std::endl;
}
```
