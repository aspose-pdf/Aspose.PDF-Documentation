---
title: Convert PDF to EPUB 
linktitle: Convert PDF to EPUB
type: docs
weight: 170
url: /java/convert-pdf-to-epub/
lastmod: "2021-06-05"
description: Aspose.PDF for Java supports the feature to convert PDF documents to EPUB format. You may try using the code snippet to accomplish this requirement.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

EPUB (short for electronic publication) is a free and open e-book standard from the International Digital Publishing Forum (IDPF). Files have the extension .epub.EPUB is designed for reflowable content, meaning that an EPUB reader can optimize text for a particular display device. EPUB also supports fixed-layout content. The format is intended as a single format that publishers and conversion houses can use in-house, as well as for distribution and sale. It supersedes the Open eBook standard.


{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-epub](https://products.aspose.app/pdf/conversion/pdf-to-epub)

{{% /alert %}}

Aspose.PDF for Java supports the feature to convert PDF documents to EPUB format. Aspose.PDF for Java has a class named [EpubSaveOptions](https://apireference.aspose.com/pdf/java/com.aspose.pdf/classes/EpubSaveOptions) which can be used as the second argument to the [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/classes/Document).save(..) method, to generate an EPUB file. Please try using the following code snippet to accomplish this requirement.

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPDFtoEPUB {

    private ConvertPDFtoEPUB() {

    }

    // The path to the documents directory.
    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {

        // Load PDF document
        Document pdfDocument = new Document(_dataDir + "PDFToEPUB.pdf");
        // Instantiate Epub Save options
        EpubSaveOptions options = new EpubSaveOptions();
        // Specify the layout for contents
        options.ContentRecognitionMode = EpubSaveOptions.RecognitionMode.Flow;
        // Save the ePUB document
        pdfDocument.save(_dataDir + "PDFToEPUB_out.epub", options);
    }
}
```