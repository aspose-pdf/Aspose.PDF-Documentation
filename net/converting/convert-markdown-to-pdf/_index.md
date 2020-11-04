---
title: Convert Markdown to PDF
type: docs
weight: 170
url: /net/convert-markdown-to-pdf/
---
# Convert Markdown to PDF

> This feature is supported by version 19.6 or greater.

>Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/md-to-pdf](https://products.aspose.app/pdf/conversion/md-to-pdf)

Aspose.PDF for .NET  provides the functionality to create a PDF document based on input Markdown data file. In order to convert the markdown to PDF, you need to initialize the Document using MdLoadOptions. The following code snippet shows how to use this functionality:

```csharp
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Open Markdown document
Document pdfDocument= new Document(dataDir + "sample.md", new MdLoadOptions());
// Save document in PDF format
pdfDocument.Save(dataDir + "MarkdownToPDF.pdf");
```
