---
title: PDF to LaTeX using C#
linktitle: Convert PDF to LaTeX/TeX
type: docs
weight: 130
url: /net/convert-pdf-to-latex-tex/
lastmod: "2021-06-05"
description: This article describes the features of converting PDF files to LaTeX format. To convert PDF files to TeX, Aspose.PDF use the class LaTeXSaveOptions.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for .NET** support converting PDF to LaTeX/TeX.
The LaTeX file format is a text file format with the special markup and used in TeX-based document preparation system for high-quality typesetting.

## Live Example

Aspose.PDF for .NET presents you online free application ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), where you may try to investigate the functionality and quality it works.

[![PDF to LaTeX](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)

To convert PDF files to TeX, Aspose.PDF has the class [LaTeXSaveOptions](https://apireference.aspose.com/pdf/net/aspose.pdf/latexsaveoptions) which provides the property OutDirectoryPath for saving temporary images during the conversion process.

The following code snippet shows the process of converting PDF files into the TEX format with C#.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Create Document object
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "PDFToTeX.pdf");

// Instantiate LaTex save option          
LaTeXSaveOptions saveOptions = new LaTeXSaveOptions();

// Specify the output directory
string pathToOutputDirectory = dataDir;

// Set the output directory path for save option object
saveOptions.OutDirectoryPath = pathToOutputDirectory;

// Save PDF file into LaTex format           
doc.Save(dataDir + "PDFToTeX_out.tex", saveOptions);
```
