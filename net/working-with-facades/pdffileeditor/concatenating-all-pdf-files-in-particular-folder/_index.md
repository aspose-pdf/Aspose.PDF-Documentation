---
title: Concatenate PDF files in folder
linktitle: Concatenating PDF files
type: docs
weight: 70
url: /net/concatenating-all-pdf-files-in-particular-folder/
description: Aspose.PDF allows you concatenating all PDF files in Particular folder using C#.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF in C#** gives the opportunity to concatenate all PDF files in Particular folder.

[PdfFileEditor](http://www.aspose.com/api/net/pdf/aspose.pdf.facades/pdffileeditor) class in Aspose.Pdf.Facades namespace offers you the capability to concatenate the PDF file. You can even read all the Pdf files in a particular folder at runtime and concatenate them, without even knowing the file names. Simply provide the path of directory, which contains the PDF documents, that you would like to concatenate.

Please try using the following code snippet to achieve this functionality from Aspose.PDF:

```csharp
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

// Retrieve names of all the Pdf files in a particular Directory
string[] fileEntries = Directory.GetFiles(dataDir, "*.pdf");

// Get the current System date and set its format
string date = DateTime.Now.ToString("MM-dd-yyyy");
// Get the current System time and set its format
string hoursSeconds = DateTime.Now.ToString("hh-mm");
// Set the value for the final Resultant Pdf document
string masterFileName = date + "_" + hoursSeconds + "_out.pdf";

// Instantiate PdfFileEditor object
Aspose.Pdf.Facades.PdfFileEditor pdfEditor = new PdfFileEditor();

// Call Concatenate method of PdfFileEditor object to concatenate all input files
// Into a single output file
pdfEditor.Concatenate(fileEntries, dataDir + masterFileName);
```
