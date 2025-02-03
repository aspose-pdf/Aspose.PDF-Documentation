---
title: Working with Image Placement
linktitle: Image Placement
type: docs
weight: 50
url: /java/working-with-image-placement/
description: This section describes the features of working with image placement PDF file using Java library.
lastmod: "2021-06-05"
TechArticle: true 
AlternativeHeadline: Image placement PDF file using Java library
Abstract: The article discusses the use of Aspose.PDF for Java, specifically focusing on the classes `ImagePlacement`, `ImagePlacementAbsorber`, and `ImagePlacementCollection`, which are used to determine an image's resolution and position within a PDF document. The `ImagePlacementAbsorber` class is responsible for searching and collecting `ImagePlacement` objects, which provide properties such as `Resolution` and `Rectangle` to extract image placement details. The article includes a Java code example demonstrating how to utilize these classes. It shows loading a PDF document, extracting image properties like width, height, and resolution, and then retrieving and processing images from the PDF. The example further illustrates how to scale and replace images using Java's `BufferedImage` class. This provides a practical implementation of handling and manipulating images within PDF documents using the Aspose.PDF library.
SoftwareApplication: java

---

Aspose.PDF for Java introduced classes called [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement), [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber) and [ImagePlacementCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementCollection) which provide similar capability as the classes described above to get an image's resolution and position in a PDF document.

- ImagePlacementAbsorber performs image usage search as the ImagePlacement objects collection.
- ImagePlacement provides the members Resolution and Rectangle that return actual image placement values.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;


import javax.imageio.ImageIO;

public class ExampleWorkingWithImagePlacement {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void WorkingWithImagePlacement() throws IOException {
        // Load the source PDF file
        Document doc = new Document(_dataDir + "ImageInformation.pdf");
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

        // Load the contents of first page
        doc.getPages().get_Item(1).accept(abs);
        for (ImagePlacement imagePlacement : abs.getImagePlacements()) {
            // Get image properties
            System.out.println("image width:" + imagePlacement.getRectangle().getWidth());
            System.out.println("image height:" + imagePlacement.getRectangle().getHeight());
            System.out.println("image LLX:" + imagePlacement.getRectangle().getLLX());
            System.out.println("image LLY:" + imagePlacement.getRectangle().getLLY());
            System.out.println("image horizontal resolution:" + imagePlacement.getResolution().getX());
            System.out.println("image vertical resolution:" + imagePlacement.getResolution().getY());

            // Retrieve image with visible dimensions
            // Bitmap scaledImage;
            // Retrieve image from resources
            ByteArrayOutputStream imageStream = new ByteArrayOutputStream();
            imagePlacement.getImage().save(imageStream, ImageType.getPng());

            // Bitmap resourceImage = (Bitmap)Bitmap.FromStream(imageStream);
            BufferedImage resourceImage = ImageIO.read(new ByteArrayInputStream(imageStream.toByteArray()));

            // Create bitmap with actual dimensions
            BufferedImage scaledImage = toBufferedImage( 
            resourceImage.getScaledInstance((int) imagePlacement.getRectangle().getWidth(),
                    (int) imagePlacement.getRectangle().getHeight(), java.awt.Image.SCALE_SMOOTH));

            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            ImageIO.write(scaledImage, "jpg", baos);
            ByteArrayInputStream fis = new ByteArrayInputStream(baos.toByteArray());

            imagePlacement.getImage().replace(fis);
        }
    }
    
    public static BufferedImage toBufferedImage(java.awt.Image img) {
        if (img instanceof BufferedImage) {
            return (BufferedImage) img;
        }

        // Create a buffered image with transparency
        BufferedImage bimage = new BufferedImage(img.getWidth(null), img.getHeight(null), BufferedImage.TYPE_INT_ARGB);

        // Draw the image on to the buffered image
        Graphics2D bGr = bimage.createGraphics();
        bGr.drawImage(img, 0, 0, null);
        bGr.dispose();

        // Return the buffered image
        return bimage;
    }
}
```

