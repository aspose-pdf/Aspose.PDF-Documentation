---
title: Convert PDF/A to PDF 
linktitle: Convert PDF/A to PDF
type: docs
weight: 350
url: /cpp/convert-pdfa-to-pdf/
lastmod: "2021-06-05"
description: To convert PDF/A to PDF you should remove restrictions from the original document. Aspose.PDF for C++ allows you to solve this problem easly and simply.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Convert PDF/A document to PDF means removing <abbr title="Portable Document Format Archive
">PDF/A</abbr> restriction from the original document. Class [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) has method 'RemovePdfaCompliance' to remove the PDF compliance information from input/source file.
After [Save](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa) the input file.

```cpp
void ConvertPDFAtoPDF()
{
 std::clog << "PDF/A to PDF convert: Start" << std::endl;
 String _dataDir("C:\\Samples\\Conversion\\");
 String infilename("sample-pdfa.pdf");
 String outfilename("PDFAToPDF_out.pdf");

 auto document = MakeObject<Document>(_dataDir + infilename);

 // Remove PDF/A compliance information
 document->RemovePdfaCompliance();

 // Save updated document
 document->Save(_dataDir + outfilename);
 std::clog << "PDF/A to PDF convert: End" << std::endl;
}
```

This info also removes if you make any changes in the document (e.g. add pages). In the following example, the output document loses PDF/A compliance after the page adding.

```cpp
void ConvertPDFAtoPDFAdvanced()
{
 std::clog << "PDF/A to PDF convert: Start" << std::endl;
 String _dataDir("C:\\Samples\\Conversion\\");
 String infilename("sample-pdfa.pdf");
 String outfilename("PDFAToPDF_out.pdf");

 auto document = MakeObject<Document>(_dataDir + infilename);
 // Adding a new (empty) page removes PDF/A compliance information.

 document->get_Pages()->Add();
 // Save updated document
 document->Save(_dataDir + outfilename);
 std::clog << "PDF/A to PDF convert: End" << std::endl;
}
```
