---
title: Convert PDF to SVG 
linktitle: Convert PDF to SVG
type: docs
weight: 60
url: /java/convert-pdf-to-svg/
lastmod: "2021-06-05"
description: Aspose.PDF for Java supports the feature to convert SVG images to PDF format using SvgSaveOptions class.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

This article teacher you how to convert PDF to <abbr title="Scalable Vector Graphics">SVG</abbr> using Java

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-svg](https://products.aspose.app/pdf/conversion/pdf-to-svg)

{{% /alert %}}

**Scalable Vector Graphics (SVG)** is a family of specifications of an XML-based file format for two-dimensional vector graphics, both static and dynamic (interactive or animated). The SVG specification is an open standard that has been under development by the World Wide Web Consortium (W3C) since 1999.

SVG images and their behaviors are defined in XML text files. This means that they can be searched, indexed, scripted and if required, compressed. As XML files, SVG images can be created and edited with any text editor, but it is often more convenient to create them with drawing programs such as Inkscape.

## Convert PDF pages to SVG images

Aspose.PDF for Java supports the feature to convert PDF file to SVG format. To accomplish this requirement, the [SvgSaveOptions](https://apireference.aspose.com/java/pdf/com.aspose.pdf/SvgSaveOptions) class has been introduced into the com.aspose.pdf package. Instantiate an object of [SvgSaveOptions](https://apireference.aspose.com/java/pdf/com.aspose.pdf/SvgSaveOptions) and pass it as a second argument to the [Document](https://apireference.aspose.com/java/pdf/com.aspose.pdf/Document).save(..) method.

The following code snippet shows the steps for converting a PDF file to SVG format.

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public class ConvertPDFtoSVG {
    private ConvertPDFtoSVG() {

    }

    // The path to the documents directory.
    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {
        String pdfFileName = Paths.get(_dataDir.toString(), "input.pdf").toString();
        String svgFileName = Paths.get(_dataDir.toString(), "PDFToSVG_out.svg").toString();
        
        // Load PDF document
        Document doc = new Document(pdfFileName);
        
        // Instantiate an object of SvgSaveOptions
        SvgSaveOptions saveOptions = new SvgSaveOptions();
        
        // Do not compress SVG image to Zip archive
        saveOptions.CompressOutputToZipArchive = false;
        
        // Save the output in SVG files
        doc.save(svgFileName, saveOptions);
    }

}
```