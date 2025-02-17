---
title: Extract Images from PDF 
linktitle: Extract Images
type: docs
weight: 20
url: /java/extract-images-from-the-pdf-file/
description: How to extract a part of the image from PDF using Aspose.PDF for Java
lastmod: "2025-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to Extract Images from PDF using Aspose.PDF for Java
Abstract: The article provides a detailed guide on extracting images from a PDF document using the Aspose.PDF library in Java. It explains that each PDF page contains resources such as images, forms, and fonts, which can be accessed using the `getResources` method of the `Page` class. The `Resources` class includes an `XImageCollection`, from which images can be retrieved using the `getImages` method. To extract an image, one must first obtain a reference to the desired page, then access its resources and image collection. Images are accessed by their index in the collection, returning an `XImage` object. This object offers a `Save` method to save the image to an output stream. A code example demonstrates the process - loading a PDF document, accessing the first page, retrieving the first image from the collection, and saving it as a JPEG file. The article also includes exception handling for file output operations.
SoftwareApplication: java
---

Each page in PDF document contain resources (images, forms and fonts). We can access to these resources by calling [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) method. Class [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) contain [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) and we can get list of images by calling [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--) method.

Thus to extract image from page, we need to get reference to the page, next to the page resources and last to the image collection.
Particular image we can extract for example by index.

The image's index returns an [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) object.
This object provides a [Save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) method which can be used to save the extracted image. The following code snippet shows how to extract images from a PDF file.

 ```java
 public static void Extract_Images(){
        // The path to the documents directory.
        String _dataDir = "/home/admin1/pdf-examples/Samples/";
        String filePath = _dataDir + "ExtractImages.pdf";

        // Load PDF document
        com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

        com.aspose.pdf.Page page = pdfDocument.getPages().get_Item(1);
        com.aspose.pdf.XImageCollection xImageCollection = page.getResources().getImages();
        // Extract a particular image
        com.aspose.pdf.XImage xImage = xImageCollection.get_Item(1);

        try {
            java.io.FileOutputStream outputImage = new java.io.FileOutputStream(_dataDir + "output.jpg");
            // Save output image
            xImage.save(outputImage);
            outputImage.close();
        } catch (java.io.FileNotFoundException e) {
            // TODO: handle exception
            e.printStackTrace();
        } catch (java.io.IOException e) {
            // TODO: handle exception
            e.printStackTrace();
        }
    }
```
