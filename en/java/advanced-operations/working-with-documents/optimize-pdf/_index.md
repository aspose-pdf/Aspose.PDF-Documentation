---
title: Optimize, Compress or Reduce PDF Size in Java
linktitle: Optimize PDF Document
type: docs
weight: 40
url: /java/optimize-pdf/
description: Optimize PDF file, shrink all images, reduce size PDF, Unembed fonts, Remove unused objects with Java.
lastmod: "2021-06-05"
TechArticle: true 
AlternativeHeadline: Guide on optimizing and reducing the size of PDF files using Aspose.PDF for Java
Abstract: The article provides a comprehensive guide on optimizing and reducing the size of PDF files using various techniques, primarily through the Aspose.PDF API. It emphasizes the benefits of optimizing PDFs for better network transfer, storage efficiency, and suitability for online publishing. Key optimization strategies discussed include optimizing page content for web browsing, compressing images, merging duplicate streams, unembedding fonts, and removing unused objects, streams, annotations, and form fields. The article also provides detailed code examples for implementing these techniques in Java, demonstrating how to linearize PDFs for online viewing, compress and resize images, remove redundant data, and convert color spaces to grayscale for improved printing efficiency. Additionally, it covers advanced features like using FlateDecode compression and storing images in XImageCollection for further optimization. Overall, the guide aims to equip users with practical methods to enhance PDF performance and manage file sizes effectively.
SoftwareApplication: java
---


A PDF document can sometimes contain additional data. Reducing the size of a PDF file will help you optimize network transfer and storage. This is especially handy for publishing on web pages, sharing on social networks, sending by e-mail, or archiving in storage. We can use several techniques to optimize PDF:

- Optimize page content for online browsing
- Shrink or compress all images
- Enable reusing page content
- Merge duplicate streams
- Unembed fonts
- Remove unused objects
- Remove flattening form fields
- Remove or flatten annotations

## Optimize PDF Document for the Web

Optimization or linearization refers to the process of making a PDF file suitable for online browsing using a web browser. Aspose.PDF supports this process.

To optimize a PDF for web display:

1. Open the input document in a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object.
1. Use the [optimize()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#optimize--) method.
1. Save the optimized document using the save(..) method.

The following code snippet shows how to optimize a PDF document for the web.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.time.Clock;
import java.time.Duration;

import com.aspose.pdf.*;
import com.aspose.pdf.optimization.ImageCompressionVersion;
import com.aspose.pdf.optimization.ImageEncoding;

public class ExampleOptimize {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void OptimizePDFDocumentForTheWeb() {

        // Open document
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // Optimize for web
        pdfDocument.optimize();

        // Save output document
        pdfDocument.save(_dataDir + "OptimizeDocument_out.pdf");
    }
```

## Reduce PDF File Size

This topic explains the steps to optimize/reduce the PDF file size. Aspose.PDF API provides the [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.optimization/class-use/OptimizationOptions) class that gives the flexibility to optimize output PDF by removing unnecessary objects and compressing PDF files having images. Both these options are elaborated in the following sections.

### Remove Unnecessary Objects
We can optimize the size of PDF documents by removing duplicate and unused objects. The following code snippet shows how.

```java
public static void ReduceSizePDF() {

        // Open document
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // Optimize PDF document. Note, though, that this method cannot guarantee
        // document shrinking
        pdfDocument.optimizeResources();

        // Save output document
        pdfDocument.save(_dataDir + "OptimizeDocument_out.pdf");
    }
```
## Shrinking or Compressing All Images

If the source PDF file contains images, consider compressing the images and setting their quality. In order to enable image compression, pass true as an argument to the setCompressImages(..) method. All the images in a document will be re-compressed. The compression is defined by the setImageQuality(..) method, which is the value of the quality in percent. 100% is unchanged quality and image size. To decrease image size, pass an argument of less than 100 to the setImageQuality(..) method.

```java
public static void ShrinkingCompressing() {
        // Open document
        Document pdfDocument = new Document(_dataDir + "Shrinkimage.pdf");

        // Initialize OptimizationOptions
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // Set CompressImages option
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);

        // Set ImageQuality option
        optimizationOptions.getImageCompressionOptions().setImageQuality(50);

        // Optimize PDF document using OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "Shrinkimage_out.pdf";
        // Save updated document
        pdfDocument.save(_dataDir);
    }
```
Another way is to resize the images with a lower resolution. In this case, we should set ResizeImages to true and MaxResolution to the appropriate value.

```java
public static void ShrinkingCompressing2() {
        // Open document
        Document pdfDocument = new Document(_dataDir + "ResizeImage.pdf");

        // Initialize OptimizationOptions
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // Set CompressImages option
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);
        // Set ImageQuality option
        optimizationOptions.getImageCompressionOptions().setImageQuality(75);

        // Set ResizeImage option
        optimizationOptions.getImageCompressionOptions().setResizeImages(true);

        // Set MaxResolution option
        optimizationOptions.getImageCompressionOptions().setMaxResolution(300);

        // Optimize PDF document using OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "ResizeImages_out.pdf";
        // Save updated document
        pdfDocument.save(_dataDir);
    }
