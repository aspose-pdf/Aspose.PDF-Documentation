---
title: Save PDF Document using C++
linktitle: Save PDF Document
type: docs
weight: 30
url: /cpp/save-pdf-document/
description: Learn how to save PDF file with Aspose.PDF for C++ library. 
lastmod: "2021-11-01"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Save PDF document to file system

You can save the created or manipulated PDF document to file system using Save method of [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) class.

```cpp
void SaveDocument()
{
 // String for path name
 String _dataDir("C:\\Samples\\");

 String originalFileName("SimpleResume.pdf");
 String modifiedFileName("SimpleResumeModified.pdf");

 auto document = MakeObject<Document>(_dataDir + originalFileName);
 // make some manipation, i.g add new empty page
 document->get_Pages()->Add();
 document->Save(_dataDir + modifiedFileName);
}
```

## Save PDF document to stream

You can also save the created or manipulated PDF document to stream by using overloads of Save methods.

```cpp
void SaveDocumentStream()
{
 // String for path name
 String _dataDir("C:\\Samples\\");

 String originalFileName("SimpleResume.pdf");
 String modifiedFileName("SimpleResumeModified.pdf");

 auto document = MakeObject<Document>(_dataDir + originalFileName);

 // make some manipation, i.g add new empty page
 document->get_Pages()->Add();

 auto fileStream = System::IO::File::OpenWrite(_dataDir + modifiedFileName);
 document->Save(fileStream);
}
```

## Save PDF/A or PDF/X format

PDF/A is an ISO-standardized version of the Portable Document Format (PDF) for use in archiving and long-term preservation of electronic documents.
PDF/A differs from PDF in that it prohibits features not suitable for long-term archiving, such as font linking (as opposed to font embedding) and encryption. ISO requirements for PDF / A viewers include color management guidelines, embedded font support, and a user interface for reading embedded annotations.

PDF/X is a subset of the PDF ISO standard. The purpose of PDF/X is to facilitate graphics exchange, and it therefore has a series of printing-related requirements which do not apply to standard PDF files.

In both cases, the Save method is used to store the documents, while the documents must be prepared using the [PdfFormatConversionOptions](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.pdf_format_conversion_options).

```cpp
void SaveDocumentAsPDFx()
{
 // String for path name
 String _dataDir("C:\\Samples\\");

 // String for file name
 String infilename("SimpleResume.pdf");
 String outfilename("SimpleResume_A3U.pdf");

 auto document = MakeObject<Document>(_dataDir + infilename);
 auto options = new PdfFormatConversionOptions(Aspose::Pdf::PdfFormat::PDF_A_3U);
 try
 {
  document->Convert(options);
 }
 catch (const std::exception& e)
 {
  std::cerr << e.what();
 }

 document->Save(_dataDir + outfilename);
}
```
