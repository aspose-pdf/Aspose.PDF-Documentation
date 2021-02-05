---
title: Convert PDF to LaTeX/TeX 
linktitle: Convert PDF to LaTeX/TeX
type: docs
weight: 130
url: /java/convert-pdf-to-latex-tex/
lastmod: "2021-02-05"
description: This article describes the features of converting PDF files to LaTeX format. To convert PDF files to TeX, Aspose.PDF use the class LaTeXSaveOptions.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Java** support converting PDF to LaTeX/TeX.
The LaTeX file format is a text file format with the special markup and used in TeX-based document preparation system for high-quality typesetting.

{{% alert color="primary" %}}

Try online: You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-tex](https://products.aspose.app/pdf/conversion/pdf-to-tex)

{{% /alert %}}

To convert PDF files to TeX, Aspose.PDF has the class [LaTeXSaveOptions](https://apireference.aspose.com/pdf/java/com.aspose.pdf/class-use/LaTeXSaveOptions) which provides the property OutDirectoryPath for saving temporary images during the conversion process.

The following code snippet shows the process of converting PDF files into the TEX format with Java.

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPDFtoLATEX {

    private ConvertPDFtoLATEX() {

    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "PDFToTeX.pdf").toString();
        String texDocumentFileName = Paths.get(_dataDir.toString(), "PDFToTeX_out.tex").toString();
        
        // Create Document object
        Document doc = new Document(pdfDocumentFileName);

        // Instantiate LaTex save option           
        TeXSaveOptions saveOptions = new TeXSaveOptions();

        // Specify the output directory
        String pathToOutputDirectory = _dataDir.toString();

        // Set the output directory path for save option object
        saveOptions.setOutDirectoryPath(pathToOutputDirectory);

        // Save PDF file into LaTex format            
        doc.save(texDocumentFileName, saveOptions);
    }

}
```
