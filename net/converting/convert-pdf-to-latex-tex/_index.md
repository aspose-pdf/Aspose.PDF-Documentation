---
title: Convert PDF to LaTeX/TeX
type: docs
weight: 290
url: /net/convert-pdf-to-latex-tex/
---
# Convert PDF to LaTeX/TeX

The LaTeX file format is a text file format with markup in the LaTeX 2ε derivative of the TeX family of languages and LaTeX is a derived format of the TeX system.

>Try online: You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-tex](https://products.aspose.app/pdf/conversion/pdf-to-tex)

To convert PDF files to TeX, Aspose.PDF has the class [LaTeXSaveOptions](https://apireference.aspose.com/pdf/net/aspose.pdf/latexsaveoptions) which provides the property OutDirectoryPath for saving temporary images during the conversion process.

The following code snippet shows the process of converting PDF files into the TEX format.

```// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
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