---
title: Working with Images
type: docs
weight: 30
url: /java/working-with-image/
description: This section explains how to replace image with Aspose.PDF Facades - a toolset for popular operations with PDF.
lastmod: "2021-06-25"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Delete Images from a Particular Page of PDF (Facades)

[PdfContentEditor](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) class allows you to replace image in an existing PDF file. The [replaceImage](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) method helps you achieve this goal. You need to create an object of [PdfContentEditor](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) class and bind the input PDF file using bindPdf method. After that, you need to call [replaceImage](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) method with three parameters: a page number, index of the image to replace, and path of the image to be replaced.

The following code snippet shows you how to replace an image in an existing PDF file.

```java
public class PdfContentEditorImages {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/facades/PdfContentEditor/";

    public static void DeleteImage()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.deleteImage(2, new int [] { 1,3 });
        editor.save(_dataDir + "PdfContentEditorDemo10.pdf");
    }
```

## Delete All the Images from a PDF File (Facades)

All the images can be deleted from a PDF file using [deleteImage](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) method of the [PdfContentEditor](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor). Call the [deleteImage](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) method – the overload without any parametes – to delete all the images, and then save the updated PDF file using Save method.

```java
   public static void DeleteImages()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.deleteImage();
        editor.save(_dataDir + "PdfContentEditorDemo11.pdf");
    }
```

## Replace Images in PDF File (Facades)

You may replace images in PDF file using [replaceImage](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) method of the [PdfContentEditor](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor).

```java
   public static void ReplaceImage()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample_cats_dogs.pdf"));
        editor.replaceImage(2, 4, _dataDir+"cat04.jpg");
        editor.save(_dataDir + "PdfContentEditorDemo12.pdf");
    }
```
