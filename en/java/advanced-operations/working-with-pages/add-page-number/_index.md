---
title: Add Page Number to PDF 
linktitle: Add Page Number
type: docs
weight: 100
url: /java/add-page-number/
description: Aspose.PDF for Java allows you to add Page Number Stamp to your PDF file using PageNumber Stamp class.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: 
Abstract: This article provides a guide on how to add page numbers to a PDF document using Aspose.PDF for Java. The PageNumberStamp class is utilized to create a page number stamp, allowing customization of format, margins, alignments, starting number, and font attributes. The process involves creating a Document object and a PageNumberStamp object with the desired properties, followed by using the addStamp(..) method of the Page class to apply the stamp. The article includes a Java code snippet that demonstrates how to implement this functionality, including setting text properties such as font type, size, style, and color. The article also offers an online tool for checking the quality of Aspose.PDF conversion at the provided link.
---

All the documents must have page numbers in it. The page number makes it easier for the reader to locate different parts of the document.
**Aspose.PDF for Java** allows you to add page numbers with PageNumberStamp.

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/page-number](https://products.aspose.app/pdf/page-number)

{{% /alert %}}

You can use [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) class to add a page number stamp in a PDF document. The [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) class provides methods to create a page number based stamp like format, margins, alignments, starting number etc. In order to add page number stamp, you need to create a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object and a [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) object with required properties. After that, you can call [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) method of the [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) class to add the stamp in PDF file. You can also set the font attributes of the page number stamp.

The following code snippet shows you how to add page numbers in a PDF file.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.FontStyles;
import com.aspose.pdf.HorizontalAlignment;
import com.aspose.pdf.PageNumberStamp;

public class ExampleAddPageNumberToPDF {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() {

        // Open document
        Document pdfDocument = new Document(_dataDir + "PageNumberStamp.pdf");

        // Create page number stamp
        PageNumberStamp pageNumberStamp = new PageNumberStamp();

        // Whether the stamp is background
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # of " + pdfDocument.getPages().size());
        pageNumberStamp.setBottomMargin (10);
        pageNumberStamp.setHorizontalAlignment ( HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        // Set text properties
        pageNumberStamp.getTextState().setFont (FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize (14.0F);
        pageNumberStamp.getTextState().setFontStyle (FontStyles.Bold);        
        pageNumberStamp.getTextState().setForegroundColor (Color.getAqua());

        // Add stamp to particular page
        pdfDocument.getPages().get_Item(1).addStamp(pageNumberStamp);

        _dataDir = _dataDir + "PageNumberStamp_out.pdf";
        // Save output document
        pdfDocument.save(_dataDir);

    }
}
```


