---
title: Add Image to Existing PDF File 
linktitle: Add Image
type: docs
weight: 10
url: /java/add-image-to-existing-pdf-file/
description: This section describes how to add image to existing PDF file using Java library.
lastmod: "2021-06-05"
---

Every PDF page contains Resources and Contents properties. Resources can be images and forms for example, while content is represented by a set of PDF operators. Each operator has its name and argument. This example uses operators to add an image to a PDF file.

To add an image to an existing PDF file:

- Create a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object and open the input PDF document.
- Get the page you want to add an image to.
- Add the image into the page’s [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) collection.
- Use operators to place the image on the page:
- Use the GSave operator to save the current graphical state.
- Use [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators.class-use/concatenatematrix) operator to specify where the image is to be placed.
- Use the [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/class-use/Do) operator to draw the image on the page.
- Finally, use [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators.class-use/grestore) operator to save the updated graphical state.
- Save the file.

The following code snippet shows how to add the image in a PDF document.

```java
package com.aspose.pdf.examples;

import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfFileMend;
import com.aspose.pdf.operators.*;

public class ExampleAddImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddImageToExistingPDF() throws IOException {
        // Open a document
        Document pdfDocument1 = new Document(_dataDir + "sample.pdf");

        // Set coordinates
        int lowerLeftX = 50;
        int lowerLeftY = 750;
        int upperRightX = 100;
        int upperRightY = 800;

        // Get the page you want to add the image to
        Page page = pdfDocument1.getPages().get_Item(1);

        // Load image into stream
        java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File(_dataDir + "logo.png"));

        // Add an image to the Images collection of the page resources
        page.getResources().getImages().add(imageStream);

        // Using the GSave operator: this operator saves current graphics state
        page.getContents().add(new GSave());

        // Create Rectangle and Matrix objects
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

        // Using ConcatenateMatrix (concatenate matrix) operator: defines how image must
        // be placed
        page.getContents().add(new ConcatenateMatrix(matrix));
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());

        // Using Do operator: this operator draws image
        page.getContents().add(new Do(ximage.getName()));

        // Using GRestore operator: this operator restores graphics state
        page.getContents().add(new GRestore());

        // Save the new PDF
        pdfDocument1.save(_dataDir + "updated_document.pdf");

        // Close image stream
        imageStream.close();
    }
```

## Adding image from BufferedImage into PDF

Starting release of Aspose.PDF for Java 9.5.0, we have introduced the support to add image from BufferedImage instance to PDF document. In order to support this requirement, a method is implemented: [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection).add(BufferedImage image);

```java
    public static void AddingImageFromBufferedImageIntoPDF() throws IOException {
        BufferedImage originalImage = ImageIO.read(new File("anyImage.jpg"));
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();
        page.getResources().getImages().add(originalImage);
    }
```
You can use any InputStream and not just only FileInputStream object to add image. So when using java.io.ByteArrayInputStream object, you do not need to store any files over system:

```java
    public static void AddingImageFromBufferedImageIntoPDF2() throws IOException {
        BufferedImage originalImage = ImageIO.read(new File("anyImage.jpg"));
        ByteArrayOutputStream baos = new ByteArrayOutputStream();

        Document pdfDocument = new Document();
        ImageIO.write(originalImage, "jpg", baos);
        baos.flush();
        Page page = pdfDocument.getPages().get_Item(1);
        page.getResources().getImages().add(new ByteArrayInputStream(baos.toByteArray()));
    }
```

## Add Image in an Existing PDF File (Facades)

There is also an alternative, easier way to add a Image to a PDF file. You can use AddImage method of the [PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend) class. The AddImage method requires the image to be added, the page number at which the image needs to be added and the coordinate information. After that, save the updated PDF file using Close method. 

The following code snippet shows you how to add image in an existing PDF file.

```java
    public static void AddImageInAnExistingPDFFile_Facades() {
        // Open document
        PdfFileMend mender = new PdfFileMend();

        // Create PdfFileMend object to add text
        mender.bindPdf(_dataDir + "AddImage.pdf");

        // Add image in the PDF file
        mender.addImage(_dataDir + "aspose-logo.jpg", 1, 100, 600, 200, 700);

        // Save changes
        mender.save(_dataDir + "AddImage_out.pdf");

        // Close PdfFileMend object
        mender.close();
    }
```

## Add Reference of a single Image multiple times in a PDF Document

Sometimes we have a requirement to use same image multiple times in a PDF document. Adding a new instance increases the resultant PDF document. We have added a new method XImageCollection.add(XImage) that supports Ximage object to add in the Images Collection. This method allows to add reference to the same PDF object as original image that optimize the PDF Document size.

```java
    public static void AddReferenceOfaSingleImageMultipleTimes() throws FileNotFoundException {
        Rectangle imageRectangle = new Rectangle(0, 0, 30, 15);
        Document document = new Document(_dataDir + "sample.pdf");
        document.getPages().add();
        document.getPages().add();
        java.io.FileInputStream imageStream = new java.io.FileInputStream(
                new java.io.File(_dataDir + "aspose-logo.png"));

        XImage image = null;

        for (Page page : document.getPages()) {
            WatermarkAnnotation annotation = new WatermarkAnnotation(page, page.getRect());
            XForm form = annotation.getAppearance().get_Item("N");
            form.setBBox(page.getRect());
            String name;
            if (image == null) {
                name = form.getResources().getImages().add(imageStream);
                image = form.getResources().getImages().get_Item(name);
            } else {
                name = form.getResources().getImages().add(image);
            }
            form.getContents().add(new GSave());
            form.getContents().add(new ConcatenateMatrix(
                    new Matrix(imageRectangle.getWidth(), 0, 0, imageRectangle.getHeight(), 0, 0)));
            form.getContents().add(new Do(name));
            form.getContents().add(new GRestore());
            page.getAnnotations().add(annotation, false);
            imageRectangle = new Rectangle(0, 0, imageRectangle.getWidth() * 1.01, imageRectangle.getHeight() * 1.01);
        }
        document.save(_dataDir + "output.pdf");
    }
```

## Identify if image inside PDF is Colored or Black & White

Different type of compression can be applied over images to reduce their size. The type of compression being applied over image depends upon the ColorSpace of source image i.e. if image is Color (RGB), then apply JPEG2000 compression, and if it is Black & White, then JBIG2/JBIG2000 compression should be applied. Therefore identifying each image type and using an appropriate type of compression will create best/optimized output.

A PDF file may contain Text, Image, Graph, Attachment, Annotation etc elements and if the source PDF file contains images, we can determine image Color space and apply appropriate compression for image to reduce PDF file size. The following code snippet shows the steps to Identify if image inside PDF is Colored or Black & White.

```java
    public static void CheckColors() {

        Document document = new Document(_dataDir + "test4.pdf");
        try {
            // iterate through all pages of PDF file
            for (Page page : (Iterable<Page>) document.getPages()) {
                // create Image Placement Absorber instance
                ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
                page.accept(abs);
                for (ImagePlacement ia : (Iterable<ImagePlacement>) abs.getImagePlacements()) {
                    /* ColorType */
                    int colorType = ia.getImage().getColorType();
                    switch (colorType) {
                    case ColorType.Grayscale:
                        System.out.println("Grayscale Image");
                        break;
                    case ColorType.Rgb:
                        System.out.println("Colored Image");
                        break;
                    }
                }
            }
        } catch (Exception ex) {
            System.out.println("Error reading file = " + document.getFileName());
        }
    }
}
```



