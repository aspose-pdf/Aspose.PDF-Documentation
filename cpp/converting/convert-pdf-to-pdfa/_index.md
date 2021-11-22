---
title: Convert PDF to PDF/A formats using C++
linktitle: Convert PDF to PDF/A formats
type: docs
weight: 100
url: /cpp/convert-pdf-to-pdfa/
lastmod: "2021-11-01"
description: This topic show you how to Aspose.PDF allows to convert a PDF file to a PDF/A compliant PDF file. 
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for C++** allows you to convert a PDF file to a <abbr title="Portable Document Format / A">PDF/A</abbr> compliant PDF file. Before doing so, the file must be validated. This topic explains how.

{{% alert color="primary" %}}

Please note we follow Adobe Preflight for validating PDF/A conformance. All tools on the market have their own “representation” of PDF/A conformance. Please check this article on PDF/A validation tools for reference. We chose Adobe products for verifying how Aspose.PDF produces PDF files because Adobe is at the center of everything connected to PDF.

{{% /alert %}}

Convert the file using the Document class Convert method. Before converting the PDF to PDF/A compliant file, validate the PDF using the Validate method. The validation result is stored in an XML file and then this result is also passed to the Convert method. You can also specify the action for the elements which cannot be converted using the ConvertErrorAction enumeration.
## Convert PDF file to PDF/A-1b

The following code snippet shows how to convert PDF files to PDF/A-1b compliant PDF.

```cpp
void ConverttoPDFA_1b()
{
 std::clog << __func__ << ": Start" << std::endl;
 // String for path name
 String _dataDir("C:\\Samples\\Conversion\\");

 // String for input file name
 String infilename("sample.pdf");
 // String for log file name
 String logfilename("log.xml");
 // String for input file name
 String outfilename("PDFToPDFA_out.pdf");

 // Open document
 auto document = new Document(_dataDir + infilename);

 // Convert to PDF/A compliant document
 // During conversion process, the validation is also performed
 document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_1B, ConvertErrorAction::Delete);

 // Save output document
 document->Save(_dataDir + outfilename);
 std::clog << __func__ << ": Finish" << std::endl;
}
```

To perform validation only, use the following line of code:

```cpp
void ConverttoPDFA_1b_Validation()
{
 std::clog << __func__ << ": Start" << std::endl;
 // String for path name
 String _dataDir("C:\\Samples\\Conversion\\");

 // String for input file name
 String infilename("sample.pdf");
 // String for log file name
 String logfilename("log.xml");

 // Open document
 auto document = new Document(_dataDir + infilename);

 // Convert to PDF/A compliant document
 // During conversion process, the validation is also performed
 document->Validate(_dataDir + logfilename, PdfFormat::PDF_A_1B);
 std::clog << __func__ << ": Finish" << std::endl;
}
```

## Convert PDF file to PDF/A-3b

Aspose.PDF for C++ also supports the feature to convert a PDF file to PDF/A-3b format.

```cpp
void ConverttoPDFA_3b()
{
 std::clog << __func__ << ": Start" << std::endl;
 // String for path name
 String _dataDir("C:\\Samples\\Conversion\\");

 // String for input file name
 String infilename("sample.pdf");
 // String for log file name
 String logfilename("log.xml");
 // String for input file name
 String outfilename("PDFToPDFA3b_out.pdf");

 // Open document
 auto document = new Document(_dataDir + infilename);

 // Convert to PDF/A compliant document
 // During conversion process, the validation is also performed
 document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_3B, ConvertErrorAction::Delete);

 // Save output document
 document->Save(_dataDir + outfilename);
 std::clog << __func__ << ": Finish" << std::endl;
}
```

## Convert PDF file to PDF/A-2u

Aspose.PDF for C++ also supports the feature to convert a PDF file to PDF/A-2u format.

```cpp
void ConverttoPDFA_2u()
{
 std::clog << __func__ << ": Start" << std::endl;
 // String for path name
 String _dataDir("C:\\Samples\\Conversion\\");

 // String for input file name
 String infilename("sample.pdf");
 // String for log file name
 String logfilename("log.xml");
 // String for input file name
 String outfilename("PDFToPDFA3b_out.pdf");

 // Open document
 auto document = new Document(_dataDir + infilename);

 // Convert to PDF/A compliant document
 // During conversion process, the validation is also performed
 document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_2U, ConvertErrorAction::Delete);

 // Save output document
 document->Save(_dataDir + outfilename);
 std::clog << __func__ << ": Finish" << std::endl;
}
```

