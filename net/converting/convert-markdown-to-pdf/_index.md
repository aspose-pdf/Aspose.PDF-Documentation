---
title: Convert Markdown to PDF | C#
linktitle: Convert Markdown to PDF
type: docs
weight: 270
url: /net/convert-markdown-to-pdf/
lastmod: "2020-12-27"
description: This article discribes that Aspose.PDF for .NET allows to create a PDF document based on input Markdown data file.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**This feature is supported by version 19.6 or greater.**

## Live Example

Aspose.PDF for .NET presents you online free application ["Markdown to PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf), where you may try to investigate the functionality and quality it works.

[![Convert Markdown to PDF](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)

Aspose.PDF for .NET provides the functionality to create a PDF document based on input [Markdown](https://daringfireball.net/projects/markdown/syntax) data file. In order to convert the Markdown to PDF, you need to initialize the [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) using [MdLoadOptions](https://apireference.aspose.com/pdf/net/aspose.pdf/mdloadoptions).

The following code snippet shows how to use this functionality with Aspose.PDF library:

```csharp
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Open Markdown document
Document pdfDocument= new Document(dataDir + "sample.md", new MdLoadOptions());
// Save document in PDF format
pdfDocument.Save(dataDir + "MarkdownToPDF.pdf");
```
