---
title: Delete Images from PDF File
linktitle: Delete Images
type: docs
weight: 20
url: /java/delete-images-from-pdf-file/
description: This section explain how to delete Images from PDF File using Aspose.PDF for Java.
lastmod: "2025-02-17"
TechArticle: true 
AlternativeHeadline: Remove an image from a PDF file using the Aspose.PDF library for Java
Abstract: This article provides a step-by-step guide on how to delete an image from a PDF file using the Aspose.PDF library for Java. The process begins by creating a `Document` object to open the input PDF file. The desired page containing the image is accessed through the `Pages` collection of the `Document` object. Images within a page are managed by the `Images` collection, which is part of the page's `Resources` collection. To remove an image, the `Delete` method of the `Images` collection is employed. After modifying the document, it is saved using the `Save` method of the `Document` object. The article includes a code snippet demonstrating the deletion of an image from a PDF file, showcasing the creation and configuration of a `PageNumberStamp` and its addition to a PDF page, followed by saving the updated document.
SoftwareApplication: java
---

To delete an image from a PDF file, simply use the Images collection's delete(..) method.

1. Create a Document object and open the input PDF file.
1. Get the Page that holds the image from the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object's [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) collection.
1. Images are held in the Images collection, found in the page's [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) collection.
1. Delete an image with the Images collection's Delete method.
1. Saved the output like using the Document object's Save method.

The following code snippet shows how to delete an image from a PDF file.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.FontStyles;
import com.aspose.pdf.HorizontalAlignment;
import com.aspose.pdf.PageNumberStamp;

public class ExampleDeleteImages {

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