```
Another important issue is the execution time. But again, we can manage this setting too. Currently, we can use two algorithms - Standard and Fast. To control the execution time we should set a Version property. The following snippet demonstrates the Fast algorithm:

```java
public static void ShrinkingCompressing3() {

        Clock clock = Clock.systemUTC();

        Duration tickDuration = Duration.ofNanos(250000);
        Clock clock1 = Clock.tick(clock, tickDuration);
        System.out.println("Start : " + clock.instant());

        // Open document
        Document pdfDocument = new Document(_dataDir + "ResizeImage.pdf");

        // Initialize OptimizationOptions
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // Set CompressImages option
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);

        // Set ImageQuality option
        optimizationOptions.getImageCompressionOptions().setImageQuality(75);

        // Set Image Compression Version to fast
        optimizationOptions.getImageCompressionOptions().setVersion(ImageCompressionVersion.Fast);

        // Optimize PDF document using OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);

        _dataDir = _dataDir + "ResizeImages_out.pdf";

        // Save updated document
        pdfDocument.save(_dataDir);
        System.out.println("Finish : " + clock1.instant());
    }
```
## Removing Unused Objects

A PDF document sometimes contains the PDF objects that are not referenced from any other object in the document. This may happen, for example, when a page is removed from the document page tree but the page object itself isn’t removed. Removing these objects doesn’t make the document invalid but rather shrinks it.

```java
    public static void RemovingUnusedObjects() {

        // Open document
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        
        optimizationOptions.setRemoveUnusedObjects(true);
        pdfDocument.optimizeResources(optimizationOptions);
        
        _dataDir = _dataDir + "emoveUnusedObjects_out.pdf";

        // Save updated document
        pdfDocument.save(_dataDir);

    }
