---
title: Convert PDF to XPS 
linktitle: Convert PDF to XPS
type: docs
weight: 160
url: /java/convert-pdf-to-xps/
lastmod: "2021-06-05"
description: This page describes the definition of an XPS document and how to use it. Convert PDF to XPS with Aspose.PDF for Java, using XpsSaveOptions class. 
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-xps](https://products.aspose.app/pdf/conversion/pdf-to-xps)

{{% /alert %}}

The XPS file type is primarily associated with the XML Paper Specification by Microsoft Corporation. The XML Paper Specification (XPS), formerly codenamed Metro and subsuming the Next Generation Print Path (NGPP) marketing concept, is Microsoft's initiative to integrate document creation and viewing into the Windows operating system.

To convert PDF files to XPS, Aspose.PDF has the class [XpsSaveOptions](https://apireference.aspose.com/pdf/java/com.aspose.pdf/XpsSaveOptions) class that is used as the second argument to the Document.save(..) constructor to generate the XPS file. The following code snippet shows the process of converting PDF files into XPS format.

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPDFtoXPS {

    private ConvertPDFtoXPS() {

    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo.pdf").toString();
        String xpsDocumentFileName = Paths.get(_dataDir.toString(), "demo_out.xps").toString();
        
        // Create Document object
        Document doc = new Document(pdfDocumentFileName);

        // Instantiate XPS Save options
        XpsSaveOptions saveOptions = new XpsSaveOptions();

        // Save output in XML format
        doc.save(xpsDocumentFileName, saveOptions);
    }

}
```