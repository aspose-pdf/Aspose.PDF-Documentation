---
title: Convert PDF to text 
linktitle: Convert PDF to text
type: docs
weight: 120
url: /androidjava/convert-pdf-to-txt/
lastmod: "2021-06-05"
description: With Aspose.PDF for Java you can convert a whole PDF document to a text file or convert only a PDF page to a text file.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Java** support converting whole PDF document and single page to a Text file. 

## Convert whole PDF document to Text file

You can convert PDF document to TXT file using Visit method of [TextAbsorber](https://apireference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) class.

The following code snippet explains how to extract the texts from the all pages.

```java
package com.aspose.pdf.examples;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public class ConvertPDFtoTXT {
    private ConvertPDFtoTXT() {

    }

    // The path to the documents directory.
    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {
        ConvertPDFDoctoTXT();
        ConvertPDFPagestoTXT();
    }

    public static void ConvertPDFDoctoTXT() throws IOException {
        // Open document
        String pdfFileName = Paths.get(_dataDir.toString(), "demo.pdf").toString();
        String txtFileName = Paths.get(_dataDir.toString(), "PDFToTXT_out.txt").toString();

        // Load PDF document
        Document pdfDocument = new Document(pdfFileName);
        TextAbsorber ta = new TextAbsorber();
        ta.visit(pdfDocument);
        // Save the extracted text in text file
        BufferedWriter writer = new BufferedWriter(new FileWriter(txtFileName));
        writer.write(ta.getText());
        writer.close();
    }

```

{{% alert color="primary" %}} 

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-txt](https://products.aspose.app/pdf/conversion/pdf-to-txt)

{{% /alert %}}

## Convert PDF page to text file

You can convert PDF document to TXT file with Aspose.PDF for Java. You should use Visit method of [TextAbsorber](https://apireference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) class for resolve this task.

The following code snippet explains how to extract the texts from the particular pages.

```java
public static void ConvertPDFPagestoTXT() throws IOException {
        String pdfFileName = Paths.get(_dataDir.toString(), "demo.pdf").toString();
        String txtFileName = Paths.get(_dataDir.toString(), "PDFToTXT_out.txt").toString();

        // Load PDF document
        Document pdfDocument = new Document(pdfFileName);

        TextAbsorber ta = new TextAbsorber();
        int[] pages = new int[] { 1, 3, 4 };

        for (int page : pages) {
            ta.visit(pdfDocument.getPages().get_Item(page));
        }

        // Save the extracted text in text file
        BufferedWriter writer = new BufferedWriter(new FileWriter(txtFileName));
        writer.write(ta.getText());
        writer.close();
    }
}
```
