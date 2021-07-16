---
title: Extract Text from PDF File
type: docs
weight: 30
url: /java/extract-text/
description: This section explains how to extract text with Aspose.PDF Facades using PdfExtractor Class.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extract Text from the Whole PDF File (facades)

[pdfExtractor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor) class allows you to extract text from the whole PDF file. You need to create an object of [pdfExtractor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor) class and bind the input PDF file using [**bindPdf**](http://www.aspose.com/api/java/pdf/com.aspose.pdf.facades/classes/pdfextractor/methods/bindPdf\(java.lang.String\)/) method. [extractText](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor#extractText--) method helps you extract all the text into the memory. However, in order to get the text, you need to use getText method. The following code snippet shows you how to extract text from the whole PDF file.

```java

    public static void ExtractText(Boolean WholeText)
    {            
        // Create an object of the PdfExtractor class
        PdfExtractor pdfExtractor = new PdfExtractor();

        // Bind the input PDF
        pdfExtractor.bindPdf(_dataDir + "sample.pdf");

        // ExtractText
        pdfExtractor.extractText();

        if (!WholeText)
        {
            pdfExtractor.getText(_dataDir + "sample.txt");
        }
        else
        {
            // Extract the text into separate files
            int pageNumber = 1;
            while (pdfExtractor.hasNextPageText())
            {
                pdfExtractor.getNextPageText(_dataDir+"/sample"+pageNumber+".txt");
                pageNumber++;
            }
        }
    }
```
