
**Enhanced metafile format (EMF)** stores graphical images device-independently. Metafiles of EMF comprises of variable-length records in chronological order that can render the stored image after parsing on any output device. 

We have several approaches to convert EMF into PDF.

## Using Image class 

A PDF document comprises pages and each page contains one or more paragraph objects. A paragraph can be a text, image,table, floating box, graph, heading, form field or an attachment. 
To convert an image file into PDF format, enclose it in a paragraph.
     
It is possible to convert images at a physical location on the local hard
drive, found at a web URL or in a Stream instance. 

To add an image:

1. Create an object of the com.aspose.pdf.Image class. 
1. Add the image to a [`Paragraphs`](https://apireference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) collection of page instance. 
1. Specify the path or source of Image.
    -  If an image is at a location on the hard drive, specify the path location using the [`Image.setFile(…)`](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Image) method. 
    -  If an image is placed in a FileInputStream, pass the object holding the image to the [`Image.setImageStream(…)`](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Image) method.

The following code snippet shows how to load an image object, set the page margin, place the image on page and save the output as PDF.

```java
package com.aspose.pdf.examples;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;

/**
 * Convert EMF to PDF
 */

import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;

public final class ConvertEMFtoPDF {

    private ConvertEMFtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {

        convertEMFtoPDF_01();
        convertEMFtoPDF_02();
    }

    

    public static void convertEMFtoPDF_01() throws FileNotFoundException {                
        // Instantiate Document Object
        Document doc = new Document();
        // Add a page to pages collection of document
        Page page = doc.getPages().add();
        // Load the source image file to Stream object
        java.io.FileInputStream fs = new java.io.FileInputStream(
            Paths.get(_dataDir.toString(),"source.emf").toString());

        // Set margins so image will fit, etc.
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);

        page.setCropBox(new Rectangle(0, 0, 400, 400));
        // Create an image object
        Image image1 = new Image();
        // Add the image into paragraphs collection of the section
        page.getParagraphs().add(image1);
        // Set the image file stream
        image1.setImageStream(fs);
        // Save resultant PDF file
        doc.save("EMFtoPDF_01.pdf");
    }   
    public static void convertEMFtoPDF_02() throws IOException {
        // see code below
    } 
}
```
     
### Add image from BufferedImage
    
Aspose.PDF for Java also offers the feature to load image from Stream instance where an image can be loaded to BufferedImage object and can be placed inside paragraphs collection of Pdf file.
    
```java
public static void convertEMFtoPDF_02() throws IOException {    
    Document doc = new Document();
    // add a page to pages collection of Pdf file
    Page page = doc.getPages().add();
    // create image instance
    Image image1 = new Image();
    // create BufferedImage instance
    java.awt.image.BufferedImage bufferedImage = ImageIO.read(new File("source.emf"));
    ByteArrayOutputStream baos = new ByteArrayOutputStream();
    // write buffered Image to OutputStream instance
    ImageIO.write(bufferedImage, "emf", baos);
    baos.flush();
    ByteArrayInputStream bais = new ByteArrayInputStream(baos.toByteArray());
    // add image to paragraphs collection of first page
    page.getParagraphs().add(image1);
    // set image stream as OutputStream holding Buffered image
    image1.setImageStream(bais);
    // save resultant PDF file
    doc.save("BufferedImage.pdf");
}
```

## Add Image using PDF Operators

Every PDF page object contains the [getResources()](https://apireference.aspose.com/java/pdf/com.aspose.pdf/Page#getResources--) and [getContents()](https://apireference.aspose.com/java/pdf/com.aspose.pdf/Page#getContents--) methods. Resources can be images and forms, for example, while content is represented by a set of PDF operators. Each operator has its own name and argument. 

This example use operators to add an image to a PDF file.

To add an image to an existing PDF file:

1. Create a [Document](https://apireference.aspose.com/java/pdf/com.aspose.pdf/Document) object and open the input PDF document.
1. Get the page you want to add an image to.
1. Add the image into the page's [getResources()](https://apireference.aspose.com/java/pdf/com.aspose.pdf/Page#getResources--) collection.
1. Use operators to place the image on the page:
   1. Use the GSave operator to save the current graphical state.
   1. Use the ConcatenateMatrix operator to specify where the image is to be placed.
   1. Use the Do operator to draw the image on the page.
   1. Finally, use the GRestore operator to save the updated graphical state.
1. Save the file.

The following code snippet shows how to add image to a PDF document.

```java
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-Java
// Open a document
Document pdfDocument1 = new Document("input.pdf");

// Set coordinates
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// Get the page you want to add the image to
Page page = pdfDocument1.getPages().get_Item(1);

// Load image into stream
java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File("input_image1.jpg"));

// Add an image to the Images collection of the page resources
page.getResources().getImages().add(imageStream);

// Using the GSave operator: this operator saves current graphics state
page.getContents().add(new Operator.GSave());

// Create Rectangle and Matrix objects
Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0, rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

// Using ConcatenateMatrix (concatenate matrix) operator: defines how image must be placed
page.getContents().add(new Operator.ConcatenateMatrix(matrix));
XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());

// Using Do operator: this operator draws image
page.getContents().add(new Operator.Do(ximage.getName()));

// Using GRestore operator: this operator restores graphics state
page.getContents().add(new Operator.GRestore());

// Save the new PDF
pdfDocument1.save("Updated_document.pdf");

// Close image stream
imageStream.close();
```