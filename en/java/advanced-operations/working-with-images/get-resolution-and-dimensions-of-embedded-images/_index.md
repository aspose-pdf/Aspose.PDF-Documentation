---
title: Get Resolution and Dimensions of Embedded Images
linktitle: Get Resolution and Dimensions
type: docs
weight: 40
url: /java/get-resolution-and-dimensions-of-embedded-images/
description: Discover how to extract image resolutions and dimensions from embedded images in PDF files using Aspose.PDF in Java.
lastmod: "2021-06-05"
---

This topic explains how to use the operator classes in the Aspose.PDF namespace which provide the capability to get resolution and dimension information about images without having to extract them.

There are different ways of achieving this. This article explains how to use an `arraylist` and [Image placement classes](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement).

1. First, load the source PDF file (with images).
1. Then create an ArrayList object to hold the names of any images in the document.
1. Get the images using the Page.Resources.Images property.
1. Create a stack object to hold the image's graphics state and use it to keep track of different image states.
1. Create a ConcatenateMatrix object which defines current transformation. It also supports scaling, rotating, and skewing any content. It concatenates the new matrix with previous one. Please note that we cannot define the transformation from scratch but only modify the existing transformation.
1. Because we can modify the matrix with ConcatenateMatrix, we may also need to revert back to the original image state. Use GSave and GRestore operators. These operators are paired so they should be called together. For example, if you do some graphics work with complex transformations and finally return transformations back to initial state, the approach will be something like this:

```java
// Draw some text
GSave

ConcatenateMatrix  // rotate contents after the operator

// Some graphics work

ConcatenateMatrix // scale (with previous rotation) contents after the operator

// Some other graphics work

GRestore

// Draw some text
```

As a result, text is drawn in regular form but some transformations are performed between the text operators. In order to display the image or to draw form objects and images, we need to use the Do operator.

We also have a class named XImage which provides two properties,l Width and Height, which can be used to get image dimensions.

1. Perform some calculations to compute the image resolution.
1. Display the information in a Command Prompt along with the image name.

The following code snippet shows you how to get an image's dimensions and resolution without extracting the image from the PDF document.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.operators.*;
import java.util.*;

public class ExampleImagesResolution {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() 
    {
        // Load the source PDF file
        Document doc = new Document(_dataDir+ "ImageInformation.pdf");
        
        // Define the default resolution for image
        int defaultResolution = 72;

        Stack<Object> graphicsState = new Stack<Object>();

        // Define array list object which will hold image names
        List<String> imageNames = Arrays.asList(doc.getPages().get_Item(1).getResources().getImages().getNames());
        //ArrayList imageNames = new ArrayList<>(Arrays.asList(names));
        // Insert an object to stack
        graphicsState.push(new Matrix(1, 0, 0, 1, 0, 0));

        // Get all the operators on first page of document
        for (Operator op : doc.getPages().get_Item(1).getContents())
        {
            // Use GSave/GRestore operators to revert the transformations back to previously set
            GSave opSaveState = (GSave) op;
            GRestore opRestoreState = (GRestore) op;
            // Instantiate ConcatenateMatrix object as it defines current transformation matrix.
            ConcatenateMatrix opCtm = (ConcatenateMatrix) op;
            // Create Do operator which draws objects from resources. It draws Form objects and Image objects
            Do opDo = (Do) op;

            if (opSaveState != null)
            {
                // Save previous state and push current state to the top of the stack
                Matrix m = new Matrix((Matrix)graphicsState.peek());
                graphicsState.push(m);
            }
            else if (opRestoreState != null)
            {
                // Throw away current state and restore previous one
                graphicsState.pop();
            }
            else if (opCtm != null)
            {
                Matrix cm = new Matrix(
                (float)opCtm.getMatrix().getA(),
                (float)opCtm.getMatrix().getB(),
                (float)opCtm.getMatrix().getC(),
                (float)opCtm.getMatrix().getD(),
                (float)opCtm.getMatrix().getE(),
                (float)opCtm.getMatrix().getF());

                // Multiply current matrix with the state matrix
                ((Matrix)graphicsState.peek()).multiply(cm);

                continue;
            }
            else if (opDo != null)
            {
                // In case this is an image drawing operator
                if (imageNames.contains(opDo.getName()))
                {
                    Matrix lastCTM = (Matrix)graphicsState.peek();
                    // Create XImage object to hold images of first pdf page
                    XImage image = doc.getPages().get_Item(1).getResources().getImages().get_Item(opDo.getName());

                    // Get image dimensions
                    double scaledWidth = Math.sqrt(Math.pow(lastCTM.getElements()[0], 2) + Math.pow(lastCTM.getElements()[1], 2));
                    double scaledHeight = Math.sqrt(Math.pow(lastCTM.getElements()[2], 2) + Math.pow(lastCTM.getElements()[3], 2));
                    // Get Height and Width information of image
                    double originalWidth = image.getWidth();
                    double originalHeight = image.getHeight();

                    // Compute resolution based on above information
                    double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                    double resVertical = originalHeight * defaultResolution / scaledHeight;

                    // Display Dimension and Resolution information of each image
                    System.out.printf(_dataDir + "image %s (%.2f:%.2f): res %.2f x %.2f",
                                        opDo.getName(), scaledWidth, scaledHeight, resHorizontal,
                                        resVertical);
                }
                // Save output document
                doc.save(_dataDir);
            }
        }
    }
}
```
