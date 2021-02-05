---
title: Convert Markdown to PDF 
linktitle: Convert Markdown to PDF
type: docs
weight: 270
url: /java/convert-markdown-to-pdf/
lastmod: "2021-02-05"
description: This article discribes that Aspose.PDF for Java allows to create a PDF document based on input Markdown data file.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Markdown is a text to HTML conversion tool for web authors. Markdown allows you to write in an easy-to-read and write plain text format and then convert it to structurally valid XHTML (or HTML).

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/md-to-pdf](https://products.aspose.app/pdf/conversion/md-to-pdf)

{{% /alert %}}


The following code snippet shows how to use this functionality with Aspose.PDF for Java:

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertMDtoPDF {

    private ConvertMDtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Instantiate Latex Load option object
        MdLoadOptions options = new MdLoadOptions();
        
        // Create Document object
        String markdownFileName = Paths.get(_dataDir.toString(), "samplefile.md").toString();
        Document document = new Document(markdownFileName, options);

        // Save output PDF document
        document.save(Paths.get(_dataDir.toString(),"MarkdownToPDF.pdf").toString());
    }
}

```