## Convert PDF file to PDF/A-3u

Aspose.PDF for C++ also supports the feature to convert a PDF file to PDF/A-3u format.

```cpp
void ConverttoPDFA_3u()
{
 std::clog << __func__ << ": Start" << std::endl;
 // String for path name
 String _dataDir("C:\\Samples\\Conversion\\");

 // String for input file name
 String infilename("sample.pdf");
 // String for log file name
 String logfilename("log.xml");
 // String for input file name
 String outfilename("PDFToPDFA3b_out.pdf");

 // Open document
 auto document = new Document(_dataDir + infilename);

 // Convert to PDF/A compliant document
 // During conversion process, the validation is also performed
 document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_2U, ConvertErrorAction::Delete);

 // Save output document
 document->Save(_dataDir + outfilename);
 std::clog << __func__ << ": Finish" << std::endl;
}
```

## Add Attachment to PDF/A file

In case you have a requirement to attach files to PDF/A compliance format, then we recommend using PDF_A_3A value from Aspose.PDF.PdfFormat enumeration.
PDF/A_3a is the format that provides the feature to attach any file format as an attachment to PDF/A compliant file.

```cpp
void ConverttoPDFA_AddAttachment()
{
 std::clog << __func__ << ": Start" << std::endl;
 // String for path name
 String _dataDir("C:\\Samples\\Conversion\\");

 // String for input file name
 String infilename("sample.pdf");
 // String for log file name
 String logfilename("log.xml");
 // String for input file name
 String outfilename("PDFToPDFA3b_out.pdf");

 // Open document
 auto document = new Document(_dataDir + infilename);

 // Setup new file to be added as attachment
 auto fileSpecification = MakeObject<FileSpecification>(_dataDir + String("aspose-logo.jpg"), String("Large Image file"));
 // Add attachment to document's attachment collection
 document->get_EmbeddedFiles()->Add(fileSpecification);

 // Convert to PDF/A compliant document
 // During conversion process, the validation is also performed
 document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_3A, ConvertErrorAction::Delete);

 // Save output document
 document->Save(_dataDir + outfilename);
 std::clog << __func__ << ": Finish" << std::endl;
}
```

## Replace missing fonts with alternative fonts

As per PDFA standards, fonts should be embedded in PDFA document. However, if the fonts are not embedded in the source document or exist on the machine then PDFA fails the validation. In this case, we have a requirement to substituent missing fonts with some alternative fonts from the machine. We can substitute missing fonts using the SimpleFontSubsituation method as following during PDF to PDFA conversion.

```cpp
void ConverttoPDFA_ReplaceFont()
{
 std::clog << __func__ << ": Start" << std::endl;
 // String for path name
 String _dataDir("C:\\Samples\\Conversion\\");

 // String for input file name
 String infilename("sample.pdf");
 // String for log file name
 String logfilename("log.xml");
 // String for input file name
 String outfilename("PDFToPDFA3b_out.pdf");

 // Open document
 auto document = new Document(_dataDir + infilename);

 System::SharedPtr<Aspose::Pdf::Text::Font> originalFont;
 try
 {
  originalFont = FontRepository::FindFont(String("AgencyFB"));
 }
 catch (Exception)
 {
  // Font is missing on destination machine
  auto substitutions = FontRepository::get_Substitutions();
  auto substitution = MakeObject<SimpleFontSubstitution>(String("AgencyFB"), String("Helvetica"));
  substitutions->Add(substitution);
 }

 // Convert to PDF/A compliant document
 try {
  // During conversion process, the validation is also performed
  document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_1B, ConvertErrorAction::Delete);

  // Save output document
  document->Save(_dataDir + outfilename);
 }
 catch (Exception ex) {
  std::cerr << ex->get_Message();
 }
 std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="primary" %}}
**Try to convert PDF to PDF/A online**

Aspose.PDF for C++ presents you online free application ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to PDF/A with Free App](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


