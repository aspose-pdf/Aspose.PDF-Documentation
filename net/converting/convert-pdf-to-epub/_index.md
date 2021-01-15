---
title: Convert PDF to EPUB
linktitle: Convert PDF to EPUB
type: docs
weight: 170
url: /net/convert-pdf-to-epub/
lastmod: "2020-12-27"
description: Aspose.PDF for .NET supports the feature to convert PDF documents to EPUB format. You may try using the code snippet to accomplish this requirement.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-epub](https://products.aspose.app/pdf/conversion/pdf-to-epub)

{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr> (short for Electronic Publication)** is a free and open e-book standard from the International Digital Publishing Forum (IDPF). Files have the extension .epub.
EPUB is designed for reflowable content, meaning that an EPUB reader can optimize text for a particular display device. EPUB also supports fixed-layout content. The format is intended as a single format that publishers and conversion houses can use in-house, as well as for distribution and sale. It supersedes the Open eBook standard.

Aspose.PDF for .NET also supports the feature to convert PDF documents to EPUB format. Aspose.PDF for .NET has a class named EpubSaveOptions which can be used as the second argument to [`Document.Save(..)`](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) method, to generate an EPUB file.
Please try using the following code snippet to accomplish this requirement with C#. 

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Load PDF document
Document pdfDocument = new Document(dataDir + "PDFToEPUB.pdf");
// Instantiate Epub Save options
EpubSaveOptions options = new EpubSaveOptions();
// Specify the layout for contents
options.ContentRecognitionMode = EpubSaveOptions.RecognitionMode.Flow;
// Save the ePUB document
pdfDocument.Save(dataDir + "PDFToEPUB_out.epub", options);
```
