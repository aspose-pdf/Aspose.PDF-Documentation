---
title: Extract Images from PDF 
linktitle: Extract Images
type: docs
weight: 20
url: /androidjava/extract-images-from-the-pdf-file/
description: How to extract a part of the image from PDF using Aspose.PDF for Android via Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Each page in PDF document contain resources (images, forms and fonts). We can access to these resources by calling [getResources](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) method. Class [Resources](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Resources) contain [XImageCollection](https://apireference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) and we can get list of images by calling [getImages](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--) method.

Thus to extract image from page, we need to get reference to the page, next to the page resources and last to the image collection.
Particular image we can extract for example by index.

The image's index returns an [XImage](https://apireference.aspose.com/pdf/java/com.aspose.pdf/XImage) object.
This object provides a [Save](https://apireference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) method which can be used to save the extracted image. The following code snippet shows how to extract images from a PDF file.

 ```java
 public void extractImage () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        com.aspose.pdf.Page page=document.getPages().get_Item(1);
        com.aspose.pdf.XImageCollection xImageCollection=page.getResources().getImages();
        // Extract a particular image
        com.aspose.pdf.XImage xImage=xImageCollection.get_Item(1);
        File file=new File(fileStorage, "extracted-image.jpeg");
        try {
            java.io.FileOutputStream outputImage=new java.io.FileOutputStream(file.toString());
            // Save output image
            xImage.save(outputImage, ImageType.getJpeg());
            outputImage.close();
        } catch (java.io.IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.
          }
```
