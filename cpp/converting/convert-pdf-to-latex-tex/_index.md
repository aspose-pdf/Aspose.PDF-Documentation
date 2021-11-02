---
title: Convert PDF to LaTeX 
linktitle: Convert PDF to LaTeX/TeX
type: docs
weight: 130
url: /cpp/convert-pdf-to-latex-tex/
lastmod: "2021-06-05"
description: This article describes the features of converting PDF files to LaTeX format. To convert PDF files to TeX, Aspose.PDF use the class LaTeXSaveOptions.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for C++** support converting PDF to LaTeX/TeX.
The LaTeX file format is a text file format with the special markup and used in TeX-based document preparation system for high-quality typesetting.

## Live Example

Aspose.PDF for C++ presents you online free application ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), where you may try to investigate the functionality and quality it works.

[![PDF to LaTeX](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)

To convert PDF files to TeX, Aspose.PDF has the class [LaTeXSaveOptions](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.la_te_x_save_options) which provides the property OutDirectoryPath for saving temporary images during the conversion process.

The following code snippet shows the process of converting PDF files into the TEX format with C++.

```cpp
void ConvertPDFtoLaTeX()
{
 std::clog << __func__ << ": Start" << std::endl;
 // String for path name
 String _dataDir("C:\\Samples\\Conversion\\");

 // String for input file name
 String infilename("sample.pdf");
 // String for output file name
 String outfilename("PDFToTeX_out.tex");

 // Open document
 auto document = MakeObject<Document>(_dataDir + infilename);

 // Instantiate LaTex save option
 auto saveOptions = MakeObject<LaTeXSaveOptions>();

 // Set the output directory path for save option object
 saveOptions->set_OutDirectoryPath(_dataDir);

 // Save PDF file into LaTex format
 document->Save(_dataDir + outfilename, saveOptions);
 std::clog << __func__ << ": Finish" << std::endl;
}
```
