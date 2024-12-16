---
title: Extract Images from PDF 
linktitle: Extract Images
type: docs
weight: 20
url: /php-java/extract-images-from-the-pdf-file/
description: How to extract a part of the image from PDF using Aspose.PDF for PHP
lastmod: "2024-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Each page in PDF document contain resources (images, forms and fonts). We can access to these resources by calling [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) method. Class [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) contain [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) and we can get list of images by calling [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--) method.

Thus to extract image from page, we need to get reference to the page, next to the page resources and last to the image collection.
Particular image we can extract for example by index.

The image's index returns an [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) object.
This object provides a [save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) method which can be used to save the extracted image. The following code snippet shows how to extract images from a PDF file.

 ```php
 
    // Load the PDF document
    $document = new Document($inputFile);

    // Get the first page of the document
    $page = $document->getPages()->get_Item(1);

    // Get the collection of images on the page
    $xImageCollection = $page->getResources()->getImages();

    // Get the first image from the collection
    $xImage = $xImageCollection->get_Item(1);

    // Create a new FileOutputStream object to save the image
    $outputImage = new java("java.io.FileOutputStream", $outputFile);

    // Save the image to the output file
    $xImage->save($outputImage);

    // Close the output image file
    $outputImage->close();
```
