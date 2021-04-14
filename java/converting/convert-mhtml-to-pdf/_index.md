---
title: Convert MHTML to PDF 
linktitle: Convert MHTML to PDF 
type: docs
weight: 290
url: /java/convert-mhtml-to-pdf/
lastmod: "2021-02-05"
description: This article describes how to convert MHT or MHTML files to PDF format programmatically with Aspose.PDF for Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/mhtml-to-pdf](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)

{{% /alert %}}

<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>, short for MIME HTML, is a web page archive format used to combine resources that are typically represented by external links (such as images, Flash animations, Java applets, and audio files) with HTML code into a single file. The content of an MHTML file is encoded as if it were an HTML email message, using the MIME type multipart/related.

Next code snippet show how to covert MHTML files to PDF format with Java:

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertMHTMLtoPDF {

    private ConvertMHTMLtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Instantiate MHTML Load option object
        MhtLoadOptions options = new MhtLoadOptions();
        
        // Create Document object
        String mhtmlFileName = Paths.get(_dataDir.toString(), "samplefile.mhtml").toString();
        Document document = new Document(mhtmlFileName, options);

        // Save output PDF document
        document.save(Paths.get(_dataDir.toString(),"TEXtoPDF.pdf").toString());
    }
}
```