```
## Removing Unused Streams

Sometimes a document contains unused resource streams. These streams are not “unused objects” because they are referenced from a page's resource dictionary. This may happen in cases where an image has been removed from the page but not from the page resources. Also, this situation often occurs when pages are extracted from the document and document pages have “common” resources, that is, the same Resources object. Page contents are analyzed in order to determine if a resource stream is used or not. Unused streams are removed. Sometimes this decreases the document size.

```java
public static void RemovingUnusedStream() {
        // Open document
        Document pdfDocument = new Document(_dataDir + 
        "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setRemoveUnusedStreams(true);
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "removeUnusedObjects_out.pdf";
        
        // Save updated document
        pdfDocument.save(_dataDir);
        
    }
```
## Linking Duplicate Streams

Sometimes a document contains several identical resource streams (for example images). This may happen for example when a document is concatenated with itself. The output document contains two independent copies of the same resource stream. We analyze all resource streams and compare them. If streams are duplicated they are merged, that is, only one copy is left, references are changed appropriately and copies of the object are removed. Sometimes this decreases the document size.

```java
    public static void LinkingDuplicateStream() {
        // Open document
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setRemoveUnusedStreams(true);
        
        // Optimize PDF document using OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        
        // Save updated document
        pdfDocument.save(_dataDir);
    }
```
Additionally, we can use AllowReusePageContent settings. If this property is set to true, the page content will be reused when optimizing the document for identical pages.

```java
public static void AllowReusePageContent() {
        // Open document
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setAllowReusePageContent(true);
        
        // Optimize PDF document using OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        
        // Save updated document
        pdfDocument.save(_dataDir);
    }
```
## Unembedding Fonts 

If the document uses embedded fonts it means that all font data is placed in the document. The advantage is that the document is viewable regardless of whether the font is installed on the user's machine or not. But embedding fonts makes the document larger. The unembed fonts method removes all embedded fonts. This decreases the document size but the document may become unreadable if the correct font is not installed.

```java
    public static void UnembedFonts() {
        // Open document
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setUnembedFonts(true);
        
        // Optimize PDF document using OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // Save updated document
        pdfDocument.save(_dataDir);
    }
```

## Removing or Flattening Annotations

Annotations can be deleted when they are unnecessary. When they are needed but do not require additional editing, they can be flattened. Both of these techniques will reduce the file size.

```java
    public static void FlatteningAnnotations() {
        // Open document
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        for (Page page : pdfDocument.getPages()) {
            for (Annotation annotation : page.getAnnotations())
                annotation.flatten();
        }

        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // Save updated document
        pdfDocument.save(_dataDir);
    }

```
## Removing Form Fields

If the PDF document contains AcroForms, we can try to reduce the file size by flattening form fields.

```java
    public static void RemovingFormFields() {
        // Open document
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        // Flatten Forms
        if (pdfDocument.getForm().getFields().length > 0) {
            for (Field field : pdfDocument.getForm().getFields()) {
                field.flatten();
            }
        }
        _dataDir = _dataDir + "FlattenForms_out.pdf";
        // save the updated document
        pdfDocument.save(_dataDir);
    }

```
## Convert a PDF from RGB colorspace to grayscale

A PDF file is comprised of Text, Image, Attachment, Annotations, Graphs and other objects. You may come across a requirement to convert a PDF from RGB colorspace to Grayscale so that it would be faster while printing those PDF files. Also when the file is converted to Grayscale, the size of the document is also reduced but with this change, the quality of the document may drop. Currently, this feature is supported by the Pre-Flight feature of Adobe Acrobat, but when talking about Office automation, Aspose.PDF is an ultimate solution to provide such leverages for document manipulation.

In order to accomplish this requirement, the following code snippet can be used.

```java
    public static void ConvertRGBtoGrayscale() {

        // Open document
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        com.aspose.pdf.RgbToDeviceGrayConversionStrategy strategy = new com.aspose.pdf.RgbToDeviceGrayConversionStrategy();
        for (int idxPage = 1; idxPage <= pdfDocument.getPages().size(); idxPage++) {
            Page page = pdfDocument.getPages().get_Item(idxPage);
            strategy.convert(page);
        }
        pdfDocument.save("output.pdf");
    }
```
## FlateDecode Compression

Aspose.PDF for Java provides support of FlateDecode compression for PDF Optimisation functionality. The following code snippet below shows how to use the option in Optimization to store images with FlateDecode compression:

```java
    public static void FlateDecodeCompression() {

        // Open document
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        optimizationOptions.getImageCompressionOptions().setEncoding(ImageEncoding.Flate);

        // Optimize PDF document using OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);

        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // Save updated document
        pdfDocument.save(_dataDir);
    }
```
## Store Image in XImageCollection 

Aspose.PDF for Java provides the ability to store new images into [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/XImageCollection) with FlateDecode compression. To enable this option you can use ImageFilterType.Flate flag. The following code snippet shows how to use this functionality:

```java
    public static void StoreImageInXImageCollection() {
        // Initialize Document
        Document document = new Document();
        document.getPages().add();
        Page page = document.getPages().get_Item(1);

        // Load image into stream
        java.io.FileInputStream imageStream = null;
        try {
            imageStream = new java.io.FileInputStream(new java.io.File("input_image1.jpg"));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            return;
        }
        page.getResources().getImages().add(imageStream, ImageFilterType.Flate);
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        page.getContents().add(new com.aspose.pdf.operators.GSave());

        // Set coordinates
        int lowerLeftX = 0;
        int lowerLeftY = 0;
        int upperRightX = 600;
        int upperRightY = 600;
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });
        // Using ConcatenateMatrix (concatenate matrix) operator: defines how image must be placed
        page.getContents().add(new com.aspose.pdf.operators.ConcatenateMatrix(matrix));
        page.getContents().add(new com.aspose.pdf.operators.Do(ximage.getName()));
        page.getContents().add(new com.aspose.pdf.operators.GRestore());

        document.save(_dataDir + "FlateDecodeCompression.pdf");
    }

}
```
