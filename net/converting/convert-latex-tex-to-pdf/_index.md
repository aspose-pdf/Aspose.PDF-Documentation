---
title: Convert LaTeX/TeX to PDF | C#
linktitle: Convert LaTeX/TeX to PDF
type: docs
weight: 310
url: /net/convert-latex-tex-to-pdf/
lastmod: "2021-01-15"
description: This page describes the use of files in the LaTeX format. Also, article explains how to convert LaTeX files to PDF format with Aspose.PDF library.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

The LaTeX file format is a text file format with markup in the LaTeX derivative of the TeX family of languages and LaTeX is a derived format of the TeX system. LaTeX (ˈleɪtɛk/lay-tek or lah-tek) is a document preparation system and document markup language. It is widely used for the communication and publication of scientific documents in many fields, including mathematics, physics, and computer science. It also has a prominent role in the preparation and publication of books and articles that contain complex multilingual materials, such as Sanskrit and Arabic, including critical editions. LaTeX uses the TeX typesetting program for formatting its output, and is itself written in the TeX macro language.

## Live Example

Aspose.PDF for .NET presents you online free application ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), where you may try to investigate the functionality and quality it works.

[![TeX to PDF](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)

Aspose.PDF for .NET supports the feature to convert TeX files to PDF format and in order to accomplish this requirement, Aspose.Pdf namespace has a class named [LatexLoadOptions](https://apireference.aspose.com/pdf/net/aspose.pdf/latexloadoptions) which provides the capabilities to load LaTex files and render the output in PDF format using [Document class](https://apireference.aspose.com/pdf/net/aspose.pdf/document).
The following code snippet shows the process of converting LaTex file to PDF format with C#.

```csharp
public static void ConvertTeXtoPDF()
{
    // Instantiate Latex Load option object
    TeXLoadOptions options = new TeXLoadOptions();
    // Create Document object
    Aspose.Pdf.Document pdfDocument= new Aspose.Pdf.Document(_dataDir + "samplefile.tex", options);
    // Save the output in PDF file
    pdfDocument.Save(_dataDir + "TeXToPDF_out.pdf");
}
```
