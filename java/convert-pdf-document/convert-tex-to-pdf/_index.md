---
title: Convert LaTeX/TeX to PDF 
linktitle: Convert LaTeX/TeX to PDF
type: docs
weight: 310
url: /java/convert-latex-tex-to-pdf/
lastmod: "2021-02-05"
description: This page describes the use of files in the LaTeX format. Also, article explains how to convert LaTeX files to PDF format with Aspose.PDFf or Java library. 
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

The LaTeX file format is a text file format with markup in the LaTeX derivative of the TeX family of languages and LaTeX is a derived format of the TeX system. LaTeX (ˈleɪtɛk/ lay-tek or lah-tek) is a document preparation system and document markup language. It is widely used for the communication and publication of scientific documents in many fields, including mathematics, physics, and computer science. It also has a prominent role in the preparation and publication of books and articles that contain complex multilingual materials, such as Sanskrit and Arabic, including critical editions. LaTeX uses the TeX typesetting program for formatting its output and is itself written in the TeX macro language.

**Aspose.PDF for Java** supports the feature to convert TeX files to PDF format and in order to accomplish this requirement, com.aspose.pdf package has a class named [LatexLoadOptions](https://apireference.aspose.com/pdf/java/com.aspose.pdf/LatexLoadOptions) which provides the capabilities to load LaTex files and render the output in PDF format using the [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/document) class. The following code snippet shows the process of converting LaTex file to PDF format.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertLATEXtoPDF {

    private ConvertLATEXtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Instantiate Latex Load option object
        TeXLoadOptions options = new TeXLoadOptions();
        
        // Create Document object
        String latexFileName = Paths.get(_dataDir.toString(), "samplefile.tex").toString();
        Document document = new Document(latexFileName, options);

        // Save output PDF document
        document.save(Paths.get(_dataDir.toString(),"TEXtoPDF.pdf").toString());
    }
}
```