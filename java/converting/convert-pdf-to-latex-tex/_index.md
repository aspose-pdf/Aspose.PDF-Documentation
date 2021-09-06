---
title: Convert PDF to LaTeX/TeX Java
linktitle: Convert PDF to LaTeX/TeX
type: docs
weight: 130
url: /java/convert-pdf-to-latex-tex/
lastmod: "2021-06-05"
description: This article describes the features of converting PDF files to LaTeX format. To convert PDF files to TeX, Aspose.PDF use the class LaTeXSaveOptions.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for Java** support converting PDF to LaTeX/TeX.
The LaTeX file format is a text file format with the special markup and used in TeX-based document preparation system for high-quality typesetting.

{{% alert color="primary" %}}

Try online: You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-tex](https://products.aspose.app/pdf/conversion/pdf-to-tex)

{{% /alert %}}

To convert PDF files to TeX, Aspose.PDF has the class [TeXSaveOptions](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TeXSaveOptions) which provides the method `setOutDirectoryPath` for saving temporary images during the conversion process.

The following code snippet shows the process of converting PDF files into the TEX format with Java.

```java
/    public static void name() {
        // Create Document object
        com.aspose.pdf.Document doc = new com.aspose.pdf.Document(_dataDir + "PDFToTeX.pdf");
        
        // Instantiate LaTex save option          
        com.aspose.pdf.TeXSaveOptions saveOptions = new com.aspose.pdf.TeXSaveOptions();
        
        // Specify the output directory
        String pathToOutputDirectory = _dataDir;
        
        // Set the output directory path for save option object
        saveOptions.setOutDirectoryPath (pathToOutputDirectory);
        
        // Save PDF file into LaTex format           
        doc.save(_dataDir + "PDFToTeX_out.tex", saveOptions);        
    }
```
