---
title: Convert PDF File to PDF/A | C#
linktitle: Convert PDF File to PDF/A
type: docs
weight: 180
url: /net/convert-pdf-file-to-pdfa/
lastmod: "2021-06-05"
description: This topic show you how to Aspose.PDF allows to convert a PDF file to a PDF/A compliant PDF file. 
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for .NET** allows you to convert a PDF file to a <abbr title="Portable Document Format / A">PDF/A</abbr> compliant PDF file. Before doing so, the file must be validated. This topic explains how.

{{% alert color="primary" %}}

Please note we follow Adobe Preflight for validating PDF/A conformance. All tools on the market have their own “representation” of PDF/A conformance. Please check this article on PDF/A validation tools for reference. We chose Adobe products for verifying how Aspose.PDF produces PDF files because Adobe is at the center of everything connected to PDF.

{{% /alert %}}

Convert the file using the Document class Convert method. Before converting the PDF to PDF/A compliant file, validate the PDF using the Validate method. The validation result is stored in an XML file and then this result is also passed to the Convert method. You can also specify the action for the elements which cannot be converted using the ConvertErrorAction enumeration.

## Live Example

Aspose.PDF for .NET presents you online free application ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), where you may try to investigate the functionality and quality it works.

[![C# convert PDF to PDF/A](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)

## Convert PDF file to PDF/A-1b

The following code snippet shows how to convert PDF files to PDF/A-1b compliant PDF.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Open document
Document pdfDocument = new Document(dataDir + "PDFToPDFA.pdf");
           
// Convert to PDF/A compliant document
// During conversion process, the validation is also performed
pdfDocument.Convert(dataDir + "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

dataDir = dataDir + "PDFToPDFA_out.pdf";
// Save output document
pdfDocument.Save(dataDir);
```

To perform validation only, use the following line of code:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Open document
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// Validate PDF for PDF/A-1a
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1B);
```

## Convert PDF file to PDF/A-3b

Aspose.PDF for .NET also supports the feature to convert a PDF file to PDF/A-3b format.

```csharp
/ For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Open document
Document pdfDocument = new Document(dataDir + "input.pdf");           
           
pdfDocument.Convert(new MemoryStream(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

dataDir = dataDir + "PDFToPDFA3b_out.pdf";
// Save output document
pdfDocument.Save(dataDir);
```

## Convert PDF file to PDF/A-2u

Aspose.PDF for .NET also supports the feature to convert a PDF file to PDF/A-2u format.

```csharp
string inFile = "input.pdf";
string outFile = "output.pdf";
Aspose.PDF.Document doc = new Aspose.PDF.Document(inFile);
doc.Convert(new MemoryStream(), PdfFormat.PDF_A_2U, ConvertErrorAction.Delete);
doc.Save(outFile);
```

## Convert PDF file to PDF/A-3u

Aspose.PDF for .NET also supports the feature to convert a PDF file to PDF/A-3u format.

```csharp
string inFile = "input.pdf";
string outFile = "output.pdf";
Aspose.PDF.Document doc = new Aspose.PDF.Document(inFile);
doc.Convert(new MemoryStream(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);
doc.Save(outFile);
```

## Add Attachment to PDF/A file

In case you have a requirement to attach files to PDF/A compliance format, then we recommend using PDF_A_3A value from Aspose.PDF.PdfFormat enumeration.
PDF/A_3a is the format that provides the feature to attach any file format as an attachment to PDF/A compliant file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Instantiate Document instance to load existing file
Aspose.Pdf.Document doc = new Document(dataDir + "input.pdf");
// Setup new file to be added as attachment
FileSpecification fileSpecification = new FileSpecification(dataDir + "aspose-logo.jpg", "Large Image file");
// Add attachment to document's attachment collection
doc.EmbeddedFiles.Add(fileSpecification);
// Perform conversion to PDF/A_3a so attachment is included in resultnat file
doc.Convert(dataDir + "log.txt", Aspose.Pdf.PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
// Save resultant file
doc.Save(dataDir + "AddAttachmentToPDFA_out.pdf");
```

## Replace missing fonts with alternative fonts

As per PDFA standards, fonts should be embedded in PDFA document. However, if the fonts are not embedded in the source document or exist on the machine then PDFA fails the validation. In this case, we have a requirement to substituent missing fonts with some alternative fonts from the machine. We can substitute missing fonts using the SimpleFontSubsituation method as following during PDF to PDFA conversion.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Aspose.Pdf.Text.Font originalFont = null;
try
{
    originalFont = FontRepository.FindFont("AgencyFB");
}
catch (Exception)
{
    // Font is missing on destination machine
    FontRepository.Substitutions.Add(new SimpleFontSubstitution("AgencyFB", "Arial"));
}
var fileNew = new FileInfo(dataDir + "newfile_out.pdf");
var pdf = new Document(dataDir + "input.pdf");
pdf.Convert( dataDir +  "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
pdf.Save(fileNew.FullName);
```
