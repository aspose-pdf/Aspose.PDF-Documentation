---
title: Create Document
type: docs
weight: 10
url: /java/create-pdf-document/
description: Aspose.PDF for Java helps you to create PDF document and searchable PDF file in few easy steps.
lastmod: "2025-02-17"
TechArticle: true
AlternativeHeadline: Guide on using the Aspose.PDF for Java API to generate and read PDF files
Abstract: This article provides a comprehensive guide on using the Aspose.PDF for Java API to generate and read PDF files within Java applications. Aspose.PDF for Java allows developers to embed PDF processing capabilities directly into their applications, eliminating the need for additional software installations. It supports various Java application types, including Desktop, JSP, and JSF applications. The article outlines a step-by-step process for creating PDF files using Java by instantiating a `Document` object, adding a `Page` to its pages collection, inserting a `TextFragment` into the page's paragraphs, and saving the document. An example code snippet demonstrates the creation of a simple one-page PDF with "Hello, World!" text. Additionally, the article explores creating searchable PDFs using Aspose.PDF for Java. It details the use of a callback function to perform text recognition on PDF images, leveraging external OCR tools like Google Tesseract. The complete code example illustrates the conversion process, including handling image files and generating the searchable.
SoftwareApplication: java
---

 In this article, we are going to show how to use Aspose.PDF for Java API to easily generate and read PDF files in Java applications.

Aspose.PDF for Java API lets Java application developers to embed PDF documents processing functionality in their applications. It can be used to create and read PDF files without the need of any other software installed on the underlying machine. Aspose.PDF for Java can be used in a variety of Java application types such as Desktop, JSP, and JSF applications.

## How to Create PDF File using Java

To create a PDF file using Java, the following steps can be used.

1. Create an object of [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) class
1. Add a [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) object to the Pages collection of the Document object
1. Add [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) to [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) collection of the page
1. Save the resultant PDF document

```java
package com.aspose.pdf.examples;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;
import com.aspose.pdf.Document.CallBackGetHocr;

public class ExampleCreate {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Create() {
        Document document = new Document();

        //Add page
        Page page = document.getPages().add();

        // Add text to new page
        page.getParagraphs().add(new TextFragment("Hello World!"));

        // Save updated PDF
        document.save(_dataDir+"HelloWorld_out.pdf");
    }
```

In this case, we create a PDF one-page document with A4 page size, portrait orientation. Our page will contain a "Hello, World" in the upper left part of the page.

Also, Aspose.PDF for Java provides the ability to create how to create a searchable PDF. Let's learn the next code snippet:

```java
public static void CreateSearchablePDF() {
        Document doc = new Document(_dataDir + "sample1.pdf");

        // Create callBack - logic recognize text for pdf images. Use outer OCR supports HOCR standard(http://en.wikipedia.org/wiki/HOCR).
        // We have used free google tesseract OCR(http://en.wikipedia.org/wiki/Tesseract_%28software%29)

        CallBackGetHocr cbgh = new CallBackGetHocr() {
            @Override
            public String invoke(java.awt.image.BufferedImage img) {
                File outputfile = new File(_dataDir + "test.jpg");
                try {
                    ImageIO.write(img, "jpg", outputfile);
                } catch (IOException e1) {
                    e1.printStackTrace();
                }

                try {
                    java.lang.Process process = Runtime.getRuntime().exec("tesseract" + " " + _dataDir + "test.jpg" + " " + _dataDir + "out hocr");
                    System.out.println("tesseract" + " " + _dataDir + "test.jpg" + " " + _dataDir + "out hocr");
                    process.waitFor();

                } catch (IOException e) {
                    e.printStackTrace();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }

                // reading out.html to string
                File file = new File(_dataDir + "out.hocr");
                StringBuilder fileContents = new StringBuilder((int) file.length());
                Scanner scanner = null;
                try {
                    scanner = new Scanner(file);
                    String lineSeparator = System.getProperty("line.separator");

                    while (scanner.hasNextLine()) {
                        fileContents.append(scanner.nextLine() + lineSeparator);
                    }
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                } finally {
                    if (scanner != null)
                        scanner.close();
                }

                // deleting temp files
                File fileOut = new File(_dataDir + "out.hocr");
                if (fileOut.exists()) {
                    fileOut.delete();
                }
                File fileTest = new File(_dataDir + "test.jpg");
                if (fileTest.exists()) {
                    fileTest.delete();
                }

                return fileContents.toString();
            }
        };
        // End callBack

        doc.convert(cbgh);
        doc.save(_dataDir + "output971.pdf");
    }
}
```