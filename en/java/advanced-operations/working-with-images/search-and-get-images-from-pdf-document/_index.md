---
title: Search and Get Images from PDF Document
linktitle: Search and Get Images
type: docs
weight: 60
url: /java/search-and-get-images-from-pdf-document/
description: This section explain how to search and get images from PDF document with Aspose.PDF for Java library.
lastmod: "2021-06-05"
TechArticle: true 
AlternativeHeadline: 
Abstract: This article provides a guide on using the `ImagePlacementAbsorber` class from the Aspose.PDF library to search for images across all pages of a PDF document. The process involves calling the `Accept` method of the `Pages` collection with an `ImagePlacementAbsorber` object to collect `ImagePlacement` items, which contain properties of the images found, such as dimensions and resolution. The article includes a Java code example demonstrating how to open a PDF document, create an `ImagePlacementAbsorber`, and retrieve properties of images within the document through iteration of `ImagePlacement` objects. Additionally, it shows how to extract images from a specific page using a modified `Accept` method call.
---

The [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber) allows you to search among images on all pages in a PDF document.

To search a whole document for images:

1. Call the [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection) collection's Accept method. The Accept method takes an [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber) object as a parameter. This returns a collection of [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement) objects.
1. Loop through the ImagePlacements objects and get their properties (Image, dimensions, resolution and so on).

The following code snippet shows how to search a document for all its images.

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import com.aspose.pdf.*;

public class ExampleSearchAndGet {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void SearchImages() throws IOException {
        // Open document
        Document doc = new Document(_dataDir + "SearchAndGetImages.pdf");

        // Create ImagePlacementAbsorber object to perform image placement search
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

        // Accept the absorber for all the pages
        doc.getPages().accept(abs);

        // Loop through all ImagePlacements, get image and ImagePlacement Properties
        for (ImagePlacement imagePlacement : abs.getImagePlacements()) {
            // Get the image using ImagePlacement object
            // XImage image = imagePlacement.getImage();

            // Display image placement properties for all placements
            System.out.println("image width:" + imagePlacement.getRectangle().getWidth());
            System.out.println("image height:" + imagePlacement.getRectangle().getHeight());
            System.out.println("image LLX:" + imagePlacement.getRectangle().getLLX());
            System.out.println("image LLY:" + imagePlacement.getRectangle().getLLY());
            System.out.println("image horizontal resolution:" + imagePlacement.getResolution().getX());
            System.out.println("image vertical resolution:" + imagePlacement.getResolution().getY());
        }

    }
}
```
To get an image from an individual page, use the following code:

```java
doc.getPages().get_Item(1).accept(abs)
```