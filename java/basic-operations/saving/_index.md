---
title: Save PDF document programmatically
linktitle: Save 
type: docs
weight: 30
url: /java/save-pdf-document/
description: Learn how to save PDF file with Aspose.PDF for Java library. 
aliases:
    - /java/saving/
lastmod: "2021-02-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Save PDF document to file system

You can save the created or manipulated PDF document to file system using Save method of [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) class.
When you do not provide the format type (options), then the document is saved in Aspose.PDF v.1.7 (*.pdf) format.

```java
package com.aspose.pdf.examples;


import java.io.FileOutputStream;

import java.nio.file.Path;
import java.nio.file.Paths;
import com.aspose.pdf.*;

public final class BasicOperationsSave {

    private BasicOperationsSave() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) {
        SaveDocument();
        SaveDocumentStream();
        SaveDocumentAsPDFx();
    }

    public static void SaveDocument() {
        String originalFileName = _dataDir + "/SimpleResume.pdf";
        String modifiedFileName = _dataDir + "/SimpleResumeModified.pdf";

        Document pdfDocument = new Document(originalFileName);
        // make some manipation, i.g add new empty page
        pdfDocument.getPages().add();
        pdfDocument.save(modifiedFileName);
    }
```

## Save PDF document to stream

You can also save the created or manipulated PDF document to stream by using overloads of Save methods.

```java
public static void SaveDocumentStream() {
        String originalFileName = _dataDir + "/SimpleResume.pdf";
        String modifiedFileName = _dataDir + "/SimpleResumeModified.pdf";

        Document pdfDocument = new Document(originalFileName);
        // make some manipation, i.g add new empty page
        pdfDocument.getPages().add();
        try {
            pdfDocument.save(new FileOutputStream(modifiedFileName));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

    }

```

## Save PDF document in Web applications

To save documents in Web applications, you can use the ways proposed above. In addition, the [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) class has overloaded method Save.
```java
    // @RequestMapping(value = "/files/{file_name}", method = RequestMethod.GET)
    // public void getFile(@PathVariable("file_name") String fileName, HttpServletResponse response) {
    //     try {
    //         response.setContentType("application/pdf");
    //         // get your file as InputStream
    //         InputStream is = new FileInputStream(_dataDir + fileName);
    //         // copy it to response's OutputStream
    //         org.apache.commons.io.IOUtils.copy(is, response.getOutputStream());
    //         response.flushBuffer();
    //     } catch (IOException ex) {
    //         log.info("Error writing file to output stream. Filename was '{}'", fileName, ex);
    //         throw new RuntimeException("IOError writing file to output stream");
    //     }
    // }
```

For more detailed explanation please follow to [Showcase]() section.

## Save PDF/A or PDF/X format

PDF/A is an ISO-standardized version of the Portable Document Format (PDF) for use in archiving and long-term preservation of electronic documents.
PDF/A differs from PDF in that it prohibits features not suitable for long-term archiving, such as font linking (as opposed to font embedding) and encryption. ISO requirements for PDF / A viewers include color management guidelines, embedded font support, and a user interface for reading embedded annotations.

PDF/X is a subset of the PDF ISO standard. The purpose of PDF/X is to facilitate graphics exchange, and it therefore has a series of printing-related requirements which do not apply to standard PDF files.

In both cases, the Save method is used to store the documents, while the documents must be prepared using the Convert method.

```java
public static void SaveDocumentAsPDFx() {
        Document pdfDocument = new Document("../../../Samples/SimpleResume.pdf");
        pdfDocument.getPages().add();
        pdfDocument.convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
        pdfDocument.save("../../../Samples/SimpleResume_X3.pdf");
    }

}
```
