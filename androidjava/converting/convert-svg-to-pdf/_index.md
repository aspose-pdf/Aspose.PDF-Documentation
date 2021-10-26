---
title: Convert SVG to PDF 
linktitle: Convert SVG to PDF
type: docs
weight: 240
url: /androidjava/convert-svg-to-pdf/
lastmod: "2021-06-05"
description: This page shows the possibility of converting SVG to PDF with Aspose.PDF and describes how to get SVG dimensions and overview SVG Supported Features.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Scalable Vector Graphics (SVG) is a family of specifications of an XML-based file format for two-dimensional vector graphics, both static and dynamic (interactive or animated). The SVG specification is an open standard that has been under development by the World Wide Web Consortium (W3C) since 1999.

SVG images and their behaviors are defined in XML text files. This means that they can be searched, indexed, scripted and, if required, compressed. As XML files, SVG images can be created and edited with any text editor, but it is often more convenient to create them with drawing programs such as Inkscape

## How to convert SVG file to PDF format

To convert SVG files to PDF, use the class named [SvgLoadOptions](https://apireference.aspose.com/pdf/java/com.aspose.pdf/svgsaveoptions) which is used to initialize the [LoadOptions](https://apireference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions) object. Later, this object is passed as an argument during the [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/document) object initialization and helps the PDF rendering engine to determine the input format of the source document.

The following code snippet shows the process of converting SVG file into PDF format.

```java
package com.aspose.pdf.examples;

/**
 * Convert SVG to PDF
 */

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertSVGtoPDF {

    private ConvertSVGtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        ConvertSvgToPDF_Simple();
    }

    public static void ConvertSvgToPDF_Simple() {
        // Initialize document object

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "svg_test.pdf").toString();
        String svgDocumentFileName = Paths.get(_dataDir.toString(), "car.svg").toString();
        
        SvgLoadOptions option = new SvgLoadOptions();
        Document pdfDocument = new Document(svgDocumentFileName, option);
        pdfDocument.save(pdfDocumentFileName);
    }
```
