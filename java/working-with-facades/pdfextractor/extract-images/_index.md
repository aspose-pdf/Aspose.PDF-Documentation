---
title: Extract Images from PDF (facades)
type: docs
weight: 30
url: /java/extract-images/
description: This section explains how to extract images with Aspose.PDF Facades using PdfExtractor Class.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[PdfExtractor](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor) class allows you to extract images from a PDF file. First off, you need to create an object of [PdfExtractor](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor) class and bind input PDF file using bindPdf method. After that, call [extractImage](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#extractImage--) method to extract all the images into memory. Once the images are extracted, you can get those images with the help of hasNextImage and getNextImage methods. You need to loop through all the extracted images using a while loop. In order to save the images to disk, you can call the overload of the getNextImage method which takes file path as argument. The following code snippet shows you how to extract images from the whole PDF to files.

```java   
public static void ExtractImages()
 {
    //Create an extractor and bind it to the document
    Document document = new Document(_dataDir + "sample.pdf");
    PdfExtractor extractor = new PdfExtractor(document);
    extractor.setStartPage(1);
    extractor.setEndPage(3);            

    //Run the extractor
    extractor.extractImage();
    int imageNumber = 1;
    //Iterate througth extracted images collection
    while (extractor.hasNextImage())
    {
        //Retrieve image from collection and save it in a file 
        extractor.getNextImage(_dataDir + String.format("image%03d.png", imageNumber++),ImageType.getPng());
    }
}
```



