---
title: Convert XPS to PDF 
linktitle: Convert XPS to PDF
type: docs
weight: 330
url: /cpp/convert-xps-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF for C++ allows you to convert XPS to PDF files with a class named XpsLoadOptions. Check code snippet to solve this task.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for C++** support feature converting <abbr title="XML Paper Specification">XPS</abbr> files to PDF format. Check this article to resolve your tasks.

The XPS file type is primarily associated with the XML Paper Specification by Microsoft Corporation. The XML Paper Specification (XPS), formerly codenamed Metro and subsuming the Next Generation Print Path (NGPP) marketing concept, is Microsoft's initiative to integrate document creation and viewing into its Windows operating system.

{{% alert color="primary" %}}

The file format is basically a zipped XML file which is primarily used for distribution and storage. It's very difficult to edit and mostly implemented by Microsoft.

{{% /alert %}}

In order to convert XPS to PDF with Aspose.PDF for C++, we have introduced a class named [XpsLoadOption](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.load_options) which is used to initialize a [LoadOptions](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.load_options) object. Later, this object is passed as an argument during the Document object initialization and it helps the PDF rendering engine to determine the source document's input format.

The following code snippet shows the process of converting XPS file into PDF format with C++.

```cpp
void ConvertXPStoPDF()
{
 std::clog << "XPS to PDF convert: Start" << std::endl;
 String _dataDir("C:\\Samples\\Conversion\\");
 String infilename("sample.oxps");
 String outfilename("XPStoPDF.pdf");
 auto options = MakeObject<XpsLoadOptions>();
 try {
  auto document = MakeObject<Document>(_dataDir + infilename, options);
  document->Save(_dataDir + outfilename);
 }
 catch (System::Exception ex) {
  std::cerr << ex->get_Message() << std::endl;
 };
 std::clog << "XPS to PDF convert: Finish" << std::endl;
}
```
