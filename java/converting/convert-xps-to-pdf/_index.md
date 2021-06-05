---
title: Convert XPS to PDF 
linktitle: Convert XPS to PDF
type: docs
weight: 330
url: /java/convert-xps-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF for Java allows you to convert XPS to PDF files with a class named XpsLoadOptions. Check code snippet to solve this task. 
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Java** support feature converting <abbr title="XML Paper Specification">XPS</abbr> files to PDF format. Check this article to resolve your tasks.

## Convert XPS to PDF 

XPS, XML Paper Specification, is a Microsoft file format used to integrate document creation and viewing into Windows. With Aspose.PDF for Java, it is possible to convert XPS files to PDF, the portable file format from Adobe.

The file format is basically a zipped XML file, primarily used for distribution and storage. It's very difficult to edit and mostly implemented by Microsoft.


To convert an XPS file to PDF using [Aspose.PDF for Java](https://products.aspose.com/pdf/java), use [XpsLoadOptions](https://apireference.aspose.com/java/pdf/com.aspose.pdf/XpsLoadOptions) class. This is used to initialize a [LoadOptions](https://apireference.aspose.com/java/pdf/com.aspose.pdf/LoadOptions) object. Later, this object is passed as an argument during the [Document](https://apireference.aspose.com/java/pdf/com.aspose.pdf/document) object initialization and helps the PDF rendering engine to determine the source document's input format.

In both XP and Windows 7, you should find an XPS Printer pre-installed if you look in the Control Panel and then Printers. To create XPS files you can use that printer for the output device. In Windows 7, you should be able to just double-click the file to open it in an XPS viewer. You may also download [XPS viewer](http://windows.microsoft.com/en-US/windows-vista/what-is-the-xps-viewer) from Microsoft's website.

The following code snippet shows the process of converting the XPS file into PDF format.

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertXPStoPDF {

final static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

public static void main(String[] args) throws IOException {
Convert_XPS_to_PDF();
}

public static void Convert_XSLFO_to_PDF() throws IOException {
// Initialize document object

String pdfDocumentFileName = Paths.get(_dataDir.toString(), "sample.pdf").toString();
String xpsDocumentFileName = Paths.get(_dataDir.toString(), "sample.xps").toString();

// Instantiate LoadOption object using XPS load option
LoadOptions options = new XpsLoadOptions();

// Instantiate a Document object by calling its empty constructor
Document pdfDocument = new Document(xpsDocumentFileName, options);

// Save resultant PDF file
pdfDocument.save(pdfDocumentFileName);
}

```

